num = input("Digite um número entre 0 e 9999: ")
if not  num.isdigit() or not ( 0 <=int(num) <=9999):
    print("Número inválido.")
else:
    s = num.zfill(4)
    print(f"Milhar:  {s[0]}")
    print(f"Centena: {s[1]}")
    print(f"Dezena:  {s[2]}")
    print(f"Unidade: {s[3]}")