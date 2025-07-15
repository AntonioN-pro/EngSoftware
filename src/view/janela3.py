#Necessário para realizar import em python
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

#importando os módulos de controle
from controler.itemControler import ItemControler

class Janela3:
    
    @staticmethod
    def mostrar_janela3(database_name: str) -> None:
        """
        View para cadastrar novos itens no menu
        
        :param database_name: Nome do banco de dados
        :return: None
        """
        
        print('----------Cadastrar Item no Menu----------\n')
        
        continuar = 'y'
        
        while continuar == 'y':
            try:
                # Coleta dos dados do item
                nome = input('Nome do item: ').strip()
                if not nome:
                    print('Nome não pode estar vazio!')
                    continue
                
                descricao = input('Descrição: ').strip()
                if not descricao:
                    print('Descrição não pode estar vazia!')
                    continue
                
                # Validação do preço
                preco_input = input('Preço (R$): ').strip()
                try:
                    preco = float(preco_input)
                    if preco <= 0:
                        print('Preço deve ser maior que zero!')
                        continue
                except ValueError:
                    print('Preço deve ser um número válido!')
                    continue
                
                # Seleção da categoria
                print('\nSelecione a categoria:')
                print('1 - Pizza')
                print('2 - Bebida')
                print('3 - Sobremesa')
                print('4 - Outro')
                
                categoria_opcao = input('Digite o número da categoria: ').strip()
                
                categorias = {
                    '1': 'Pizza',
                    '2': 'Bebida',
                    '3': 'Sobremesa',
                    '4': 'Outro'
                }
                
                if categoria_opcao not in categorias:
                    print('Opção de categoria inválida!')
                    continue
                
                categoria = categorias[categoria_opcao]
                
                # Confirmação dos dados
                print('\n----------Confirmar Dados----------')
                print(f'Nome: {nome}')
                print(f'Descrição: {descricao}')
                print(f'Preço: R$ {preco:.2f}')
                print(f'Categoria: {categoria}')
                
                confirmar = input('\nConfirmar cadastro? (s/n): ').strip().lower()
                
                if confirmar == 's':
                    # Criar o item usando o controller
                    dados_item = [nome, preco, categoria, descricao]
                    item = ItemControler.create_item(dados_item)
                    
                    if item:
                        # Inserir no banco de dados
                        resultado = ItemControler.insert_into_item(database_name, item)
                        
                        if resultado == True:
                            print(f'\nItem "{nome}" cadastrado com sucesso!')
                        else:
                            print(f'\nErro ao cadastrar item: {resultado}')
                    else:
                        print('\nErro ao criar o item. Verifique os dados informados.')
                else:
                    print('\nCadastro cancelado.')
                
            except Exception as e:
                print(f'\nErro inesperado: {e}')
                print('Tente novamente.')
            
            # Pergunta se deseja continuar cadastrando
            continuar = input('\nCadastrar outro item? (y-Sim, n-Não): ').strip().lower()
            
            if continuar not in ['y', 'n']:
                print('Opção inválida. Retornando ao menu principal.')
                break
        
        print('\nVoltando ao menu principal...')