import users
import projects

def project_management():
    while True:
        print("\n===== Project Management =====")
        print("1️ Create a New Project")
        print("2️ View All Projects")
        print("3️ Edit a Project")
        print("4️ Delete a Project")
        print("5️ Search Projects by Date")
        print("6️ Logout")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter Project Title: ")
            details = input("Enter Project Details: ")
            target = input("Enter Target Amount: ")
            start_date = input("Enter Start Date (YYYY-MM-DD): ")
            end_date = input("Enter End Date (YYYY-MM-DD): ")
            print(projects.Project.create_project( title, details, target, start_date, end_date))
        elif choice == "2":
            print(projects.Project.view_projects())
        elif choice == "3":
            title = input("Enter Project Title to Edit: ")
            new_title = input("Enter New Title: ")
            new_details = input("Enter New Details: ")
            new_target = input("Enter New Target Amount: ")
            new_start_date = input("Enter New Start Date (YYYY-MM-DD): ")
            new_end_date = input("Enter New End Date (YYYY-MM-DD): ")
            print(projects.Project.edit_project(title, new_title, new_details, new_target, new_start_date, new_end_date))
        elif choice == "4":
            title = input("Enter Project Title to Delete: ")
            print(projects.Project.delete_project(title))
        elif choice == "5":
            date = input("Enter Date (YYYY-MM-DD): ")
            print(projects.Project.search_by_date(date))
        elif choice == "6":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice! Please try again.")


def main():
    while True:
        print("\n===== User Management System =====")
        print("1️ Register")
        print("2️ Login")
        print("3️ Activate Account")
        print("4️ Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            confirm_password = input("Confirm Password: ")
            mobile = input("Enter Mobile Number: ")
            print(users.User.register(first_name, last_name, email, password, confirm_password, mobile))
        elif choice == "2":
            email = input("Enter Email: ")
            password = input("Enter Password: ")
            success=users.User.login(email, password)
            if success:
                project_management()
        elif choice == "3":
            email = input("Enter Email to Activate: ")
            print(users.User.activation(email))
        elif choice == "4":
            print("Exit..")
            break
        else:
            print("Invalid choice! Please try again.")



if __name__ == "__main__":
    main()
