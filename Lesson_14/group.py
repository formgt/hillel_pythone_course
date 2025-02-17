from student import Student


class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()

    def add_student(self, student):
        self.students.add(student)

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.students.remove(student)

    def __str__(self):
        sorted_students = sorted(self.students, key=lambda s: s.last_name)
        student_list = "\n".join(str(student) for student in sorted_students)
        return f"Number: {self.number}\n{student_list}"
