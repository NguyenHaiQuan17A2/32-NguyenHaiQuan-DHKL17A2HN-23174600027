import math

class Diem:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def display(self):
        print(f"Diem({self.x}, {self.y})")

class Elip(Diem):
    def __init__(self, x, y, truc_lon, truc_nho):
        super().__init__(x, y)
        self.truc_lon = truc_lon
        self.truc_nho = truc_nho

    def dien_tich(self):
        return math.pi * self.truc_lon * self.truc_nho

    def display(self):
        super().display()
        print(f"Elip với trục lớn: {self.truc_lon}, trục nhỏ: {self.truc_nho}")
        print(f"Diện tích: {self.dien_tich()}")

class Hinh_tron(Elip):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, radius)
        self.radius = radius

    def display(self):
        super().display()
        print(f"Bán kính hình tròn: {self.radius}")
        print(f"Diện tích: {self.dien_tich()}")

diem = Diem(1, 2)
diem.display()

elip = Elip(1, 2, 3, 4)
elip.display()

hinh_tron = Hinh_tron(1, 2, 3)
hinh_tron.display()