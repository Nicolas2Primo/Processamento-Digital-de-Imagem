import numpy as np

def erosion(image, kernel, iterations=1):
    """
    Aplica a operação de erosão em uma imagem utilizando um kernel específico.
    
    Args:
        image: numpy.ndarray, a imagem de entrada em escala de cinza.
        kernel: numpy.ndarray, o kernel a ser aplicado na erosão.
        iterations: int, o número de iterações da erosão (padrão é 1).
        
    Returns:
        numpy.ndarray, a imagem após a erosão.
    """
    # Obtém as dimensões da imagem e do kernel
    img_height, img_width = image.shape
    kernel_height, kernel_width = kernel.shape
    
    # Calcula o deslocamento para centralizar o kernel
    pad_height = kernel_height // 2
    pad_width = kernel_width // 2
    
    
    
    # Itera sobre o número de iterações especificado
    for _ in range(iterations):
        # Cria uma cópia da imagem original para armazenar a erosão atual
        temp_image = np.copy(image)
        
        # Itera sobre cada pixel na imagem
        for i in range(pad_height, img_height - pad_height):
            for j in range(pad_width, img_width - pad_width):
                # Inicializa o valor mínimo com um valor alto
                min_val = 255

                # Itera sobre o kernel
                for m in range(kernel_height):
                    for n in range(kernel_width):
                        # Obtém as coordenadas do pixel no kernel
                        k_i = i + m - pad_height
                        k_j = j + n - pad_width

                        # Calcula o valor do pixel após a erosão
                        if kernel[m, n] == 1:
                            pixel_val = image[k_i, k_j]
                            min_val = min(min_val, pixel_val)

                # Atribui o valor mínimo à posição atual na imagem erodida
                temp_image[i, j] = min_val
        
        # Atualiza a imagem original para a próxima iteração
        image = np.copy(temp_image)
        
    # Retorna a imagem após a erosão
    return image