import cv2
import requests
import numpy as np
import imutils


# чтение и отображение картинки
def printImage():
    # name = input("Введите адрес изображения: \n")
    name = "anakin.jpg"
    img = cv2.imread(name)
    cv2.namedWindow("Window1", cv2.WINDOW_NORMAL)
    # WINDOW_NORMAL - пользователь может изменять размер окна (без ограничений)
    # WINDOW_AUTOSIZE - пользователь не может изменить размер окна

    # меняем на чб
    gray1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Window1', gray1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# чтение и отображение видоса
def printVideo():
    # name = input("Введите адрес видео: \n")
    name = "space.mp4"
    cap = cv2.VideoCapture(name, cv2.CAP_ANY)

    ret, frame = cap.read()
    while True:
        ret, frame = cap.read()
        if not (ret):
            cv2.waitKey(0)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:  # 0xFF ждёт escape
            break

    cap.release()
    cv2.destroyAllWindows()


# чтение и запись с вебки компьютера
def readVideoWriteToFile():
    ip = int(input("С какой камеры будем вести запись? \n 0 - с компьютера \n 2 - с камеры телефона \n"))
    video = cv2.VideoCapture(ip)
    ok, img = video.read()
    w = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter("output.mov", fourcc, 25, (w, h))
    while (True):
        ok, img = video.read()
        cv2.imshow('img', img)
        video_writer.write(img)
        # Esc для выхода
        if cv2.waitKey(1) & 0xFF == 27:
            break
    video.release()
    cv2.destroyAllWindows()


# чтение и запись с камеры телефона
def phoneCamera():
    # домашняя сеть
    # url = "http://192.168.1.69:8080/shot.jpg"

    # сеть с телефона
    url = "http://10.118.229.44:8080/shot.jpg"

    # While для постоянного получения данных по url
    while True:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=1000, height=1800)
        cv2.imshow("Android_cam", img)

        # Esc для выхода
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()


# printImage()
# printVideo()
# readVideoWriteToFile()
phoneCamera()
