import cv2 as cp
import numpy as np

canvas=np.zeros((500,500,3))
cp.line(canvas,(0,0),(100,100),(0,255,0),2,cp.LINE_4)
cp.line(canvas,(0,20),(120,120),(0,255,0),2,cp.LINE_AA)
cp.rectangle(canvas,(200,200),(250,270),(0,0,255),-1)
cp.circle(canvas,(250,250),10,(255,0,0),3)
cp.arrowedLine(canvas,(400,400),(400,500),(255,255,255),tipLength=0.5)
cp.imshow('image',canvas)
cp.waitKey()