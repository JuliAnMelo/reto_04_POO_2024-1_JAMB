# reto_04_POO_2024-1_JAMB
## The Restaurant Part II
This Restaurant with no name yet, in its interior contains ~~six~~ seven classes:

### MenuItem
```python
class MenuItem:
    def __init__(self):
        pass
    def calculate_total_price(self):
        return 0
    def get_price(self):
        item_price = self.calculate_total_price()
        return item_price
```
Nothing relevant, the default price is zero, now with a getter.

### Beverage
```python
class Beverage(MenuItem):
    def __init__(self, size):
        self.size = size
    def calculate_total_price(self):
        total = 0
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total 
```
As you can notice this MenuItem class is defined by three price modifiers, sorted by the size of the drink.

### Appetizer
```python
class Appetizer(MenuItem):
    def __init__(self, double):
        self.double = double

    def calculate_total_price(self):
        total = 0
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total
```
This MenuItem class has two price modificators, you can see that the double one, actually multiply by 1.8 the original price.

### Main Course
```python
class MainCourse(MenuItem):
    def __init__(self, addition):
        self.addition = addition

    def calculate_total_price(self):
        total = 0
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total     
```
In this case there is an modificator that multiply the base price by 1.5.

### Payment
```python
class Payment:
  def __init__(self):
    pass

  def to_pay(self, amount):
    raise NotImplementedError("SubClass must implement to_pay()")

class Card(Payment):
  def __init__(self, number, amount_committed):
    super().__init__()
    self.number = number
    self.amount_committed = amount_committed

  def to_pay(self, amount):
    print(f"Paying ${amount} with card:   ****{self.number[-4:]}")
    if self.amount_committed >= amount:
      print(f"Payment made with Card. Change: ${self.amount_committed - amount}")
    else:
      print(f"Insufficient funds. Missing ${amount - self.amount_committed} to complete payment.")

class Cash(Payment):
  def __init__(self, amount_committed):
    super().__init__()
    self.amount_committed = amount_committed

  def to_pay(self, amount):
    if self.amount_committed >= amount:
      print(f"Payment made in cash. Change: ${self.amount_committed - amount}")
    else:
      print(f"Insufficient money. Missing ${amount - self.amount_committed} to complete payment.")
```
A copypaste from class number ten.

### THE ORDER CLASS, HARDER, BETTER(?), (not)FASTER, STRONGER(definitely)
```python
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item=1):
        self.items.append((item))

    def calculate_total_bill(self):
        total_bill = 0
        for item in self.items:
            total_bill += item.calculate_total_price()
        return int(total_bill)
        
    def protocol(self):
        #...
        #code
        #...
        #more code
        #...
        #even more code
        #...

    def get_total_receipt(self):
        print("\n""\t\t""YOUR RECEIPT""\n""\t""ITEM""\t\t\t\t""PRICE")
        sub_total = []
        for item in self.items:
            print(item.get_receipt())
            sub_total.append(int(item.get_price()))
        print(f"Sub Total:\t\t\t\t ${sum(sub_total)}\n")

        rounding_dis = 0
        amount_dis = 0
        if len(sub_total) >= 6:           
            for st in sub_total:
                if st >= 2000 and st <= 5000: rounding_dis += 1000
                if st < 2000: rounding_dis += st
            print(f"Discount for Rounding:\t\t\t\t ${rounding_dis}")
        if len(sub_total) == 8:
            amount_dis += 2000
            print(f"Discount for Eight items:\t\t\t ${amount_dis}")
        if len(sub_total) == 12:
            amount_dis += 4000
            print(f"Discount for Twelve items:\t\t\t ${amount_dis}")
        if len(sub_total) > 12 and len(sub_total) < 20:
            amount_dis += 8000
            print(f"Discount for Big Order:\t\t\t ${amount_dis}")
        if len(sub_total) > 20:
            amount_dis += (sum(sub_total)) / 10
            print(f"Discount for Buffet Order:\t\t ${amount_dis}")
        total = sum(sub_total) - (rounding_dis + amount_dis)
        print(f"\nTotal Bill:\t\t\t\t ${total}")

        pay = int(input("\nIf you are paying with a Credit Card,\t write 1" "\nIf you are paying with Cash,\t\t write 2\n"))
        if pay == 1:
            code = input("Please write your card's number\n")
            money = int(input("Please write the amount you will pay\n$"))
            payment = Card(code, money)
            payment.to_pay(total)
        if pay == 2:
            money = int(input("Please write the amount you will pay\n$"))
            payment = Cash(money)
            payment.to_pay(total)
```
The heart of the whole program, the protocol() method has lines and lines of pure pleasure to work with. This time includes the payment steps, including discounts, with the Payment Class.

## The Menu
The Menu is composed by 12 base items, i say base, because, the focus i gave to the challenge was the modificators, such as size, as you already saw (i hope so) in the MenuItem classes, and and as you will see below, where is more clear than THE ORDER CLASS:

### Beverage SubClasses
```python
class Water(Beverage):
    def __init__(self, size):
        super().__init__(size)
        self.name = "Water"

    def calculate_total_price(self):
        total = 1500
        if self.size == "Small": total *= 0
        if self.size == "Regular": total *= 0
        if self.size == "Large": total *= 1
        return total

    def get_receipt(self):
        receipt = f"{self.size} {self.name}:\t\t\t\t ${int(self.get_price())}"
        return receipt
```
Base price $1500, but corresponds to the Large size, Small and Regular size are courtesy of the house.

```python
class Juice(Beverage):
    def __init__(self, size, fruit):
        super().__init__(size)
        self.fruit = fruit
        self.name = "Juice"

    def calculate_total_price(self):
        total = 2000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.fruit == "Orange": total *= 1
        if self.fruit == "Blackberry": total *= 1.2
        if self.fruit == "Mango": total *= 1.4
        return total

    def get_receipt(self):
        receipt = f"{self.size} {self.fruit} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt
```
Base price $2000, first apply the size modificator, then a fruit multiplier

```python
class Soda(Beverage):
    def __init__(self, size, flavor):
        super().__init__(size)
        self.flavor = flavor
        self.name = "Soda"

    def calculate_total_price(self):
        total = 3000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.flavor == "Coke": total += 100
        if self.flavor == "Lemon": total += 200
        if self.flavor == "Grapefruit": total += 500
        return total

    def get_receipt(self):
        receipt = f"{self.size} {self.flavor} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt
```
Base price $3000, first apply the size modificator, then a flavor extra, by executing the program you will notice that it will be refered as a brand.

```python
class Beer(Beverage):
    def __init__(self, size, brand):
        super().__init__(size)
        self.brand = brand
        self.name = "Beer"
    
    def calculate_total_price(self):
        total = 4000
        if self.brand == "Corona": total += 500
        if self.brand == "Budweiser": total += 1000
        if self.brand == "Heineken": total += 1500
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total

    def get_receipt(self):
        receipt = f"{self.size} {self.brand}:\t\t\t ${int(self.get_price())}"
        return receipt
```
First apply a brand modificator to the base price ($4000), and then the size modificator.

### Appetizer SubClasses
```python
class Soup(Appetizer):
    def __init__(self, double, type):
        super().__init__(double)
        self.type = type
        self.name = "Soup"

    def calculate_total_price(self):
        total = 4000
        if self.type == "Corn": total += 0
        if self.type == "Tomato": total += 200
        if self.type == "Chicken": total += 500
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.type} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt
```
First an extra due to the main ingredient of the soup, then the Simple/Double modificator over the $4000 base price.

```python
class Egg(Appetizer):
    def __init__(self, double, preparation):
        super().__init__(double)
        self.preparation = preparation
        self.name = "Egg"

    def calculate_total_price(self):
        total = 2000
        if self.preparation == "Boiled": total += 0
        if self.preparation == "Fried": total += 400
        if self.preparation == "Scrambled": total += 800
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.preparation} {self.name}:\t\t\t ${int(self.get_price())}"
        return receipt
```
First an extra due to the preparation of the egg, then the Simple/Double modificator over the $2000 base price.

```python
class Soup(Appetizer):
    def __init__(self, double, type):
        super().__init__(double)
        self.type = type
        self.name = "Soup"

    def calculate_total_price(self):
        total = 3000
        if self.kind == "Banana": total += 0
        if self.kind == "Apple": total += 300
        if self.kind == "Strawberry": total += 700
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.kind}:\t\t\t\t ${int(self.get_price())}"
        return receipt
```
First an extra due to the cost of the fruit, then the Simple/Double modificator over the $3000 base price.

```python
class Salad(Appetizer):
    def __init__(self, double, aditive):
        super().__init__(double)
        self.aditive = aditive
        self.name = "Salad"

    def calculate_total_price(self):
        total = 4000
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        if self.aditive == "No Aditive": total += 0
        if self.aditive == "Vinegar": total += 100
        if self.aditive == "Vinaigrette": total += 200
        if self.aditive == "Olive Oil": total += 300
        return total

    def get_receipt(self):
        receipt = f"{self.double} {self.name} with {self.aditive}:\t\t ${int(self.get_price())}"
        return receipt
```
First the Simple/Double modificator, and then and extra by the aditive that you want over the $4000 base price.

### Main Course SubClasses
```python
class Rice(Main_Course):
    def __init__(self, addition, color):
        super().__init__(addition)
        self.color = color
        self.name = "Rice"

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.color == "White": total += 0
        if self.color == "Yellow": total += 100
        if self.color == "Green": total += 400
        return total

    def get_receipt(self):
        receipt = f"{self.color} {self.name} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt  
```
Base price of $8000, an optional extra portion modificator, and the color extra fee.

```python
class Meat(Main_Course):
    def __init__(self, addition, vegan):
        super().__init__(addition)
        self.vegan = vegan
        self.name = "Meat"

    def calculate_total_price(self):
        total = 12000
        if self.vegan == "Animal Meat": total += 0
        if self.vegan == "Vegan Meat": total += 3000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total 

    def get_receipt(self):
        receipt = f"{self.vegan} with {self.addition}:\t\t\t ${int(self.get_price())}"
        return receipt   
```
Base price of $12000, it ask if you are vegan, then aplies the optional extra portion modificator.

```python
class Pasta(Main_Course):
    def __init__(self, addition, variety):
        super().__init__(addition)
        self.variety = variety
        self.name = "Pasta"

    def calculate_total_price(self):
        total = 10000
        if self.variety == "Spaghetti": total += 0
        if self.variety == "Shells": total += 700
        if self.variety == "Macaroni": total += 1500
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total    

    def get_receipt(self):
        receipt = f"{self.variety} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt   
```
Base price of $10000, each style of pasta has a different price, then aplies the optional extra portion fee.

```python
class Vegetables(Main_Course):
    def __init__(self, addition, making):
        super().__init__(addition)
        self.making = making
        self.name = "Vegetables"

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.making == "Boiled": total += 0
        if self.making == "Baked": total += 500
        if self.making == "Sauteed": total += 1000
        return total    

    def get_receipt(self):
        receipt = f"{self.making} {self.name} with {self.addition}:\t\t ${int(self.get_price())}"
        return receipt   
```
Base price of $8000, the optional extra portion modificator, then asks you how do you like your vegetables.

## The Execution (of the program)
```python
class Exercise(Order):
    def __init__(self, program, iterations):
        self.program = program
        self.iterations = iterations

    def execute(self):
        challenge = self.program
        counter = self.iterations
        while counter > 0:
            challenge.protocol()
            counter -=1
        return challenge.get_total_receipt()
```
I created the class Exercise as a SubClass of order, it permits that more than only one person can order and returns the receipt, the bill and the payment protocol, given the circumstances we can call it the 

```python
if __name__ == "__main__": 
    counter = int(input("Welcome to this establishment\nHow many people?\n"))
    order = Order()
    challenge_04 = Exercise(order, counter)
    challenge_04.execute()
```
This bad boy above initialize the whole monster of a program. The End

### Appendix I
The Shape Class required as an exercise, in parts, maybe it's exaggerated but I'm proud of it.

## Point Class and Line Class
```python
from math import asin
from math import acos
from math import degrees
from math import sqrt

class Point:
    def __init__(self, x: float=0, y: float=0):
        self.x = x
        self.y = y
    def move(self, new_x: float, new_y: float):
        self.x = new_x
        self.y = new_y
    def reset(self):
        self.x = 0
        self.y = 0
    def compute_distance(self, point)-> float:
        distance = ((self.x - point.x)**2+(self.y - point.y)**2)**(0.5)
        return distance


class Line:
    def __init__(self, start: Point=0, end: Point=0):
        self.start = start
        self.end = end
        self.x_cathetus = self.end.x - self.start.x
        self.y_cathetus = self.end.y - self.start.y

    def compute_length(self):
        hypotenuse = ((self.x_cathetus ** 2) + (self.y_cathetus ** 2)) ** 0.5
        return hypotenuse

    def compute_slope(self):
        hypotenuse = self.compute_length()
        rad = asin(self.y_cathetus / hypotenuse)
        slope = degrees(rad)
        return abs(slope)

    def compute_horizontal_cross(self):
        if self.start.y > 0 and self.end.y > 0:
            return False
        if self.start.y < 0 and self.end.y < 0:
            return False
        else: return True

    def compute_vertical_cross(self):
        if self.start.x > 0 and self.end.x > 0:
            return False
        if self.start.x < 0 and self.end.x < 0:
            return False
        else: return True       
```
The basis of everything

## Shape Class
```python
class Shape:
    def __init__(self, vertex: list[Point]):
        self.vertex = vertex
```
I built the program around Triangle Class, i don't know how to improve it!

## The Triangle Class
```python
class Triangle(Shape):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)
        __segments = []
        __segment_1 = Line(start=vertex[0], end=vertex[1]).compute_length()
        __segment_2 = Line(start=vertex[1], end=vertex[2]).compute_length()
        __segment_3 = Line(start=vertex[2], end=vertex[0]).compute_length()
        __segments.append(__segment_1)
        __segments.append(__segment_2)
        __segments.append(__segment_3)
        __segments.sort()
        self.edge_1 = __segments[0]
        self.edge_2 = __segments[1]
        self.edge_3 = __segments[2]
        
    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3), 3 )
        return self.perimeter
    
    def compute_area(self):
        __semi_perimeter = self.perimeter / 2
        self.area = round(sqrt( __semi_perimeter * (__semi_perimeter - self.edge_1) * (__semi_perimeter - self.edge_2) * (__semi_perimeter - self.edge_3) ), 3)
        return self.area 

    def compute_inner_angles(self):
        __angle_1v2 = acos( ((self.edge_1 ** 2) + (self.edge_2 ** 2) - (self.edge_3 ** 2))  /  (2 * (self.edge_1 * self.edge_2)) )
        __angle_2v3 = acos( ((self.edge_2 ** 2) + (self.edge_3 ** 2) - (self.edge_1 ** 2))  /  (2 * (self.edge_2 * self.edge_3)) )
        __angle_3v1 = acos( ((self.edge_3 ** 2) + (self.edge_1 ** 2) - (self.edge_2 ** 2))  /  (2 * (self.edge_3 * self.edge_1)) )
        __inner_angle_1 = round(abs(degrees(__angle_1v2)), 3)
        __inner_angle_2 = round(abs(degrees(__angle_2v3)), 3)
        __inner_angle_3 = round(abs(degrees(__angle_3v1)), 3)
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3]
    
    def compute_is_regular(self):
        regular = False
        if (sum(self.__edges) / len(self.__edges)) == self.__edges[0]: 
            regular = True
        return regular

    def get_edges(self):
        self.__edges = [round(self.edge_1, 3), round(self.edge_2, 3), round(self.edge_3, 3)]
        return ", ".join(map(str, self.__edges))   
    def get_perimeter(self):
        perimeter = self.compute_perimeter()
        return perimeter
    def get_inner_angles(self):
        inner_angles = ", ".join(map(str, self.compute_inner_angles())) 
        return inner_angles
    def get_area(self):
        area = self.compute_area()
        return area
    def get_is_regular(self):
        regular = self.compute_is_regular()
        return regular
```
The Baby Boy, the main pillar of the program 

## Triangle SubClasses
```python
class Equilateral_Triangle(Triangle):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)

    def compute_area(self):
        self.area = round( (sqrt(3) / 4) * (self.edge_1 ** 2), 3 )        
        return self.area 
    
class Isosceles_Triangle(Triangle):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)

    def compute_area(self):
        if self.edge_2 == self.edge_3:
            self.__height = sqrt((self.edge_3 ** 2) - ((self.edge_1 / 2) ** 2))
            self.area = round( ((self.edge_1 * self.__height) / 2), 3 )
            return self.area 
        if self.edge_1 == self.edge_2:
            self.__height = sqrt((self.edge_1 ** 2) - ((self.edge_3 / 2) ** 2))
            self.area = round( ((self.edge_3 * self.__height) / 2), 3 )
            return self.area 
    
class Scalene_Triangle(Triangle):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)

    def compute_area(self):
        __semi_perimeter = self.perimeter / 2
        self.area = round(sqrt( __semi_perimeter * (__semi_perimeter - self.edge_1) * (__semi_perimeter - self.edge_2) * (__semi_perimeter - self.edge_3) ), 3)
        return self.area 

class Rectangle_Triangle(Triangle):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)

    def compute_area(self):
        self.area = round( ((self.edge_1 * self.edge_2) / 2), 3 )
        return self.area
```
In theory the program will work fine only with Triangle Class, but this is it.

## The Tetragon Class
```python
class Tetragon(Shape):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)
        self.__triangule_1 = Triangle([vertex[0], vertex[1], vertex[2]])
        self.__triangule_2 = Triangle([vertex[2], vertex[3], vertex[0]])
        self.edge_1 = Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = Line(start=vertex[1], end=vertex[2]).compute_length()
        self.__diagonal_1_2 = Line(start=vertex[2], end=vertex[0]).compute_length()
        self.edge_3 = Line(start=vertex[2], end=vertex[3]).compute_length()
        self.edge_4 = Line(start=vertex[3], end=vertex[0]).compute_length()
        self.__diagonal_3_4 = Line(start=vertex[0], end=vertex[2]).compute_length()

    def compute_perimeter(self):
        self.perimeter = round( (self.__triangule_1.compute_perimeter() - self.__diagonal_1_2) + (self.__triangule_2.compute_perimeter() - self.__diagonal_3_4),3 )
        return self.perimeter
    
    def compute_area(self):
        self.area = round( (self.__triangule_1.compute_area() + self.__triangule_2.compute_area()), 3 )
        return self.area 
    
    def compute_inner_angles(self):
        __angle_1v2 = acos( ((self.edge_1 ** 2) + (self.edge_2 ** 2) - (self.__diagonal_1_2 ** 2))  /  (2 * (self.edge_1 * self.edge_2)) )
        __angle_2vd1 = acos( ((self.edge_2 ** 2) + (self.__diagonal_1_2 ** 2) - (self.edge_1 ** 2))  /  (2 * (self.edge_2 * self.__diagonal_1_2)) )
        __angle_d1v1 = acos( ((self.__diagonal_1_2 ** 2) + (self.edge_1 ** 2) - (self.edge_2 ** 2))  /  (2 * (self.__diagonal_1_2 * self.edge_1)) )        
        __angle_3v4 = acos( ((self.edge_3 ** 2) + (self.edge_4 ** 2) - (self.__diagonal_3_4 ** 2))  /  (2 * (self.edge_3 * self.edge_4)) )
        __angle_4vd2 = acos( ((self.edge_4 ** 2) + (self.__diagonal_3_4 ** 2) - (self.edge_3 ** 2))  /  (2 * (self.edge_4 * self.__diagonal_3_4)) )
        __angle_d2v3 = acos( ((self.__diagonal_3_4 ** 2) + (self.edge_3 ** 2) - (self.edge_4 ** 2))  /  (2 * (self.__diagonal_3_4 * self.edge_3)) )
   
        __inner_angle_1 = round( abs(degrees(__angle_1v2)), 3 )
        __inner_angle_2 = round( abs(degrees(__angle_2vd1 + __angle_d2v3)), 3 )
        __inner_angle_3 = round( abs(degrees(__angle_3v4)), 3 )
        __inner_angle_4 = round( abs(degrees(__angle_d1v1 + __angle_4vd2)), 3 )
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
    
    def compute_is_regular(self):
        regular = False
        if (sum(self.__edges) / len(self.__edges)) == self.__edges[0]: 
            regular = True
        return regular

    def get_edges(self):
        self.__edges = [round(self.edge_1, 3), round(self.edge_2, 3), round(self.edge_3, 3), round(self.edge_4, 3)]
        return ", ".join(map(str, self.__edges))  
    def get_perimeter(self):
        perimeter = self.compute_perimeter()
        return perimeter
    def get_inner_angles(self):
        inner_angles = ", ".join(map(str, self.compute_inner_angles())) 
        return inner_angles
    def get_area(self):
        area = self.compute_area()
        return area
    def get_is_regular(self):
        regular = self.compute_is_regular()
        return regular
```
Triangle Class younger Twin, it exist because a quadrilateral can be built by two triangles, including irregular ones, also, rectangule and square are only two of the types of quadrilaterals.

## Rectangle Class
```python
class Rectangule(Tetragon):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)
        self.edge_1 = Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = Line(start=vertex[1], end=vertex[2]).compute_length()
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_2

    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3 )
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_2, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
```
Height and width, boring.

```python
class Square(Tetragon):
    def __init__(self, vertex: list[Point]):
        super().__init__(vertex)
        self.edge_1 = Line(start=vertex[0], end=vertex[1]).compute_length()
        self.edge_2 = self.edge_1
        self.edge_3 = self.edge_1
        self.edge_4 = self.edge_1

    def compute_perimeter(self):
        self.perimeter = round( (self.edge_1 + self.edge_2 + self.edge_3 + self.edge_4), 3 )
        return self.perimeter

    def compute_area(self):
        self.area = round(self.edge_1 * self.edge_1, 3)
        return self.area
    
    def compute_inner_angles(self):
        __inner_angle_1 = round(360 / 4, 3)
        __inner_angle_2 = __inner_angle_1
        __inner_angle_3 = __inner_angle_1
        __inner_angle_4 = __inner_angle_1
        return [__inner_angle_1, __inner_angle_2, __inner_angle_3, __inner_angle_4]
```
A square is more a type of quadrilateral than a type of rectangule. 

## Exercise Class
```python
class Exercise():
    def __init__(self, sides):
        self.sides = sides

    def execute(self):
        if self.sides == 3:
            point_A = list(map(float, input("\n""Please write the x and y components of the First point:""\t\t").split()))
            point_B = list(map(float, input("\n""Please write the x and y components of the Second point:""\t").split()))
            point_C = list(map(float, input("\n""Please write the x and y components of the Third point:""\t\t").split()))
            edge_AB = round( Line(Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1])).compute_length(), 3 ) 
            edge_BC = round( Line(Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1])).compute_length(), 3 )
            edge_CA = round( Line(Point(point_C[0], point_C[1]), Point(point_A[0], point_A[1])).compute_length(), 3 )
            edges = sorted([edge_AB, edge_BC, edge_CA])
            
            if edges[0] == edges[1] and edges[1] == edges[2]:
                print("\n""\t""The Triangule is Equilateral""\n")
                The_Triangule = Equilateral_Triangle([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1])])

            if (edges[0] == edges[1] and edges[1] != edges[2]) or (edges[0] != edges[1] and edges[1] == edges[2]):
                print("\n""\t""The Triangule is Isosceles""\n")
                The_Triangule = Isosceles_Triangle([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1])])

            if edges[0] != edges[1] and edges[1] != edges[2]:
                print("\n""\t""The Triangule is Scalene""\n")
                The_Triangule = Scalene_Triangle([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1])])  
            
            print(f"The Triangule Edges are:           {The_Triangule.get_edges()}""\n")
            print(f"The Triangule is Regular:          {The_Triangule.get_is_regular()}""\n")
            print(f"The Triangule Perimeter is:        {The_Triangule.get_perimeter()}""\n")
            print(f"The Triangule Area is:             {The_Triangule.get_area()}""\n")
            print(f"The Triangule Inner Angles are:    {The_Triangule.get_inner_angles()}""\n")
            if "90.0" in The_Triangule.get_inner_angles(): print("The Triangle is Rectangule""\n")

        if self.sides == 4:
            point_A = list(map(float, input("\n""Please write the x and y components of the First point:""\t\t").split()))
            point_B = list(map(float, input("\n""Please write the x and y components of the Second point:""\t").split()))
            point_C = list(map(float, input("\n""Please write the x and y components of the Third point:""\t\t").split()))
            point_D = list(map(float, input("\n""Please write the x and y components of the Fourth point:""\t").split()))
            edge_AB = round( Line(Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1])).compute_length(), 3 ) 
            edge_BC = round( Line(Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1])).compute_length(), 3 )
            edge_CD = round( Line(Point(point_C[0], point_C[1]), Point(point_D[0], point_D[1])).compute_length(), 3 )
            edge_DA = round( Line(Point(point_D[0], point_D[1]), Point(point_A[0], point_A[1])).compute_length(), 3 )
            edges = sorted([edge_AB, edge_BC, edge_CD, edge_DA])
            
            if edges[0] == edges[1] and edges[1] == edges[2] and edges[2] == edges[3]:
                print("\n""\t""The Quadrilateral is a Square""\n")
                The_Quadrilateral = Square([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1]), Point(point_D[0], point_D[1])])

            if edges[0] == edges[1] and edges[1] != edges[2] and edges[2] == edges[3]:
                print("\n""\t""The Quadrilateral is a Rectangule""\n")
                The_Quadrilateral = Rectangule([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1]), Point(point_D[0], point_D[1])])

            if edges[0] != edges[1] or edges[2] != edges[3]:
                print("\n""\t""The Quadrilateral is Irregular""\n")
                The_Quadrilateral = Tetragon([Point(point_A[0], point_A[1]), Point(point_B[0], point_B[1]), Point(point_C[0], point_C[1]), Point(point_D[0], point_D[1])])  
            
            print(f"The Quadrilateral Edges are:           {The_Quadrilateral.get_edges()}""\n")
            print(f"The Quadrilateral is Regular:          {The_Quadrilateral.get_is_regular()}""\n")
            print(f"The Quadrilateral Perimeter is:        {The_Quadrilateral.get_perimeter()}""\n")
            print(f"The Quadrilateral Area is:             {The_Quadrilateral.get_area()}""\n")
            print(f"The Quadrilateral Inner Angles are:    {The_Quadrilateral.get_inner_angles()}""\n")
```
The comunication with the user, in the .py file are some examples, tested by me in GeoGebra

```python
if __name__ == "__main__": 
    print("\n""\t""Hi there!""\n")
    while True:
        sides = int(input("If you wanna know the components of a Triangle,""\t\t""please write 3""\n""If you wanna know the components of a Quadrilateral,""\t""please write 4""\n""If you wanna end this program,""\t\t\t\t""please write 0""\n"))
        if sides == 0: break
        else: Exercise(sides).execute()
    print("\n""\t""Have a Nice day, see you again!")
```

Finally, i'm going to the bed.
