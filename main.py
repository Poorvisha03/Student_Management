from student_operations import*
from display import* 



print("  STUDENT MANAGEMENT SYSTEM  ".center(100,"="))
print("=".center(100,"="))
print("=")
display_menu()
if __name__ == "__main__":
    load_data() 
    while True:
        print("=".center(100,"="))
        print("=")
        print("Enter 0 to display menu.")
        choice = input("Enter your choice from the MENU  :  ").strip()
        if not choice:
            print("⚠️ No input detected. Please type a number and press Enter.")
            continue

        if choice == "0":
            display_menu()

        elif choice == "1":
            print("=".center(100,"="))
            print("=")
            add_student()

        elif choice == "2":
            print("=".center(100,"="))
            print("=")
            view_student()
        
        elif choice == "3":
            print("=".center(100,"="))
            print("=")
            delete_roll()

        elif choice == "4":
            print("=".center(100,"="))
            print("=")
            search_roll()

        elif choice == "5":
            print("=".center(100,"="))
            print("=")
            update_marks()

        elif choice == "6":
            print("=".center(100,"="))
            print("=")
            print("Thank you.")
            print("=".center(100,"="))
            print("=")
            flag = False
            break

        else :
            print("Please enter valid choice")
        
        
