nombreUsuario= input("ingrese su nombre ")
edadUsuario= int(input("ingrese sus edad"))

if edadUsuario>=0 and edadUsuario<=15:
    print(f"apreciado {nombreUsuario},usted es un niño")
elif edadUsuario>15 and edadUsuario<=28:   
    print(f"apreciado {nombreUsuario},usted es un joven")
elif edadUsuario>28 and edadUsuario<=60:  
    print(f"apreciado {nombreUsuario},usted es un adulto")
elif edadUsuario>60 and edadUsuario<110:
    print(f"querido{nombreUsuario},usted es un adulto mayor") 
else:
    print("edad invalida")       
