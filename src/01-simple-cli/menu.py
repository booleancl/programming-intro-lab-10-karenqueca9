from notebook import Notebook
import sys
class Menu:
    def __init__(self):
        self.notebook = Notebook() 
    def display_menu(self):
        print("""
        Bienvenido a la opción Notebook, presione un número para continuar.
        Menú:
        1. Ver todas las notas
        2. Buscar nota
        3. Agregar Nota
        4. Modificar Nota
        5. Salir
        """)    

    def start(self):
        while True:
            self.display_menu()
            option = input("Ingrese su opción")
            if option == "1":
                self.show_notes()
            elif option == "2": 
                self.search_notes()  
            elif option == "3": 
                self.add_note()
            elif option == "4": 
                self.edit_note()
            elif option == "5": 
                print("Gracias por usar el editor de  notas") 
                sys.exit(0)
            else:
                print("Por favor ingrese una alternativa válida")
    
    def add_note(self):
        content = input("Ingrese el cuerpo de la nota: ")  
        tags = input("Ingrese los tags: ").split(" ")
        self.notebook.add_note(content,*tags)
        print("La nota fue agregada")   

    def show_notes(self, notes = None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(note.id ,note.tags, note.content)   

    def edit_note(self):
        id = int(input("Ingrese el id de la nota: "))
        content = input("Ingrese el nuevo contenido: ")
        tags = input("Ingrese los nuevos tags").split(" ")
        if content: 
            self.notebook.edit_content(id, content)
        if tags:
            self.notebook.edit_tags(id, *tags)

    def search_notes(self):
        filter = input("Buscar por: ")
        filter_notes = self.notebook.search(filter)
        self.show_notes(filter_notes)

Menu().start()

