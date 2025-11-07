from models.modelExam import Exam
from models.modelStudent import Student
from models.modelFileRW import FileRW

def main():
    # Загружаем студентов
    students = FileRW.load_students("in/in.txt")

    exam = Exam()
    for s in students:
        exam.add_student(s)

    print("Порядок сдачи экзамена по приоритету (рейтинг → FIFO):\n")
    while not exam.is_empty():
        student = exam.next_student()
        print(f"Студент {student.name} (рейтинг {student.rating}) сдает экзамен.")
        # Преподаватель ставит оценку
        mark = input(f"Введите оценку для {student.name}: ")
        student.mark = mark

    # Сохраняем результаты
    FileRW.save_students("out/out.txt", students)
    print("\nРезультаты сохранены в файл.")

if __name__ == "__main__":
    main()
