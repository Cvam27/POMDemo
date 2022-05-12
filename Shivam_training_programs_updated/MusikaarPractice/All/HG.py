import re

floors = {'0': 'Cardiology', '1': 'Oncology', '2': 'Orthopaedic', '3': 'Ophthalmology'}
problems = {'Cardiology': ['Heart', 'Blood Pressure', 'Cholesterol', 'Chest pain'],
            'Ophthalmology': ['Lasik', 'Loss of vision', 'Color blindness', 'Change in vision'],
            'Orthopaedic': ['Fracture', 'Arthritis', 'Back pain', 'Spine problem', 'Shoulder pain',
                            'Joint replacement'], 'Oncology': ['Tumour', 'Chemo', 'Radiation']}

allotment_floor = None
allotment_dept = None


class Hospital_class:

    @staticmethod
    def doctor_dept():
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

    @staticmethod
    def save_patient_info():
        global allotment_floor, allotment_dept
        try:
            patient_name = input("Enter patient name : ")
            patient_age = input("Enter patient age : ")
            patient_gender = input("Enter patient gender : ")
            print(problems.values())
            patient_disease = input("Enter patient disease : ")
            for i, j in problems.items():
                if patient_disease in j:
                    allotment_dept = i
                    for k, l in floors.items():
                        if allotment_dept in l:
                            allotment_floor = k

            # Assigning data to file
            dict_to_file = open("patient_data.txt", 'a+')
            dict_to_file.write("Name: " + patient_name + ", ")
            dict_to_file.write("Age: " + patient_age + ", ")
            dict_to_file.write("Gender: " + patient_gender + ", ")
            dict_to_file.write("Disease: " + patient_disease + ", ")
            dict_to_file.write("Department: " + allotment_dept + ", ")
            dict_to_file.write("Floor: " + allotment_floor + "\n")
            print("Data saved")
            dict_to_file.close()

            # with open("patient_data.txt", "wt") as wp:
            #
            #     wp.
            # wp.write("name:"+patient_name + ",")
            # wp.write("age:"+patient_age+ ",")
            # wp.write("gender:"+patient_gender+ ",")
            # wp.write("disease:"+patient_disease+ ",")
            # wp.write("dept:"+allotment_dept+ ",")
            # wp.write("floor:"+allotment_floor + "\n")
        except:
            print("Please verify your details!!!")

    @staticmethod
    def relative():
        # try:
        ask_patient_name_to_meet = input("Enter patient name whom you want to meet: ")
        readPatient_data = open("patient_data.txt", "r")
        loaded_data = readPatient_data.read().split("\n")
        # print(loaded_data)
        for i in loaded_data:
            find_patient_floor = re.findall(r"\b(Floor+.+)", i)
            if ask_patient_name_to_meet in i:
                print(f"Patient {ask_patient_name_to_meet} is on floor",
                      str(re.findall(r"\d", str(find_patient_floor))))
                break
            else:
                print("No such patient admitted")
                break

            # else:
            #     raise Exception
    # except:
    #
    # for i in

    # readPatient = open("patient_data.txt", 'r')
    # print(readPatient)
    # floor_finder_regex= re.findall("\b['floor']+.+", ask_patient_name_to_meet)
    # if ask_patient_name_to_meet in floor_finder_regex:
    #     print(f"{ask_patient_name_to_meet} is on floor {floor_finder_regex}")
    # except:
    #     print("No such patient admitted")


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


'''