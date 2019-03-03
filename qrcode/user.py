from Qrcode import maker

def main():
    nome = input('Escreva seu nome: ')
    altura = float(input('Escreva sua altura: '))
    peso = float(input('Escreva seu peso: '))
    imc = peso/(altura*altura)
    conc = massa(imc)
    result = maker(imc,nome,peso,altura,conc)    

def massa(imc):
    if imc <= 18.5 :
        return 'Abaixo do peso'
    elif imc >= 18.6 or imc <= 24.9:
        return 'Parabéns, peso ideal'
    elif imc >= 25 or imc <= 29.9:
        return 'Sobrepeso'
    elif imc >= 30 or imc <= 34.9:
        return 'Obesidade grau I'
    elif imc >= 35 or imc <= 39.9 :
        return 'Obesidade grau II'
    elif imc >= 40:
        return 'Obesidade grau III'

    
if __name__=='__main__':
    main()
