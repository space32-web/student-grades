"""Расчёт успеваемости студентов."""


def average(grades):
    """Средний балл; для пустого списка — 0."""
    if not grades:
        return 0
    return sum(grades) / len(grades)


def best_student(students):
    """Имя студента с наибольшим средним баллом."""
    return max(students, key=lambda name: average(students[name]))


STUDENTS = {
    "Иванов": [5, 4, 5],
    "Петров": [3, 4, 4],
    "Сидорова": [5, 5, 5],
}


if __name__ == "__main__":
    for name, grades in STUDENTS.items():
        print(name, round(average(grades), 2))
    print("Лучший студент:", best_student(STUDENTS))
