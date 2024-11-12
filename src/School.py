from src import Student
from src.Attendance import AttendanceRecord


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.attendance_records = []

    def add_student(self, student):
        self.students.append(student)

    def get_number_of_students(self):
        return len(self.students)

    def show_students_details(self):
        if not self.students:
            print("No students enrolled.")
        else:
            print(f"List of students in {self.name}:")
            for student in self.students:
                print(f"ID: {student.student_id}, Name: {student.full_name}, Grade: {student.grade}")

    def delete_student(self, student_id):
        updated_students = []
        for student in self.students:
            if student.student_id != student_id:
                updated_students.append(student)
                print(f"Student with ID {student_id} has been deleted")

        self.students = updated_students

    def mark_attendance(self):
        print(f"Marking attendance for {self.name}")
        for student in self.students:
            while True:
                status = input(f"Is {student.full_name} (ID: {student.student_id}) present? yes/no: ").strip().lower()
                if status in ["yes", "no"]:
                    break
                else:
                    print("Invalid input. Please enter yes/no")
            self.attendance_records.append(AttendanceRecord(student, status))

    def show_attendance(self):
        print(f"Attendance records for {self.name}")
        for record in self.attendance_records:
            if record.status == "yes":
                status = "Present"
            elif record.status == "no":
                status = "Absent"
            print(f"Student: {record.student.full_name}, Grade: {record.student.grade}, Status: {status}")