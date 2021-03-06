import numpy as np
import cv2



def show_webcam(mirror=False):
    cc = "rtsp://101.95.3.151:554/1/stream1"
    cam = cv2.VideoCapture(cc)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=False)


if __name__ == '__main__':
    main()