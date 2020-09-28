from ip_camera import VideoCamera, VideoCamera_second #IpCam_my, IpCam_his
from flask import Flask, render_template, Response
from os import path
import sys

app = Flask(__name__)

basedir = path.abspath(path.dirname(__file__))
url = 'http://213.193.89.202/mjpg/video.mjpg'

@app.route('/')
def index():
    return render_template('index.html')

def frame_generator(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global url
    return Response(frame_generator(VideoCamera(url)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_second')
def video_feed_second():
    global url
    return Response(frame_generator(VideoCamera_second(url)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed_his')
# def video_feed_his():
#     global url
#     return Response(frame_generator_his(IpCam_his(url)),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
