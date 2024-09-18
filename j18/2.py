# تعریف یک کلاس جدید که از کلاس Car ارث می‌برد
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        # فراخوانی سازنده کلاس پایه
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    # متد جدید برای نمایش ظرفیت باتری
    def display_battery_info(self):
        print(f"Battery Capacity: {self.battery_capacity} kWh")


# ایجاد شیء از کلاس ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 2023, 100)

# نمایش اطلاعات خودرو و ظرفیت باتری
my_electric_car.display_info()
my_electric_car.display_battery_info()
