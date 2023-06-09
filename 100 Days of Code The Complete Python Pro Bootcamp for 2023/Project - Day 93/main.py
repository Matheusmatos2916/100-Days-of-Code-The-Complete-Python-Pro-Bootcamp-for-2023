import time

from PIL import ImageGrab

import pyautogui



def detect_collision(data):

    # Verifica se há um pixel preto na região onde ocorre a colisão

    for i in range(415, 480):

        for j in range(520, 590):

            if data[i, j] < 100:

                return True

    return False



def jump():

    # Simula um pressionamento de tecla para o dinossauro pular

    pyautogui.keyDown('space')

    time.sleep(0.05)

    pyautogui.keyUp('space')



def play_game():

    # Espera 3 segundos antes de começar a jogar

    time.sleep(3)



    while True:

        # Captura a região da tela onde ocorre o jogo

        screen = ImageGrab.grab((400, 500, 950, 600))

        # Converte a imagem capturada para escala de cinza

        grayscale_image = screen.convert('L')

        # Obtém os dados dos pixels da imagem

        data = grayscale_image.load()



        # Verifica se ocorreu uma colisão

        if detect_collision(data):

            jump()



# Inicia o jogo

play_game()

