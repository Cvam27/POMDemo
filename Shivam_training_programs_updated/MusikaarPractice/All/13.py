import re

floors = {'0': 'Cardiology', '1': 'Oncology', '2': 'Orthopaedic', '3': 'Ophthalmology'}
problems = {'Cardiology': ['Heart', 'Blood Pressure', 'Cholesterol', 'Chest pain'],
            'Ophthalmology': ['Lasik', 'Loss of vision', 'Color blindness', 'Change in vision'],
            'Orthopaedic': ['Fracture', 'Arthritis', 'Back pain', 'Spine problem', 'Shoulder pain',
                            'Joint replacement'], 'Oncology': ['Tumour', 'Chemo', 'Radiation']}

allotment_floor = None
allotment_dept = None


class Hospital_class:

    def doctor_dept(self):
        try:
            cnt = 0
            ask_dept = input("Enter Department Name : ")
            for i, j in floors.items():
                if ask_dept in j:
                    print(f"{j} department is on floor {i}")
                    break
                else:
                    cnt = cnt + 1
                if cnt == len(floors) - 1:
                    raise Exception

        except:
            print("Invalid Dept")

    def save_patient_info(self):
        global allotment_floor, allotment_dept
        try:
            patient_name = input("Enter patient name : ")
            patient_age = input("Enter patient age : ")
            patient_gender = input("Enter patient gender : ")
            patient_disease = input("Enter patient disease : ")
            for i, j in problems.items():
                if patient_disease in j:
                    allotment_dept = i
                    for k, l in floors.items():
                        if allotment_dept in l:
                            allotment_floor = k
            patient_data = {
                "Name: " + patient_name: ["Age: " + patient_age, "Gender: " + patient_gender,
                                          "Disease: " + patient_disease, "Dept: " + allotment_dept,
                                          "Floor: " + allotment_floor, ]}
            print(patient_data)

            # Assigning data to file
            dict_to_file = open("patient_data.txt", 'a+')
            dict_to_file.write(str(patient_data) + "\n")
            dict_to_file.close()


        except:
            print("Something went wrong, Please verify your input")

    def relative(self):

        ask_patient_name_to_meet = input("Enter patient name whom you want to meet: ")
        readPatient_data = open("patient_data.txt", "r")
        loaded_data = readPatient_data.read().split("\n")
        got_data = False
        for i in loaded_data:
            find_patient_floor = re.findall(r"\b(Floor+.+)", i)
            if ask_patient_name_to_meet in i:
                print(f"Patient {ask_patient_name_to_meet} is on floor ",
                      str(re.findall(r"\d", str(find_patient_floor))))
                got_data = True
                break
        if not got_data:
            print("No such data")


if __name__ == '__main__':

    hospital_obj = Hospital_class()

    while True:
        user_type = input("Enter your user type- Doctor(D), Patient(P), Relative(R): ").upper()
        if user_type == 'D':
            hospital_obj.doctor_dept()
        elif user_type == 'P':
            hospital_obj.save_patient_info()
        elif user_type == 'R':
            hospital_obj.relative()

'''
Output
Enter your user type- Doctor(D), Patient(P), Relative(R): D
Enter Department Name : Oncology
Oncology department is on floor 1
Enter your user type- Doctor(D), Patient(P), Relative(R): P
Enter patient name : Tim
Enter patient age : 22
Enter patient gender : Male
Enter patient disease : Heart
{'Name: Tim': ['Age: 22', 'Gender: Male', 'Disease: Heart', 'Dept: Cardiology', 'Floor: 0']}
Enter your user type- Doctor(D), Patient(P), Relative(R): R
Enter patient name whom you want to meet: Tim
Patient Tim is on floor  ['0']
'''
