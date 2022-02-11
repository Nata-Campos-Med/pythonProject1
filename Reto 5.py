def listar():
    archivo=open("Agenda.txt","r")
    linea=archivo.readline()
    while linea!='':
        print(linea,end="")
        linea=archivo.readline()
    archivo.close()
    
    #archivo=open("Agenda.txt","r")
    #linea=archivo.readlines()
    #print(linea)
    
def listadofiltrado(letra):
    archivo=open("Agenda.txt", "r")
    linea=archivo.readline()
    while linea!='':
        if linea.startswith(letra.title()):
            print(linea,end="")
            linea=archivo.readline()
            print(linea,end="")
            linea=archivo.readline()
            print(linea,end="")
        else:
            linea=archivo.readline()
    archivo.close()

def agregar():
    nombre=input("Digite nombre y apellido del beneficiario ")
    cedula = input("Digite cédula del beneficiario ")
    celular = input("Digite número celular del beneficiario ")
    
    archivo=open("Agenda.txt", "r")
    if cedula in archivo.read():    #Busca con read() en el archivo
         print("No se grabo porque la cedula ya existe")
         archivo.close()
    else:
        archivo.close()
        
        archivo = open("Agenda.txt", "a")
        archivo.write(nombre.title() + '\n' +cedula+ '\n' +celular+ '\n')
        archivo.close()
        
def borrar():
    buscar=input("Digite la cedula del beneficiario a borrar: ")
    archivo = open("Agenda.txt", "r")
    lineas = archivo.readlines()    #lee todas las líneas del archivo
    archivo.close()
    archivo=open("Agenda.txt", "w") #Sobre escribir el archivo
    cont = 0
    for linea in lineas:
        if linea==buscar+'\n':  #Cedula + salto de línea
            lineas.pop(cont-1)
            lineas.pop(cont-1)
            lineas.pop(cont-1)
            print("\nEl usuario ha sido eliminado del listado")
            cont+=2
            break
        else:
            cont+=1
    
    for linea in lineas:
        archivo.write(linea)
    #archivo.write(lineas)
    
    archivo.close()

def main():
    #w: write (crear el archivo y si existe lo sobre escribe)
    #r: read (Abrir el archivo de lectura)
    #r+: read (Abrir el archivo de lectura y escritura)
    #a: (Abrir el archivo y agregar)
    
    #Creo un excepción si mi archivo no existe lo creo
    try:
        archivo=open("Agenda.txt","r") #Abriendo archivo de lectura (r)
    except:
        archivo=open("Agenda.txt","w") #Abrir el archivo y sobre escribirlo
    archivo.close()
    
    while True:
        print("Menu Principal")
        print("1. Ver Listado")             #r
        print("2. Ver listado filtrado")    #r
        print("3. Agregar beneficiario")    #a
        print("4. Buscar beneficiario")     #r
        print("5. Borrar beneficiario")     #r+
        print("6. Salir")
        
        opcion=input("Digite opción deseada: ")
        if opcion =='6':
            break
        elif opcion == '1':
            listar()
        elif opcion == '2':
            letra = input("Digite la letra para filtrar busqueda: ")
            listadofiltrado(letra)
        elif opcion == '3':
            agregar()
        elif opcion == '4':
            nombre = input("Digite el nombre y apellido del beneficiario a buscar: ")
            listadofiltrado(nombre)
        elif opcion == '5':
            borrar()

main()
            
