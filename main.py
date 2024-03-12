def calc_media():
    print("Bem-vindo à calculadora de média feita com Python!")
    while True:
        try:
            n = int(input("Quantos valores serão calculados? "))
            if n > 0:
                break
            else:
                print("Por favor, insira um númeroo maior que zero.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    soma = 0

    for i in range(n):
        while True:
            try:
                nota = float(input(f"Insira o valor {i + 1}: "))
                soma += nota
                break
            except ValueError:
                print("Por favor, insira um número real válido.")

    media = soma / n
    print("A média é: ", media)

calc_media()