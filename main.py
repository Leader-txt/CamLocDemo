import cv2
import numpy

# mtx = numpy.array([[552.55515494,0,381.34840949],[ 0,540.09716608,200.47852233],[0,0,1]])
# dist = numpy.array([[0.041228,0.2283424,-0.01510533,0.03421304,-0.41339633]])
mtx = numpy.array([numpy.fromfile('mtx.bin')[i*3:i*3+3] for i in range(3)])
dist = numpy.fromfile('dist.bin')
cap = cv2.VideoCapture(0)
img = cap.read()[1]
h,w = img.shape[:2]
cv2.namedWindow('calibresult')
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
mtx_inv = numpy.linalg.inv(newcameramtx)
Zc = 505# 对窗口的鼠标动作做出回应
f = 0.1

# 鼠标回调函数，传入到callback参数上去
def mouse_callback(event, x, y, flags, userdata):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        print(numpy.dot(Zc,numpy.dot(numpy.linalg.pinv(numpy.array([[f,0,0,0],[0,f,0,0],[0,0,1,0]])),numpy.dot(mtx_inv,numpy.array([x,y,1])))))

cv2.setMouseCallback('calibresult', mouse_callback)
while 1:
    img = cap.read()[1]
    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
    # 剪裁图像
    x, y, w, h = roi
    # dst = dst[y:y+h, x:x+w]
    # cv2.rectangle(dst,(150,150),(176,176),(0,0,255))
    cv2.imshow('calibresult', dst)
    cv2.waitKey(1)