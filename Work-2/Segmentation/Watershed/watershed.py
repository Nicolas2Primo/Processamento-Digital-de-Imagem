import cv2
import numpy as np

def watershed_segmentation(image):
    # Converte a imagem para escala de cinza
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Aplica um filtro gaussiano para reduzir o ruído
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Aplica a detecção de bordas Canny
    edges = cv2.Canny(blurred, 30, 100)
    
    # Encontra os contornos na imagem
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Cria uma máscara para os marcadores
    markers = np.zeros(gray.shape, dtype=np.int32)
    
    # Desenha os contornos como marcadores
    for i in range(len(contours)):
        cv2.drawContours(markers, contours, i, (i+1), -1)
    
    # Adiciona o fundo como marcador
    cv2.circle(markers, (5, 5), 3, (255, 255, 255), -1)
    
    # Aplica o algoritmo Watershed
    markers = cv2.watershed(image, markers)
    
    # Cria uma cópia da imagem para desenhar as regiões segmentadas
    colored_markers = np.copy(image)
    
    # Preenche as regiões segmentadas com cores aleatórias
    for marker in np.unique(markers):
        if marker!= -1 and marker!= 0:
            colored_markers[markers == marker] = list(np.random.choice(range(256), size=3))
    
    # Combina a imagem original com as regiões coloridas para melhor visualização
    alpha = 0.5
    blended = cv2.addWeighted(colored_markers, alpha, image, 1-alpha, 0)
    
    return blended