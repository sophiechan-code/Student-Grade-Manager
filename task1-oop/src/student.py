from .person import Person

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
        self.grades = []

    def get_role(self):
        return "Student"
