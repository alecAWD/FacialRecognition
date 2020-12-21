# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:25:51 2019

@author: amd6563
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import argparse
import os
import json

import facialRecognition
import webcamSnapshotGenerator



class S(BaseHTTPRequestHandler):

    def do_GET(self):
        rootdir = os.getcwd() 
  
        try:
            print(rootdir + self.path)
            
            path = self.path.split("?",1)[0]
            if path == '/':
                self.path += 'index.html'   # default to index.html
             
            elif path == '/register':
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin","*")
                self.send_header("Access-Control-Allow-Methods","*")
                self.send_header("Access-Control-Allow-Headers","*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                model = facialRecognition.buildNetwork()
                
                webcamSnapshotGenerator.create_User()
                facialRecognition.fit_evaluate_Model(model)
                facialRecognition.serialize_Model(model)
                facialRecognition.serialize_Weights(model)
                
            #files of front-end    
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))  
                f.close()  
            elif self.path.endswith('.js'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header("Content-type", "application/javascript")
                self.end_headers()
                self.wfile.write(f.read().encode('utf-8'))  
                f.close()
            else:
                self.send_error(404, 'file not supported')  
                
        except IOError:
            self.send_error(404, 'file not found') 
            


    def do_POST(self):
    # Doesn't do anything with POST yet
       #self.send_error(404, 'POST not supported')
        rootdir = os.getcwd() 
  
        try:
            print(rootdir + self.path)
            
            path = self.path.split("?",1)[0]
            if path == '/':
                self.path += "index.html"   # default to Home.html

            elif path == '/login':
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin","*")
                self.send_header("Access-Control-Allow-Methods","*")
                self.send_header("Access-Control-Allow-Headers","*")
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                
                # call the prediction function in ml.py
                result = facialRecognition.predict()
                
                # make a dictionary from the result
                resultObj = { "result": result }
                
                # convert dictionary to JSON string
                resultString = json.dumps(resultObj)
                
                self.wfile.write(resultString.encode('utf-8'))
                
        
                
        except IOError:
            self.send_error(404, 'file not found') 
        

def run(server_class=HTTPServer, handler_class=S, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting server on {addr}:{port}")
    httpd.serve_forever()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
       "-l",
       "--listen",
       default="localhost",
       help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
       "-p",
       "--port",
       type=int,
       default=8000,
       help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)