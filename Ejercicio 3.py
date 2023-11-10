Alçada = float(input("Quant mesura?"))
Pes = int(input("Quant pesa?"))

IMC = Pes / (Alçada**2)

if IMC < 18.5:
    print("Sota pes normal")

if IMC >= 18.5 or IMC <= 24.9:
    print("Normal")
elif IMC >= 25 or IMC <= 29.9:
    print("Sobrepès")

if IMC > 30:
    print("Obesitat")
    