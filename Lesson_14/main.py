from student import Student
from group import Group

if __name__ == "__main__":
    st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
    st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
    gr = Group("PD1")
    gr.add_student(st1)
    gr.add_student(st2)

    print(gr)
    assert gr.find_student("Jobs") == st1, "Test failed: st1 not found"
    assert gr.find_student("Jobs2") is None, "Test failed: non-existent student found"

    gr.delete_student("Taylor")
    print(gr)
