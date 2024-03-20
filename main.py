import json
import os
from datetime import datetime

# Путь к файлу с заметками
NOTES_FILE = "notes.json"

# Функция для загрузки заметок из файла
def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []  # Если файл не существует, возвращаем пустой список
    with open(NOTES_FILE, "r") as f:
        return json.load(f)

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)

# Функция для добавления новой заметки
def add_note(title, body):
    notes = load_notes()  # Загружаем текущие заметки
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Получаем текущее время
    note = {"id": len(notes) + 1, "title": title, "body": body, "timestamp": now}  # Создаем новую заметку
    notes.append(note)  # Добавляем заметку в список
    save_notes(notes)  # Сохраняем обновленный список заметок в файл
    print("Заметка успешно добавлена.")

# Функция для редактирования существующей заметки
def edit_note(note_id, title, body):
    notes = load_notes()  # Загружаем текущие заметки
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["body"] = body
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Обновляем время изменения
            save_notes(notes)  # Сохраняем обновленный список заметок в файл
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным идентификатором не найдена.")

# Функция для удаления существующей заметки
def delete_note(note_id):
    notes = load_notes()  # Загружаем текущие заметки
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)  # Удаляем заметку из списка
            save_notes(notes)  # Сохраняем обновленный список заметок в файл
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным идентификатором не найдена.")

# Функция для вывода списка всех заметок
def list_notes():
    notes = load_notes()  # Загружаем текущие заметки
    if not notes:
        print("Нет сохранённых заметок.")
    else:
        print("Список заметок:")
        for note in notes:
            print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Дата создания: {note["timestamp"]}')

# Функция для вывода информации о конкретной заметке
def view_note(note_id):
    notes = load_notes()  # Загружаем текущие заметки
    for note in notes:
        if note["id"] == note_id:
            print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Текст: {note["body"]}, Дата создания: {note["timestamp"]}')
            return
    print("Заметка с указанным идентификатором не найдена.")

# Функция для фильтрации заметок по дате
def filter_notes_by_date(date):
    notes = load_notes()  # Загружаем текущие заметки
    filtered_notes = [note for note in notes if note["timestamp"].split()[0] == date]  # Фильтруем заметки
    if not filtered_notes:
        print("Заметок за указанную дату нет.")
    else:
        print(f"Список заметок за {date}:")
        for note in filtered_notes:
            print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Дата создания: {note["timestamp"]}')

# Основная функция программы
def main():
    while True:
        print("\n1. Показать все заметки")
        print("2. Добавить новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать заметку")
        print("6. Выборка по дате")
        print("7. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == "1":
            list_notes()
        elif choice == "2":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            add_note(title, body)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новый текст заметки: ")
            edit_note(note_id, title, body)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            delete_note(note_id)
        elif choice == "5":
            note_id = int(input("Введите ID заметки для просмотра: "))
            view_note(note_id)
        elif choice == "6":
            date = input("Введите дату в формате ГГГГ-ММ-ДД: ")
            filter_notes_by_date(date)
        elif choice == "7":
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()