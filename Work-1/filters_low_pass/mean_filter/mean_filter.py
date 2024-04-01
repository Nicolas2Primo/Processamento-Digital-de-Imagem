import numpy as np
import math as m
import cv2
import matplotlib.pyplot as plt
import random

class MeanFilter:
  def __init__(self, img , kernel_size):
    self.img = np.array(img)
    self.original = self.img.copy()
    self.img_size_lin, self.img_size_col = self.img.shape
    self.kernel_size = kernel_size
    self.kernel = np.ones((kernel_size, kernel_size))
    self.central = m.floor((kernel_size / 2))
    self.padding = np.zeros((self.img_size_lin + self.central * 2, self.img_size_col + self.central * 2))

  def _filter(self):
    self.padding[(0 + self.central):(self.img_size_lin + self.central), (0 + self.central):(self.img_size_col + self.central)] = self.img.copy()
    sum = 0
    final_array = np.zeros(self.img.shape)
    for j in range(0, self.img_size_lin):
      for k in range(0, self.img_size_col):
        for kl in range(0, self.kernel_size):
          for kk in range(0, self.kernel_size):
            sum = (self.padding[j + kl, k + kk] * self.kernel[kl, kk]) + sum
        value = m.ceil((sum / (self.kernel_size * self.kernel_size)))
        sum = 0
        final_array[j, k] = value
    final_array = np.uint8(final_array)
    
    return final_array
  
  def add_noise(self):
    img = self.img.copy()
    row , col = self.img.shape 
    number_of_pixels = random.randint(300, 10000)

    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1) 
        img[y_coord][x_coord] = 255
          
    number_of_pixels = random.randint(300 , 10000) 

    for i in range(number_of_pixels): 
        y_coord=random.randint(0, row - 1) 
        x_coord=random.randint(0, col - 1) 
        img[y_coord][x_coord] = 0
          
    return img 

  def run(self, num_increments):
        original = self.original
        
        aux = np.zeros((self.img_size_lin, self.img_size_col))
        auxs = [original]
        plt.imshow(original, 'gray')
        plt.title('Original')
        plt.show()

        for i in range(num_increments):
            aux[:, :] = self._filter()
            auxs.append(aux.copy())
            self.img = aux.copy()

            plt.imshow(aux, 'gray')
            plt.title(f'Filtered - Iteration {i + 1}')
            plt.show()

            
        cv2.imwrite(f'filtered_image_k{self.kernel_size}_n{num_increments}.png',aux)











        plt.imshow(original, 'gray')
        plt.title('Original')
        plt.show()

        for i in range(num_increments):
            aux[:, :] = self._filter()
            #print(f"{i}\n", aux)
            auxs.append(aux.copy())
            self.img = aux.copy()

            plt.imshow(aux, 'gray')
            plt.title(f'Filtered - Iteration {i + 1}')
            plt.show()

            
        cv2.imwrite(f'filtered_image_k{self.kernel_size}_n{num_increments}.png',aux)
        self.img = original.copy()
        
        
