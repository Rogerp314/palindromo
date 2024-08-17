print('-='*25)
print('O programa a seguir dirá se a frase digitada é ou não um palindro \nObs: A frase analizada não tem espaços e acentos.')
frase = input('Digite uma frase: ').upper().strip()
frase_invertida = frase[::-1]
if frase == frase_invertida:
    print('A frase digitada é um palíndromo:')
    print('{} | {}'.format(frase, frase_invertida))
else:
    print('A frase digitada não é um palíndromo')
    print('{} | {}'.format(frase, frase_invertida))
print('-='*25)
print('Precione Enter para finalizar esse programa ', end='')
input()