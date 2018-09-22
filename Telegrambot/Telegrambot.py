from Model.Services.StudentsService import StudentsService

studentService = StudentsService()

print(studentService.get_student("01-011"))

studentService.close()