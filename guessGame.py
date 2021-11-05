n = 45
print("Você tem apenas 5 chances. \n\t", "Jogue com calma")
i = 1
while i<=5:
    thenum = int(input("Digite seu número com dois algarismos entre 0 e 50\n\n\t"))
    if thenum > 45:
        print("!!!! Por favor tente um numero menor!!!")
    elif thenum < 45:
        print("!!! Por favor tente um numero maior")
    else:
        print("!!!!\n Parabéns você ganhou")
        print("Sua pontuação é: ",i)
        break
        print(5-i, "tentativas")
    i=i+1
    if i>5:
        print("Fim de jogo")

# made by Hacktoberfest-2021
