# Программа для управления задачами
class Task:  # Класс Task для управления задачами с атрибутами описания, срока и статуса выполнения
    def __init__(self, description, deadline):
        self.description = description  # Описание задачи
        self.deadline = deadline        # Срок выполнения задачи
        self.is_done = False            # Статус выполнения (False - не выполнено)

    # Метод для отметки выполненной задачи
    def mark_as_done(self):
        self.is_done = True

    # Метод для вывода информации о задаче
    def __str__(self):
        status = "Выполнено" if self.is_done else "Не выполнено"
        return f"{self.description} - Срок: {self.deadline} - Статус: {status}"


# Список для хранения всех задач
tasks = []


# Функция добавления новой задачи
def add_task(description, deadline):
    new_task = Task(description, deadline)
    tasks.append(new_task)


# Функция для отметки задачи как выполненной по описанию
def mark_task_done(description):
    for task in tasks:
        if task.description == description:
            task.mark_as_done()
            break


# Функция для вывода списка текущих (не выполненных) задач
def list_not_done_tasks():
    print("Текущие (не выполненные) задачи:")
    for task in tasks:
        if not task.is_done:
            print(task)


# Функция для вывода списка всех задач
def list_all_tasks():
    print("Все задачи:")
    for task in tasks:
        print(task)


# Функция для вывода списка выполненных задач
def list_done_tasks():
    print("Выполненные задачи:")
    for task in tasks:
        if task.is_done:
            print(task)


# Добавление задач
add_task("Написать отчет", "2024-04-17")
add_task("Купить продукты", "2024-04-18")
add_task("Написать письмо", "2024-04-19")
add_task("Закончить проект", "2024-04-20")

# Вывод списка всех задач
list_all_tasks()

# Отметка выполненной задачи
mark_task_done("Написать отчет")
mark_task_done("Купить продукты")

# Вывод списка выполненных задач
list_done_tasks()

# Вывод списка невыполненных задач
list_not_done_tasks()
