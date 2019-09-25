import numpy as np
import matplotlib.pyplot as plt
import cv2

def printImage(img):
    fig=plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='k')
    plt.axis("off")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()

def pontoY(x, linha):
    r = linha[0][0]    
    t = linha[0][1]    
    a = np.cos(t)
    b = np.sin(t)
    x0 = a*r
    y0 = b*r
    pi = int((x - x0)/-b )    
    pY = int(y0 + pi*(a))
    return pY

def diferenca(img, imgV):
    
    linhaV = []
    linhaE = []
    for j in range(imgV.shape[1]):
      for i in range(imgV.shape[0]):
          if np.all(imgV[i][j] == [0, 0, 0], axis=0):
              linhaV.append(i)
              break
    for j in range(img.shape[1]):      
        for i in range(img.shape[0]):
            if np.all(img[i][j] == [0, 255, 0], axis=0):
              linhaE.append(i)
              break    
    soma = 0
    for i in range(len(linhaV)):
      soma = soma + abs(linhaE[i] - linhaV[i])
    return(soma/len(linhaE))

def linhaHorizonte(_img):
    hsv = cv2.cvtColor(_img, cv2.COLOR_BGR2HSV)#converte para hsv
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)
    h, s, v = cv2.split(blur)
    
    sobely = cv2.Sobel(v,cv2.CV_64F,0,1,ksize=5)
    abs_sobel64f = np.absolute(sobely)
    kernel = np.ones((3,3))
    erosion2 = cv2.erode(abs_sobel64f,kernel,iterations = 1)
    scale_factor = np.max(erosion2)/255
    grad = (erosion2/scale_factor).astype(np.uint8)
    edges = cv2.Canny(grad,90,100)
    
    lines = cv2.HoughLines(edges,1,np.pi/180,100)
    
    menor_rho = lines[0][0][0]*2
    indice = 0
    img2 = _img.copy()
    
    for i in range(0,6):        
        y0 = pontoY(_img.shape[1]//2,lines[i])
        if y0 < menor_rho:
            menor_rho = y0
            indice = i
    
    for rho,theta in lines[indice]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 2000*(-b))
        y1 = int(y0 + 2000*(a))
        x2 = int(x0 - 2000*(-b))
        y2 = int(y0 - 2000*(a))
    cv2.line(img2,(x1,y1),(x2,y2),(0,255,0),1)
    
    return img2



img = cv2.imread(file)
imgSaida= linhaHorizonte(img)