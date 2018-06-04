from flask import Flask, request
from datetime import date
import os

app = Flask(__name__)

# The following two lines will allow all URIs. This stores path name in Variable path
@app.route('/', defaults={'path':''})
@app.route('/<path:path>', methods=['GET','POST','PUT','DELETE','HEAD'])
def all_requests(path):

    #create a logging Directory in container if none exists
    if not os.path.exists("/tmp/logs/"):
        os.makedirs("/tmp/logs/")

    today = str(date.today())

    try:
        log_file_name = '/tmp/logs/log-' + today + '.txt'
        log_file = open(log_file_name,'a')
        log_file.write("{ 'method' : '" + request.method + "', 'uri' : '/" + path + "'}\n")
        log_file.close()
    except Exception as e:
        return 'Error : %s' %str(e)
    return 'Successfully Loggged ' + request.method +  ' Request: ' + path

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=3000)
