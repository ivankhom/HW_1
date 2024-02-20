class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.grade = {}
        self.finished_courses = []
        self.courses_in_progress = []

    def average_grade(self):
        total_grades = 0
        num_courses = 0
        for grades in self.grade.values():
            total_grades += sum(grades)
            num_courses += len(grades)
        if num_courses != 0:
            return total_grades / num_courses
        else:
            return 0

    def grand_average_grade(self, course):
        if course in self.courses_in_progress:
            if course in self.grade:
                total_grade = sum(self.grade[course])
                num_lecturers = len(self.grade[course])
                if num_lecturers != 0:
                    return total_grade / num_lecturers
        return 0
    def lect_rate(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.courses_attached and course in self.courses_in_progress:
            if grade <= 10:
                if course in lecture.grades:
                    lecture.grades[course] += [grade]
                else:
                    lecture.grades[course] = [grade]
            else:
                return 'Оцените по 10-балльной шкале'
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания {self.average_grade()}\n'
                f'Курсы в процессе изучения {self.courses_in_progress}\n'
                f'Завершенные курсы: Введение в программирование')

    def __lt__(self, other):
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = 0
        num_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            num_courses += len(grades)
        if num_courses != 0:
            return total_grades / num_courses
        else:
            return 0

    def grand_average_grade(self, course):
        if course in self.courses_attached:
            if course in self.grades:
                total_grade = sum(self.grades[course])
                num_lecturers = len(self.grades[course])
                if num_lecturers != 0:
                    return total_grade / num_lecturers
        return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n Средняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        return self.average_grade() > other.average_grade()


class Reviewer(Mentor):

    def hm_rate(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress and course in self.courses_attached:
            if course in student.grade:
                student.grade[course] += [grade]
            else:
                student.grade[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


stud_1 = Student('I', 'Kh', 'male')
stud_2 = Student('Mario', 'Cart', 'male')
stud_1.courses_in_progress = ['Git']
stud_2.courses_in_progress = ['Python', 'Git']
reviw1 = Reviewer('A', 'I')
reviw2 = Reviewer('Stanis', 'Barateon')
reviw1.courses_attached = ['Git']
reviw2.courses_attached = ['Python', 'Git']
reviw1.hm_rate(stud_1, 'Git', 6)
lect1 = Lecturer('Lect', 'Urer')
lect2 = Lecturer('Ivan', 'Khomchenko')
lect2.courses_attached = ['Python', 'Git']
lect1.courses_attached = ['Python']
stud_1.lect_rate(lect1, 'Python', 9)
stud_2.lect_rate(lect1, 'Python', 3)
stud_1.lect_rate(lect2, 'Python', 6)
print(stud_1)
print(stud_2)
print(lect1)
print(lect1 < lect2)
print(lect1.grand_average_grade("Git"))
