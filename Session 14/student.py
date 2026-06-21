# create simple system for school,
# create class for student
# add these info to the user: name, age, ..
# add 2 methods to the user: take_exams, show_results
# user should take 2 exams and store the results in a list
# (take the results from the user in take_exams method),
# then show results on the screen using show_result method


class Student:
    name = ""
    age = None
    results = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def take_exams(self):
        for i in range(2):
            subject = input("what is the subject name? ")
            mark = input(f"what is the {subject} mark? ")

            self.results.append({"subject": subject, "mark": mark})

    def show_results(self):
        count = len(self.results)
        text = ""
        if count:
            total = 0

            for i in self.results:
                total += int(i["mark"])
                text += f'{i["subject"]} mark is {i["mark"]} '

            return f"avg is {total / count} and marks are {text}"

        else:
            return "add marks first"


student1 = Student("Fatma", 20)
student1.take_exams()
print(student1.show_results())
