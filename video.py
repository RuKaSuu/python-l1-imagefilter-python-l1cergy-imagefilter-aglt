import cv2

def VideoCapture(vidcap):
    count = 0
    vidcap = cv2.VideoCapture(f'video/{vidcap}')
    success, image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC, (count * 1000))
        cv2.imwrite("list_image/frame%d.jpg" % count, image)
        success, image = vidcap.read()
        count += 1
