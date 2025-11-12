from models.modelExam import Exam
from models.modelCalculator import Calculator
from models.modelFileRW import FileRW

def main():
    print("\n1⃣  СТАТИЧЕСКИЙ ПОЛИМОРФИЗМ:")
    print("-" * 60)
    calc = Calculator()
    print(f"Результат: {calc.add(5, 3)}")
    print(f"Результат: {calc.add(5, 3, 2)}")
    print(f"Результат: {calc.add(1, 2, 3, 4, 5)}")
    # Загружаем студентов
    students = FileRW.load_students("in/in.txt")

    exam = Exam()
    for s in students:
        exam.add_student(s)

    print("\nПорядок сдачи экзамена по приоритету (рейтинг → FIFO):\n")
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
