# ip_camera.py
import cv2

class Ip_Camera(object):
    def __init__(self, url, grayscale=False, treshold=False):
        self.url = url
        self.video = cv2.VideoCapture(self.url)
        self.grayscale = bool(grayscale)
        self.treshold = bool(treshold)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()

        if self.grayscale:
            image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        elif self.treshold:
            image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
            cret, image = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY)
        else:
            image = self.draw_text(image, text=self.url)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def draw_text(self, image, text='default'):
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (int(image.shape[1]/10), int(image.shape[0]/2))
        fontScale = int(0.0025 * image.shape[0])
        color = (0, 0, 255) #BGR
        thickness = 2 #px
        return cv2.putText(image, text, position, font, fontScale, color, thickness, cv2.LINE_AA)

    def treshold_filter(self, image, tresh=50):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image[image < tresh] = 255
        image[image >= tresh] = 0
        return image

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
