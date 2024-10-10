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

date = Date(28, 1, 2005)
date.display()
date.next()
date.display() 