import pyautogui
import time

# 1 Clicar e digitar meu usuario
# 2 Clicar e digitar minha senha
# 3 Clicar em Entrar

pyautogui.alert('O código vai começar, favor não usar o computador enquanto o código estará rodando')
pyautogui.click(671, 385, duration=1)
pyautogui.write('RicardoA')
pyautogui.click(669, 411, duration=1)
pyautogui.write('123456')
pyautogui.click(589, 441, duration=1)

# 1 Clicar e digitar produto
# 2 Clicar e digitar quantidade
# 3 Clicar e digitar quantidade
# 4 Clicar em registrar
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        # 1 - Clicar e digitar produto
        pyautogui.click(387, 373, duration=1)
        pyautogui.write(produto)
        # 2- Clicar e digitar quantidade
        pyautogui.click(385, 400, duration=1)
        pyautogui.write(quantidade)

        # 3 - Clicar e digitar preco
        pyautogui.click(412, 424, duration=1)
        pyautogui.write(preco)
        # 4 - clicar em registrar
        pyautogui.click(309, 583, duration=1)
        pyautogui.click(309, 583)
        # 4 - Clicar em registrar
       
        
