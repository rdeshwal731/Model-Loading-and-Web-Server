# Task Objective:
1) Load a **DeepSeek R1 1.5** model without using any third-party libraries.
2) Implement a web server that:
     <br/>&emsp;(i)  Is connected to a simple web-based user interface (WebUI);
     <br/>&emsp;(ii)  Handles incoming requests, passes them to the model for processing, and returns the results to the client;
     <br/>&emsp;(iii)  Treats each request independently, with no shared context between requests;
     <br/>&emsp;(iv)  Queues multiple simultaneous requests and processes them sequentially, ensuring only one task is handled at a time.

## System Requirements:
1) Hardware-
     <br/>&emsp;(i)  Processor: Minimum Quad-core CPU (Intel i5/i7, AMD Ryzen 5/7);
     <br/>&emsp;(ii)  RAM: At least 16GB (Recommended: 32GB for large models);
     <br/>&emsp;(iii)  GPU (Optional but recommended for inference speed-up): NVIDIA GPU with CUDA support (e.g., RTX 3060);
     <br/>&emsp;(iv)  VRAM: Minimum 8GB, Recommended 12GB+;
     <br/>&emsp;(v)  Storage: At least 50GB of free disk space (for model and dependencies).

2) Software-
     <br/>&emsp;Operating System: Windows 10/11, Ubuntu 20.04+/Debian/macOS (M1/M2 with Rosetta)
---
## Libraries used: 
     torch
     Flask
     transformers
     queue
     
## Networking Requirements:
     Open port 5000 for Flask if accessing from other devices.
     Internet connection required for initial model download.
     

