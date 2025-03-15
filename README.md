<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

![GitHub followers](https://img.shields.io/github/followers/iaminhri?style=for-the-badge&logo=github)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/iaminhri/semanticSearch?style=for-the-badge&logo=github)

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="reports/">
    <img src="images/result.jpg" alt="Logo" width="1080" height="420">
  </a>

  <h3 align="center">AI Video Retrieval: A Semantic Search & Timestamp Alignment System</h3>

  <p align="center">
    View Project
    <br />
    <a href="#usage">View Demo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#project-summary">Project Summary</a>
      <ul>
        <li>
          <a href="#built-with">Our Goal</a>
          <a href="#objectives">Objectives</a>
        </li>
      </ul>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Installation, Building, and Running the Project</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#top-contributors">Top Contributors</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The AI Video Retrieval (AIVR) system enhances video search by integrating deep learning models for speech recognition, image captioning, and embedding generation. It uses txtai for indexing and Django for integration, enabling real-time video processing and semantic search. The system retrieves precise video timestamps based on natural language queries. A usability study confirms its improved retrieval accuracy and efficiency over traditional methods. Future extensions include OCR, object detection, and action recognition for enhanced relevance.

## Project Summary  

### Our Goal  
To develop an AI-powered video retrieval system that enables precise semantic search within videos by leveraging deep learning models for automatic speech recognition, image captioning, and embedding generation. The system aims to enhance retrieval accuracy, efficiency, and usability by indexing multimodal data and providing timestamp-aligned search results, with potential extensions for OCR, object detection, and action recognition.
The content will be formatted for various platforms, including:

---

### Objectives  
- **Develop an AI-driven semantic video retrieval system** – Leverage deep learning models for speech recognition, image captioning, and embedding generation to enable accurate and efficient video search.
- **Enhance retrieval accuracy and timestamp precision** – Implement multimodal indexing and vector embeddings to improve search relevance and ensure precise timestamp alignment for retrieved segments.
- ** Ensure scalability and real-time processing** – Design a framework that supports real-time video uploads, indexing, and search queries while allowing future enhancements like OCR, object detection, and action recognition.
---

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [![Docker][Docker.com]][Docker-url]
* [![Django][Django.com]][Django-url]
* [![Python][Python.com]][Python-url]
* [![HTML][HTML.com]][HTML-url]
* [![CSS][CSS.com]][CSS-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

The project can be viewed and run locally by installing the following tools.

### Installation, Building, and Running the Project

1. Install Docker Container
 ```sh
 https://www.docker.com/products/docker-desktop/
 ```
2. Install GitHub
 ```sh
 https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/installing-github-desktop
 ```
3. Use Git Clone to create a local repo
 ```sh
 git clone https://github.com/iaminhri/semanticSearch.git
 cd semanticSearch
 ```
4. Build the docker project by using the docker-compose-deploy.yml file.
 ```sh
 docker-compose -f docker-compose-deploy build
 ```
5. Run the Project:
 ```sh
 docker-compose -f docker-compose-deploy up
 ```
6. Access The Website:
 ```sh
 127.0.0.1:8080
 ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

# AI Video Retrieval System

## Query & Retrieval
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/query_retrieval.png)

## Query & Retrieval - Compact View
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/result.jpg)

## Upload Videos
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/uploadForm.png)

## Video Archive and Index
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/IndexVideos.png)

## Single Query Search
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/Single%20Query.png)

## Multiple Query Search
![Web Interface: Home Page](https://github.com/iaminhri/semanticSearch/blob/master/images/MultipleQuery.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/iaminhri/semanticSearch/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=iaminhri/semanticSearch" />
</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

The authors wish to acknowledge the Responsible & Applied Machine Learning Laboratory (RAML Lab) at the Department of Computer Science, Brock University, Canada.


<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Docker.com]: https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green
[Django-url]: https://www.djangoproject.com/

[Python.com]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[HTML.com]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5

[CSS.com]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://developer.mozilla.org/en-US/docs/Web/CSS

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

