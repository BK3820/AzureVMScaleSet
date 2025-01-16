from flask import Flask, send_from_directory
import socket

app = Flask(__name__)

# Serve the index.html file
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Dynamic endpoint to fetch the VM name (local hostname)
@app.route('/vm-name')
def vm_name():
    return socket.gethostname()

if __name__ == '__main__':
    app.run()
