from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__, static_folder="static")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/streaming')
def webcam():
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return render_template('streaming.html', alphabet=ALPHABET)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/streaming-2')
def webcam2():
    return render_template('streaming-2.html')


@app.route('/streaming-3')
def webcam3():
    return render_template('streaming-3.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
