# -*- coding: utf-8 -*-
"""hsv_costa-Pasta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fonTu-c_SDE4iaz4CzIsvYVBuX2Bjj3R
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
def printImage(img):
    fig=plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='k')
    plt.axis("off")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()    
def printImageGray(img):
    fig=plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='k')
    plt.axis("off")    
    plt.imshow(img, cmap='gray')
    plt.show()
def conect8(m, i,j,value):
    if i == 0 and j == 0:
        if m[i][j+1] == value:
            return True
        elif m[i+1][j+1] == value:
            return True
        elif m[i+1][j+1] == value:
            return True
        else:
            return False
    elif i == 0 and j == m.shape[1]-1:
        if m[i][j-1] == value:
            return True
        elif m[i+1][j-1] == value:
            return True
        elif m[i+1][j] == value:
            return True
        else:
            return False
    elif i == m.shape[0]-1 and j == 0:
        if m[i-1][j-1] == value:
            return True
        elif m[i-1][j+1] == value:
            return True
        elif m[i][j+1] == value:
            return True
        else:
            False
    elif i == m.shape[0]-1 and j == m.shape[1]-1:
        if m[i-1][j] == value:
            return True
        elif m[i-1][j-1] == value:
            return True
        elif m[i][j-1] == value:
            return True
        else:
            return False
    elif i == 0 and (j > 0 and j < m.shape[1]-1):
        if m[i][j-1] == value:
            return True
        elif m[i+1][j-1] == value:
            return True
        elif m[i+1][j] == value:
            return True
        elif m[i+1][j+1] == value:
            return True
        elif m[i][j+1] == value:
            return True
        else:
            return False
    elif (i > 0 and i < m.shape[0]-1) and j ==0:
        if m[i-1][j] == value:
            return True
        elif m[i-1][j+1] == value:
            return True
        elif m[i][j+1] == value:
            return True
        elif m[i+1][j+1] == value:
            return True
        elif m[i+1][j] == value:
            return True
        else:
            return False
    elif (i > 0 and i < m.shape[0]-1) and j == m.shape[1]-1:
        if m[i-1][j] == value:
            return True
        elif m[i-1][j-1] == value:
            return True
        elif m[i][j-1] == value:
            return True
        elif m[i+1][j-1] == value:
            return True
        elif m[i+1][j] == value:
            return True
        else:
            return False
    elif i == m.shape[0]-1 and (j > 0 and j < m.shape[1]-1):
        if m[i][j-1] == value:
            return True
        elif m[i-1][j-1] == value:
            return True
        elif m[i-1][j] == value:
            return True
        elif m[i-1][j+1] == value:
            return True
        elif m[i][j+1] == value:
            return True
        else:
            return False
    else:
        if m[i][j-1] == value:
            return True
        elif m[i+1][j-1] == value:
            return True
        elif m[i+1][j] == value:
            return True
        elif m[i+1][j+1] == value:
            return True
        elif m[i][j+1] == value:
            return True
        elif m[i-1][j-1] == value:
            return True
        elif m[i-1][j] == value:
            return True
        elif m[i-1][j+1] == value:
            return True
        else:
            return False

def linhaCosta(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#converte para hsv
    hsv = cv2.GaussianBlur(hsv, (5, 5), 5)
    b, g ,r = cv2.split(hsv)
    zeros = np.zeros(img.shape[:2], dtype = "uint8")
    b_3d = cv2.merge([b, zeros, zeros])
    ret1,th1 = cv2.threshold(b,65,255,cv2.THRESH_BINARY)#65
    im2, contours, hierarchy = cv2.findContours(th1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    img2 = img.copy()
    areas = [] 
    image_saida = np.zeros([img.shape[0], img.shape[1]], dtype=np.uint8)
    for i in range(0,len(contours)):
        area = cv2.contourArea(contours[i])
        areas.append(area)
    indiceAreaMaior = areas.index(max(areas))
    saida = cv2.drawContours(image_saida, contours, indiceAreaMaior, (255), -1)
    s = cv2.bitwise_not(saida)
    im3, contours2, hierarchy2 = cv2.findContours(s,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas2 = [] 
    image_saida2 = np.zeros([img.shape[0], img.shape[1]], dtype=np.uint8)
    contours2F = []
    for i in range(0,len(contours2)):
        area2 = cv2.contourArea(contours2[i])
        if area2 > 3000:
            contours2F.append(contours2[i])
        areas2.append(area2)
    indiceAreaMaior2 = areas2.index(max(areas2))
    saida2 = cv2.drawContours(image_saida2, contours2F, -1, (255), -1)    
    mask_inv = cv2.bitwise_not(saida2)
    imgOut = img.copy()
    for i in range(mask_inv.shape[0]):
        for j in range(mask_inv.shape[1]):
            if(mask_inv[i][j] == 0 and conect8(mask_inv,i,j, 255)):
                imgOut[i][j] = [0,255,0]
    return imgOut


def diferenca(img, imgV):
    linhaV = []
    linhaE = []
    for j in range(imgV.shape[1]):
      for i in range(imgV.shape[0]):
          if np.all(imgV[i][j] == [0, 255, 0], axis=0):
              linhaV.append(i)
              break
    for j in range(img.shape[1]):      
        for i in range(img.shape[0]):
            if i == img.shape[0]-1 and not(np.all(imgOut[i][j] == [0, 255, 0], axis=0)):
                linhaE.append(linhaE[-1])                
            elif np.all(imgOut[i][j] == [0, 255, 0], axis=0):
              linhaE.append(i)
              break    
    soma = 0
    for i in range(len(linhaV)):
      soma = abs(linhaE[i] - linhaV[i])
    return(soma/len(linhaE))

img = cv2.imread(file) 
imgOut = linhaCosta(img)
    