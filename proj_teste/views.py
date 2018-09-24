from django.http import HttpResponse

def first(request):
    return HttpResponse('Ola Bucetão! Vou te meter a piroca!')



def articles(request, year):
    return HttpResponse('O ano enviado é:'+str(year))


def fname(request, param):
    result = lerDoBanco(param)
    print(result)
    print(param)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, possui : '+str(result['idade']) + ' anos')
    else:
        return HttpResponse('A pessoa não foi encontrada')

def lerDoBanco(nome):
    print('Entrou no lerbanco', nome)
    lista_nomes = [
        {'nome': 'patricia', 'idade': 20},
        {'nome': 'Conrad', 'idade': 39},
        {'nome': 'patricia', 'idade': 20},
        {'nome': 'aurora', 'idade': 15}
    ]
    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            print('achou')
            nome =''
            return pessoa
        else:
            print('nao achou')
            nome = ''
            return {'nome':'Não encontrado', 'idade': 0 }