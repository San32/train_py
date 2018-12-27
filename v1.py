import cv2
cap = cv2.VideoCapture("rtsp://101.95.3.101:554/1/stream1")

while True:
    if cap.grab():
        flag, frame = cap.retrieve()
        if not flag:
            continue
        else:
            cv2.imshow('video', frame)
    if cv2.waitKeqy(10) == 27:
        break