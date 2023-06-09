import numpy as np

from sklearn.cluster import KMeans

import matplotlib.pyplot as plt



def generate_color_palette(image_path, num_colors):

    # Carrega a imagem

    image = plt.imread(image_path)



    # Obtém as dimensões da imagem

    width, height, _ = image.shape



    # Redimensiona a imagem para um formato adequado ao algoritmo K-means

    reshaped_image = image.reshape(width * height, 3)



    # Aplica o algoritmo K-means para encontrar os clusters de cores

    kmeans = KMeans(n_clusters=num_colors)

    kmeans.fit(reshaped_image)



    # Obtém as cores centrais dos clusters encontrados

    colors = kmeans.cluster_centers_



    # Converte os valores das cores para o intervalo de 0 a 255

    colors = colors.astype(int)



    return colors



# Exemplo de uso

image_path = "./image.jpg"  # Insira o caminho para a imagem que deseja gerar a paleta de cores

num_colors = 5  # Número de cores da paleta



colors = generate_color_palette(image_path, num_colors)



# Exibe a paleta de cores

plt.imshow([colors], aspect='auto')

plt.axis('off')

plt.show()