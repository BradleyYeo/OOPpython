from collections import defaultdict
from collections import namedtuple
from sys import getsizeof
Contact = namedtuple('Contact', "Email firstname lastname Country")
contacts = [Contact("james@jamesbond.com", "james", "Bond", "UK"),
           Contact("Rei@tan.com", "Rei", "Tan", "SG"),
           Contact("Brad@yeo.com", "Brad", "Yeo", "SG")]

# for contact in contacts:
#     print(f"Hello {contact.firstname} {contact.lastname} from {contact.Country} your email is {contact.Email}")

rei_good = Contact("Rei@tan.com", "Rei", "Tan", "SG")
print(getsizeof(rei_good))
rei = dict(email="Rei@tan.com", f2irstname="Rei", lastname= "Tan", country="SG")
print(getsizeof(rei))

class SimpleGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


class BySubjectGradebook:
    def __init__(self):
        self._grades = {}  # Outer dict

    def add_student(self, name):
        self._grades[name] = defaultdict(list)  # Inner dict

    def report_grade(self, name, subject, grade):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = defaultdict(list)

    def report_grade(self, name, subject, score, weight):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = defaultdict(Subject)

    def get_subject(self, name):
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = defaultdict(Student)

    def get_student(self, name):
        return self._students[name]


book = SimpleGradebook()
book.add_student('Isaac Newton')
book.report_grade('Isaac Newton', 90)
book.report_grade('Isaac Newton', 95)
book.report_grade('Isaac Newton', 85)

# print(book.average_grade('Isaac Newton'))

book = BySubjectGradebook()
book.add_student('Albert Einstein')
book.report_grade('Albert Einstein', 'Math', 75)
book.report_grade('Albert Einstein', 'Math', 65)
book.report_grade('Albert Einstein', 'Gym', 90)
book.report_grade('Albert Einstein', 'Gym', 95)
# print(book.average_grade('Albert Einstein'))

grades = [(95, 0.45), (85, 0.55)]
total = sum(score * weight for score, weight in grades)
total_weight = sum(weight for _, weight in grades)
average_grade = total / total_weight

Grade = namedtuple('Grade', ('score', 'weight'))

