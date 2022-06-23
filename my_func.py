from classes import *

print("\nЗадание 4\n")


def average_grade_students(students, cours):
    average_grade = []
    for student in students:
        if cours in student.courses_in_progress or student.finished_courses:
            grades_dict = student.grades
            grades = grades_dict[cours]
            for grade in grades:
                average_grade.append(grade)
    print(round(sum(average_grade) / len(average_grade), 2))


def average_grade_lectures(lecturers, cours):
    average_grade = []
    for lecturer in lecturers:
        if cours in lecturer.courses_attached:
            grades_dict = lecturer.grades
            grades = grades_dict[cours]
            for grade in grades:
                average_grade.append(grade)
    print(round(sum(average_grade) / len(average_grade), 2))

print("Средняя оценка за домашние задания по всем студентам в рамках Python курса")
average_grade_students(students, "Python")

print("Cредняя оценка за лекции всех лекторов в рамках Python курса")
average_grade_lectures(lecturers, "Python")

