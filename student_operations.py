import json
import os

details_dict = {}

FILE_NAME = "data.json"
def load_data():
    global details_dict
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                details_dict = json.load(file)
            
                details_dict = {int(k): v for k, v in details_dict.items()}
            except json.JSONDecodeError:
                details_dict = {}  
    else:
        details_dict = {}


def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(details_dict, file, indent=4)


def add_student():
    load_data()
    name = input("Name : ")
    roll = int(input("Roll Number : "))
    marks = int(input("Marks : "))
    if roll in details_dict:
        print(f"Roll No : {roll} Already Exists.")

    else:        
        details_dict[roll] = {
            "Name" : name,
            "Roll" : roll,
            "Marks" : marks
        }
        save_data()
        print("Student Added Successfully!!")

def view_student():
    load_data()
    if not details_dict:
        print("No students Found")
    else:
        for key,value in details_dict.items():
            print(f"Student Id = {key}")
            print(f"Name : {value["Name"]}")
            print(f"Roll : {value["Roll"]}")
            print(f"Marks : {value["Marks"]}")
            print("\n")

def delete_roll():
    load_data()
    del_roll = int(input("Enter Roll no to  Delete : "))
    if del_roll in details_dict:
        del details_dict[del_roll]
        save_data()
        print("Student Deleted Successfully!!")
    else:
        print(f"Roll no : {del_roll} Doesn't exist!!")

def search_roll():
    load_data()
    search_id = int(input("Enter Roll No : "))
    print("Searching.......")
    print("=".center(100,"="))
    print("=")
    if search_id not in details_dict:
        print("Roll No doesn't Exist.")
    else:
        print("Student Details")
        print("=".center(100,"="))
        print("=")
        for key, value in details_dict[search_id].items():
           
            print(f"{key} : {value}")

def update_marks():
    load_data()
    up_roll = int(input("Enter the Roll No : "))
    if up_roll not in details_dict:
        print("Roll No Doesn't Exist.")
    else:
        up_marks = int(input("Enter Updated Marks : "))
        details_dict[up_roll]["Marks"] = up_marks
        save_data()
        print("Student Marks Updated Successfully!!")