import csv

def get_student_from_file():
    try:
        with open("students.txt", 'r', encoding='utf-8') as rfile:
            return rfile.readlines()
    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)


def get_message():
    try:
        with open("message.txt", 'r', encoding='utf-8') as rfile:
            return rfile.read()
    except FileNotFoundError as ferr:
        print("Pliku nie znaleziono:", ferr)


def put_data_on_list(student_data):
    names = []
    tasks = []
    grades = []
    for student in student_data:
        student = list(student.split(','))
        names.append(student[1] + ' ' + student[2])
        tasks.append(student[3])
        grades.append(student[4].replace('\n',''))
    return names, tasks, grades


def complete_data(names, tasks, grades):
    message = get_message()
    try:
        for name, task, grade in zip(names, tasks, grades):
            print(message.format(name, task, grade, int(grade) + 1))
    except ValueError as verr:
        print("Nieprawidłowa wartość", verr)

def main():
    student_data = get_student_from_file()
    name, task, grade = put_data_on_list(student_data)
    complete_data(name, task, grade)


if __name__ == '__main__':
    main()