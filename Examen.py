# funciones.

def leer_opcion():
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Copias por género")
    print("2. Búsqueda de libros por rango de multa")
    print("3. Actualizar multa de libro")
    print("4. Agregar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    print("=====================================")

    while True:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion > 6 and opcion <= 0:
                print("Opcion invalida, escoga una opcion valida (1-6)")
            else:
                return opcion
        except ValueError:
            print("Solo se pueden ingresar numeros enteros validos")    

def copias_genero(genero, dicc_libros, dicc_prestamos):

    genero = genero.strip().lower()
    acumulador = 0

    for clave_libro, libro in dicc_libros.items():
        if genero == libro[2]:
            for clave_prest, prestamo in dicc_prestamos.items():
                if clave_libro == clave_prest:
                    acumulador += prestamo[1]
    
    print(f"El total de copias disponibles es: {acumulador}")

def busqueda_multa(m_min, m_max, dicc_libros, dicc_prestamos):

    lista = []

    for clave_prest, prestamo in dicc_prestamos.items():
        if prestamo[0] >= m_min and prestamo[0] <= m_max and prestamo[1] > 0:
            for clave_libro, libro in dicc_libros.items():
                if clave_prest == clave_libro:
                    lista.append(f"Los libros encontrados son: {libro[0]} -- {clave_libro}")

    if len(lista) == 0:
        print("No hay libros en ese rango de multa.")
    else:

        lista.sort()
        for i in lista:
            print(i)

def buscar_codigo(codigo, dicc_libros):
    for codigo_libro in dicc_libros.keys():
        if codigo == codigo_libro:
            return True
    
    return False

def codigo(codigo, dicc_libro, dicc_prestamos):
    if codigo != dicc_libro and dicc_prestamos:
        libros[codigo] = codigo
        prestamos[codigo] = codigo

        return True
    
    return False

def titulo(titulo, dicc_libro, dicc_prestamos):
    if titulo != dicc_libro and dicc_prestamos:
        libros[0] = titulo

def actualizar_multa(codigo,nueva_multa,dicc_prestamo):

    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, dicc_prestamo) == True:
        lista_prestamos = dicc_prestamo[codigo]
        lista_prestamos[0] = nueva_multa
        return True
    
    return False

def eliminar_libro(codigo,dicc_libros,dicc_prestamos):

    codigo = codigo.strip().upper()
    if buscar_codigo(codigo, dicc_prestamos) == True:
        
        del (dicc_libros[codigo])
        del (dicc_prestamos[codigo])
        
        return True
    
    return False

# diccionarios

libros = {
'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
}

prestamos = {
'L001': [500, 4],
'L002': [700, 0],
'L003': [300, 10],
'L004': [400, 2],
'L005': [600, 1],
'L006': [350, 6],
}

# Programa principal

while True:
    opcion_escogida = leer_opcion()

    if opcion_escogida == 1:
        genero = input("Ingrese genero a consultar: ").strip().lower()
        copias_genero(genero, libros, prestamos)
    
    elif opcion_escogida == 2:
        try:
            r_min = int(input("Ingrese multa mínima: "))
            r_max = int(input("Ingrese multa máxima: "))

            busqueda_multa(r_min, r_max, libros, prestamos)
        except ValueError:
            print("Debe ingresar valores enteros.")
    
    elif opcion_escogida == 3:

        codigo_a_buscar = input("Ingrese el codigo del libro: ")
        nueva_multa = int(input("Ingrese nueva multa: "))
        actualizada = actualizar_multa(codigo_a_buscar,nueva_multa,prestamos)

    elif opcion_escogida == 4:
        codigo_nuevo = input("ingrese el codigo del libro: ").upper().strip()
        codigo_validado = codigo(codigo_nuevo, libros, prestamos)
        if codigo_validado != True:
            print("Codigo invalido")
        elif codigo_validado == True:
            titulo_nuevo = input("Ingrese el titulo")
            titulo(titulo_nuevo, libros, prestamos)

    elif opcion_escogida == 5:
        codigo_eliminar = input("Ingrese codigo del libro a eliminar: ")
        eliminar_libro(codigo_eliminar,libros,prestamos)

    elif opcion_escogida == 6:
        print("Programa finalizado.")
        break