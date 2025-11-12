class Calculator:

    def add(self, *args):
        """Перегруженный метод сложения - работает с разным количеством аргументов"""
        if len(args) == 2:
            return self._add_two(args[0], args[1])
        elif len(args) == 3:
            return self._add_three(args[0], args[1], args[2])
        else:
            return sum(args)

    def _add_two(self, a, b):
        print(f"Сложение двух чисел: {a} + {b}")
        return a + b

    def _add_three(self, a, b, c):
        print(f"Сложение трёх чисел: {a} + {b} + {c}")
        return a + b + c