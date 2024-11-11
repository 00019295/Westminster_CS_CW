from src.Attendance import AttendanceRecord


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.attendance_records = []

    def add_student(self, student):
        self.students.append(student)

    def mark_attendance(self):
        print(f"Marking attendance for {self.name}")
        for student in self.students:
            status = input(f"Is {student.full_name} (ID: {student.student_id}) present? yes/no").strip().lower()
            print(f"Student: {student.full_name}, Grade: {student.grade}, IsPresent: {status}")
            self.attendance_records.append(AttendanceRecord(student, status))

    def show_attendance(self):
        print(f"Attendance records for {self.name}")
        for record in self.attendance_records:
            if(record.status == "yes"):
                status = "Present"
            elif(record.status == "no"):
                status = "Absent"
            print(f"Student: {record.student.full_name}, Grade: {record.student.grade}, Status: {status}")