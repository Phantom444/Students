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
                      Lecturer) and self.courses_in_progress and self.finished_courses and course in lecturer.courses_attached and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        grades = []
        for grade in self.grades.values():
            for i in grade:
                grades.append(int(i))
        average_grades = sum(grades) / len(grades)
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {str(self.average_rating())}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_rating(self):
        grades = []
        for grade in self.grades.values():
            for i in grade:
                grades.append(int(i))
        average_grades = sum(grades) / len(grades)
        return average_grades

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.average_rating() < other.average_rating()

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {str(self.average_rating())}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grades):
        if isinstance(student,
                      Student) and course in lecturer.courses_attached and course in student.courses_in_progress and grades <= 10:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


student = Student('Ruoy', 'Eman', 'man')
student_1 = Student('Alex', 'Golovko', 'man')
student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
lecturer = Lecturer('Some', 'Buddy')
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

reviewer = Reviewer('Some', 'Buddy')

student.rate_lecturer(lecturer, 'Python', 10)
student_1.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 10)

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student_1, 'Python', 10)
reviewer.rate_hw(student, 'Git', 10)
reviewer.rate_hw(student_1, 'Git', 10)

student_list = [student, student_1]
lecturer_list = [lecturer, lecturer_1]


def average_grades_students(student, course):
    grade = 0
    count = 0
    for stud in student:
        if course in stud.courses_in_progress:
            value = stud.grades[course]
            count += len(value)
            grade += sum(value)
    return f'Средняя оценка всех студентов по курсу {course}: {grade / count}'


def average_grades_lecturer(lector, course):
    grade = 0
    count = 0
    for teacher in lector:
        for value in teacher.grades.values():
            for i in value:
                grade += i
                count += 1
    return f'Средняя оценка всех лекторов по курсу {course}: {grade / count}'



print(lecturer)
print()
print(lecturer_1)
print()
print(student)
print()
print(student_1)
print()
print(reviewer)
print()

print(average_grades_students(student_list, 'Python'))
print(average_grades_lecturer(lecturer_list, 'Python'))