# ip_camera.py

import cv2

class VideoCamera(object):
    def __init__(self, url):
        self.url = url
        self.video = cv2.VideoCapture(self.url)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        # image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        # gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

class VideoCamera_second(object):
    def __init__(self, url):
        self.url = url
        # self.video = cv2.VideoCapture(self.url)

    def __del__(self):
        # self.video.release()
        pass

    def get_frame(self):
        video = cv2.VideoCapture(self.url)
        success, image = video.read()
        video.release()
        # image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        # image=cv2.resize(image,None,fx=ds_factor,fy=ds_factor,interpolation=cv2.INTER_AREA)
        # gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

# class IpCam_my(object):
#
#     def __init__(self, url):
#         self.url = url
#         self.data_format = self.__get_data_format__()
#         assert self.data_format != '', 'Data format error.'
#
#     def __get_data_format__(self):
#         available_data_formats = ['.jpg', '.mjpg']
#         data_format = ''.join([data_format if data_format in self.url.lower() else '' for data_format in available_data_formats])
#         # print(f'Detected format: {data_format}.') if data_format != '' else print(f'Format ERROR!\nExpected to be one of {available_data_formats}.')
#         return data_format
#
#     def get_frame(self):
#         if self.data_format == '.jpg':
#             frame = self.__get_frame_jpg__()
#         elif self.data_format == '.mjpg':
#             frame = self.__get_frame_mjpg__()
#         else:
#             assert False, 'get_single_frame() else statement activated.'
#         return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).tobytes()
#
#     def __get_frame_mjpg__(self):
#         capture = cv2.VideoCapture(self.url)
#         retval, frame = capture.read()
#         capture.release()
#         return frame
#
#     def __get_frame_jpg__(self):
#         img_data = requests.get(self.url).content
#         arr = np.frombuffer(img_data, np.uint8)
#         return cv2.imdecode(arr, cv2.IMREAD_COLOR)
#
#
# class IpCam_his(object):
#
#     def __init__(self, url):
#         self.url = url
#         self.video = cv2.VideoCapture(self.url)
#
#     def __del__(self):
#         self.video.release()
#
#     def get_frame(self):
#         retval, frame = self.video.read()
#         return frame.tobytes()
