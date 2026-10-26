'''
TABELA: petshop
id          - int - autoincrement
tipo_pet    - varchar2(30)
nome_pet    - varchar2(30)
idade       - int
'''
import os
import oracledb # python -m pip install oracledb
import pandas as pd # python -m pip install pandas

os.system("cls")

usuario = "" # Adicione sua credencial do Oracle
senha = "" # Adicione sua senha
dsn = ""  # Adicione o DSN de conexão do Oracle

try:
    conn = oracledb.connect(user = usuario, password = senha, dsn= dsn)
    inst_cadastro = conn.cursor() # Cia um cursor para cadastro - Entende comandos sql
    inst_consulta = conn.cursor() # Cia um cursor para cadastro - Entende comandos sql
    inst_alteracao = conn.cursor() # Cia um cursor para cadastro - Entende comandos sql
    inst_exclusao = conn.cursor() # Cia um cursor para cadastro - Entende comandos sql

except Exception as e:
    print("ERRO: ", e)
    conexao = False
else:
    conexao = True

while conexao:
    print("""
    ------ CRUD - PETSHOP ------
    0 - SAIR
    1 - Cadastrar pets
    2 - Listar pets
    3 - Alterar pets       
    4 - Excluir pets
    5 - Apagar todos
    """)
    escolha = input("Escolha: ")
    os.system("cls")
    match escolha:
        case '0':
            break
        case '1':
            try:
                # Capturar os dados do usuário
                print("CADASTRAR PET")
                tipo = input("Tipo.......: ")
                nome = input("Nome.......: ")
                idade = int(input("Idade....: "))

                # Montagem da instrução CQL de cadastro
                cadastro = f"""
                INSERT INTO petshop
                (tipo_pet, nome_pet, idade)
                VALUES ('{tipo}', '{nome}', {idade})
                """

                # Executa a instrução SQL
                inst_cadastro.execute(cadastro)
                conn.commit() # efetua a gravação magneticamente
            except ValueError:
                print("Digite um número na idade!")
            except Exception as e:
                print("ERRO: ", e)
            else:
                print("\nDADOS GRAVADOS!")
                conn.close()

        case '2': # listar todos os pets
            print("LISTAR PETS")
            lista_dados = []

            # montar a instrução SQL da listagem dos registros
            inst_consulta.execute('SELECT * FROM petshop')

            data = inst_consulta.fetchall() # captura todos os registros e joga no objeto data

            if data: # se há registros
                # inserir os registros na lista
                for dt in data:
                    lista_dados.append(dt)
            else:
                input("Nenhum registro encontrado!")
                continue

            lista_dados.sort()

            dados_df = pd.DataFrame(
                lista_dados,
                columns=['Id', 'Tipo', 'Nome', 'Idade'],
            )

            print(dados_df.to_string(
                index=False,
                col_space = {
                    "Id": 5,
                    "Tipo": 15,
                    "Nome": 20,
                    "Idade": 8
                },
                justify="left" 
            ))
        
        case '3': # Editar 
            try:
                print("EDITANDO OS DADOS")
                consulta = """
                SELECT id, nome_pet
                FROM petshop
                ORDER BY id
                """

                inst_consulta.execute(consulta)

                data = inst_consulta.fetchall()

                if not data:
                    input("A tabela esta vazia!")
                    continue

                dados_df = pd.DataFrame(
                    data, 
                    columns=["Id","Nome"]
                )

                print(dados_df.to_string(index=False, col_space=15))

                lista_dados = []

                pet_id = int(input("Id.....: "))

                consulta = f"""
                SELECT *
                FROM petshop
                WHERE id = {pet_id}
                """     

                inst_consulta.execute(consulta)
                data = inst_consulta.fetchall() # inst_cadastro

                if not data:
                    print("Registro não encontrado")       
                    continue

                for dt in data:
                    lista_dados.append(dt)

                print("Editar PET")
                novo_tipo = input("Tipo.......: ")
                novo_nome = input("Nome.......: ")
                nova_idade = int(input("Idade....: "))
                
                # construir a instrução de edição de registro
                alteracao = f"""
                UPDATE petshop
                SET tipo_pet='{novo_tipo}', nome_pet='{novo_nome}', idade={nova_idade}
                WHERE id = {pet_id}
                """
                inst_alteracao.execute(alteracao)
                conn.commit()
            except Exception as e:
                print("Erro: ", e)
            else:
                
                print("Dados atualizados!")
        case '4': # excluir registro
            try:
                print("EXCLUIR PET")
                lista_dados = []
                pet_id = int(input("Id......:"))

                consulta = f"SELECT * FROM petshop WHERE id = {pet_id}"

                inst_consulta.execute(consulta)

                data = inst_consulta.fetchall()

                for dt in data:
                    lista_dados.append(dt)

                if len(lista_dados) == 0:
                    print("Pet não cadastrado com este ID")
                else: # está cadastrado
                    exclusao = f"DELETE FROM petshop WHERE id = {pet_id}"
                    inst_exclusao.execute(exclusao)
                    conn.commit()
                    print("Pet apagado!")
                
                    
            except Exception as e:
                print("Erro: ", e)
            else:
                conn.close()

        case '5': # excluir todos os registros
            print("!!!!! EXCLUIR TODOS OS REGISTROS DA TABELA !!!!!")
            try:
                exclusao = "DELETE FROM petshop"
                inst_exclusao.execute(exclusao)
                conn.commit()

                # zerando os ids
                data_reset_ids = """ ALTER TABLE petshop MODIFY(ID GENERATED AS IDENTITY (START WITH 1)) """
                inst_exclusao.execute(data_reset_ids)
                conn.commit()
                print("Todos os registros foram exluidos")


            except Exception as e:
                print("ERRO: ", e)
            else:
                conn.close()

    input("Pressione algo para continuar . . .")
                






    