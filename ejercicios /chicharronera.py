a = float(input('INgresa el valor de A'))
b = float(input('Ingresa el valor de B'))
c = float(input('Ingresa el valor de C'))

X1 = (-b + (b*b - 4*a*c)**0.5)/(2*a)
X2 = (-b - (b*b - 4*a*c)**0.5)/(2*a)

print(X1, '', X2)
