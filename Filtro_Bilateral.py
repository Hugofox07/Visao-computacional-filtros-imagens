import cv2 as cv
import numpy as np 

path = 'visao_computacional.png'
img = cv.imread(path)
cv.imshow('Original', img)

# Filtro medianBlur deve ser um valor ímpar
bilateral = cv.bilateralFilter(img,d=13,sigmaColor=75,sigmaSpace=75)
cv.imshow('Janela_MedianBlur', bilateral)
cv.waitKey()
cv.destroyAllWindows()