from flask import Flask, render_template, Response
from YOLOv8inferenceClass import ObjectDetection

app = Flask(__name__)

detector = ObjectDetection('video_2.mp4')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(detector.__call__(), mimetype='multipart/x-mixed-replace; boundary=frame')


app.run()

