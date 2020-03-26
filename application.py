from flask import Flask, render_template, request
import json
from python_files.main  import generateResponse
import sys
# Elastic Beanstalk initalization
application = Flask(__name__)
application.debug=True

# change this to your own value
application.secret_key = 'cC1YCIWOj9GkjbkjbkjbgWspgNEo2'   

@application.route('/', methods=['POST'])
def index():

    '''
        
             { {
                "by":"server",
                "userId":'123',
                "text":"Hello, what would you like to do?",
                "time":"UNIX_TIMESTAMP"
                }
            }
    '''
    message = {} 
    message[ 'sender' ] = { 'id': request.form['userId']   } 
    message[ 'message'] = {
        'text' : request.form['text']
    }
    if request.files:
        message['message']['attachment'] = {}
        files_dict = request.files.to_dict()
        for fileName,fileObject in files_dict.items():
            fileObject.save( fileName )
            message['message']['attachment']['name'] = fileName
            fileType = 'image'
            if fileObject.content_type.find('application') != -1:
                fileType = 'file'
            
            message['message']['attachment']['type'] = fileType    
    print(message)
    
    #print(generateResponse( message ))       
         
        

    return render_template('index.html')
if __name__ == '__main__':
    application.run(host='127.0.0.1')