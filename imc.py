def mostrar_divisor():
       divisor = "-" * 230

       print(divisor)

mostrar_divisor()

print("Seja bem vindo ao nosso site ❤️  , aqui nos calculamos o seu Índice de Massa Corporal (IMC) ")
print("Aqui tem um pequno texto sobre IMC")
print("Criado no século 19 pelo matemático Lambert Quételet, o Índice de Massa Corporal, conhecido pela sigla IMC, é um cálculo simples que permite medir se alguém está ou não com o peso ideal.")
nome = input("Digite o seu nome : ")
print(f"{nome}, vamos lá, agora vamos calcula o seu  Índice de Massa Corporal (IMC)")

#1receber peso em kg

peso_kg = float(input(f"{nome}, digite o seu peso em kg : "))


#2 recebert a variavel altura 

altura_metros = float(input(f"{nome}, digite a sua altura : "))


#pedir a variavel IMC
IMC = (peso_kg/(altura_metros** 2))

print(f"Valor do IMC: {IMC}")


#📊 Itens Desejáveis:

IMC = peso_kg / (altura_metros**2)


mostrar_divisor()
if IMC >= 30.0 :
    print("Cuidado com a saúde, lembre sempre você é importante💕")
elif IMC < 30.0 :
    print("Tudo ok 👌")



if IMC < 18.5:
    print ("Abaixo do peso")
    print("Mantenha sua alimentação assim ela esta muito boa😁")
elif 18.5 > IMC < 24.9:
    print ("Peso normal")
    print("A sua alimentação esta perfeita👌continue assim")
elif 25.0 > IMC < 29.9:
    print("Sobrepeso")
    print("Aqui vai uma dica sobre (sobrepeso)")
    print("A sua alimentação deve ser ajustada, com mais alimentos naturais e menos industrializados. Vamos lá temos que cuidar da nossa saúde 😊")
elif 30.0> IMC < 34.9:
    print ("Obesidade Grau I")
    print("Aqui vai uma dica sobre Obesidade Grau I")
    print("Tenha uma alimentação saudável, baseada em alimentos in natura. Pratique atividades físicas. Controle o consumo em excesso de sal e açúcar. Beba pelo menos dois litros de água diariamente. Vamos lá temos que cuidar da nossa saúde 😁")
elif 35.0 > IMC < 39.9:
    print ("Obesidade Grau II")
    print("Aqui vai uma dica sobre Obesidade Grau II")
    print("Tenha uma alimentação saudável, baseada em alimentos in natura. Pratique atividades físicas. Controle o consumo em excesso de sal e açúcar. Beba pelo menos dois litros de água diariamente. Vamos lá temos que cuidar da nossa saúde 😊")
elif IMC > 40.0 :
    print("Obesidade Grau III (Mórbida)")
    print("Aqui vai uma dica sobre Obesidade Grau III (Mórbida)")
    print("Tenha uma alimentação saudável, baseada em alimentos in natura. Pratique atividades físicas. Controle o consumo em excesso de sal e açúcar. Beba pelo menos dois litros de água diariamente. Vamos lá temos que cuidar da nossa saúde 😁")
    

mostrar_divisor()

#Vai Corinthians 🦅🦅🦅🦅
#Aqui é o Procópio 
#volei_e_Corinthians_e_vida Vitor