d=int(input("Cantidad entera dinero en COP: "))
#b=billetes
#m=monedas
b1=(d-(d%100000))//100000
d=d%100000
b2=(d-(d%50000))//50000
d=d%50000
b3=(d-(d%20000))//20000
d=d%20000
b4=(d-(d%10000))//10000
d=d%10000
b5=(d-(d%5000))//5000
d=d%5000
b6=(d-(d%2000))//2000
d=d%2000
b7=(d-(d%1000))//1000
d=d%1000
m1=(d-(d%500))//500
d=d%500
m2=(d-(d%200))//200
d=d%200
m3=(d-(d%100))//100
d=d%100
m4=(d-(d%50))//50
print("Billetes de $100000: ",b1)
print("Billetes de $50000: ",b2)
print("Billetes de $20000: ",b3)
print("Billetes de $10000: ",b4)
print("Billetes de $5000: ",b5)
print("Billetes de $2000: ",b6)
print("Billetes de $1000: ",b7)
print("Monedas de $500: ",m1)
print("Monedas de $200: ",m2)
print("Monedas de $100: ",m3)
print("Monedas de $50: ",m4)

