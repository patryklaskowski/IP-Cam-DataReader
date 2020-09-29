from ip_camera import Ip_Camera
from flask import Flask, render_template, Response, url_for, request
from os import path
import sys
import argparse

from markupsafe import escape

basedir = path.abspath(path.dirname(__file__))

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', action='append', default=['http://162.245.149.145/mjpg/video.mjpg', 'http://174.6.126.86/mjpg/video.mjpg'])#required=True)#'http://213.193.89.202/mjpg/video.mjpg'
args = vars(parser.parse_args())
urls_flag = args['url']

print(f'-------------------\nURLS:\n{urls_flag}\n-------------------')

app = Flask(__name__)


@app.route('/')
def index():
    urls = urls_flag
    return render_template('index.html', urls_html=urls)


@app.route('/video_feed')
def video_feed():
    url = request.args.get('url')
    grayscale = bool(request.args.get('grayscale'))
    treshold = bool(request.args.get('treshold'))
    return Response(frame_generator(Ip_Camera(url, grayscale=grayscale, treshold=treshold)),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def frame_generator(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
