import re

tabela_lexica = {}

def encontrar_lexema(string):
    for (expressao, lexema) in tabela_lexica.items():
        if re.fullmatch(expressao, string):
            return lexema
    raise ValueError(f"EXPRESSÃO SEM LEXEMA CORRESPONDENTE --> ({string})")

def string_to_lexemas(string):
    
    regex = r"(\"[^\"]*\"|\'[^\']*\')|([;=+-\/*(),])|(\w+)"
    lexemas_na_string = []
    
    for match in re.finditer(regex, string):
        if match.group(1):  # Strings com aspas duplas ou simples
            palavra = match.group(1)
        elif match.group(2):  # Caracteres especiais
            palavra = match.group(2)
        elif match.group(3):  # Palavras (identificadores ou números)
            palavra = match.group(3)
        else:
            continue  # Ignorar espaços em branco

        try:
            lexema_valorado = f"{encontrar_lexema(palavra)}({palavra})"
            lexemas_na_string.append(lexema_valorado)
        except ValueError as e:
            print(e)  # Exibe o erro sem interromper o programa
    return "".join(lexemas_na_string)

def configurar_tabela_lexica():
    linhas = []
     #Lê as linhas do documento,remove os espaços vazios e armazena na lista 'linhas'
    for line in open("tabela_lexica.txt"):
        linhas.append(line.replace(" ",""))

    #remove as strings \n e aloca as expressões e os lexemas no dicionario 'tabela_lexica'
    for line in linhas:
        (expressao, lexema) = line.replace('\n', '').split("-->")   
        tabela_lexica[expressao] = lexema

if __name__ == "__main__":

    configurar_tabela_lexica()
    print(tabela_lexica)
    lexemas_na_string_string_unica = string_to_lexemas(input("digite uma linha de código:\n"))

    print('em lexemas:\n',lexemas_na_string_string_unica)