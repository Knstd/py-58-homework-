class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.lect_grades:
                lecturer.lect_grades[course] += [grade]
            else:
                lecturer.lect_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _student_average_score(self):
        average_score = []
        for grades in self.grades.values():
            average_score.extend(grades)
        if len(average_score) != 0:
            return round(sum(average_score) / len(average_score), 1)
        else:
            return 'Оценок нет'

    def __str__(self):
        return f'Имя: {self.name}\
        \nФамилия: {self.surname}\
        \nСредняя оценка за домашние задания: {self._student_average_score()}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return 'Это не студент'
        else:
            return self._student_average_score() < other._student_average_score()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return 'Это не студент'
        else:
            return self._student_average_score() < other._student_average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}

    def _lect_average_score(self):
        average_score = []
        for grades in self.lect_grades.values():
            average_score.extend(grades)
        if len(average_score) != 0:
            return round(sum(average_score) / len(average_score), 1)
        else:
            return 'Оценок нет'

    def __str__(self):
        return f'Имя: {self.name}\
        \nФамилия: {self.surname}\
        \nСредняя оценка за лекции: {self._lect_average_score()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это не преподаватель'
        else:
            return self._lect_average_score() < other._lect_average_score()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Это не преподаватель'
        else:
            return self._lect_average_score() < other._lect_average_score()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached\
                and course in student.courses_in_progress and grade in range(1, 11):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

#Средняя оценка студентов в рамках курса
def student_average_course(course, *students):
    average_score = []
    for student in students:
        if student.grades.get(course):
            average_score.extend(student.grades[course])
    return f'Средняя оценка студентов в рамках курса "{course}": {round(sum(average_score)/len(average_score), 1)}'

#Средняя оценка преподавателей в рамках курса
def lecturer_average_course(course, *lecturers):
    average_score = []
    for lecturer in lecturers:
        if lecturer.lect_grades.get(course):
            average_score.extend(lecturer.lect_grades[course])
    return f'Средняя оценка преподавателей в рамках курса "{course}": {round(sum(average_score)/len(average_score), 1)}'

#Создаем экземпляры классов
student_1 = Student('Alisa', 'Petrova', 'female')
student_2 = Student('Alexey', 'Alexeev', 'male')
reviewer_1 = Reviewer('Oleg', 'Ivanov')
reviewer_2 = Reviewer('Nikolay', 'Sidorov')
lecturer_1 = Lecturer('Boris', 'Petrov')
lecturer_2 = Lecturer('Ivan', 'Vasiliev')

#Прикрепляем к курсам
student_1.courses_in_progress += ['Python', 'C#', 'Git']
student_1.finished_courses += ['Java']
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['C#']
lecturer_1.courses_attached += ['Python', 'Git']
lecturer_2.courses_attached += ['Python', 'C#', 'Git']
reviewer_1.courses_attached += ['Python', 'C#', 'Git']
reviewer_2.courses_attached += ['C#', "Git"]

#Оценки
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_1, "C#", 7)
reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 5)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'C#', 4)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_2, 'Python', 7)

#Вывод
print(reviewer_1, end='\n\n')
print(reviewer_2, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print(student_1, end='\n\n')
print(student_2, end='\n\n')

print(lecturer_1.lect_grades)
print(student_1.grades, end='\n\n')

print(student_1 > student_2)
print(lecturer_2 > lecturer_1)
print(lecturer_2 > student_2, end='\n\n')
print(student_average_course('Python', student_1, student_2))
print(lecturer_average_course('Git', lecturer_2, lecturer_1))