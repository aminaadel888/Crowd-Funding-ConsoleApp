import datetime
import users

class Project:
    projects_file = "projectsDB.txt"

    def __init__(self, owner_email, title, details, target, start_date, end_date):
        self.owner_email = owner_email
        self.title = title
        self.details = details
        self.target = target
        self.start_date = start_date
        self.end_date = end_date

    def validate_date(date):
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")  # YYYY-MM-DD
            return True
        except ValueError:
            return False

    @staticmethod
    def create_project(title, details, target, start_date, end_date):
        if not Project.validate_date(start_date) or not Project.validate_date(end_date):
            return "Invalid date !!"
        new_project=Project(users.User.current_user, title, details, target, start_date, end_date)
        f=open(Project.projects_file,'a')
        f.write(f"{users.User.current_user};{title};{details};{target};{start_date};{end_date}\n")
        f.close()
        return "project create successfuly !!"

    @staticmethod 
    def view_projects():
        f=open(Project.projects_file,'r')
        projects=f.readlines()
        return "\n".join(projects)

    @staticmethod
    def edit_project(title, new_title, new_details, new_target, new_start_date, new_end_date):
        if users.User.current_user=="":
            return "You must be logged in to edit a project!"
        updated_projects = []
        found = False
        f=open(Project.projects_file,'r')
        for l in f:
            line=l.strip().split(";")
            if line[0] == users.User.current_user and line[1] == title:
                line[1] = new_title
                line[2] = new_details
                line[3] = new_target
                line[4] = new_start_date
                line[5] = new_end_date
                found = True
            updated_projects.append(";".join(line))

        if found==False:
            return "Project not found or not owned by you!"
        f=open(Project.projects_file,'w')  
        f.write("\n".join(updated_projects) + "\n")
        f.close()
        return "Project Updated successfully!"

    @staticmethod
    def delete_project (title):
        if users.User.current_user=="":
            return "You must be logged in to edit a project!"
        updated_projects = []
        found = False
        f=open(Project.projects_file,'r')
        for l in f:
            line=l.strip().split(";")
            if line[0] == users.User.current_user and line[1] == title:
                found=True
                continue
            updated_projects.append(";".join(line))
        if found==False:
            return "Project not found or not owned by you!"
        f=open(Project.projects_file,'w')  
        f.write("\n".join(updated_projects) + "\n")
        f.close()
        return "Project deleted successfully!"

    @staticmethod
    def search_by_date(date):
        if not Project.validate_date(date):
            return "Invalid date format! Use YYYY-MM-DD"

        matched_projects = []
        f=open(Project.projects_file,'r')
        for l in f:
            line = l.strip().split(";")
            if line[4] == date or line[5] == date:
                matched_projects.append(";".join(line))

        if matched_projects:
            return "\n".join(matched_projects)
        else:
            return "No projects found on this date!"
 