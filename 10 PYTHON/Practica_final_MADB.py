# Crea una clase Libro con los atributos titulo (str), autor (str), isbn (str) y disponible (booleano con True por defecto).
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    # Incluye un método agregar() que permita introducir un nuevo libro con sus características.
    def agregar(self):
        return f"El libro {self.titulo} (ISBN: {self.isbn}) se ha agregado con éxito."

    # Incluye un método prestar() que cambie el estado de disponible a False si el libro está disponible, y muestre un mensaje si ya está prestado.
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro {self.titulo} (ISBN: {self.isbn}) se ha prestado con éxito."
        else:
            return f"Lo sentimos, el libro {self.titulo} (ISBN: {self.isbn}) ya está prestado."

    # Incluye un método devolver() que cambie el estado de disponible a True si estaba prestado, y muestre un mensaje si ya estaba disponible.
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro {self.titulo} (ISBN: {self.isbn}) se ha devuelto con éxito."
        else:
            return f"El libro {self.titulo} (ISBN: {self.isbn}) ya está disponible."

    # Incluye un método mostrar() que devuelva una lista con todos los libros de la biblioteca y los muestre en pantalla con todos sus datos y diga si estás disponible o no.
    def mostrar(self):
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - {disponibilidad}"

    # Incluye un método buscar() que busque un libro en concreto por su ISBM y lo muestre en pantalla con todos sus datos y diga si está disponible o no.
    def buscar(self):
        return f"{self.titulo} de {self.autor} - ISBN: {self.isbn} - {'Disponible' if self.disponible else 'No disponible'}"

# Implementa un bucle que permita al usuario interactuar con el programa mediante un menú con las funciones agregar, prestar, devolver, mostrar y salir.
def menu():
    libros = []    # Lista para almacenar objetos de la clase Libro.

    # Libro de ejemplo para que la lista no esté vacía.
    libro_11111 = Libro("El Principito", "Antoine de Saint-Exupéry", "11111")
    libros.append(libro_11111)

    while True:
        print("\nBienvenido al Sistema de Gestión de Biblioteca")
        print("1. Agregar libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Mostrar libros")
        print("5. Buscar libro")
        print("6. Salir")

        opcion = input("Teclea el número de una opción y pulsa Enter: ")

        if opcion == "1":    # Agregar un nuevo libro.
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")

            # Verifica si el ISBN ya existe.
            if any(libro.isbn == isbn for libro in libros):
                print("Ya existe un libro con este ISBN.")
            else:
                libro = Libro(titulo, autor, isbn)
                libros.append(libro)
                print(libro.agregar())

            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.

        elif opcion == "2":    # Prestar un libro.
            isbn_buscar = input("Por favor, ingresa el ISBN del libro a prestar: ")
            libro_encontrado = next((libro for libro in libros if libro.isbn == isbn_buscar), None)
            if libro_encontrado:
                print(libro_encontrado.prestar())
            else:
                print("Lo sentimos, el libro con ese ISBN no existe.")
            
            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.

        elif opcion == "3":    # Devolver un libro.
            isbn_buscar = input("Por favor, ingresa el ISBN del libro a devolver: ")
            libro_encontrado = next((libro for libro in libros if libro.isbn == isbn_buscar), None)
            if libro_encontrado:
                print(libro_encontrado.devolver())
            else:
                print("Lo sentimos, el libro con ese ISBN no existe.")
            
            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.

        elif opcion == "4":    # Mostrar todos los libros y mostrar en columnas.
            if libros:    # Verifica si la lista de libros no está vacía.
                print("\nLista de libros en la biblioteca:")
                print(f"{'Título':<30} {'Autor':<30} {'ISBN':<15} {'Disponibilidad':<15}")    # Imprime los encabezados.
                print("-" * 90)    # Línea separadora.

                #    Imprime los libros.
                for libro in libros:
                    disponibilidad = "Disponible" if libro.disponible else "No disponible"
                    print(f"{libro.titulo:<30} {libro.autor:<30} {libro.isbn:<15} {disponibilidad:<15}")
            else:
                print("No hay libros en la biblioteca.")

            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.

        elif opcion == "5":    # Buscar un libro por ISBN y mostrar en columnas.
            isbn_buscar = input("Por favor, ingresa el ISBN del libro a buscar: ")
            libro_encontrado = next((libro for libro in libros if libro.isbn == isbn_buscar), None)
            if libro_encontrado:
                print(f"{'Título':<30} {'Autor':<30} {'ISBN':<15} {'Disponibilidad':<15}")    # Imprimir los encabezados.
                print("-" * 90)    # Línea separadora.

                # Mostrar el libro encontrado
                disponibilidad = "Disponible" if libro_encontrado.disponible else "No disponible"
                print(f"{libro_encontrado.titulo:<30} {libro_encontrado.autor:<30} {libro_encontrado.isbn:<15} {disponibilidad:<15}")
            else:
                print("Lo sentimos, el libro con ese ISBN no existe.")

            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.
        
        elif opcion == "6":    # Salir del programa.
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor ingresa una opción válida.")
            input("\nPulsa Enter para volver al menú...")    # Intro para volver al inicio.

menu()