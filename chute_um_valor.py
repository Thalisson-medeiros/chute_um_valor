from random import randint

print('='*40)
print('{:=^40}'.format('CHUTE UM VALOR ENTRE 1 E 100'))
print('='*40)

num = randint(1, 100)

while True:
    
    chute = int(input('Qual o seu número: '))
    print('.'*40)
    
    if chute == num:
        print('='*40)
        print('|{:^38}|'.format('Você acertou!'))
        print('='*40)
        break
        
    elif chute > num:
        print('Chutou alto! é um número menor!')
        print('.'*40)
        
    else:
        if chute < num:
            print('Chutou baixo! é um número maior!')
            print('.'*40)
        
        