"""Формирование отчёта об успеваемости в CSV."""
import csv

from grades import STUDENTS, average


def status(avg):
    """Статус студента по среднему баллу."""
    if avg >= 4.5:
        return "отличник"
    if avg >= 3.5:
        return "хорошист"
    return "требует внимания"


def save_report(students, path="report.csv"):
    """Сохраняет отчёт в CSV-файл и возвращает число строк."""
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Студент", "Средний балл", "Статус"])
        for name, grades in students.items():
            avg = round(average(grades), 2)
            writer.writerow([name, avg, status(avg)])
    return len(students)


if __name__ == "__main__":
    print("Записано строк:", save_report(STUDENTS))
