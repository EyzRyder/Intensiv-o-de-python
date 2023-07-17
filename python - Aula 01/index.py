# pip list to see the packages list
import pyautogui # py -m pip install pyautogui
import pyperclip # py -m pip install pyperclip
import time
import pandas as pd # py -m pip install pandas openpyxl

pyautogui.press("win")
time.sleep(2)
pyautogui.write("opera")
time.sleep(2)
pyautogui.press("enter")
time.sleep(3)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga") # pyautogui.write("") could be used but i think this is faster
pyautogui.hotkey("ctrl", "v")
time.sleep(2)
pyautogui.press("enter")
time.sleep(12)

pyautogui.click (x=430, y=370, clicks=2)
time.sleep(3)

pyautogui.click (x=446, y=370) # click the file
pyautogui.click (x=640, y=219) # download the file
time.sleep(5)
pyautogui.click (x=160, y=60) # click the seach bar
pyautogui.write("www/intensivao/aula 01")
pyautogui.press("enter")

pyautogui.click (x=922, y=704) # click to save in the file
time.sleep(3)

tabela = pd.read_excel("Vendas - Dez.xlsx")
print(tabela) # display(tabela)

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox?compose=new")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(10)
#pyautogui.click (x=151, y=212) # click to compose
#time.sleep(3)
pyautogui.write("gabrielbessi4@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
texto = f"""
Prezados, bom dia
O faturamento de ontem foi de: R$ {faturamento:,.2f}
A quantidade de produtos foi de : {quantidade:,.2f}
Abs
Biel
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

# print(pyautogui.position()) # to discover position