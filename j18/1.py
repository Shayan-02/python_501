# تعریف یک کلاس ساده
class Car:
    # متد سازنده (Constructor)
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # متد برای نمایش اطلاعات خودرو
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


# ایجاد شیء از کلاس Car
my_car = Car("Toyota", "Corolla", 2020)
print((my_car))
# نمایش اطلاعات خودرو
# my_car.display_info()

my_car.year = 2021
my_car.display_info()
