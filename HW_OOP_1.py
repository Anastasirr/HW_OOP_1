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

    def rate_lec(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in
                lecturer.courses_attached):
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __average_score_st(self):
        if self.grades:
            com_lst_st = sum(self.grades.values(), start=[])
            return sum(com_lst_st) / len(com_lst_st)

    def __str__(self):
        return (f"Имя: {self.name} \n"
                f"Фамилия: {self.surname} \n"
                f"Средняя оценка за домашние задания: {self.__average_score_st()} \n"
                f"Курсы в процессе изучения: {','.join (self.courses_in_progress)} \n"
                f"Завершенные курсы: {','.join (self.finished_courses)}")

    def __lt__(self, other):
        if self.__average_score_st() < other.__average_score_st():
            return True
        else:
            return False


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

    def __average_score_lec(self):
        com_lst = sum(self.grades_lecturer.values(), start=[])
        return sum(com_lst) / len(com_lst)

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.__average_score_lec()}")

    def __lt__(self, other):
        if self.__average_score_lec() < other.__average_score_lec():
            return True
        else:
            return False


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}"


some_student_1 = Student("Rio", "Eman", "your_gender")
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']
some_student_1.finished_courses += ['Введение в программирование']

some_student_2 = Student("Rubi", "Evan", "your_gender")
some_student_2.courses_in_progress += ['Python']
some_student_2.finished_courses += ['Введение в программирование']

some_lecturer_1 = Lecturer("Andrey", "Pavlov")
some_lecturer_1.courses_attached += ['Python']

some_lecturer_2 = Lecturer("Nikolai", "Denisov")
some_lecturer_2.courses_attached += ['Python']
some_lecturer_2.courses_attached += ['Git']

some_reviewer_1 = Reviewer("Some", "Buddy")
some_reviewer_1.courses_attached += ['Python']
some_reviewer_1.courses_attached += ['Git']

some_reviewer_2 = Reviewer("Roman", "Bugaev")
some_reviewer_2.courses_attached += ['Python']
some_reviewer_2.courses_attached += ['Git']

some_student_1.rate_lec(some_lecturer_1, 'Python', 10)
some_student_1.rate_lec(some_lecturer_1, 'Python', 8)
some_student_2.rate_lec(some_lecturer_1, 'Python', 5)

some_student_1.rate_lec(some_lecturer_2, 'Git', 9)
some_student_2.rate_lec(some_lecturer_2, 'Python', 7)
some_student_2.rate_lec(some_lecturer_2, 'Python', 8)

some_reviewer_1.rate_hw(some_student_1, 'Python', 10)
some_reviewer_1.rate_hw(some_student_1, 'Python', 5)
some_reviewer_1.rate_hw(some_student_2, 'Python', 8)

some_reviewer_1.rate_hw(some_student_2, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Python', 8)
some_reviewer_2.rate_hw(some_student_2, 'Git', 9)

print(some_reviewer_1)
# print(some_reviewer_2)
print('')
print(some_lecturer_1)
# print(some_lecturer_2)
print('')
print(some_student_1)
# print(some_student_2)
print('')
print(some_student_1 > some_student_2)
print(some_lecturer_1 < some_lecturer_2)

student_lst = [some_student_1, some_student_2]
lecturer_lst = [some_lecturer_1, some_lecturer_2]


def avg_grade_all_student(student_lst, course):
    grade_all_st = []
    if student_lst:
        for student in student_lst:
            for key, value in student.grades.items():
                if key == course:
                    grade_all_st += value
    return sum(grade_all_st) / len(grade_all_st)


print(avg_grade_all_student(student_lst, "Python"))


def avg_grade_all_lecturer(lecturer_lst, course):
    grade_all_lec = []
    if lecturer_lst:
        for lecturer in lecturer_lst:
            for key, value in lecturer.grades_lecturer.items():
                if key == course:
                    grade_all_lec += value
    return sum(grade_all_lec) / len(grade_all_lec)


print(avg_grade_all_lecturer(lecturer_lst, "Python"))
