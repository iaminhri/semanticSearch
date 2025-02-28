from django.shortcuts import render
from django.http import HttpResponse
from . import searchEmbeddings
from searchApp.models import UserData

# Create your views here.

def home(request):
    return render(request, 'home.html')

def searchQuery(request):
    embeddings = searchEmbeddings.loadEmbeddings()

    searchQuery  = request.GET['searchInput']
    
    if(searchQuery == ""):
        return render(request, 'home.html')
    
    searchList = [item.strip() for item in searchQuery.split(',')]

    searchQuery = searchEmbeddings.searchInEmbeddingsDB_multiquery(searchList, embeddings)

    return render(request, 'home.html', {'search_query':searchQuery}) 

def server(request):
    userdata = UserData.objects.all()
    return render(request, 'servefiles.html', {'userdata': userdata})