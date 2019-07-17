def  emprestimo(idade, valorEmprestimo, salario, qtdParcelas):
    if(idade < 22 or idade > 55 or valorEmprestimo < 1000 or valorEmprestimo > salario * 15 or qtdParcelas < 3 or qtdParcelas > 20):
        print('Não aceito')

    else:
        print('Aceito')
        montante = round(valorEmprestimo * (1 + 0.08) ** qtdParcelas)
        montante = montante
        parcela = round(montante/qtdParcelas)
        parcela = parcela
        print(f"O valor total do empréstimo é de {montante} e o valor da parcela é de {parcela}")

emprestimo(25, 1300, 50000, 3)