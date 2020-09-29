# IP-Cam-DataReader

[![made-with-Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-Flask](https://img.shields.io/badge/Made%20with-Flask-1f425f.svg)](https://palletsprojects.com/p/flask/)
[![made-with-OpenCV](https://img.shields.io/badge/Made%20with-OpenCV-1f425f.svg)](https://docs.opencv.org/)

---

#### 1. Download github repository
```
git clone https://github.com/patryklaskowski/IP-Cam-DataReader.git
cd IP-Cam-DataReader
```
#### 2. It is reccomended to run virtual environment to prevent version problems.
```
python3 -m venv env
source env/bin/activate
```
#### 3. Install required libraries
```
pip install -r requirements.txt
```
#### 4. Run app
```
python main.py
```
> [NOTE:]
> Use flag `-u` or `--url` to add custom video sources
> e.g. `python main.py --url http://187.157.229.132/mjpg/video.mjpg --url http://162.245.149.145/mjpg/video.mjpg`
> This will source data from two IP cameras.

That's it. App should be now up and running on **http://0.0.0.0:5000/**.
You are also able to visit this page from other devices in the same local area network.

Once you're done close the app by pressing `Ctrl+c` or `Cmd+c` in terminal.

#### 5. Deactivate virtual environment
```
deactivate
```

---
