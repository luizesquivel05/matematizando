import os

print('''
      SALVE SALVE CARO USUÁRIO, VAMOS AGORA AO MATEMATIZANDO, PROGRAMA QUE USA DE MODELOS PARA A RESOLUÇÃO DE SEU PROBLEMA MATEMÁTICO.
      
      TRATA-SE DA RESOLUÇÃO DE FUNÇÕES DE ENÉSIMO GRAU, COM BASE EM RESOLUÇÕES MATEMÁTICAS, ANTES ALGUNS CONCEITOS:
      
        1)É PRECISO DAR A FUNÇÃO COM VARIÁVEIS PASSÍVEL DE RESPONDER, EX:
            Y = 5*4 + 2
            Y = 5*2^2 + 3*2 + 8
            
        2)CHAMAM-SE FUNÇÕES A RELAÇÃO ENTRE 2 OU MAIS CONJUNTOS QUE SE RELACIONAM DE ACORDO COM UMA LEI DE FUNCIONAMENTO.
        
        3)É PRECISO USAR OPERADORES:
            + (SOMA)
            - (SUBTRAÇÃO)
            * (PRODUTO)
            / (RAZÃO)
            % (PROPORÇÃO)
            ^ (POTENCIALIZAÇÃO)
    
    VOCÊ ESTÁ CIENTE? 
''')
verificar = int(input('Digite 1 para continuar: '))
while verificar != 1:
    verificar = int(input('Digite 1 para continuar: '))
else:
    try:
        os.system('cls')
    except:
        os.system('clear')
        
print(f'''
    QUE BOM SABER QUE ESTÁ APRENDENDO MATEMÁTICA, ESTAMOS AQUI PARA LHE AUXILIAR!!
    
    PARA COMEÇAR ESCOLHA UMA DAS OPÇÕES ABAIXO:
    
{"="*53}
| ESCOLHA UMA FUNÇÃO: {" "*31}|
|{" "*51}|
| 1 - FUNÇÃO DO PRIMEIRO GRAU: f(x) = a*x+b {" "*8}|
{"="*53}
    
    ESTAMOS TRABALHANDO PARA AUMENTAR O NUMÉRIO DE FUNÇÕES, MAS É O QUE TEMOS ATÉ AGORA. VAMOS NESSA!
''')
# print(f'''
#     QUE BOM SABER QUE ESTÁ APRENDENDO MATEMÁTICA, ESTAMOS AQUI PARA LHE AUXILIAR!!
    
#     PARA COMEÇAR ESCOLHA UMA DAS OPÇÕES ABAIXO:
    
# {"="*53}
# | 1 - FUNÇÃO DO PRIMEIRO GRAU: f(x) = a*x+b {" "*8}|
# |{" "*51}|
# | 2 - FUNÇÃO QUADRÁTICA: f(x) = a*x^2 + b*x + c {" "*4}|
# |{" "*51}|
# | 3 - FUNÇÃO TRIPLA: f(x) = a*x^3 + b*x^2 + c*x + d |
# {"="*53}
    
#     ESTAMOS TRABALHANDO PARA AUMENTAR O NUMÉRIO DE FUNÇÕES, MAS É O QUE TEMOS ATÉ AGORA. VAMOS NESSA!
# ''')
verificar = int(input('Digite uma das opções acima: '))
resolução = str()
# while verificar > 3 or verificar < 1:
while verificar != 1:
    verificar = int(input('Você deve digitar uma das opções acima: '))
else:
    try:
        os.system('cls')
    except:
        os.system('clear')

if verificar == 1: resolução = "afim"
# elif verificar == 2: resolução = "quadratica"
# else: resolução = "tripla"
while True:
    if resolução == "afim":
        print('''
    MUITO BOM SABER QUE ESCOLHEU A FUNÇÃO AFIM!
    
    EIS A LEI GERAL DE FUNCIONAMENTO:
        f(x) = a*x + b: a !=0
        
    ELA DEVE SER DESCRITA ASSIM:
        y = num1*x + num2
        
    SEPARE A FUNÇÃO E VAMOS COMEÇAR! 
        ''')
        
        funcao = str(input('Escreva a função: ')).lower()
        
        while funcao[5:7] != "*x":
            print('VOCÊ DEVE ESCREVER A FUNÇÃO CONFORME DESCRITO ACIMA: ')
            funcao = str(input('Escreva a função: ')).lower()
        else:
            try:
                os.system('cls')
            except:
                os.system('clear')
        while True:
            num1 = funcao[4]
            num2 = funcao[10]
            num1, num2 = int(num1), int(num2)
            
            print('''
        AGORA PARA ETAPAS DE PERGUNTAS DA FUNÇÃO:
        
        1)VOCÊ DESEJA SABER y OU x.
            ''')
            
            direcao = str(input('Digite y para saber y e x para saber x: ')).lower()
            while direcao != "x":
                if direcao == "y":
                    try:
                        os.system('cls')
                    except:
                        os.system('clear')
                elif direcao != "y": direcao = str(input('Digite y para saber y e x para saber x: ')).lower()
            else:
                try:
                    os.system('cls')
                except:
                    os.system('clear')
            if direcao == "x":    
                print('''
            PRÓXIMA ETAPA:
            
            2)DÊ UM VALOR PARA Y.
                ''')
                
                y = int(input('O valor de y é: '))
                
                x = (y - num2)/num1
                
                print(f'O RESULTADO FINAL É: {x}')
            else:    
                print('''
            PRÓXIMA ETAPA:
            
            2)DÊ UM VALOR PARA X;
                ''')
                
                x = int(input('O valor de y é: '))
                
                y = (num1*x) + num2
                
                print(f'O RESULTADO FINAL É: {y}')
                
            verificar = str(input('Digite S para outra operação e N para outra função: '))
            while verificar != "S":
                try:
                    os.system('cls')
                except:
                    os.system('clear')         
            else:
                break
    verificar = str(input('Digite S para menu inicial e N para encerrar o programa: '))
    if verificar != "S":
        try:
            os.system('cls')
        except:
            os.system('clear')
    else:
        break   