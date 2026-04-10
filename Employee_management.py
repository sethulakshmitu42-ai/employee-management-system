
import sqlite3

###create a database
def create_db():
    conn=sqlite3.connect("Employee.db")
    print("Database created Successfully.")

    ###create department table
    C=conn.cursor()
    C.execute(""" 
    CREATE TABLE department_tbl(
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name VARCHAR(50) NOT NULL,
            location VARCHAR(50),
            total_staff INTEGER,
            description VARCHAR(70)  )
    """)

    ###create HR table
    C.execute("""
    CREATE TABLE hr_tbl(
              hr_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR(50) NOT NULL,
              department_id INTEGER,
              department_name VARCHAR(50),
              age INTEGER,
              phone VARCHAR(20),
              place VARCHAR(30),
              email VARCHAR(50) NOT NULL UNIQUE,
              salary VARCHAR(20),
              password VARCHAR(30),
              FOREIGN KEY (department_id) REFERENCES department_tbl(department_id)

            )
    """)
    conn.commit()
    conn.close()
    print("successful create 2 tables.")
# create_db() 



### insert  into department
def Add_department(dept_name, location, total_staff, description):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO department_tbl(department_name, location, total_staff, description)
        VALUES (?, ?, ?, ?)
    """, (dept_name, location, total_staff, description))

    conn.commit()
    conn.close()

# dept_name = input("Enter Department Name: ")
# location = input("Enter Location: ")
# total_staff = int(input("Enter Total Staff: "))
# description = input("Enter Description: ")
# print(" Add Department successfully.")
    
# # Add_department(dept_name, location, total_staff, description)   


### view department
from tabulate import tabulate
def view_dept():
    print("\n"+"="*90)
    print("                                 VIEW DEPARTMENT                        ")
    print("="*90)
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM department_tbl """)
    rows=C.fetchall()
    conn.commit()
    conn.close()

    headers=["DEPARMENT_ID","DEPARTMENT_NAME","LOCATION","TOTAL_STAFF","DESCRIPTION"]
    print(tabulate(rows,headers,tablefmt="fancy_grid"))

# view_dept()

###  update dept
def update_department(dept_name, location, total_staff, description,dept_id):   
    
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()
    c.execute("""
        UPDATE department_tbl
        SET department_name=?, location=?, total_staff=?, description=?
        WHERE department_id=?
    """, (dept_name, location, total_staff, description, dept_id))

    conn.commit()
    if c.rowcount > 0:
        print("Updated Department Table successfully!")
    else:
        print("Department ID not found")
    conn.close()
# dept_id = int(input("Enter Department ID to update: "))
# dept_name = input("Enter new Department Name: ")
# location = input("Enter new Location: ")
# total_staff = int(input("Enter new Total Staff: "))
# description = input("Enter new Description: ")
# update_department(dept_name, location, total_staff, description,dept_id)
# print("updated Department Table successfully!")



### Delete Department
def delete_department(dept_id):
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" 
        DELETE FROM department_tbl WHERE department_id=?
""",(dept_id,))
    conn.commit()
    conn.close()
    print("Deleted Successfully")
# dept_id=int(input("enter Department  id : "))
# delete_department(dept_id)




### Hr Table Add
    
def Add_hr(name,department_id,department_name,age,phone,place,email,salary,password):
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute("""
         INSERT INTO hr_tbl(name, department_id, department_name, age, phone, place, email, salary, password)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (name, department_id, department_name, age, phone, place, email, salary, password))
    conn.commit()
    conn.close()
    print("Successfull")

# Name=input("Enter the name:")
# Department_id=input("Enter the Department_id:")
# Department_name=input("Enter the Department name :")
# Age=int(input("Enter hr age:"))
# Phone=input("Enter the phone number:")
# place=input("Enter the Place:")
# Email=input("Enter the email id:")
# Salary=input("Enter the salary:")
# Password=input("Enter the password:")
# Add_hr(Name,Department_id,Department_name,Age,Phone,place,Email,Salary,Password)    


###VIEW hr table
def view_hr():
    print("\n"+"="*90)
    print("                                 VIEW HR                       ")
    print("="*90)
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM hr_tbl """)
    rows=C.fetchall()
    conn.commit()
    conn.close()

    headers=["HR_ID","NAME","DEPT_ID","DEPT_NAME","AGE","PHONE","PLACE","EMAIL","SALARY","PASSWORD"]
    print(tabulate(rows,headers,tablefmt="grid"))
    
# view_hr()


###Update Hr
def update_hr(name, department_id, department_name, age, phone,place, email, salary, password, hr_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()                   
    C.execute(""" 
        UPDATE hr_tbl 
        SET name=?, department_id=?, department_name=?, age=?, phone=?,place=?, email=?, salary=?, password=? 
        WHERE hr_id=?
    """, (name, department_id, department_name, age, phone,place, email, salary, password, hr_id))
    conn.commit()
    conn.close()

# hr_id = int(input("Enter HR id: "))
# new_name = input("Enter new name: ")
# new_dept_id = input("Enter new dept id: ")
# new_dept_name = input("Enter new dept name: ")
# new_age = int(input("Enter new age: "))
# new_phone = input("Enter new phone: ")
# new_place = input("Enter new place: ")
# new_email = input("Enter new email: ")
# new_salary = input("Enter new salary: ")
# new_password = input("Enter new password: ")

# update_hr(new_name, new_dept_id, new_dept_name, new_age, new_phone,new_place, new_email, new_salary, new_password, hr_id)
# print("updated hr details successfully!")  
    
### Delete hr
def delete_hr(hr_id):
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" 
        DELETE FROM hr_tbl WHERE hr_id=?
""",(hr_id,))
    conn.commit()
    conn.close()
    print("Deleted Successfully")
# hr_id=int(input("enter HR id : "))
# delete_hr(hr_id)    



###staff table
    
def staff_tbl():
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()
  
    c.execute("""
       CREATE TABLE staff_tbl(
              staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name VARCHAR(50) NOT NULL,
              department_id VARCHAR(20) NOT NULL,
              department_name VARCHAR(20) NOT NULL,
              age INT,
              phone VARCHAR(50),
              email VARCHAR(50) UNIQUE,
              place VARCHAR(100),
              designature VARCHAR(20),
              salary VARCHAR(50), 
              password VARCHAR(25)
       )

""")
    conn.commit()
    conn.close()
    print("Successfull create staff table")
# staff_tbl() 


## Add staff details          
def Add_staff(name,department_id,department_name,age,phone,email,place,designature,salary,password):
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute("""
        INSERT INTO staff_tbl(name,department_id,department_name,age,phone,email,place,designature,salary,password) VALUES(?,?,?,?,?,?,?,?,?,?)
    """,(name,department_id,department_name,age,phone,email,place,designature,salary,password))
    conn.commit()
    conn.close()
    print("Successfull")

# Name=input("Enter the name:")
# Department_id=input("Enter the Department_id:")
# Department_name=input("Enter the Department name :")
# Age=int(input("Enter the age:"))
# Phone=input("Enter the phone number:")
# Email=input("Enter the email id:")
# place=input("Enter the place:")
# Designature=input("Enter the Designature:")
# Salary=input("Enter the salary:")
# Password=input("Enter the password:")
# Add_staff(Name,Department_id,Department_name,Age,Phone,Email,place,Designature,Salary,Password)    




## update staff details
def update_staff(name, department_id, department_name, age, phone, email, place, designature, salary, password, staff_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()                   
    C.execute(""" 
        UPDATE staff_tbl SET name=?, department_id=?, department_name=?, age=?, phone=?, email=?, place=?, designature=?, salary=?, password=? 
        WHERE staff_id=?
    """, (name, department_id, department_name, age, phone, email, place, designature, salary, password, staff_id))
    conn.commit()
    conn.close()


# staff_id = int(input("Enter staff id: "))
# new_name = input("Enter new name: ")
# new_dept_id = input("Enter new dept id: ")
# new_dept_name = input("Enter new dept name: ")
# new_age = int(input("Enter new age: "))
# new_phone = input("Enter new phone: ")
# new_email = input("Enter new email: ")
# new_place = input("Enter new place: ")
# new_designature = input("Enter new designature: ")
# new_salary = input("Enter new salary: ")
# new_password = input("Enter new password: ")

# update_staff(new_name, new_dept_id, new_dept_name, new_age, new_phone, new_email, new_place, new_designature, new_salary, new_password, staff_id)
# print("Staff record updated successfully!")
    
### VIEW STAFF
def view_staff():
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" SELECT * FROM staff_tbl """)
    rows=C.fetchall()
    conn.commit()
    conn.close()
    
    headers=["Staff_id","NAME","DEPT_ID","DEPT_NAME","AGE","PHONE","EMAIL","PLACE","DESIGNATURE","SALARY","PASSWORD"]
    print(tabulate(rows,headers,tablefmt="fancy_grid"))
    
# view_staff()    



###view staff profile
def view_staff_profile(staff_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()

    C.execute("""
        SELECT * FROM staff_tbl WHERE staff_id=?
    """, (staff_id,))

    row = C.fetchone()

    conn.close()

    if row:
        headers = ["Id","Name","Dept_id","Dept_name","Age","Phone","Email","Place","Designature","Salary","Password"]
        print(tabulate([row], headers=headers, tablefmt="double_grid"))
    else:
        print("Staff not found")  


### delete staff
def delete_staff(staff_id):
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()                   
    C.execute(""" 
        DELETE FROM staff_tbl WHERE staff_id=?
""",(staff_id,))
    conn.commit()
    conn.close()
    print("Deleted Successfully")
# staff_id=int(input("enter Staff id : "))
# delete_staff(staff_id)    







##view hr profile
def view_hr_profile(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
    SELECT hr_id,name,department_id,department_name,age,phone,place,email,salary,password
    FROM hr_tbl
    WHERE hr_id=?
    """,(hr_id,))

    row = c.fetchone()
    if row:
        headers = ["HR_ID","NAME","DEPT_ID","DEPT_NAME","AGE","PHONE","PLACE","EMAIL","SALARY","PASSWORD"]
        print(tabulate([row], headers=headers, tablefmt="fancy_grid"))
    else:
        print("HR not found")

    conn.close()

def update_staff_by_hr(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("SELECT department_id FROM hr_tbl WHERE hr_id=?", (hr_id,))
    dept_id = c.fetchone()[0]

    c.execute("""
        SELECT staff_id, name FROM staff_tbl
        WHERE department_id=?
    """, (dept_id,))
    
    rows = c.fetchall()
    print(tabulate(rows, headers=["Staff ID", "Name"], tablefmt="fancy_grid"))

    staff_id = int(input("Enter Staff ID : "))

    new_name = input("Enter new name : ")
    new_age = int(input("Enter new age : "))
    new_phone = input("Enter new phone : ")
    new_email = input("Enter new email : ")
    new_place = input("Enter new place : ")
    new_designature = input("Enter new designature : ")
    new_salary = input("Enter new salary : ")
    new_password = input("Enter new password : ")

    c.execute("""
        UPDATE staff_tbl
        SET name=?, age=?, phone=?, email=?, place=?, designature=?, salary=?, password=?
        WHERE staff_id=? AND department_id=?
    """, (
        new_name, new_age, new_phone, new_email,
        new_place, new_designature, new_salary,
        new_password, staff_id, dept_id
    ))

    conn.commit()
    conn.close()

    print(" Staff updated successfully")


### view staff in my department
def view_staff_same_department(hr_id):

    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("SELECT department_name FROM hr_tbl WHERE hr_id=?", (hr_id,))
    dept_row = c.fetchone()

    if not dept_row:
        print("HR not found")
        conn.close()
        return

    dept = dept_row[0]

    c.execute("""
    SELECT staff_id,name,department_name,phone,email,designature,salary
    FROM staff_tbl
    WHERE department_name=?
    """, (dept,))

    rows = c.fetchall()

    if rows:
        headers = ["STAFF_ID","NAME","DEPT_NAME","PHONE","EMAIL","DESIGNATION","SALARY"]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No staff found in this department")

    conn.close()

###update staff
def update_staff_profile(name,department_name, age, phone, email, place, password, staff_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()

    C.execute("""
        UPDATE staff_tbl
        SET name=?, department_name=?, age=?, phone=?, email=?, place=?, password=?
        WHERE staff_id=?
    """, (name,department_name, age, phone, email, place, password, staff_id))

    conn.commit()
    conn.close()  




##########TASK 
def create_task_table():
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()
    C.execute(""" CREATE TABLE task_tbl(
              task_id INTEGER PRIMARY KEY AUTOINCREMENT,
              staff_id INTEGER,
              task_name VARCHAR(70),
              task_description VARCHAR(200),
              status VARCHAR(30)
    )

    """)
    conn.commit()
    conn.close()
    print("Task table created successful!. ")
# create_task_table()  


### HR assign task only to own department staff
def assign_task(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("SELECT department_id FROM hr_tbl WHERE hr_id=?", (hr_id,))
    dept_id = c.fetchone()[0]

    c.execute("SELECT staff_id,name FROM staff_tbl WHERE department_id=?", (dept_id,))
    rows = c.fetchall()

    print(tabulate(rows, headers=["Staff ID", "Name"], tablefmt="fancy_grid"))

    staff_id = int(input("Enter Staff ID : "))
    task_name = input("Enter Task Name : ")
    task_description = input("Enter Task Description : ")

    c.execute("""
        INSERT INTO task_tbl(staff_id, task_name, task_description, status)
        VALUES (?, ?, ?, ?)
    """, (staff_id, task_name, task_description, "Pending"))

    conn.commit()
    conn.close()
    print(" Task assigned successfully")


### HR view own department tasks
def view_department_tasks(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("SELECT department_id FROM hr_tbl WHERE hr_id=?", (hr_id,))
    dept_id = c.fetchone()[0]

    c.execute("""
        SELECT t.task_id, s.name, t.task_name, t.task_description, t.status
        FROM task_tbl t
        JOIN staff_tbl s ON t.staff_id = s.staff_id
        WHERE s.department_id=?
    """, (dept_id,))

    rows = c.fetchall()

    headers = ["Task ID", "Staff Name", "Task", "Description", "Status"]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    conn.close()


### HR edit task only own department
def edit_task(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    view_department_tasks(hr_id)

    task_id = int(input("Enter Task ID : "))
    task_name = input("New Task Name : ")
    task_description = input("New Description : ")

    c.execute("""
        UPDATE task_tbl
        SET task_name=?, task_description=?
        WHERE task_id=? AND staff_id IN (
            SELECT staff_id FROM staff_tbl WHERE department_id=
            (SELECT department_id FROM hr_tbl WHERE hr_id=?)
        )
    """, (task_name, task_description, task_id, hr_id))

    conn.commit()
    conn.close()

    print(" Task updated successfully")


### HR delete task only own department
def delete_task(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    view_department_tasks(hr_id)

    task_id = int(input("Enter Task ID : "))

    c.execute("""
        DELETE FROM task_tbl
        WHERE task_id=? AND staff_id IN (
            SELECT staff_id FROM staff_tbl WHERE department_id=
            (SELECT department_id FROM hr_tbl WHERE hr_id=?)
        )
    """, (task_id, hr_id))

    conn.commit()
    conn.close()

    print("Task deleted successfully")

###staff view task
def view_tasks(staff_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()

    C.execute("""
    SELECT task_id, task_name, task_description, status
    FROM task_tbl
    WHERE staff_id=?
    """, (staff_id,))

    rows = C.fetchall()

    if rows:
        headers = ["Task ID", "Task Name", "Description", "Status"]
        print(tabulate(rows, headers=headers, tablefmt="double_grid"))
    else:
        print("No task assigned")

    conn.close() 



###staff Update task status
def update_taskstaus(staff_id):
    conn = sqlite3.connect("Employee.db")
    C = conn.cursor()

    view_tasks(staff_id)

    task_id = int(input("Enter Task ID : "))
    new_status = input("Enter status (Completed / Pending / In Progress): ")

    C.execute("""
    UPDATE task_tbl
    SET status=?
    WHERE task_id=? AND staff_id=?
    """, (new_status, task_id, staff_id))

    conn.commit()
    conn.close()

    print("Task updated successfully.")




#### Leave Table
def create_leave_table():
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE leave_tbl(
            leave_id INTEGER PRIMARY KEY AUTOINCREMENT,
            staff_id INTEGER,
            leave_reason VARCHAR(100),
            from_date VARCHAR(20),
            to_date VARCHAR(20),
            status VARCHAR(20)
        )
    """)

    conn.commit()
    conn.close()
    print("Leave table created successfully")
    
# create_leave_table()
    
### Staff Apply Leave
def apply_leave(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    reason = input("Enter leave reason : ")
    from_date = input("Enter from date (YYYY-MM-DD): ")
    to_date = input("Enter to date (YYYY-MM-DD): ")

    c.execute("""
        INSERT INTO leave_tbl(staff_id, leave_reason, from_date, to_date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (staff_id, reason, from_date, to_date, "Pending"))

    conn.commit()
    conn.close()

    print("Leave applied successfully") 
   

### Staff View Leave Status
def view_my_leave(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT leave_id, leave_reason, from_date, to_date, status
        FROM leave_tbl
        WHERE staff_id=?
    """, (staff_id,))

    rows = c.fetchall()

    if rows:
        headers = ["Leave ID", "Reason", "From Date", "To Date", "Status"]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No leave records found")

    conn.close()

###Staff update leave
def update_my_leave(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT leave_id, leave_reason, from_date, to_date, status
        FROM leave_tbl
        WHERE staff_id=?
    """, (staff_id,))

    rows = c.fetchall()

    if rows:
        headers = ["Leave ID", "Reason", "From Date", "To Date", "Status"]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

        leave_id = int(input("Enter Leave ID : "))
        reason = input("Enter new reason : ")
        from_date = input("Enter new from date : ")
        to_date = input("Enter new to date : ")

        c.execute("""
            UPDATE leave_tbl
            SET leave_reason=?, from_date=?, to_date=?
            WHERE leave_id=? AND staff_id=? AND status='Pending'
        """, (reason, from_date, to_date, leave_id, staff_id))

        conn.commit()
        print(" Leave updated successfully")

    else:
        print("No leave record found")

    conn.close()

###delete staff leave 
def delete_my_leave(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT leave_id, leave_reason, from_date, to_date, status
        FROM leave_tbl
        WHERE staff_id=?
    """, (staff_id,))

    rows = c.fetchall()

    if rows:
        headers = ["Leave ID", "Reason", "From Date", "To Date", "Status"]
        print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

        leave_id = int(input("Enter Leave ID : "))

        c.execute("""
            DELETE FROM leave_tbl
            WHERE leave_id=? AND staff_id=? AND status='Pending'
        """, (leave_id, staff_id))

        conn.commit()
        print(" Leave deleted successfully")

    else:
        print("No leave record found")

    conn.close()


### HR View Leave Requests
def view_leave_requests():
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT * FROM leave_tbl
    """)

    rows = c.fetchall()

    headers = ["Leave ID", "Staff ID", "Reason", "From Date", "To Date", "Status"]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    conn.close()

### Hr->Update Leave Status
def update_leave_status():
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    leave_id = int(input("Enter Leave ID : "))
    status = input("Enter status (Approved / Rejected): ")

    c.execute("""
        UPDATE leave_tbl
        SET status=?
        WHERE leave_id=?
    """, (status, leave_id))

    conn.commit()
    conn.close()

    print("Leave updated successfully")


### Salary Table
def create_salary_table():
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE salary_tbl(
            salary_id INTEGER PRIMARY KEY AUTOINCREMENT,
            staff_id INTEGER,
            basic_salary INTEGER,
            bonus INTEGER,
            deduction INTEGER,
            total_salary INTEGER,
            month VARCHAR(20),
            FOREIGN KEY (staff_id) REFERENCES staff_tbl(staff_id)
        )
    """)

    conn.commit()
    conn.close()
    print("Salary table created successfully")

# create_salary_table()
    
### HR Add Salary
def add_salary(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("SELECT department_id FROM hr_tbl WHERE hr_id=?", (hr_id,))
    dept_id = c.fetchone()[0]

    c.execute("SELECT staff_id,name FROM staff_tbl WHERE department_id=?", (dept_id,))
    rows = c.fetchall()

    print(tabulate(rows, headers=["Staff ID", "Name"], tablefmt="fancy_grid"))

    staff_id = int(input("Enter Staff ID : "))
    basic = int(input("Enter Basic Salary : "))
    bonus = int(input("Enter Bonus : "))
    deduction = int(input("Enter Deduction : "))
    month = input("Enter Month : ")

    total = basic + bonus - deduction

    c.execute("""
        INSERT INTO salary_tbl(staff_id,basic_salary,bonus,deduction,total_salary,month)
        VALUES(?,?,?,?,?,?)
    """, (staff_id, basic, bonus, deduction, total, month))

    conn.commit()
    conn.close()

    print("Salary added successfully")

###HR edit salary
def edit_salary(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT sal.salary_id, s.name, sal.basic_salary, sal.bonus, sal.deduction, sal.month
        FROM salary_tbl sal
        JOIN staff_tbl s ON sal.staff_id=s.staff_id
        WHERE s.department_id=(SELECT department_id FROM hr_tbl WHERE hr_id=?)
    """, (hr_id,))

    rows = c.fetchall()
    print(tabulate(rows, headers=["Salary ID","Name","Basic","Bonus","Deduction","Month"], tablefmt="fancy_grid"))

    salary_id = int(input("Enter Salary ID : "))
    basic = int(input("New Basic Salary : "))
    bonus = int(input("New Bonus : "))
    deduction = int(input("New Deduction : "))

    total = basic + bonus - deduction

    c.execute("""
        UPDATE salary_tbl
        SET basic_salary=?, bonus=?, deduction=?, total_salary=?
        WHERE salary_id=?
    """, (basic, bonus, deduction, total, salary_id))

    conn.commit()
    conn.close()

    print("Salary updated successfully")  

###Hr->Deleted salary  
def delete_salary(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT sal.salary_id, s.name, sal.month
        FROM salary_tbl sal
        JOIN staff_tbl s ON sal.staff_id=s.staff_id
        WHERE s.department_id=(SELECT department_id FROM hr_tbl WHERE hr_id=?)
    """, (hr_id,))

    rows = c.fetchall()
    print(tabulate(rows, headers=["Salary ID","Name","Month"], tablefmt="fancy_grid"))

    salary_id = int(input("Enter Salary ID : "))

    c.execute("DELETE FROM salary_tbl WHERE salary_id=?", (salary_id,))

    conn.commit()
    conn.close()

    print("Salary deleted successfully")    

###HR->view salary details
def view_salary_details(hr_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT sal.salary_id, s.name, sal.basic_salary, sal.bonus,
               sal.deduction, sal.total_salary, sal.month
        FROM salary_tbl sal
        JOIN staff_tbl s ON sal.staff_id = s.staff_id
        WHERE s.department_id = (
            SELECT department_id FROM hr_tbl WHERE hr_id=?
        )
    """, (hr_id,))

    rows = c.fetchall()

    headers = ["Salary ID", "Name", "Basic", "Bonus", "Deduction", "Total", "Month"]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))

    conn.close()    


### View Salary
def view_salary(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT salary_id, staff_id, basic_salary, bonus, deduction, total_salary, month
        FROM salary_tbl
        WHERE staff_id=?
    """, (staff_id,))

    rows = c.fetchall()

    if rows:
        headers = ["Salary ID","Staff ID","Basic","Bonus","Deduction","Total","Month"]
        print(tabulate(rows, headers=headers, tablefmt="double_grid"))
    else:
        print("No salary record found")

    conn.close()

#### Generate Monthly Payslip in Table Format
def generate_payslip(staff_id):
    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
        SELECT s.name, s.designature, sal.basic_salary, sal.bonus,
               sal.deduction, sal.total_salary, sal.month
        FROM staff_tbl s
        JOIN salary_tbl sal ON s.staff_id = sal.staff_id
        WHERE s.staff_id=?
        ORDER BY sal.salary_id DESC
        LIMIT 1
    """, (staff_id,))

    row = c.fetchone()

    conn.close()

    if row:
        headers = [
            "Name",
            "Designation",
            "Basic Salary",
            "Bonus",
            "Deduction",
            "Total Salary",
            "Month"
        ]

        print("\n" + "="*90)
        print("                     MONTHLY PAYSLIP")
        print("="*90)

        print(tabulate([row], headers=headers, tablefmt="fancy_grid"))

    else:
        print("No salary record found")

###hrlogin
def hr_login():
    hr_id=int(input("Enter the HR id : "))
    password=input("Enter the Password : ")
    conn=sqlite3.connect("Employee.db")
    C=conn.cursor()
    C.execute("SELECT * FROM hr_tbl WHERE hr_id=? and password=?",(hr_id,password))
    user=C.fetchone()
    conn.close()
    if user:
        print("Welcome HR")
        hr_menu(hr_id)

    else: 
        print("Invalid login ! check id and password. ") 




###stafflogin
def staff_login():
    staff_id = int(input("Enter Staff ID: "))
    password = input("Enter Password: ")

    conn = sqlite3.connect("Employee.db")
    c = conn.cursor()

    c.execute("""
    SELECT * FROM staff_tbl
    WHERE staff_id=? AND password=?
    """,(staff_id,password))

    user = c.fetchone()

    conn.close()

    if user:
        staff_menu(staff_id)
    else:
        print("Invalid Login !. please check you id and password. ")






###hr menu
def hr_menu(hr_id):
    while True:
        menu_data = [
            ["1", "👤 View my Profile"],
            ["2", "✏️ Update my profile"],

            ["3", "➕ Add staff"],
            ["4", "📋 View Staff details in my department"],
            ["5", "🗑️ Delete staff"],
            ["6", "✏️ Edit staff details"],


            ["7", "📌 Assign task"],
            ["8", "📋 View department tasks"],
            ["9", "✏️ Edit department tasks"],
            ["10", "🗑️ Delete task"],
            
            ["11", "📄 View leave requests from staff"],
            ["12", "✅ Approve / Reject leave from staff"],

            ["13", "💰 Add salary"],
            ["14", "✏️ Edit salary"],
            ["15", "🗑️ Delete salary"],
            ["16", "📄 View salary details"],


            ["17", "🚪Exit"],
        ]

        print("\n" + "=" * 40)
        print("      👨‍💼HR MENU 👨‍💼    ")
        print("=" * 40)
        headers = ["choice", "Action"]
        print(tabulate(menu_data, headers, tablefmt="fancy_grid"))

        try:
            choice = int(input("👉 Enter your choice : "))

            if choice == 1:
                view_hr_profile(hr_id)

            elif choice == 2:
                new_name = input("Enter new name: ")
                new_dept_id = input("Enter new dept id: ")
                new_dept_name = input("Enter new dept name: ")
                new_age = int(input("Enter new age: "))
                new_phone = input("Enter new phone: ")
                new_place = input("Enter new place: ")
                new_email = input("Enter new email: ")
                new_salary = input("Enter new salary: ")
                new_password = input("Enter new password: ")

                update_hr(
                    new_name, new_dept_id, new_dept_name,
                    new_age, new_phone, new_place,
                    new_email, new_salary, new_password, hr_id
                )

            elif choice == 3:
                Name = input("Enter the name: ")
                Department_id = input("Enter the Department_id: ")
                Department_name = input("Enter the Department name : ")
                Age = int(input("Enter staff age: "))
                Phone = input("Enter the phone number: ")
                Email = input("Enter the email id: ")
                place = input("Enter the place: ")
                Designature = input("Enter the Designature: ")
                Salary = input("Enter the salary: ")
                Password = input("Enter the password: ")

                Add_staff(
                    Name, Department_id, Department_name,
                    Age, Phone, Email, place,
                    Designature, Salary, Password
                )

            elif choice == 4:
                view_staff_same_department(hr_id)

            elif choice == 5:
                Staff_id = int(input("Enter Staff id : "))
                delete_staff(Staff_id)
            elif choice == 6:
                update_staff_by_hr(hr_id)    

            elif choice == 7:
                assign_task(hr_id)

            elif choice==8:
                view_department_tasks(hr_id)    

            elif choice==9:
                edit_task(hr_id)

            elif choice==10:
                delete_task(hr_id)
                    


            elif choice == 11:
                view_leave_requests()
            elif choice == 12:
                update_leave_status()  
              
            elif choice == 13:
                add_salary(hr_id)
            elif choice == 14:
                edit_salary(hr_id)
            elif choice == 15:
                delete_salary(hr_id) 
            elif choice == 16:
                view_salary_details(hr_id)          

            elif choice == 17:
                print("🚪Exiting program!")
                break

            else:
                print("⚠️ Please enter numbers correctly.! Please try again.")

        except ValueError:
            print("⚠️ Invalid input! Please enter numbers correctly.")

        except Exception as e:
            print("❌ Error! somethin went wrong", e)    




###staff menu
def staff_menu(staff_id):

    while True:
        menu_data = [
            ["1", "👤 View my profile"],
            ["2", "✏️ Update my profile"],

            ["3", "📋 View task"],
            ["4", "✅ Update/submit task information"],

            ["5", "📝 Apply Leave"],
            ["6", "📄 View Approve Leave"],
            ["7", "✏️ Update my leave"],
            ["8", "🗑️ Delete my leave"],

            ["9","💰  View Salary"],
            ["10","🧾  View Monthly Payslip"],

            ["11", "🚪Exit"]

        ]

        print("\n" + "=" * 40)
        print("      👩‍💻 STAFF MENU 👨‍💻  ")
        print("=" * 40)
        headers = ["Choice", "Action"]
        print(tabulate(menu_data, headers, tablefmt="fancy_grid"))

        try:
            choice = int(input("👉 Enter your choice : "))

            if choice == 1:
                view_staff_profile(staff_id)

            elif choice == 2:
                new_name = input("Enter new name: ")
                department_name=input("Enter new department name: ")
                new_age = int(input("Enter new age: "))
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_place = input("Enter new place: ")
                new_password = input("Enter new password: ")

                update_staff_profile(
                    new_name,
                    department_name,
                    new_age,
                    new_phone,
                    new_email,
                    new_place,
                    new_password,
                    staff_id
                )

                print("✅ Profile updated successfully!")
                view_staff_profile(staff_id)

            elif choice == 3:
                view_tasks(staff_id)

            elif choice == 4:
                update_taskstaus(staff_id)
            elif choice == 5:
                apply_leave(staff_id)
            elif choice == 6:
                view_my_leave(staff_id)
            elif choice == 7:
                update_my_leave(staff_id)   
            elif choice == 8:
                delete_my_leave(staff_id)    
            elif choice == 9:
                view_salary(staff_id)
            elif choice==10:
                generate_payslip(staff_id)    
            elif choice == 11:
                print("🚪 Exiting program!")
                break

            else:
                print("⚠️ Invalid choice! Please try again.")

        except ValueError:
            print("⚠️ Invalid input! Please enter numbers where required.")

        except Exception as e:
            print("❌ Error! Somethin went wrong:", e)




### admin menu
def admin_menu():
    while True:
        menu_data = [
            ["1", "🏢 Add Department"],
            ["2", "📋 View Department"],
            ["3", "✏️ Update Department"],
            ["4", "🗑️ Delete Department"],

            ["5", "👨‍💼 Add HR"],
            ["6", "📄 View HR"],
            ["7", "✏️ Update HR"],
            ["8", "🗑️ Delete HR"],

            ["9", "👩‍💻 View staff"],
            ["10","🗑️ Delete staff"],

            ["11","🚪 Exit"]
        ]

        print("\n" + "=" * 40)
        print("      👑 ADMIN MENU 👑     ")
        print("=" * 40)
        headers = ["Choice", "Action"]
        print(tabulate(menu_data, headers, tablefmt="fancy_grid"))

        try:
            choice = int(input("👉 Enter your choice : "))

            if choice == 1:
                dept_name = input("Enter Department Name: ")
                location = input("Enter Location: ")
                total_staff = int(input("Enter Total Staff: "))
                description = input("Enter Description: ")
                Add_department(dept_name, location, total_staff, description)
                print("✅ Department added successfully.")

            elif choice == 2:
                view_dept()

            elif choice == 3:
                dept_id = int(input("Enter Department ID to update: "))
                dept_name = input("Enter new Department Name: ")
                location = input("Enter new Location: ")
                total_staff = int(input("Enter new Total Staff: "))
                description = input("Enter new Description: ")
                update_department(dept_name, location, total_staff, description, dept_id)
                print("✅ Department updated successfully!")

            elif choice == 4:
                dept_id = int(input("Enter Department ID: "))
                delete_department(dept_id)

            elif choice == 5:
                Name = input("Enter the name: ")
                Department_id = input("Enter Department ID: ")
                Department_name = input("Enter Department name: ")
                Age = int(input("Enter HR age: "))
                Phone = input("Enter phone number: ")
                place = input("Enter place: ")
                Email = input("Enter email id: ")
                Salary = input("Enter salary: ")
                Password = input("Enter password: ")
                Add_hr(Name, Department_id, Department_name, Age, Phone, place, Email, Salary, Password)
                print("✅ HR added successfully.")

            elif choice == 6:
                view_hr()

            elif choice == 7:
                hr_id = int(input("Enter HR id: "))
                new_name = input("Enter new name: ")
                new_dept_id = input("Enter new dept id: ")
                new_dept_name = input("Enter new dept name: ")
                new_age = int(input("Enter new age: "))
                new_phone = input("Enter new phone: ")
                new_place = input("Enter new place: ")
                new_email = input("Enter new email: ")
                new_salary = input("Enter new salary: ")
                new_password = input("Enter new password: ")

                update_hr(
                    new_name, new_dept_id, new_dept_name,
                    new_age, new_phone, new_place,
                    new_email, new_salary, new_password, hr_id
                )
                print("✅ HR updated successfully!")

            elif choice == 8:
                hr_id = int(input("Enter HR id: "))
                delete_hr(hr_id)
            elif choice==9:
                view_staff()
            elif choice==10:
                staff_id=int(input("enter Staff id : "))
                delete_staff(staff_id)  
            elif choice == 11:
                print("🚪Exiting program. Goodbye!")
                break

            else:
                print("❌ Invalid choice! Please try again.")

        except ValueError:
            print("⚠️ Invalid input! Please enter numbers where required.")

        except Exception as e:
            print("❌ Error! Something went wrong :", e) 



##login

def login():
    while True:
        try:
            print("\n ===== 🔐LOGIN 🔐===== ")
            role = input("Login as (Admin/HR/Staff): ").strip().lower()

            if role == "admin":
                username = input("👤 Enter Admin Username : ")
                password = input("🔑 Enter the password : ")

                if username == "admin" and password == "a123":
                    print("✅ Login successful! Welcome Admin.")
                    admin_menu()
                    break
                else:
                    print("❌Invalid Username and Password")

            elif role == "hr":
                print("✅ Login successful! Welcome HR.")
                hr_login()
                break

            elif role == "staff":
                print("✅ Login successful! Welcome Staff.")
                staff_login()
                break

            else:
                print("⚠️ Invalid User! Please choose Admin, HR, or Staff")

        except Exception as e:
            print("❌ Error!!invalid user", e)


login()
