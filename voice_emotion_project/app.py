import json
import os
from flask import Flask
from flask import render_template, request, jsonify
from scripts import predict

app = Flask(__name__, static_folder='app/static', template_folder='app/templates')

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route("/upload-emotion", methods=["POST"])
def uploadImage():

    ''' This function recieves image from ajax and returns string to be printed below the image,
    containing prediction '''

    #get image from ajax
    voice_file = request.files['file']
    filepath = os.path.join(os.path.dirname(__file__) + "/app/voice", 'voice.wav')
    print(voice_file)

    #save our image
    voice_file.save(filepath)

    #get the prediction text
    msg = predict.predict_emotion(filepath)
    print(msg)
    return msg


def main():
    app.run(host='127.0.0.1', port=3001, debug=True)


if __name__ == '__main__':
    main()