import cv2
import serial.tools.list_ports
import os


t = serial.Serial()


def generateOneFrame(img):
    frame =[] # 一帧图像
    img = cv2.resize(img, (72, 39))
    channel = img.shape[2]
    for col in range(72):
        frame.append([0x00, 0x00, 0x00, 0x00])
        for row in range(39):
            oneData = [0xef] # 一个led的数据
            for c in range(channel):
                pix = img[row, col, c]
                oneData.append(pix)
            frame.append(oneData)
        frame.append([0xff, 0xff, 0xff, 0xff])
    return frame


def blue_tooth_connect():
    global t
    try:
        t = serial.Serial('com7', 38400)
    except OSError:
        pass


def send_images_by_dir(rootdir):
    global t
    images_list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(images_list)):
        path = os.path.join(rootdir, images_list[i])
        if os.path.isfile(path):
            img = cv2.imread(path)
            frame = generateOneFrame(img)
            t.writelines(frame)


def send_one_image(dir):
    global t
    img = cv2.imread(dir)
    frame = generateOneFrame(img)
    t.writelines(frame)


# 发送的图片
# img = cv2.imread('img/colorworld.jpg')
# t = serial.Serial('com7', 38400)
# frame = generateOneFrame(img)
# print(t.portstr)
# t.writelines(frame)

# t = serial.Serial('com7', 38400)
# rootdir = 'img'
# list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
# for i in range(0,len(list)):
#     path = os.path.join(rootdir,list[i])
#     if os.path.isfile(path):
#         print(path)
#         img = cv2.imread(path)
#         frame = generateOneFrame(img)
#         t.writelines(frame)



# 发送字符
# strInput = input('enter some words:')
# strInput = strInput.encode("utf-8")
# n = t.write(strInput)
# print(n)
# str = t.read(n)
# print(str)


# plist = list(serial.tools.list_ports.comports())
# if len(plist) <= 0:
#     print("没有发现端口!")
# else:
#     plist_0 = list(plist[0])
#     serialName = plist_0[0]
#     serialFd = serial.Serial(serialName, 38400, timeout=60)
#     print("可用端口名>>>", serialFd.name)


# img = cv2.imread("img/nnb.jpg")
# cv2.namedWindow('image')
# cv2.imshow('image', cv2.resize(img, (72, 39)))
# cv2.waitKey(0)