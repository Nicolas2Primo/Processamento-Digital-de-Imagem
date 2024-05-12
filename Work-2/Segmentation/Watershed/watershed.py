import cv2
import numpy as np
import random

def apply_watershed(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 30, 100)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    markers = np.zeros(gray.shape, dtype=np.int32)
    
    for i in range(len(contours)):
        cv2.drawContours(markers, contours, i, (i+1), -1)
    
    cv2.circle(markers, (5, 5), 3, (255, 255, 255), -1)
    
    markers = cv2.watershed(image, markers)
    
    color_map = np.zeros(image.shape, dtype=np.uint8)
    
    colors = [
        (255, 0, 0),     # Azul
        (0, 255, 0),     # Verde
        (0, 0, 255),     # Vermelho
        (255, 255, 0),   # Ciano
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Amarelo
    ]
    
    for i in range(1, np.max(markers) + 1):
        color = colors[(i - 1) % len(colors)]
        color_map[markers == i] = color
    
    alpha = 0.5
    result = cv2.addWeighted(image, 1 - alpha, color_map, alpha, 0)
    
    return result