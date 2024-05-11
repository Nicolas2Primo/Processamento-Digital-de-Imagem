import numpy as np

def dilation(image, kernel, iterations=1):
    """
    Aplica a operação de dilatação em uma imagem utilizando um kernel específico.
    
    Args:
        image: numpy.ndarray, a imagem de entrada em escala de cinza.
        kernel: numpy.ndarray, o kernel a ser aplicado na dilatação.
        iterations: int, o número de iterações da dilatação (padrão é 1).
        
    Returns:
        numpy.ndarray, a imagem após a dilatação.
    """
    # Obtém as dimensões da imagem e do kernel
    img_height, img_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # Calcula o deslocamento para centralizar o kernel
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    
    # Cria uma matriz para armazenar a imagem após a dilatação
    dilated_image = np.zeros_like(image)
    
    # Itera sobre o número de iterações especificado
    for _ in range(iterations):
        # Cria uma cópia da imagem original para armazenar a dilatação atual
        temp_image = np.copy(image)
        
        # Itera sobre cada pixel na imagem
        for i in range(pad_height, img_height - pad_height):
            for j in range(pad_width, img_width - pad_width):
                # Inicializa o valor máximo com um valor baixo
                max_val = 0

                # Itera sobre o kernel
                for m in range(kernel_height):
                    for n in range(kernel_width):
                        # Obtém as coordenadas do pixel no kernel
                        k_i = i + m - pad_height
                        k_j = j + n - pad_width

                        # Calcula o valor do pixel após a dilatação
                        if kernel[m, n] == 1:
                            pixel_val = image[k_i, k_j]
                            max_val = max(max_val, pixel_val)

                # Atribui o valor máximo à posição atual na imagem dilatada
                temp_image[i, j] = max_val
        
        # Atualiza a imagem original para a próxima iteração
        image = np.copy(temp_image)
    
    # Retorna a imagem após a dilatação
    return image