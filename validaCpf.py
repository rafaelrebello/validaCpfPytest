#Crie as seguintes funções: valida_cpf(), gera_cpf_valido() e gera_lista_cpfs()
from random import randint as rint

def geraDigitosVerificadores(cpf):

    if len(cpf) != 9:
        return False
    
    soma1 = [int(numero)*(multiplicador+2) for multiplicador,numero in enumerate(cpf[::-1])]
    dv1 = (sum(soma1))*10%11
    

    soma2 = [int(numero)*(multiplicador+3) for multiplicador,numero in enumerate(cpf[::-1])]
    dv2 = ((sum(soma2)) + (dv1*2)) * 10 % 11

    dv1 = str(dv1%10)
    dv2 = str(dv2%10)

    digitoVerificador = dv1 + dv2
    return str(cpf)+str(digitoVerificador)

def geraCpfValido():
    stringGeraCpf = ''

    for x in range(9):
        stringGeraCpf+= str(rint(0,9))

    return geraDigitosVerificadores(stringGeraCpf)

def validaNumeroCpf(cpf):
    cpf = cpf.replace('.','').replace('-','')
    if len(cpf) != 11:
        return False
    cpfVerificado = cpf[:9]
    cpfVerificado = geraDigitosVerificadores(cpfVerificado)
    return cpfVerificado == cpf


def geraListaCpf(qtd):
    listaCpf = []
    for x in range(qtd):
        listaCpf.append(geraCpfValido())
    return listaCpf


print(validaNumeroCpf(geraCpfValido()))