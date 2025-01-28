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



#5---initializing web server
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <html>
                <head><title>DeepSeek R1 1.5 Web UI</title></head>
                <body>
                    <h1>DeepSeek R1 1.5 Web UI</h1>
                    <form action="/process" method="POST">
                        <label for="inputData">Enter Data:</label>
                        <input type="text" id="inputData" name="inputData" required>
                        <input type="submit" value="Process">
                    </form>
                </body>
                </html>
            ''')
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/process':
            # Parse the form data
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = parse_qs(post_data.decode('utf-8'))['inputData'][0]

            #request adding to queue for processing
            request_queue.put(data)

            #responding back
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f'''
                <html>
                <head><title>Processing...</title></head>
                <body>
                    <h1>Request Received</h1>
                    <p>Your request is being processed. Please wait.</p>
                </body>
                </html>
            '''.encode())


#6--running web server
def run_server():



#main thread
if __name__ == '__main__':
    run_server()
