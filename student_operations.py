
details_dict = {}
def add_student():
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
        print("Student Added Successfully!!")

def view_student():
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
    del_roll = int(input("Enter Roll no to  Delete : "))
    if del_roll in details_dict:
        del details_dict[del_roll]
        print("Student Deleted Successfully!!")
    else:
        print(f"Roll no : {del_roll} Doesn't exist!!")

def search_roll():
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
    up_roll = int(input("Enter the Roll No : "))
    if up_roll not in details_dict:
        print("Roll No Doesn't Exist.")
    else:
        up_marks = int(input("Enter Updated Marks : "))
        details_dict[up_roll]["Marks"] = up_marks
        print("Student Marks Updated Successfully!!")