print("Programa que acepte datos de estudiantes y los escriba en un HTML.\n")

perfil = True

while perfil == True:
    nombre=input("Introduzca su nombre: ")
    apellido=input("Introduzca su apellido: ")
    matricula=input("Introduzca su matricula: ")
    n1=input("Introduzca su primera calificacion: ")
    n2=input("Introduzca su segunda calificacion: ")
    n3=input("Introduzca su tercera calificacion: ")

    datos_html = """ <tr>
                        <td>"""+(nombre)+"""</td>
                        <td>"""+(apellido)+"""</td>
                        <td>"""+(matricula)+"""</td>
                        <td>"""+(n1)+"""</td>
                        <td>"""+(n2)+"""</td>
                        <td>"""+(n3)+"""</td>
                    </tr> """

    base = ("20175001.html")
    abrir = open(base, "a+")
    abrir.write(datos_html)

    while True:
        cond = input("Desea crear otro perfil? (S/N): ")

        if cond == "S" or cond == "s":
            print("\n")
            perfil = True
            break

        elif cond == "N" or cond == "n":
            print("\n")
            perfil = False
            break

r=input("Presione Enter para salir")
