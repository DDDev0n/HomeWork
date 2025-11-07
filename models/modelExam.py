import heapq

class Exam:
    def __init__(self):
        self.queue = []  # приоритетная очередь
        self.counter = 0  # счётчик для FIFO

    def add_student(self, student):
        heapq.heappush(self.queue, (-student.rating, self.counter, student))
        self.counter += 1

    def next_student(self):
        if self.queue:
            # возвращаем самого приоритетного (наибольший рейтинг, первый добавленный)
            return heapq.heappop(self.queue)[2]
        return None

    def is_empty(self):
        return not self.queue