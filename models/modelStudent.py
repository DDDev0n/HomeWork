class Student:
    def __init__(self, student_id, name, rating, mark=None):
        self.id = student_id
        self.name = name
        self.rating = rating
        self.mark = mark

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.rating}, {self.mark}"



