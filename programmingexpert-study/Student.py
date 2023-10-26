class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        if new_grade < 0 or new_grade > 100:
            raise ValueError("New grade not in the accepted range of [0-100].")
        self._grade = new_grade

    @classmethod
    def get_best_student(cls):
        best_student = None
        for student in cls.all_students: 
            if best_student == None or student.grade > best_student.grade:
                best_student = student
        return best_student

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @staticmethod
    def calculate_average_grade(students):
        total_num_students = len(students)
        if total_num_students == 0:
            return -1
            
        grade_sum = 0
        for student in students:  # add up the student grades
            grade_sum += student.grade

        return grade_sum / total_num_students