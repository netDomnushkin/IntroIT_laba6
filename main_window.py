from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QLabel
from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QListWidget
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Менеджер задач")
        self.setBaseSize(500, 400)

        #Подготовка виджетов
        self.newTask_label = QLabel("Новая задача")
        self.anountTask_label = QLabel("Количество задач: 0")
        self.taskName_input = QLineEdit()
        self.addTask_button = QPushButton("Добавить задачу")
        self.task_list = QListWidget()
        self.deleteTask_button = QPushButton("Удалить задачу")
        self.clearAll_button = QPushButton("Очистить список")
        self.taskName_input.setPlaceholderText("Название задачи")

        #Создание центрального виджета
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        #Создание слоев для добавления и удаления задач
        #Связывание слоев с соответствующими виджетами
        addTask_layout = QHBoxLayout()
        addTask_layout.addWidget(self.taskName_input)
        addTask_layout.addWidget(self.addTask_button)
        deleteTask_layout = QHBoxLayout()
        deleteTask_layout.addWidget(self.deleteTask_button)
        deleteTask_layout.addWidget(self.clearAll_button)

        #Создание главного слоя и привязка к нему других слоев и виджетов
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.newTask_label)
        main_layout.addLayout(addTask_layout)
        main_layout.addWidget(self.task_list)
        main_layout.addLayout(deleteTask_layout)
        main_layout.addWidget(self.anountTask_label)

        #Привязка главного слоя к центральному виджету
        central_widget.setLayout(main_layout)

        #Создание обработчиков нажатия кнопки для добавления задачи
        self.addTask_button.clicked.connect(self.add_task)
        self.taskName_input.returnPressed.connect(self.add_task)

        #Создание обработчиков нажатия кнопки для удаления задачи
        self.deleteTask_button.clicked.connect(self.delete_task)

        #Создание обработчика нажатия кнопки для очистки списка
        self.clearAll_button.clicked.connect(self.clear_tasks)


    #Функция для добавления задачи в список
    def add_task(self):
        text = self.taskName_input.text().strip()
        if text:
            self.task_list.addItem(text)
            self.taskName_input.clear()
            self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка", "Введите название задачи")

    #Функция для удаления выбранной задачи из списка
    def delete_task(self):
        row = self.task_list.currentRow()
        if row >= 0:
            answer = QMessageBox.question(self, "Удаление", "Вы действительно хотите удалить задачу?")
            if answer == QMessageBox.StandardButton.Yes:
                self.task_list.takeItem(row)
                self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка", "Задача не была выбрана")

    #Функция для очистки списка
    def clear_tasks(self):
        if self.task_list.count() > 0:
            answer = QMessageBox.question(self, "Удаление", "Вы действительно хотите очистить список?")
            if answer == QMessageBox.StandardButton.Yes:
                self.task_list.clear()
                self.update_counter()
        else:
            QMessageBox.warning(self, "Ошибка", "Список пуст")

    #Функция для счета задач
    def update_counter(self):
        count = self.task_list.count();
        self.anountTask_label.setText(f"Количество задач: {count}")

        


        

       
      



     
    