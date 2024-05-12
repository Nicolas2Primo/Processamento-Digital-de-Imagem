import numpy as np

def mean_threshold(image, kernel):
    """
    Aplica a técnica de limiarização por média móvel em uma imagem.

    Args:
        image: numpy.ndarray, a imagem de entrada em escala de cinza.
        kernel: int, o tamanho da janela para calcular a média móvel.

    Returns:
        numpy.ndarray, a imagem binarizada após a limiarização por média móvel.
    """
    # Obtém as dimensões da imagem
    height, width = image.shape

    # Cria uma matriz para armazenar a imagem binarizada após a limiarização
    binary_image = np.zeros_like(image)

    # Itera sobre cada pixel na imagem
    for i in range(height):
        for j in range(width):
            # Calcula a média dos valores de intensidade na vizinhança do pixel
            avg_intensity = np.mean(image[max(0, i - kernel // 2):min(height, i + kernel // 2 + 1),
                                          max(0, j - kernel // 2):min(width, j + kernel // 2 + 1)])

            # Define o valor do limiar como a média calculada
            threshold = avg_intensity

            # Binariza o pixel com base no limiar calculado
            binary_image[i, j] = 255 if image[i, j] > threshold else 0

    return binary_image
