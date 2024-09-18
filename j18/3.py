class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

# یک تابع که از چندریختی استفاده می‌کند
def animal_sound(animal):
    print(animal.sound())

# ایجاد اشیاء از کلاس‌های مختلف
dog = Dog()
cat = Cat()

# فراخوانی تابع با اشیاء مختلف
animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!
