class Patient:
    is_admitted = False
    name = None
    disease = None
    age = None
    medicine = None

    def __init__(self, name, disease, age):
        self.name = name
        self.disease = disease
        self.age = age

    def admission(self):
        self.is_admitted = True
        return f"{self.name} is admitted to the hospital for {self.disease}, and he is {self.age} years old"

    def diagnosis(self, medicine):
        self.medicine = medicine
        return f"doctor gave the patient {medicine} for his {self.disease}"

    def medication(self):
        if self.medicine:
            return f"patient is taking the {self.medicine}"
        return "no medicine to take"

    def discharge(self):
        if self.is_admitted:
            return f"{self.name} is discharged after medication"
        return "patient is not admitted yet"


person = Patient("Sameh", "flu", 30)
print(person.admission())
print(person.diagnosis("paracetamol"))
print(person.medication())
print(person.discharge())
