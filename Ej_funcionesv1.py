print("Manejo de funciones V1 :)")
def hola_mundo():
    print("Hola aqui estoy dentro de la funcion")
def mens(msg):
    print(msg)
    
def EscribeNC(nombre,apellido):
    print(nombre,apellido)
    print("Tu nombre completo es {nombre} {apellido}")
def sum2num(n1,n2):
    s=n1+n2
    return f"La suma de {n1} y de {n2} es de: ",s
#llamando la funcion
hola_mundo()
mens("Hola WhatsApp") ##Llama a mens con un parametro
mens("El profe me sorprendio enviando mensajes") ##Llama a mens
EscribeNC("Miriam","Bonilla")
print("Funciones que regresan valores")
print(sum2num(7,3))
print(sum2num(15,45))