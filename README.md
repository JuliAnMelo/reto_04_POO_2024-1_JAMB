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
