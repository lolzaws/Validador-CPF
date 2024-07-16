"""
Data: 15/07/2024
Baseado no "Algoritmo de Validação do CPF" no blog Macoratti(https://www.macoratti.net/alg_cpf.htm)
"""

# Valida entrada de usuário removendo pontos, hífens e espaços
# retorna o CPF bruto em tipo str
def validate_input(input: str) -> int:
    treated = input.replace('.', '').replace('-', '').replace(' ', '').strip()

    try:
        int(treated)
    except ValueError:
        print("Somente números, pontos e hífens são aceitos.")
        exit()
    
    if len(treated) != 11:
        print(f"Este CPF contém somente {len(inp)} de 11 dígitos")
        exit()
    
    if len(treated) > 11:
        print(f"O número que você supriu é maior que 11 dígitos.")
    else:
        return treated


# Calcula as tabelas e os últimos dois digitos.
# retorna 0 ou 11 menos o resto da divisão
# da variável res
def calculate_tables_and_digits(tables: list) -> int:
    calcs = []
    for i, number in enumerate(tables, start=2):
        calcs.append(i * number)
    
    # Soma a lista e pega o resto da divisão por 11
    res = int(sum(calcs) % 11)
    
    """
    Aplicando as regras:
    1) Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero);
    2) Se o resto da divisão for maior ou igual a 2, então o dígito verificador é 
    igual a 11 menos o resto da divisão (11 - resto).
    
    retorna o resto da divisão(dígito)
    """
    if 2 > res:
        return 0
    elif res >= 2:
        return 11 - res

# Processa as tabelas e repassa para a função calculate_tables_and_digits()
# retorna o cpf formatado
def process_tables(cpf: str):
    list_cpf_nine_digits: list = [int(x) for x in cpf[:9]] # pega os 9 primeiros dígitos do cpf suprido
    list_cpf_nine_digits.reverse() # inverte a lista para calcular corretamente, do final para o início
    
    for i in range(2):
        # coloca o primeiro dos últimos dois dígitos na primeira posição e recalcula novamente tudo
        # para pegar o último dígito
        list_cpf_nine_digits.insert(0,calculate_tables_and_digits(list_cpf_nine_digits))
    
    list_cpf_nine_digits.reverse() # inverte a lista novamente para voltar ao estado incial
    
    return parse_cpf_string(list_cpf_nine_digits) # retorna o cpf formatado xxx.xxx.xxx-xx


def parse_cpf_string(table: list) -> str:
    cpf_str = ''
    for i, number in enumerate(table, start=1):
        cpf_str += str(number)
       
        if i % 3 == 0.0 and not i == 9:
            cpf_str += '.'
        
        if i % 9 == 0.0:
            cpf_str += '-'

    return cpf_str.strip()
            
        

def main():
    #exemplo: '111.444.777-05', resultado: 111.444.777-35, situação: inválido
    original : str = input("Insira seu CPF: ")
    validated: int = validate_input(original)
    
    parsed   : str = parse_cpf_string([x for x in validated])
    expected : str = process_tables(validated)
    
    value = 'válido' if expected == parsed else 'inválido'
    print(parsed, value)


if __name__ == "__main__":
    main()