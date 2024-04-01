import numpy as np
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, img):
        self.img = np.array(img).astype('uint8')
        self.img_size_lin, self.img_size_col = self.img.shape  # Não precisamos de *_ aqui
        self.histogram = np.zeros(256)  # Inicializa o histograma se  dtype == 'uint8'

    def calc_hist(self):
        if self.img.dtype == 'uint8':
            for j in range(self.img_size_lin):
                for k in range(self.img_size_col):
                    self.histogram[(self.img[j, k])] += 1
        else:
            print("A imagem precisa ser do tipo 'uint8' para o cálculo do histograma.")

    def normalize_hist(self):
        total_pixels = self.img_size_lin * self.img_size_col
        self.histogram = 100 * self.histogram / total_pixels

    def calc_and_plot(self):
        self.calc_hist()
        #self.normalize_hist()

        fig, axs = plt.subplots(1, 2, figsize=(10, 4))

        # Plotagem da imagem à esquerda
        axs[0].imshow(self.img, cmap='gray')


        # Plotagem do histograma à direita
        axs[1].bar(range(256), self.histogram)
        plt.subplots_adjust(wspace=0.5)

        plt.show()
