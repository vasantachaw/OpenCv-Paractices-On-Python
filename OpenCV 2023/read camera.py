import cv2 as cp
cap=cp.VideoCapture('k.mp4',0)
print('Height',cap.get(cp.CAP_PROP_FRAME_HEIGHT))
print('Width',cap.get(cp.CAP_PROP_FRAME_WIDTH))
print('fs',cap.get(cp.CAP_PROP_FPS))
while(cap.isOpened):
    ret,frame=cap.read()
    if ret==True:
        cp.imshow('video',frame)
        if cp.waitKey(10)==ord('q'):
            break
cap.release()
cp.destroyAllWindows()