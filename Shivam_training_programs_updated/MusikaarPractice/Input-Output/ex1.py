import json

id = input("Enter Emp ID")
name = input("Enter name")
salary = input("Enter salary")
designation = input("Enter Designation")

di1 = {"id": id,
       "Name": name,
       "salary": salary,
       "designation": designation
       }

json_obj = json.dumps(di1, indent=4)

with open("emp_detail.json", "a+") as emp_write:
    emp_write.write(json_obj)
    emp_write.seek(0)
    print(emp_write.read())

# with open("emp_detail.json", "r") as emp_read:
