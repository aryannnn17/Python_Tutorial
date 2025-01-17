class student:
    def student_skill(self):
        print("i can code and i play football")
class teacher:
    def teacher_skill(self):
        print("i teach students and i love math")
class youtuber:
    def youtuber_skill(self):
        print("i make videos and i am an entertainer")
class role(student,teacher,youtuber):
    pass

x=role()
x.teacher_skill()
x.youtuber_skill()
x.student_skill()