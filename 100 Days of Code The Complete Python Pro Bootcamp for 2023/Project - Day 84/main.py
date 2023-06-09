from PIL import Image
 
 
def adicionar_marca_dagua(imagem_original, marca_dagua):
    imagem = Image.open(imagem_original)
    marca = Image.open(marca_dagua)
 
    largura_imagem, altura_imagem = imagem.size
    largura_marca, altura_marca = marca.size
 
    # Calcula a posição para colocar a marca d'água
    posicao = (largura_imagem - largura_marca, altura_imagem - altura_marca)
 
    # Combina as duas imagens
    imagem.paste(marca, posicao, marca)
 
    # Salva a imagem resultante
    imagem.save("imagem_com_marca_dagua.jpg")
    print("Marca d'água adicionada com sucesso!")
 
 
# Exemplo de uso
imagem_original = "imagem_origem.jpg"
marca_dagua = "imagem_marca_dagua.png"
adicionar_marca_dagua(imagem_original, marca_dagua)