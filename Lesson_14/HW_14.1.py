class GroupFullException(Exception):
    """Exception raised when attempting to add more than 10 students to a group."""

    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return (self.first_name, self.last_name, self.record_book) == (
                other.first_name,
                other.last_name,
                other.record_book,
            )
        return NotImplemented

    def __hash__(self):
        return hash((self.first_name, self.last_name, self.record_book))


class Group:
    def __init__(self, number):
        self.number = number
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise GroupFullException(
                "Група заповнена! Не можна додати більше 10 студентів."
            )
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


if __name__ == "__main__":
    group = Group("PD1")

    for i in range(1, 11):
        student = Student("Male", 20 + i, f"Student{i}", f"Lastname{i}", f"RB{i}")
        group.add_student(student)
    print(group)

    try:
        extra_student = Student("Female", 21, "Extra", "Student", "RB11")
        group.add_student(extra_student)
    except GroupFullException as e:
        print(e)
