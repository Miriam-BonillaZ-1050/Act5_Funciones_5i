print("Funciones creadas por el usuario")

def mi_lista():
    amigos=["Homero","Paty","Lety"]
    for bonilla in amigos:
        print(bonilla)
        
def tupla():
    gatos=("Gansito","Mojito","Chesse")
    for cat in gatos:
        print(cat)
    
def conjunto():
    colores={"Azul","Negro","Gris"}
    for c in colores:
        print(c)
    
def diccionario():
    yo = {
        "Nombre": "Miriam", 
        "Apellido": "Bonilla",
        "Edad": 16,
        "Hobbie": "Voleibol"
    }
    print(yo)
    
## Llamadas a funciones
mi_lista()
tupla()
conjunto()
diccionario()