import cv2 # 调用摄像头：pip install opencv-python
import ocr
'''
利用摄像头拍摄并识别文字
'''
if __name__ == '__main__':
    cv2.namedWindow('camera',1) # 创建一个固定窗口 1为固定
    video='http://admin:admin@192.168.1.1:8081/video' # 视频流来源
    capture=cv2.VideoCapture(video) # 调用摄像头

    while True:
        success,img = capture.read()
        cv2.imshow('camera',img)
        # 按键处理
        key=cv2.waitkey(10) # 帧率??
        if key == 27: # ascii esc:27
            print('退出程序')
            break
        if key == 32: # ascii space:32
            filename = '照片.jpg'
            cv2.imwriter(filename,img) # 写入文件（文件路径，文件类型）
            s = ocr.img_to_str(filename)
            print(s)
    capture.release() # 释放摄像头
    cv2.destroyWindow('camera') # 关闭窗口