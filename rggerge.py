import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, QListWidget, QLineEdit, QTextEdit)

import json

notes = {
    'Добро пожаловать': {
        'текст': 'В этом приложении можно создовать знаки с тегами.',
        'теги':['Умные заметки', 'инструкцыя']
    }
}

with open('notes.json', 'w') as file:
    json.dump(notes, file)

app = QApplication([])
window = QWidget()

Text = QTextEdit()
name1 = QLabel()
list_names = QListWidget()
b_create = QPushButton()
b_deleate = QPushButton()
b_save = QPushButton()
name2 = QLabel()
list_tags = QListWidget()
Line = QLineEdit()
Line.setPlaceholderText()
b_create_tag = QPushButton()
b_delete_tag = QPushButton()
b_serch_tag = QPushButton()

maine_line = QHBoxLayout()
v1 = QVBoxLayout()
v2 = QVBoxLayout()
v1.addWidegt(Text)
v2.addWidget(name1)
v2.addWidget(list_names)
h1 = QHBoxLayout()
h1.addWidget(b_create)
h1.addWidget(b_deleate)
v2.addLayout(h1)
v2.addWidget(b_save)
v2.addWidget(name2)
v2.addWidget(list_taqs)
h2 = QHBoxLayout()
h2.addWidget(b_create_tag)
h2.addWidget(b_deleate)
v2.addLayout(h2)
v2.addWidget(b_serch_tag)
main_line.addLayout(v1, stretch=2)
main_line.addLayout(v2, stretch=1)
window.setLayout(main_line)

list_names.addItem(notes)

def show_note():
    name = list_names.selectedItems()[0].text()
    Text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])

list_names.itemClicked.connect(show_note)


def create():
    note_name, ok = QInputDilog.getText(window, 'Добавить заметку', 'Название заметки:')
    if note_name != '' and ok:
        notes[note_name] = {'текс': '', 'теги' : []}
        list_names.addItem(note_name)

b_create.CLicked.connect(create)

def delete():
    if list_names.selectedItems():
        key = list_names.selectedItems()[0].text()
        del notes[key]
        list_names.clear()
        list_tags.clear()
        Text.clear()
        list_names.addItems(notes)
        with open('notes.json', 'w') as file:
            json.dump(notes, file)

b_create.CLicked.connect(create)

def save():
    if list_names.selectedItems():
        key = list_names.selectedItem()[0].text()
        notes[key]['текст'] = Text.toPlainText()
        with open('notes.json', 'w') as file:
            json.dump(notes, file)
            (json.dump(notes, file, sort_keys=True)

b_save.clicked.connect(save)

def create_teg():
    teg = Line.text()
    if list_names.selectedItems() and tag != '':
        key = list_names.selectedItems()[0].text()
        notes[key]['теги'].append(tag)
        list_tags.addItem(tag)
        Line.clear()
        with open('notes.json', 'w') as file:
            json.dump(notes, file)

c_create_teg.clicked.connect(create_teg)

def deleat_tag():
    if






window.show()
app.exec()