import time
import datetime
import random
from tqdm import tqdm 
import qrcode


print("================================ BEM VINDO ======================================")
print("================================ HUB COMMERCE ===================================")
print("================================ VERSÃO 1.3.1 ===================================")
#Iniciando...: 100%|█████████████████████████████████████| 100/100 [00:20<00:00,  4.96it/s]
for i in tqdm (range (100),
                colour='CYAN',
               desc="Iniciando...",
               ascii=False, ncols=90):
               time.sleep(0.1)

print("================================ BEM VINDO ======================================")
print("================================ MENU HUB =======================================")
print(" ___________________________")
print("|_________ OPÇÕES __________|")
print("| Código                    |")
print("| Produto                   |")
print("| Valor                     |")
print("| Quantidade                |")
print("| Cliente                   |")
print("| Sair                      |")
print("|___________________________|")
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
    def rejeitado():
        print('Rejeitado')
 
print("============================================================================ 1.3.1 =")
rastreio = random.randint(150000,450000)
codigo = int(input('Informe o código :'))
cliente = str(input('Informe o cliente : '))
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
print("|                1.3.1               |")
print("|====================================|")
time.sleep(0.5)
def hub():
    print('|--------------HUB COMERCE-----------|')

    def importar():
        if codigo > 1 and codigo < 100:
            print('|--------------IMPORTAR--------------|')
            Gerenciamento.atualizando()
            now = datetime.datetime.now()
            print(f'Importando : {now}')
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
               desc="Importando…", 
               colour='CYAN', 
               ascii=False, ncols=72): 
            time.sleep(0.08)
    rastreio = random.randint(150000,450000)
    print("_____________________________________________________________________________ 1.3.1 __")
    
conectar = random.randint(1,4)
if conectar == 2 or conectar == 4:
    
    if codigo == codigo:
        print(f'Emitindo a Venda : {codigo} | Pré Rastreio : {rastreio}')
        print('Resumo da Venda')
        print(f'Venda : {codigo}')
        chave =random.randint(10000000000000000000000000000000000000000000,99999999999999999999999999999999999999999999)
        protocolo = random.randint(20000000, 99999999)
        now = datetime.datetime.now()
        #print(f'Venda : {codigo} | Chave de Acesso : {chave}')
        #print(f'Numero do Protocolo : {protocolo}')
        #print(f'Data/hora da Autorização : {now}')
        for i in tqdm (range (100),
            colour='#90EE90',
            desc="Enviando...",
            ascii=False, ncols=90):
            time.sleep(0.2)
        print("======================================= RESUMO ============================== 1.3.1==")  
        print(f'Cliente : {cliente.upper()}')
        print(f'Venda : {codigo} |\nChave de Acesso : {chave}')
        print(f'Numero do Protocolo : {protocolo} |\nRastreio Autorizado : {rastreio}')
        print(f'Data/hora da Autorização : {now}')
      
    print("Processo Concluido.")
    #print("QRcode Gerado  : C:\Users\guga_\Desktop\Aulas")
    img = qrcode.make("https://github.com/gugacmp")
    img.save("qrcode.png")
    time.sleep(2)


else:
   #conectar == 1 or conectar == 3:
    if codigo == codigo:
        print(f'Emitindo a Venda : {codigo} | Pré Rastreio : {rastreio}')
        print('Resumo da Venda')
        print(f'Venda : {codigo}')
        chave =random.randint(10000000000000000000000000000000000000000000,99999999999999999999999999999999999999999999)
        protocolo = random.randint(20000000, 99999999)
        now = datetime.datetime.now()
        #print(f'Venda : {codigo} | Chave de Acesso : {chave}')
        #print(f'Numero do Protocolo : {protocolo}')
        #print(f'Data/hora da Autorização : {now}')
        for i in tqdm (range (100),
            colour='#A52A2A',
            desc="Rejeitado...",
            ascii=False, ncols=90):
            time.sleep(0.2)
        print("======================================= RESUMO ============================== 1.3.1==")
        print(f'Venda do Cliente : {cliente.upper()} Rejeitada')
        print(f'Favor Verificar os Dados da Nota de Código :{codigo}')  
        #print(f'Cliente : {cliente.upper()}')
        print(f'Venda : {codigo} |\nChave de Acesso : {chave}')
        print(f'Numero do Protocolo : {protocolo} |\nRastreio Rejeitado : {rastreio}')
        print(f'Data/hora da Rejeição : {now}')
        gerar = str(input('Deseja continuar S/N :'))    
        while gerar == "S":
            codigo = int(input('Informe o código :'))
            cliente = str(input('Informe o cliente : '))
        #venda()
        #hub()
        Gerenciamento.rejeitado
    
aprovado()
#gerar = str(input('Informe o código :'))
print("=============================================================================== 1.3.1==")
#print("Deseja continuar S/N :")
gerar = str(input('Deseja continuar S/N :'))    
while gerar == "S":
    codigo = int(input('Informe o código :'))
    cliente = str(input('Informe o cliente : '))
    venda()
    hub()
    aprovado()
    
    
else:
    gerar ="N"
    for i in tqdm (range (101),  
               desc="Encerrando…", 
               colour='#F0E68C', 
               ascii=False, ncols=72): 
            time.sleep(0.08)
print("\n")
        
print("_______________________________________________________________________________ 1.3.1 __")