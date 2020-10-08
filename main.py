from ip_camera import Ip_Camera
from flask import Flask, render_template, Response, url_for, request
from os import path
import sys
import argparse


basedir = path.abspath(path.dirname(__file__))

parser = argparse.ArgumentParser()
defaults = ['http://174.6.126.86/mjpg/video.mjpg', 'http://213.193.89.202/mjpg/video.mjpg']
parser.add_argument('-u', '--url', action='append', default=defaults)#required=True)
args = vars(parser.parse_args())
urls_flag = args['url']

if len(urls_flag) > len(defaults):
	urls_flag = urls_flag[2:]

# http://213.193.89.202/mjpg/video.mjpg
# http://187.157.229.132/mjpg/video.mjpg
# 'http://162.245.149.145/mjpg/video.mjpg',

print(20*'-')
print(f'URLS to run:\n{urls_flag}')
print(20*'-')

app = Flask(__name__)

@app.route('/')
def index():
    urls = urls_flag
    return render_template('index.html', urls_html=urls, dir=basedir)


@app.route('/video')
def video():
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
