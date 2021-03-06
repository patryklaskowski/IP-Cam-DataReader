# IP-Cam-DataReader

[![made-with-Python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-Flask](https://img.shields.io/badge/Made%20with-Flask-1f425f.svg)](https://palletsprojects.com/p/flask/)
[![made-with-OpenCV](https://img.shields.io/badge/Made%20with-OpenCV-1f425f.svg)](https://docs.opencv.org/)

---

Web page application that live stream video from multiple IP cameras.
With little customization application of any video filter or machine learning algorithm should be easy.


#### 1. Download github repository
```
git clone https://github.com/patryklaskowski/IP-Cam-DataReader.git
cd IP-Cam-DataReader
```
#### 2. It is reccomended to run virtual environment to prevent version problems.
```
python3.7 -m venv env
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

![Terminal screenshot](https://github.com/patryklaskowski/IP-Cam-DataReader/blob/master/templates/static/terminal.png)

**[NOTE:]**<br>
> Use flag `-u` or `--url` to add custom video sources<br>
> e.g. `python main.py --url http://187.157.229.132/mjpg/video.mjpg --url http://162.245.149.145/mjpg/video.mjpg`<br>
> This example source data from two IP cameras. There is no limits on urls count.

There are many unsecured IP cams to explore [here](https://www.insecam.org/en/byrating/).

That's it. App should be now up and running on **http://0.0.0.0:5000/**.
You are also able to visit this page from other devices in the same local area network.

![Application screenshot](https://github.com/patryklaskowski/IP-Cam-DataReader/blob/master/templates/static/home_page.png)

Once you're done close the app by pressing `ctrl+c` in terminal.

#### 5. Deactivate virtual environment
```
deactivate
```

---
### TODO:
- [x] support .mjpg file type
- [ ] support .jpg file type
- [ ] add modeule that create full url link to video just by providing IP and PORT number. [This database might help](https://www.ispyconnect.com/sources.aspx).
