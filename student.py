from datetime import datetime


class Student:
    def __init__(self, student_id, name, student_class, gender, dob):
        self.student_id = student_id
        self.name = name
        self.student_class = student_class
        self.gender = gender
        self.dob = dob
        self.scores = {}
        self.date_entered = None

    def set_scores(self, scores):
        self.scores = scores
        self.date_entered = datetime.now().strftime("%Y-%m-%d %H:%M")

    def total(self):
        return sum(self.scores.values())

    def average(self):
        if not self.scores:
            return 0
        return self.total() / len(self.scores)

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        s = Student(data["student_id"], data["name"], data["student_class"],
                    data["gender"], data["dob"])
        s.scores = data["scores"]
        s.date_entered = data["date_entered"]
        return s