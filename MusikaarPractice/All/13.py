import re


class HospitalGate:
    @staticmethod
    def user_doctor(department):
        return department

    @staticmethod
    def search_patient(name):
        with open("patient_data.txt", "r") as search_patient:
            patient_name_regex = re.findall(r"\b[\w]+", ask_relative_patient_name)
            return str(patient_name_regex)


gate = HospitalGate()
user_type = input("Enter your user type- Doctor(D), Patient(P), Relative(R), Other(O): ")
if user_type == "D":
    ask_doctor_dept = input("Which Department? Cardiology(C), Oncology(O), Orthopaedic(OR), Ophthalmology(OP), "
                            "General(G) : ")
    print(gate.user_doctor("Ortho"))
elif user_type == "P":
    patient_name = input("Enter patient name : ")
    patient_age = input("Enter Patient age : ")
    patient_disease = input("Enter disease : ")
    patient_gender = input("Enter patient gender: ")
    with open("patient_data.txt", "a+") as p:
        p.write(patient_name + "\n")
        p.write(patient_age + "\n")
        p.write(patient_gender + "\n")
        p.write(patient_disease + "\n\n")
elif user_type == "R":
    try:
        ask_relative_patient_name = input("Enter patient name to meet : ")
        print("Patient is in ward", gate.search_patient())
    except Exception:
        print("No such patient")
