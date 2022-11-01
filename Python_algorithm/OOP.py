# 클래스 연동 : 한 클래스를 다른 클래스의 속성으로 받기
class Student:
    def __init__(self, name, id, studentid):
        self.name = name
        self.id = id
        self.studentid = studentid
        
class StudentId:
    def __init__(self, major, id):
        self.id = major[:3] + id