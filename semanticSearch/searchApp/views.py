from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from .forms import UserDataForm
from .models import UserData
from .pyscripts import delete as delete

import os 
import subprocess
import csv

def uploadVideo(request):
    if request.method == 'POST':
        form = UserDataForm(request.POST, request.FILES)

        # gets the form values from web interface.
        username = request.POST.get('name')
        link = request.POST.get('url')
        videoSource = request.POST.get('source')
        videoLanguage = request.POST.get('language')
        files = request.FILES.getlist('file')

        '''
            Renames uploaded files and sequence it with numbers and saves it in the media folder.
        '''
        mediaDir = os.path.join(settings.MEDIA_ROOT, 'media/')

        # extract file list from the media directory.
        existingFiles = [f for f in os.listdir(mediaDir) if f.startswith('video') and f.endswith('.mp4')]

        maxNum = 0

        # finds the maximum number of video files in a directory.
        for file in existingFiles:
            num = int(file[5:-4]) # extracts number of filenames

            if num > maxNum:
                maxNum = num

        start = maxNum + 1

        savePath = os.path.join(settings.MEDIA_ROOT, 'data/counter.txt')

        # saves the count status in a file.
        if not os.path.exists(savePath):
            with open(savePath, 'w') as file:
                newStr = str(start) + ",False"
                file.write(newStr)
        else:
            with open(savePath, 'r') as counter:
                line = counter.read().strip()
                parts = line.split(',')
                status = parts[1]

            if status == "True":
                with open(savePath, 'w') as file:
                    newStr = str(start) + ",False"
                    file.write(newStr)

        for file in files:
            renamedFile = f'video{start}.mp4'
            start += 1

            # renames the uploaded file in a sequence.
            path = os.path.join(mediaDir, renamedFile)
            with open(path, 'wb+') as rFile:
                for chunk in file.chunks():
                    rFile.write(chunk)            

            # Saves the new file form data to the database and saves files to media folder
            new_file = UserData(
                name = username,
                url = link,
                source = videoSource,
                language = videoLanguage,
                file = 'media/' + renamedFile
            )
            if form.is_valid():
                new_file.save()
                # return redirect('serve')
        else:
            form = UserDataForm()
            return render(request, 'upload.html', {'form':form})

    form = UserDataForm()

    return render(request, 'upload.html', {'form':form})

def trainVideos(request):
    
    export_model_to_csv()
    print(os.getcwd())
    
    try:
    # Start the subprocess
        process = subprocess.Popen(
            ["python", 'searchApp/pyscripts/main.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            # cwd="/Users/hridoyrahman/Desktop/COSC 4F90/runScripts/"
        )

        # print(f"Started subprocess with PID: {process.pid}")

        # while True:
        #     status = process.poll()  
        #     if status is None:
        #         print("Subprocess is still running...")
        #         time.sleep(1)  
        #     else:
        #         print("Subprocess has completed.")
        #         break
                    
        # stdout, stderr = process.communicate()
        exit_code = process.returncode

        status = "completed" if exit_code == 0 else "error"

        audioDir = os.path.join(settings.MEDIA_ROOT, 'audio/')
        delete.deleteAudioFiles(audioDir)
        
        request.session['process_pid'] = process.pid
        
        # return render(request, 'response.html', {
        #     "status": status,
        #     "exit_code": exit_code,
        #     "stdout": stdout,
        #     "stderr": stderr,
        # })
        # return render(request, 'progress.html', {"pid": process.id})
        return redirect('progress')

    except Exception as e:
        error = str(e)
        return render(request, 'response.html',{"status": status, "message": error})

def progress(request):
    return render(request, 'progress.html')

def check_progress(request):
    pid = request.session.get('process_pid')

    if not pid:
        return render(request, 'response.html', {
            "status": "error",
            "message": "Process not found",
        })
    
    try:
        process = subprocess.Popen(['ps', '-p', str(pid), '-o', 'comm='], stdout=subprocess.PIPE, text=True)
        output, _ = process.communicate()
        if output.strip():
            return JsonResponse({"status": "running", "progress": "Progress info if available"})
        else:
            request.session['process_status'] = 'completed'
            return JsonResponse({"status": "completed"})
    except subprocess.SubprocessError:
        return JsonResponse({"status": "error", "message": "Failed to check process status."})
    
def export_model_to_csv():
    # dumpDataPath = '/vol/web/media/data/metaData.csv'
    dumpDataPath = "/Users/hridoyrahman/Desktop/COSC 4F90/SemanticVideoSearch/semanticSearch/media/data/metaData.csv"

    os.makedirs(os.path.dirname(dumpDataPath), exist_ok=True)

    queryset = UserData.objects.all()

    field_names = [field.name for field in UserData._meta.fields]
    try:
        with open(dumpDataPath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(field_names)

            for obj in queryset:
                writer.writerow([getattr(obj, field) for field in field_names])

        print(f"Data successfully exported to {dumpDataPath}")
    except Exception as e:
        print(f"An error occurred while writing to the file {e}")