print("\nЗадание 2\n")


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_Lecturer = Lecturer('Some', 'Man')
best_Lecturer.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student.rate_lecturer(best_Lecturer, 'Python', 10)
best_student.rate_lecturer(best_Lecturer, 'Python', 9)
best_student.rate_lecturer(best_Lecturer, 'Python', 8)
best_student.rate_lecturer(best_Lecturer, 'Python', 10)

first_Reviewer = Reviewer('Someone', 'Else')
first_Reviewer.courses_attached += ['Python']

first_Reviewer.rate_hw(best_student, 'Python', 10)
first_Reviewer.rate_hw(best_student, 'Python', 9)
first_Reviewer.rate_hw(best_student, 'Python', 8)
first_Reviewer.rate_hw(best_student, 'Python', 7)

print("Оценки студенту за Дз, полученные от эксперта", best_student.grades)
print("Оценки лектору за лекцию, полученные от студента", best_Lecturer.grades)