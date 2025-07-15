#para pegar a data de hoje
from datetime import date
import time

#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando os módulos de model
from model.pedido import Pedido

#importando os módulos de controle
from controler.pedidoControler import PedidoControler
from controler.itemControler import ItemControler

#criação da classe janela
class Janela1:
    
    @staticmethod
    def mostrar_janela1(database_name: str) -> None:
        """
        View para o usuário utilizar o software
        
        return None
        """
        
        a = 'y'
        
        menu = ItemControler.mostrar_itens_menu(database_name)
        
        print('----------Menu----------\n')
        print(f'{menu} \n')
        while a=='y':
            lista_itens = []
            valor_total=0
            
            a = str(input('Cadastrar pedido (y-Sim, n-Nao): '))

            if a == 'y':
                print('----------Cadastrar pedido----------\n')
                adicionar = 'y'
                pedidos = PedidoControler.search_in_pedidos_all(database_name)
                numero_pedido = len(pedidos) + 1

                while adicionar == 'y':
                    try:
                        item = int(input('Numero do item: ').strip())
                        quantidade = int(input('Quantidade: ').strip())
                    except ValueError:
                        print('Entrada inválida. Tente novamente.\n')
                        continue


                    a = ItemControler.valor_item(database_name, item)

                    if not a or not a[0]:
                        print(f'Item {item} não encontrado. Tente novamente.\n')
                        continue

                    b = a[0][0] * quantidade
                    print(b)
                    valor_total += b

                    for x in range(quantidade):
                        lista_itens.append((numero_pedido, item))

                    adicionar = input('Adicionar novo item? (y-Sim, n-Nao): ').strip().lower()

                print('\n----------Finalizar pedido----------\n')
                print(f'Numero do pedido: {numero_pedido}')
                delivery = str(input('Delivery (S/N): ')).lower()
                if delivery=='s':
                    delivery = True
                elif delivery=='n':
                    delivery = False
                else:
                    print('Valor incorreto, recomeçando')
                    break
                endereco = str(input('Endereco:'))
                status_aux = int(input('status: 1-preparo, 2-pronto, 3-entregue: '))
                if status_aux == 1:
                    status = 'preparo'
                elif status_aux == 2:
                    status = 'pronto'
                elif status_aux == 3:
                    status = 'entregue'
                else:
                    print('Status inválido. Recomeçando.')
                    continue
 
                print(f'Valor Final: R${valor_total}')
                data_hoje = date.today()
                data_formatada = data_hoje.strftime('%d/%m/%Y')
                print(data_formatada)
                print(endereco)
                pedido = Pedido(status, str(delivery), endereco,data_formatada,float(valor_total))
                PedidoControler.insert_into_pedidos(database_name,pedido)
                for elem in lista_itens:
                    ItemControler.insert_into_itens_pedidos(database_name,elem)
                
            elif a=='n':
                print('Voltando ao Menu inicial')
                time.sleep(2)
                break