
def origem_destino_iguais(origem, destino, lista_de_erros):
    ''' Verifica se origem e destino são iguais '''
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e Destino não podem ser iguais'

def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    ''' Verifica se possui algum dígito numérico '''
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = 'Não inclua números nesse campo'

def data_ida_maior_que_data_volta(data_ida, data_volta, lista_de_erros):
    ''' Verifica se data de volta é menor que data de ida '''
    if data_volta < data_ida :
        lista_de_erros['data_volta'] = 'Data de volta não pode ser menor que data de ida'

def data_ida_menor_que_data_hoje(data_ida, data_pesquisa, lista_de_erros):
    ''' Verifica se data de ida é menor que data de pesquisa '''
    if data_ida < data_pesquisa :
        lista_de_erros['data_ida'] = 'Data de ida não pode ser menor que data de hoje'