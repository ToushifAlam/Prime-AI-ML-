# File I/O
f = open("sample_python_5.txt", "rb") #file object
#data = f.read()
#print(type(data),"\n", data, sep="")
#f.write("\n\nText tooverwrite \nthe complete data.")
#print(f.read())

#f = open("sample2_python_5.txt", "x")
#f.write("Some random text")
f.close()

with open("sample_python_5.txt", "r") as f:
    print(f.read())

#import os
#os.remove("sample2_python_5.txt")

# Exception Handling
try:
    x = int(input("Enter x: "))
    ans = 10/x
except ZeroDivisionError:
    print("Divide by 0 is not allowed")
except ValueError:
    print("Invalid Input")
else:
    print(f"Result = {ans}")
finally:
    print("End of program")


# List Comprehension
ls = [i**2 for i in range(1, 6) if i%2 != 0]
print(ls)

nums = [-2, -4, 3, 5, 2, -1]
ls = [0 if val<0 else val for val in nums]
print(ls)


# JSON Module
import json
json_str = '{"name":"Shradha", "isTeacher":true}'
py_obj = json.loads(json_str)
print(type(json_str), type(py_obj), py_obj)
py_obj = {
    "name": "Shradha",
    "isTeacher": True
}
json_str = json.dumps(py_obj)
print(type(json_str), json_str)
print()

d = {
    "name": "Shradha",
    "age": 27,
    "isTeacher": True
}
with open("data_python_5.json", "r") as f:
    #json.dump(d, f, indent=4, sort_keys=True)
    py_obj = json.load(f)
    print(py_obj)