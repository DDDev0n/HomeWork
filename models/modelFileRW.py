import os
from models.modelStudent import Student

class FileRW:
    @staticmethod
    def load_students(filename):
        students = []
        if not os.path.exists(filename):
            return students
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    student_id = parts[0].strip()
                    name = parts[1].strip()
                    rating = int(parts[2].strip())
                    students.append(Student(student_id, name, rating))
        return students

    @staticmethod
    def save_students(filename, students):
        with open(filename, "w") as f:
            for s in students:
                f.write(f"{s.id},{s.name},{s.rating},{s.mark}\n")