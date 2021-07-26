import streamlit as st


# Configurando o título

st.set_page_config(page_title=None, page_icon=None, layout='centered', initial_sidebar_state='expanded')

def pag_inicial():

	st.title("👋 Olá, esta é a documentação do programa!")
	st.markdown("---")
	st.markdown("### Pedro Oliveira Annoni Farah - Estágio Vetta ")
	st.markdown("---")
	st.markdown("Este documento foi feito para informar sobre o uso correto do `Sistema de Cadastro de Equipamentos e Medidores` para a construção de uma solução completa de gestão de energia. ")
	st.markdown("Aqui você poderá navegar entre os tópicos e entender o funcionamento do código!")
	st.markdown("O objetivo deste app  é fornecer mais algumas informações de como foi realizada a programação do algoritmo criado para o teste técnico da Vetta!  ")
	st.markdown("---")
	st.markdown("")
	st.markdown("### ⚡ Sobre a proposta")
	st.markdown("")
	#st.write(dict) 

	st.info("Pensando no desenvolvimento de  uma solução completa de gestão de energia e utilidades para grandes consumidores , era necessário o desenvolvimento de um sistema para permitir o registro dos equipamentos e possíveis medidores utilizados por determinada empresa.  ")
	st.markdown("### 💻 Sobre o programa")
	st.markdown("")
	st.info("O programa foi desenvolvido como uma aplicação de console, isto é, um código executável com uma interface puramente textual. Por isso, o algoritmo tem um funcionamento bastante simples e intuitivo para o usuário.")
	st.markdown("### 🚩 Sobre a documentação")
	st.markdown("")
	st.info("Neste app, é possível que seja feita a navegação interativa pela documentação. Ao lado, há um menu com algumas opções selecionáveis que se clicadas exibem informações sobre o desenvolvimento e funcionamento do algoritmo! ")

	st.markdown("<div align='center'><br>"
                "<img src='https://img.shields.io/badge/Feito%20COM-PYTHON%20-red?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/EDITADO%20COM-SUBLIME-blue?style=for-the-badge'"
                "alt='API stability' height='25'/>"
                "<img src='https://img.shields.io/badge/DESENVOLVIDO%20COM-Streamlit-green?style=for-the-badge'"
                "alt='API stability' height='25'/></div>", unsafe_allow_html=True)
	
	st.markdown("---")
add_sidebar = st.sidebar.selectbox("O que deseja entender?", ('Início','Premissas','Funcionamento','Fim'))
if(add_sidebar == 'Início'):
	pag_inicial()





if (add_sidebar == 'Premissas'):
	st.title("📑 Premissas!")
	st.markdown("---")
	st.markdown("O objetivo do sistema era possibilitar a praticidade para o cadastro dos equipamentos utilizados pela empresa. Assim, a junção da linguagem Python com a interface  do tipo console possibilitou que o programa adquirisse as seguintes características:")
	'''
	- [x] Simplicidade 
	- [x] Rapidez
	- [x] Leveza
	- [x] Praticidade



	'''
	st.warning("Juntamente com a linguagem Python, também foram utilizados o `Sublime Text` e o `Jupyter Notebook.`")
	
	'''

	O programa foi desenvolvido com um `menu`do tipo numérico, de modo que cada dígito correspondesse a uma opção a ser tomada pelo algoritmo. Assim, a cada momento o usuário teria o controle do que fazer durante a utilização do sistema. 

 ---

	'''



if (add_sidebar == 'Funcionamento'):
	st.title("🔍 Funcionamento!")
	st.markdown("---")
	'''
	O funcionamento do programa é bastante simples e intuitivo. Ao abrir o código executável, o usuário se depara com uma tela inicial e com um menu principal com as seguintes opções:

 1. Cadastrar Equipamento
 2. Pesquisar Equipamento
 3. Listar Todos 
 4. Sair
	'''
	st.markdown("---")
	st.markdown("Agora, você pode entender cada uma das seguintes etapas do código do programa!")
	st.markdown("### Tela Inicial")
	st.markdown("Essa primeira parte do código, serve apenas para que o usuário visualize uma tela inicial com o título do programa e entre em contato com o menu pela primeira vez:")
	code3 = '''def Tela_inicial():
    
    os.system('cls')
              
    print("\u001b[36;1m**********************************************")
    print("***  Sistema de cadastro de equipamentos!  ***")
    print("**********************************************\u001b[37m")
    Enter()
    print("Seja bem-vindo ao sistema de cadastros de Equipamentos e Medidores da \u001b[35;1mVetta!\u001b[37m")
    Enter()
    print("As opções do sistema estão listadas abaixo: ")
 	
# Criação do menu 
def Menu():
    
    print("\n 1: Cadastrar Equipamento \n 2: Pesquisar Equipamento \n 3: Listar todos \n 4: Sair")
    Enter()
    return input("Dígite o número correspondente ao item do menu: ")

	'''
	st.code(code3)

	st.markdown("### Menu")
	st.markdown("Para entender o funcionamento do menu, escolha sobre qual item você gostaria de ler mais: ")
	a = st.selectbox("Escolha uma opção: ", ("Cadastrar Equipamento", "Pesquisar Equipamento", "Listar todos", "Sair"))
	if(a == "Cadastrar Equipamento"):
		'''
		Ao escolher a opção 1, o usuário deve informar o nome e o código do equipamento, obrigatoriamente. Depois, fica a critério do usuário informar ou não um medidor. Caso decida informar, então deve informar também sua resolução para que o cadastro seja concluído. Se o equipamento não possuir medidor, o cadastro é automaticamente concluído assim que o usuário informar que não deseja inseri-lo. O código abaixo exemplifica o que foi escrito:

		
		'''
		code2 = '''def Cadastro():

    	os.system('cls')
    	print("Você está na sessão de \u001b[32;1mCadastro!\u001b[37m")
    	Enter()
    	print("Na sequência, você deverá informar os seguintes parâmetros: ")
    
    	print("\n A: Nome \n B: Código  \n C: Medidor (se houver) \n D: Resolução(se houver)")
    	Enter()
    	nome_eq = input("Por favor, entre com o nome do equipamento: ") 
    	Enter()
    	cod_eq = input("Agora, entre com o código do equipamento: ") 
    	Enter()
    	nomes.append(nome_eq)
    	cod.append(cod_eq)
    	# Chamada da função do medidor
    	Medidor()

    			'''
		st.code(code2)
		st.markdown("Para bem entender essa parte do código, também é importante conhecer a função `Medidor`: ")
		code1 = '''# Cadastro de um medidor para o equipamento
def Medidor():
    
    med =  input("Deseja cadastrar um medidor (S/N)? ")
    Enter()

    # Se o cliente desejar informar um medidor
    if (med == 'S'):
        nome_med = input("Por favor, informe o nome do medidor: ")
        Enter()
        res = input ("Agora, informe a resolução do medidor: ")
        medidores.append(nome_med)
        resolucoes.append(res)
        os.system('cls')
        print(" \u001b[32;1mCadastro concluído!\u001b[37m O que deseja fazer agora?")
    
    # Caso não haja medidor
    elif (med == 'N'):
        
        medidores.append('***')
        resolucoes.append('***')
        os.system('cls')
        
        print("\u001b[32;1mCadastro concluído!\u001b[37m O que deseja fazer agora?")
    
    # Comando Inválido
    else:
      print("\u001b[31;1mComando Inválido. Por favor, digite S ou N.\u001b[37m")
      Medidor()

	'''
		st.code(code1)
		st.markdown("---")


	if (a == 'Pesquisar Equipamento'):

		'''
		A opção 2 permite que o usuário pesquise pelo nome de um equipamento. Caso este já tenha sido registrado, o sistema retorna seu nome, código, medidor e resolução. Caso o sistema não encontre o equipamento buscado, então uma mensagem de aviso aparece. 
		Abaixo, é possível visualizar o código: 

		'''

		code2 = '''chave = input("Digite o nome  do equipamento que voce procura: ")
    
    procura = list(dict1.values())[0]
    x = 0
    
    # Caso já haja itens preenchidos
    if (len(procura) > 0):
        for i in range(len(procura)):
            if (chave == procura[i]):
                res = {"Nome" :procura[i], "Código": list(dict1.values())[1][i], 
                       "Medidor": list(dict1.values())[2][i], "Resolução": list(dict1.values())[3][i]}
                os.system('cls')
                print(" \u001b[32;1mAqui está seu equipamento!\u001b[37m O que deseja fazer agora?")
                print(res)
                Enter()
                
                x = 1
                
        if (x == 0):
            os.system('cls')
            print("\u001b[31;1mEquipamento não cadastrado! Favor rever se o nome está correto\u001b[37m")
    
    # Se não houver itens cadastrados
    else:
        os.system('cls')
        
        print("\u001b[31;1mPrimeiro,cadastre os equipamentos!\u001b[37m")



	'''
		st.code(code2)

		st.markdown("---")


	if (a == 'Listar todos'):
		'''
		Caso  o usuário escolha o número 3, o sistema retorna todos os registros com todos os seus parâmetros que já foram inseridos. Se não houver nenhum registro, o sistema pede que o usuário primeiro preencha com os equipamentos:


		'''

		code2 = '''# Listagem dos registros 
def Lista():

    procura = list(dict1.values())[0]
    
    # Se já houver registros
    if (len(procura) > 0):
        print("\u001b[32;1mEstes são seus registros!\u001b[37m O que deseja fazer agora?")
        for j in range(len(procura)):
            res = {"Nome" :procura[j], "Código": list(dict1.values())[1][j], 
                  "Medidor": list(dict1.values())[2][j], "Resolução": list(dict1.values())[3][j]}
            
            
            
            print(res)
            
            Enter()
    # Se ainda não houver
    else:
      os.system('cls')
      
      print("\u001b[31;1mPrimeiro,cadastre os equipamentos!\u001b[37m")


	'''
		st.code(code2)
		st.markdown("---")

	if(a == 'Sair'):

		'''
		A opção 4, como o próprio nome indica, encerra o sistema. 
		'''

		code2 = '''# Encerra o programa
def Sair():
    
    print("Ação finalizada!")

	'''
		st.code(code2)
		st.markdown("---")

if (add_sidebar == 'Fim'):
	
	st.title("❗ Informações finais!")
	st.markdown("---")

	'''
	 * Mais informações podem ser vistas no código completo.
	 * Obrigado por ter lido a documentação




	'''
	t = st.checkbox("Este documento foi útil pra você?")
	if(t == 1):
		st.balloons()
	




	

	

	

	


		









