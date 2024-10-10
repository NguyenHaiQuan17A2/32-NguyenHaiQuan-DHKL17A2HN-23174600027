class Date:
    def __init__(self, ngay = 1, thang = 1, nam = 2000):
        self.ngay = ngay
        self.thang = thang
        self.nam = nam

    def display(self):
        print(f"{self.ngay:02d}-{self.thang:02d}-{self.nam}")

    def next(self):
        ngay_trong_moi_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.nam % 4 == 0 and self.nam % 100 != 0) or (self.nam % 400 == 0):
            ngay_trong_moi_thang[1] = 29

        self.ngay += 1
        if self.ngay > ngay_trong_moi_thang[self.thang - 1]:
            self.ngay = 1
            self.thang += 1
            if self.thang > 12:
                self.thang = 1
                self.nam += 1

class Employee:
    def __init__(self, ten, ngay_sinh, ngay_vao_cty):
        self.ten = ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cty = ngay_vao_cty

    def display(self):
        print(f"Tên: {self.ten}")
        print("Ngày sinh: ", end = "")
        self.ngay_sinh.display()
        print("Ngày vào công ty: ", end = "")
        self.ngay_vao_cty.display()

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        for employee in self.employees:
            employee.display()
            print("-" * 20)

ngay_sinh1 = Date(28, 1, 2005)
ngay_vao_cty1 = Date(15, 6, 2028)
employee1 = Employee("Nguyễn Anh Quân", ngay_sinh1, ngay_vao_cty1)

ngay_sinh2 = Date(19, 2, 2004)
ngay_vao_cty2 = Date(31, 4, 2030)
employee2 = Employee("Phạm Thị Lục Bảo", ngay_sinh2, ngay_vao_cty2)

company = Company()
company.add_employee(employee1)
company.add_employee(employee2)

company.display_employees()