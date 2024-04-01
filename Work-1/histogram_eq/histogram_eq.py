import numpy as np
import matplotlib.pyplot as plt

class Histogram:
    def __init__(self, img):
        self.img = np.array(img)
        self.img_size_lin, self.img_size_col = self.img.shape
        self.histogram = np.zeros(256)

    def calc_hist(self):
        if self.img.dtype == 'uint8':
            for j in range(self.img_size_lin):
                for k in range(self.img_size_col):
                    self.histogram[(self.img[j, k])] += 1
        else:
            print("A imagem precisa ser do tipo 'uint8' para o cálculo do histograma.")

    def equalize_hist(self):
      if self.img.dtype != 'uint8':
          self.img = self.img.astype('uint8')

      # Calculando o histograma acumulado
      hist_cumsum = np.cumsum(self.histogram)

      # Encontrando o valor mínimo e máximo do histograma
      hist_min = np.min(hist_cumsum)
      hist_max = np.max(hist_cumsum)

      new_img = np.zeros((self.img_size_lin, self.img_size_col))

      for j in range(self.img_size_lin):
          for k in range(self.img_size_col):
              intensity = self.img[j, k]
              # Normalizando a intensidade para [0, 1]
              norm_intensity = (hist_cumsum[intensity] - hist_min) / (hist_max - hist_min)
              # Mapeando a intensidade equalizada
              new_intensity = np.ceil(norm_intensity * 255)
              new_img[j, k] = new_intensity

      return new_img.astype('uint8')


    def normalize_hist(self):
        total_pixels = self.img_size_lin * self.img_size_col
        self.histogram = 100 * self.histogram / total_pixels

    def plot_hist(self, equalized=False):
        if equalized:
            plt.figure(figsize=(10, 4))

            plt.subplot(121)
            plt.imshow(self.img, 'gray')
            plt.title('Equalized Image')

            plt.subplot(122)
            plt.bar(range(256), self.histogram)
            plt.title("Histogram (Equalized)")
            plt.xlabel("Pixel Value")
            plt.ylabel("Frequency")

        else:
            plt.figure(figsize=(10, 4))

            plt.subplot(121)
            plt.imshow(self.img, 'gray')
            plt.title('Original Image')

            plt.subplot(122)
            plt.bar(range(256), self.histogram)
            plt.title("Histogram")
            plt.xlabel("Pixel Value")
            plt.ylabel("Frequency")

        plt.show()

    def calc_and_plot(self):
        self.calc_hist()
        self.normalize_hist()
        self.plot_hist()  # Plot original histogram and image

        equalized_img = self.equalize_hist()
        self.img = equalized_img  # Update image
        self.calc_hist()  # Recalculate histogram
        self.normalize_hist()
        self.plot_hist(equalized=True)  # Plot equalized histogram and image
