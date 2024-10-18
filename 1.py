cantidadDeComprasaRealizar = int(input("Ingrese la catidad de comrpas: "))
print("La cantida de compras que realizo es de:" , cantidadDeComprasaRealizar)
total = 0
cantidadDeVecesQueItera = 0
for i in range (cantidadDeComprasaRealizar):
    valorDeCompra = int(input("Ingrese el valor de la compra: \n"))
    
    if (valorDeCompra >= 100000):
        valorDeCompra = valorDeCompra - (valorDeCompra * 0.10)
    elif(valorDeCompra < 100000 and valorDeCompra >= 50000):
        valorDeCompra = valorDeCompra - (valorDeCompra * 0.05)
    elif(valorDeCompra < 50000 and valorDeCompra >= 0):
        print("No tenes descuento")
    else:
        print("Ingresaste un valor invalido o negativo") 
        
    print("El valor de la compra es de: ", valorDeCompra)      
    total = total + valorDeCompra # 10000 + 90000 + 47500
    
    
print("El monto total de todas las compras es de: ",total)