import random

def gerar_cpf_aleatorio():
    # Gera 9 dígitos aleatórios para o CPF
    cpf = [random.randint(0, 9) for _ in range(9)]

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += cpf[i] * (10 - i)
    resto = soma % 11
    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += cpf[i] * (11 - i)
    resto = soma % 11
    if resto < 2:
        cpf.append(0)
    else:
        cpf.append(11 - resto)

    return ''.join(map(str, cpf))

def validar_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula os dígitos verificadores
    digitos_verificadores = [int(cpf[9]), int(cpf[10])]

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto

    # Verifica se os dígitos verificadores estão corretos
    if digitos_verificadores == [digito1, digito2]:
        return True
    else:
        return False

# Gera um CPF aleatório
cpf_aleatorio = gerar_cpf_aleatorio()
print("CPF aleatório gerado:", cpf_aleatorio)

# Valida o CPF gerado
if validar_cpf(cpf_aleatorio):
    print("CPF válido.")
else:
    print("CPF inválido.")
