# Model Loading and Web Server using python

## Description
A Flask-based web application utilizing the DeepSeek-R1-Distill-Qwen-1.5B model for natural language processing. The chatbot provides an interactive interface for users to input queries and receive AI-generated responses.
<br/>&emsp;
## Task Objective:

1) Load a **DeepSeek R1 1.5** model without using any third-party libraries.
<br/>&emsp;
2) Implement a web server that:
 <br/>&emsp;
     <br/>&emsp;(i)  Is connected to a simple web-based user interface (WebUI);
     <br/>&emsp;(ii)  Handles incoming requests, passes them to the model for processing, and returns the results;
     <br/>&emsp;(iii)  Treats each request independently, with no shared context between requests;
     <br/>&emsp;(iv)  Queues multiple simultaneous requests and processes them sequentially, ensuring only one
   <br/>&emsp;&emsp;task is handled at a time.

## Table of Contents
- [Setting-up](#Installation)
- [Running up](#Running-the-Application)
- [API Endpoints](#API-Endpoints)
- [System](#System-Requirements)
- [Libraries](#Libraries-used)
- [Networking](#Networking-Requirements)
- [License](#License)

## Installation
&emsp;1. Clone this repository: 
<br/>&emsp;&emsp;&emsp;https://github.com/rdeshwal731/Model-Loading-and-Web-Server/tree/master
<br/>&emsp;
<br/>&emsp;2. Create a virtual environment:
<br/>&emsp;&emsp;&emsp;python3 -m venv venv
<br/>&emsp;&emsp;&emsp;source venv/bin/activities '#' On Windows: venv\Scripts\activate
<br/>&emsp;
<br/>&emsp;3. Install dependencies:
<br/>&emsp;&emsp;&emsp;install all the [libraries](#librariesused)
<br/>&emsp;
<br/>&emsp;4. If using a GPU, install PyTorch with CUDA support:
<br/>&emsp;&emsp;&emsp;pip install torch torchvision torchaudio --index-url <br/>&emsp;&emsp;&emsp;https://download.pytorch.org/whl/cu118
<br/>&emsp;

## Running the Application
<br/>&emsp;1. Start the Flask application:
<br/>&emsp;<br/>&emsp;python webapp.py
<br/>&emsp;
<br/>&emsp;2. Open a web browser and go to:
<br/>&emsp;<br/>&emsp;http://127.0.0.1:5000
<br/>&emsp;

## API Endpoints
<br/>&emsp;GET/ - Renders the interface.
<br/>&emsp;
<br/>&emsp;POST /process - Processes user queries/requests AI-generated responses.
<br/>&emsp;

## System Requirements
1) Hardware-
 <br/>&emsp;
     <br/>&emsp;(i)  Processor: Minimum Quad-core CPU (Intel i5/i7, AMD Ryzen 5/7);
   <br/>&emsp;
     <br/>&emsp;(ii)  RAM: At least 16GB (Recommended: 32GB for large models);
   <br/>&emsp;
     <br/>&emsp;(iii)  GPU (Optional but recommended for inference speed-up): NVIDIA GPU with CUDA support                <br/>&emsp;&emsp;(e.g., RTX 3060);
   <br/>&emsp;
     <br/>&emsp;(iv)  VRAM: Minimum 8GB, Recommended 12GB+;
   <br/>&emsp;
     <br/>&emsp;(v)  Storage: At least 50GB of free disk space (for model and dependencies).
   <br/>&emsp;

2) Software-
   <br/>&emsp;
     <br/>&emsp;Operating System: Windows 10/11, Ubuntu 20.04+/Debian/macOS (M1/M2 with Rosetta)
   <br/>&emsp;
---
## Libraries used: 
     torch
     Flask
     transformers
     queue
     
## Networking Requirements:
     Open port 5000 for Flask if accessing from other devices.
     Internet connection required for initial model download.

## License
This project is under the MIT License
     

