import time
import datetime
import random
from tqdm import tqdm 
import qrcode

print("================================ BEM VINDO ======================================")
#Iniciando...: 100%|█████████████████████████████████████| 100/100 [00:20<00:00,  4.96it/s]
for i in tqdm (range (100),
                colour='CYAN',
               desc="Iniciando...",
               ascii=False, ncols=90):
               time.sleep(0.1)

class Gerenciamento():
    def atualizar():
        print('Atualizar')
    def analise():
        print('Analise')
    def enviar():
        print('Enviar')
    def aprovado():
        print('Aprovado')
    def atualizando():
        print('Atualizando')
    def cancelado():
        print('Cancelado')
 

codigo = int(input('Informe o código :'))
def venda():
    item = str(input('Informe o produto :'))
    valor = float(input('Informe o valor do produto :'))
    quantidade = int(input('Quantidade do Produto :'))
    pedido = [item, valor, quantidade]
    soma = valor * quantidade
    print(f'Item: {pedido} Valor Total : {soma}')



time.sleep(1)
print('|------------API COMERCE-------------|')
time.sleep(0.5)

def api():
    if codigo > 1 and codigo < 100:
        print('|--------------APROVADO--------------|')
        print(f'Item : {venda()}')
        print(f' Pedido : {codigo} '), Gerenciamento.aprovado()

    elif codigo > 100 and codigo < 500:
        print('|--------------ANALISE---------------|')
        print(f'Pedido : {codigo}')
        Gerenciamento.analise()

    elif codigo > 500 and codigo < 700:
        print('|--------------CANCELADO-------------|')
        print(f'Pedido : {codigo}')
        Gerenciamento.cancelado()
api()

print("|====================================|")
print("|====================================|")
time.sleep(0.5)
def hub():
    print('|--------------HUB COMERCE-----------|')

    def importar():
        if codigo > 1 and codigo < 100:
            print('|--------------IMPORTAR--------------|')
            Gerenciamento.atualizando()
            now = datetime.datetime.now()
            print(f'Atualizado : {now}')
    importar()    

    def atualizar():
        if codigo > 100 and codigo < 500:
            print('|--------------ATUALIZAR-------------|')

            Gerenciamento.atualizar()
    atualizar()

    if codigo > 500 and codigo < 700:
        print('|--------------CANCELAR--------------|')

        Gerenciamento.cancelado()

hub()

def aprovado():
    for i in tqdm (range (101),  
               desc="Carregando…", 
               colour='CYAN', 
               ascii=False, ncols=72): 
            time.sleep(0.08)
    rastreio = random.randint(150000,450000)
    if codigo == codigo:
        print(f'Emitindo a Venda : {codigo} | Código Rastreio : {rastreio}')
        print('Resumo da Venda')
        print(f'Venda : {codigo}')
        for i in tqdm (range (100),
            colour='CYAN',
            desc="Enviando...",
            ascii=False, ncols=90):
            time.sleep(0.2)
               
      
    print("Processo Concluido.")
    #print("QRcode Gerado  : C:\Users\guga_\Desktop\Aulas")
    img = qrcode.make("https://github.com/gugacmp")
    img.save("qrcode.png")
    time.sleep(2)

aprovado()
gerar = str(input('Informe o código :'))
print("=============================================")
print("Deseja continuar S/N :")
gerar = str(input('Informe o código :'))    
while gerar == "S":
    codigo = int(input('Informe o código :'))
    venda()
    hub()
    aprovado()
    
    
else:
    gerar ="N"


        
