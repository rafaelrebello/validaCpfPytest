def criarDigitosVerificadores(cpf):
    cpf = cpf.replace('.','').replace('-','')
    
    if len(cpf)!= 9:
        return False
 
    soma1 = [int(numero)*(multiplicador+2) for multiplicador,numero in enumerate(cpf[::-1])]
    dv1 = sum(soma1)*10%11
    soma2 = [int(numero)*(multiplicador+3) for multiplicador,numero in enumerate(cpf[::-1])]
    dv2 = (sum(soma2) + (dv1*2)) * 10 % 11
    digitoVerificador = str(dv1*10 + dv2)

    return cpf+digitoVerificador

def valida_cpf(cpf):
    cpf = cpf.replace('.','').replace('-','')
    if len(cpf) != 11:
        return False
    cpfVerificado = cpf[:9]
    cpfVerificado = criarDigitosVerificadores(cpfVerificado)
    print(cpfVerificado)
    return cpfVerificado == cpf

print(criarDigitosVerificadores('108311839'))