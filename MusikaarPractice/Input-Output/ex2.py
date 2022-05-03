import json

di1 = {
    "Employees": [
        {
            "Employee Name": "Sahil",
            "Employee Age": 27,
            "Employee Salary": 35000,
            "Programming Languages": "Java, HTML, C#"
        },
        {
            "Employee Name": "Zalak",
            "Employee Age": 29,
            "Employee Salary": 50000,
            "Programming Languages": "Java and Python"
        },
        {
            "Employee Name": "Sagar",
            "Employee Age": 32,
            "Employee Salary": 45000,
            "Programming Languages": "Java, C# and Python"
        },
        {
            "Employee Name": "Pritesh",
            "Employee Age": 22,
            "Employee Salary": 32000,
            "Programming Languages": "Java and C"
        },
        {
            "Employee Name": "Sonal",
            "Employee Age": 24,
            "Employee Salary": 22000,
            "Programming Languages": "Java, C and Python"
        }
    ]
}

json_obj = json.dumps(di1, indent=4)
with open("demo.json", 'r') as w:
    w.read()
