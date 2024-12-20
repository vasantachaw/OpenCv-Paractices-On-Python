import cv2 as cp
imge=cp.imread('g.jpg',cp.IMREAD_UNCHANGED)
imge=cp.resize(imge,(500,700))
cp.imshow('Image',imge)
cp.waitKey()
