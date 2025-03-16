import re

table = {}

def encontrar_lexema(string):
    for (expressao, lexema) in table.items():
        if re.fullmatch(expressao, string):
            return lexema
    
def string_to_lexemas(string):
    lexemas_na_string = []
    for palavra in string.split(" "):
        lexema_valorado = f"{encontrar_lexema(palavra)}({palavra})"
        lexemas_na_string.append(lexema_valorado)
    return "".join(lexemas_na_string)

def configurar_tabela_lexica():
    linhas = []
     #Lê as linhas do documento,remove os espaços vazios e armazena na lista 'linhas'
    for line in open("tabela_lexica.txt"):
        linhas.append(line.replace(" ",""))

    #remove as strings \n e aloca as expressões e os lexemas no dicionario 'table'
    for line in linhas:
        (expressao, lexema) = line.replace('\n', '').split("-->")   
        table[expressao] = lexema

if __name__ == "__main__":

    configurar_tabela_lexica()
    print(table)
    lexemas_na_string_string_unica = string_to_lexemas(input("digite uma linha de código:\n"))

    print('em lexemas:\n',lexemas_na_string_string_unica)