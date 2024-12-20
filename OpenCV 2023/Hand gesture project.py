import cv2 as cp
import numpy as np

hand = cp.imread('gg.jpg', 0)
hand = cp.resize(hand, (550, 650))
#cp.imshow('Original IMage', hand)
ret, the = cp.threshold(hand, 70, 255, cp.THRESH_BINARY)

_, contour ,_ = cp.findContours(the.copy(), cp.RETR_TREE, cp.CHAIN_APPROX_SIMPLE)

hull = [cp.convexHull(c) for c in contour]
final = cp.drawContours(hand, hull, -1, (255, 0, 0))
cp.imshow('Original IMage', hand)
cp.imshow('Threshhold image', the)
cp.imshow('Convex image', final)

cp.waitKey(0)
cp.destroyAllWindows()
