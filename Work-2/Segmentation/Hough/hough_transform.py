import cv2
import numpy as np

def hough_transform(image, rho_resolution=1, theta_resolution=np.pi/180, threshold=100):
    """
    Aplica a Transformada de Hough para detectar linhas em uma imagem.
    
    Parâmetros:
        - image: imagem de entrada (deve ser uma imagem binarizada, preferencialmente de bordas).
        - rho_resolution: resolução em pixels da distância rho na grade de Hough.
        - theta_resolution: resolução em radianos do ângulo theta na grade de Hough.
        - threshold: limiar de votação na Transformada de Hough.
        
    Retorna:
        - lines: uma lista de tuplas (rho, theta) representando as linhas detectadas.
    """
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    lines = cv2.HoughLines(edges, rho_resolution, theta_resolution, threshold)
    
    if lines is None:
        return []
    
    else:
        output_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(output_image, (x1, y1), (x2, y2), (0, 0, 255), 2)
    
    lines = [line[0] for line in lines]
    return output_image