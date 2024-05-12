import cv2
import numpy as np
import random

def apply_watershed(image):
    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica um filtro gaussiano para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Aplica a detecção de bordas Canny
    edges = cv2.Canny(blurred, 30, 100)
    
    # Encontra os contornos na imagem
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Cria uma imagem de marcadores
    markers = np.zeros(gray.shape, dtype=np.int32)
    
    # Desenha os contornos na imagem de marcadores
    for i in range(len(contours)):
        cv2.drawContours(markers, contours, i, (i+1), -1)
    
    # Adiciona o marcador de fundo
    cv2.circle(markers, (5, 5), 3, (255, 255, 255), -1)
    
    # Aplica o algoritmo Watershed
    markers = cv2.watershed(image, markers)
    
    # Cria uma imagem colorida para visualização das regiões
    color_map = np.zeros(image.shape, dtype=np.uint8)
    
    # Define uma lista de cores específicas para cada região
    colors = [
        (255, 0, 0),     # Azul
        (0, 255, 0),     # Verde
        (0, 0, 255),     # Vermelho
        (255, 255, 0),   # Ciano
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Amarelo
        # Adicione mais cores conforme necessário
    ]
    
    # Atribui cores específicas para cada região segmentada
    for i in range(1, np.max(markers) + 1):
        color = colors[(i - 1) % len(colors)]
        color_map[markers == i] = color
    
    # Aplica a máscara colorida com opacidade reduzida na imagem original
    alpha = 0.5
    result = cv2.addWeighted(image, 1 - alpha, color_map, alpha, 0)
    
    return result