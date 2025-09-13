from utilidades import Cola
texto = Cola
while True:
    palabra = input("escriba una palabra (o 'fin' para terminar): ")
    if palabra == "fin":
        break
    texto.push(palabra)
    print("historial de ultima palabra:",texto.peek())

    deshacer = input("si desea deshacer la ultima palabra ingese (s/n):")
    if deshacer == "s" or deshacer == "S":
        texto.pop()
        if not texto.is_empty():
            print("la palabra fue eliminada exitosamente ultima palabra:",texto.peek())

     

    
