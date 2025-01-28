#libraries
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify, render_template_string
from threading import Thread
from queue import Queue
import time


#1--ds model loading
def load_model():
    model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    print("Model loaded successfully!")
    return model, tokenizer

model, tokenizer = load_model()
app = Flask(__name__)


#2--queeue for request/query handling 
query_queue = Queue() 


#3--request/query processing in background and in sequence #worker threads
def worker_process(): 
    while True:
        func, args = query_queue.get() 
        func(*args)
        query_queue.task_done() 


processing_thread = Thread(target=worker_process, daemon=True) 
processing_thread.start() 


#4--Loading model and starting a eorker thread



#5---initializing simple web-UI
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DeepSeek R1 Chatbot</title>  <!-- Changed title -->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background-color: #f4f4f4; 
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            width: 80%;
            max-width: 800px;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
        }
        textarea {
            width: 100%;
            height: 120px; 
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box; 
            font-size: 16px; 
        }
        button {
            padding: 12px 25px; 
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px; 
        }
        button:hover {
            background-color: #218838; 
        }
        #response {
            margin-top: 25px; 
            padding: 15px; 
            border: 1px solid #ddd; 
            border-radius: 4px;
            background-color: #f9f9f9; 
            white-space: pre-wrap;
            font-size: 16px; 
        }
        #response.processing::before { 
            content: 'Processing... ';
            display: block;
            color: #777;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container"> <!-- Added container div -->
        <h1>DeepSeek R1 Chatbot</h1> <!-- Changed heading -->
        <form id="query-form">
            <textarea id="query" placeholder="Ask me anything..."></textarea><br> <!-- Changed placeholder -->
            <button type="button" onclick="sendQuery()">Get Response</button> <!-- Changed button text -->
        </form>
        <div id="response"></div>
    </div>
    <script>
        async function sendQuery() {
            const queryInput = document.getElementById("query"); 
            const query = queryInput.value;
            const responseDiv = document.getElementById("response");

            if (!query.trim()) { 
                responseDiv.textContent = "Please enter a query.";
                return;
            }

            responseDiv.classList.add('processing'); 

            try {
                const response = await fetch("/process", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ query })
                });

                const result = await response.json();
                responseDiv.textContent = result.response;
            } catch (error) {
                responseDiv.textContent = "Error: " + error.message;
            } finally {
                responseDiv.classList.remove('processing'); 
                queryInput.value = ''; 
            }
        }
    </script>
</body>
</html>
"""




#6--running web server




#main thread

