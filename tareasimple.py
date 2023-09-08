import os
import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.data_file = "tasks.json"

    def load_tasks(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.data_file, "w") as file:
            json.dump(self.tasks, file)

    def list_tasks(self):
        if not self.tasks:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def add_task(self, task_description):
        self.tasks.append(task_description)
        self.save_tasks()
        print(f"La tarea '{task_description}' ha sido agregada.")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            self.save_tasks()
            print(f"La tarea '{removed_task}' ha sido eliminada.")
        else:
            print("Índice de tarea no válido.")

def main():
    task_manager = TaskManager()
    task_manager.load_tasks()

    while True:
        print("\n1. Listar tareas")
        print("2. Agregar tarea")
        print("3. Eliminar tarea")
        print("4. Salir")
        choice = input("Selecciona una opción: ")

        if choice == "1":
            task_manager.list_tasks()
        elif choice == "2":
            task_description = input("Ingrese la descripción de la tarea: ")
            task_manager.add_task(task_description)
        elif choice == "3":
            task_manager.list_tasks()
            task_index = int(input("Ingrese el número de tarea a eliminar: "))
            task_manager.remove_task(task_index)
        elif choice == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()



