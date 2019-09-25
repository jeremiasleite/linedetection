import numpy as np
import matplotlib.pyplot as plt
import cv2
import networkx as nx


def printImage(img):
    fig=plt.figure(figsize=(10, 10), dpi= 80, facecolor='w', edgecolor='k')
    plt.axis("off")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show()    
def printImageGray(img):
    fig=plt.figure(figsize=(8, 8), dpi= 120, facecolor='w', edgecolor='k')
    plt.axis("off")    
    plt.imshow(img, cmap='gray')
    plt.show()

def diferenca(img, imgV):
    #print(img.shape,imgV.shape)
    linhaV = []
    linhaE = []
    for j in range(imgV.shape[1]):
      for i in range(imgV.shape[0]):
          if np.all(imgV[i][j] == [0, 255, 0], axis=0):
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

def getIdNo(i,j, img):
    g = (i*img.shape[1])+j+2
    return g
def init_vertices(grafo, im):
    grafo.add_node(0, i = -1, j = -1)#Nó inicial s 
    grafo.add_node(1, i = -1, j = -1)#Nó Final t
    cont = 2
    N = im.shape[1]-1
    for i in range(im.shape[0]):   
        for j in range(im.shape[1]):
            #y = functionCostY(i, j, N)            
            grafo.add_node(cont , i = i, j = j, weight = im[i][j])
            cont +=1
def init_link(grafo, im,t,u):    
    for j in range(im.shape[1]):
        for h in range(im.shape[0]):
            #t = 5
            g1 = getIdNo(h,j,im)
            if h >0 and h < im.shape[0]-1 and j < im.shape[1]-1:                
                
                g2 = getIdNo(h-1,j+1, im)
                g3 = getIdNo(h,j+1, im)
                g4 = getIdNo(h+1,j+1, im)
                
                c12 = im[h][j]*t+im[h-1][j]*t+u
                c13 = im[h][j]*t+im[h][j]*t
                c14 = im[h][j]*t+im[h+1][j]*t+u
                grafo.add_edge(g1, g2, weight = c12)
                grafo.add_edge(g1, g3, weight = c13)
                grafo.add_edge(g1, g4, weight = c14)
                if j == 0:
                    c = (h-im.shape[1]//2)**2
                    grafo.add_edge(0, g1, weight = c)
            elif h == 0 and j < im.shape[1]-1:
                               
                g3 = getIdNo(h,j+1, im)
                g4 = getIdNo(h+1,j+1, im)
                
                c13 = im[h][j]*t+im[h][j]*t
                c14 = im[h][j]*t+im[h+1][j]*t+u
                grafo.add_edge(g1, g3, weight = c13)
                grafo.add_edge(g1, g4, weight = c14)
                if j == 0:
                    c = (h-im.shape[1]//2)**2
                    grafo.add_edge(0, g1, weight = c)
            elif h == im.shape[0]-1 and j < im.shape[1]-1:
                g2 = getIdNo(h-1,j+1, im)
                g3 = getIdNo(h,j+1, im)
                c12 = im[h][j]*t+im[h-1][j]*t+u
                c13 = im[h][j]*t+im[h][j]*t                
                grafo.add_edge(g1, g2, weight = c12)
                grafo.add_edge(g1, g3, weight = c13)
                if j == 0:
                    c = (h-im.shape[1]//2)**2
                    grafo.add_edge(0, g1, weight = c)
            elif  j == im.shape[1]-1:
                c = (h-im.shape[1]//2)**2                
                grafo.add_edge(g1, 1, weight = c)
def encontra_linha(_img,t,u):
    hsv = cv2.cvtColor(_img, cv2.COLOR_BGR2HSV)#converte para hsv
    hsv = cv2.GaussianBlur(hsv, (9, 9), 0)#melhor resultado com 9x9
    h, s ,v = cv2.split(hsv)
    edge = cv2.Canny(h,50,40)#melhor resultado com 50 x40
    edge_inv = cv2.bitwise_not(edge)
    DG = nx.DiGraph()
    init_vertices(DG, edge_inv)
    init_link(DG, edge_inv,t,u)
    img2 = _img.copy()
    length, path = nx.single_source_dijkstra(DG, 0, 1)
    newPath = path[1:len(path)-1]    
    for i in newPath:
        l = DG.nodes[i]['i']
        c = DG.nodes[i]['j']
        img2[l][c] = [0,255,0]        
    return img2


img = cv2.imread(file)
imgOut = encontra_linha(img, 10,100)
    