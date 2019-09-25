import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cv2
import networkx as nx

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
            grafo.add_node(cont , i = i, j = j, weight = im[i][j])
            cont +=1
def init_link(grafo, im,t,pH):    
    for j in range(im.shape[1]):
        for h in range(im.shape[0]):
            #t = 5
            s=0
            pesoH = h*pH
            g1 = getIdNo(h,j,im)
            if h >0 and h < im.shape[0]-1 and j < im.shape[1]-1:                
                
                g2 = getIdNo(h-1,j+1, im)
                g3 = getIdNo(h,j+1, im)
                g4 = getIdNo(h+1,j+1, im)
                
                c12 = (im[h][j]+pesoH)*t+im[h-1][j]*t+s
                c13 = (im[h][j]+pesoH)*t+im[h][j]*t
                c14 = (im[h][j]+pesoH)*t+im[h+1][j]*t+s
                grafo.add_edge(g1, g2, weight = c12)
                grafo.add_edge(g1, g3, weight = c13)
                grafo.add_edge(g1, g4, weight = c14)
                if j == 0:
                    c = h**2
                    grafo.add_edge(0, g1, weight = c)
            elif h == 0 and j < im.shape[1]-1:
                               
                g3 = getIdNo(h,j+1, im)
                g4 = getIdNo(h+1,j+1, im)
                
                c13 = (im[h][j]+pesoH)*t+im[h][j]*t
                c14 = (im[h][j]+pesoH)*t+im[h+1][j]*t+s
                grafo.add_edge(g1, g3, weight = c13)
                grafo.add_edge(g1, g4, weight = c14)
                if j == 0:
                    c = h**2
                    grafo.add_edge(0, g1, weight = c)
            elif h == im.shape[0]-1 and j < im.shape[1]-1:
                g2 = getIdNo(h-1,j+1, im)
                g3 = getIdNo(h,j+1, im)
                c12 = (im[h][j]+pesoH)*t+im[h-1][j]*t+s
                c13 = (im[h][j]+pesoH)*t+im[h][j]*t                
                grafo.add_edge(g1, g2, weight = c12)
                grafo.add_edge(g1, g3, weight = c13)
                if j == 0:                    
                    c = h**2
                    grafo.add_edge(0, g1, weight = c)
            elif  j == im.shape[1]-1:
                c = h**2
                grafo.add_edge(g1, 1, weight = c)

def encontra_linha2(img,t,pH):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#converte para hsv
    hsv = cv2.GaussianBlur(hsv, (3, 3), 5)
    
    h, s, v = cv2.split(hsv)
    edge = cv2.Canny(v, 10,40)    
    
    edge_inv = cv2.bitwise_not(edge)    
    DG = nx.DiGraph()
    init_vertices(DG, edge_inv)
    init_link(DG, edge_inv,t, pH)
    img2 = img.copy()
    length, path = nx.single_source_dijkstra(DG, 0, 1)
    newPath = path[1:len(path)-1]
    for i in newPath:
        l = DG.nodes[i]['i']
        c = DG.nodes[i]['j']
        img2[l][c] = [0,255,0]        
    return (img2,edge_inv, edge)

img = cv2.imread('../base_imagens/original_p/boa_viagem_09072016-108.png')
img2, edge_inv, edge = encontra_linha2(img, 4,0)
printImage(img2)
printImageGray(edge)

