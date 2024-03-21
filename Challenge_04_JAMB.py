class MenuItem:
    def __init__(self):
        pass
    def calculate_total_price(self):
        return 0
    def get_price(self):
        item_price = self.calculate_total_price()
        return item_price

class Beverage(MenuItem):
    def __init__(self, size):
        self.size = size
    def calculate_total_price(self):
        total = 0
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total 

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

class Appetizer(MenuItem):
    def __init__(self, double):
        self.double = double

    def calculate_total_price(self):
        total = 0
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

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

class Fruit(Appetizer):
    def __init__(self, double, kind):
        super().__init__(double)
        self.kind = kind
        self.name = "Fruit"

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


class Main_Course(MenuItem):
    def __init__(self, addition):
        self.addition = addition

    def calculate_total_price(self):
        total = 0
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total     

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


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item=1):
        self.items.append((item))

    def get_total_bill(self):
        total_bill = 0
        for item in self.items:
            total_bill += item.get_price()
        return int(total_bill)
        
    def protocol(self):
        course_ini = int(input("\tMain Course" "\n" "We offer:"  "\nRice\t\tIf you want Rice,\t write 1" "\nMeat\t\tIf you want Meat,\t write 2" "\nPasta\t\tIf you want Pasta,\t write 3" "\nVegetables\tIf you want Vegetables,\t write 4" "\nIf you don't want a Main Course,\t write 5\n"))

        if course_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" "\nIf you want an Extra ration,\t\t write 2\n"))    
            if con_1 == 1: var_1 = "No Extra"
            if con_1 == 2: var_1 = 'Extra'
            
            if course_ini == 1:
                var_2 = ""
                con_2 = int(input("\nIf you want White Rice,\t\t\t write 1" "\nIf you want Yellow Rice,\t\t write 2" "\nIf you want Green Rice,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "White"
                if con_2 == 2: var_2 = "Yellow"
                if con_2 == 3: var_2 = "Green"
                order.add_item(Rice(var_1, var_2))

            if course_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want Regular Meat,\t\t write 1" "\nIf you want Vegan Meat,\t\t\t write 2\n"))    
                if con_2 == 1: var_2 = "Animal Meat" 
                if con_2 == 2: var_2 = "Vegan Meat"
                order.add_item(Meat(var_1, var_2))

            if course_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Spaghetti,\t\t\t write 1" "\nIf you want Shells,\t\t\t write 2" "\nIf you want Macaroni,\t\t\t write 3\n"))  
                if con_2 == 1: var_2 = "Spaghetti"
                if con_2 == 2: var_2 = "Shells"
                if con_2 == 3: var_2 = "Macaroni"
                order.add_item(Pasta(var_1, var_2))

            if course_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want Boiled Vegetables,\t\t write 1" "\nIf you want Baked Vegetables,\t\t write 2" "\nIf you want Sauteed Vegetables,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Boiled"
                if con_2 == 2: var_2 = "Baked"
                if con_2 == 3: var_2 = "Sauteed"
                order.add_item(Vegetables(var_1, var_2))

        if course_ini >= 5: pass

        appeti_ini = int(input("\t\tAppetizer" "\n" "We offer:"  "\nSoup\t\tIf you want Soup,\t write 1" "\nEgg\t\tIf you want Egg,\t write 2" "\nFruit\t\tIf you want Fruit,\t write 3" "\nSalad\t\tIf you want Salad,\t write 4" "\nIf you don't want a Appetizer,\t\t write 5\n"))

        if appeti_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" "\nIf you want a Double ration,\t\t write 2\n"))    
            if con_1 == 1: var_1 = "Single"
            if con_1 == 2: var_1 = 'Double'
            
            if appeti_ini == 1:
                var_2 = ""
                con_2 = int(input("\nIf you want a Corn Soup,\t\t write 1" "\nIf you want a Tomato Soup,\t\t write 2" "\nIf you want a Chicken Soup,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Corn"
                if con_2 == 2: var_2 = "Tomato"
                if con_2 == 3: var_2 = "Chicken"
                order.add_item(Soup(var_1, var_2))

            if appeti_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want the Egg Boiled,\t\t write 1" "\nIf you want the Egg Fried,\t\t write 2" "\nIf you want the Egg Scrambled,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Boiled"
                if con_2 == 2: var_2 = "Fried"
                if con_2 == 3: var_2 = "Scrambled"
                order.add_item(Egg(var_1, var_2))

            if appeti_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Banana,\t\t\t write 1" "\nIf you want Apple,\t\t\t write 2" "\nIf you want Strawberry,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Banana"
                if con_2 == 2: var_2 = "Apple"
                if con_2 == 3: var_2 = "Strawberry"
                order.add_item(Fruit(var_1, var_2))

            if appeti_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want No Aditive in your Salad,\t write 1" "\nIf you want Vinegar in your Salad,\t write 2" "\nIf you want Vinaigrette in your Salad,\t write 3" "\nIf you want Olive Oil in your Salad,\t write 4\n"))
                if con_2 == 1: var_2 = "No Aditive"
                if con_2 == 2: var_2 = "Vinegar"
                if con_2 == 3: var_2 = "Vinaigrette"
                if con_2 == 4: var_2 = "Olive Oil"
                order.add_item(Salad(var_1, var_2))

        if appeti_ini >= 5: pass

        bevera_ini = int(input("\t\tBeverage" "\n" "We offer:" "\nWater\t\tIf you want Water,\t write 1" "\nJuice\t\tIf you want Juice,\t write 2" "\nSoda\t\tIf you want Soda,\t write 3" "\nBeer\t\tIf you want Beer,\t write 4" "\nIf you don't want a Beverage,\t\t write 5\n"))

        if bevera_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Small Drink,\t\t write 1" "\nIf you want a Regular Drink,\t\t write 2" "\nIf you want a Large Drink,\t\t write 3\n"))    
            if con_1 == 1: var_1 = "Small"
            if con_1 == 2: var_1 = 'Regular'
            if con_1 == 3: var_1 = 'Large'
            
            if bevera_ini == 1:
                order.add_item(Water(var_1))

            if bevera_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want Orange Juice,\t\t write 1" "\nIf you want Blackberry Juice,\t\t write 2" "\nIf you want Mango Juice,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Orange"
                if con_2 == 2: var_2 = "Blackberry"
                if con_2 == 3: var_2 = "Mango"
                order.add_item(Juice(var_1, var_2))

            if bevera_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Coca-Cola,\t\t\t write 1" "\nIf you want Sprite,\t\t\t write 2" "\nIf you want Quatro,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Coke"
                if con_2 == 2: var_2 = "Lemon"
                if con_2 == 3: var_2 = "Grapefruit"
                order.add_item(Soda(var_1, var_2))

            if bevera_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want Corona,\t\t\t write 1" "\nIf you want Budweiser,\t\t\t write 2" "\nIf you want Heineken,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Corona"
                if con_2 == 2: var_2 = "Budweiser"
                if con_2 == 3: var_2 = "Heineken"
                order.add_item(Beer(var_1, var_2))

        if bevera_ini >= 5: pass
        print("\n\n")

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
            
if __name__ == "__main__": 
    counter = int(input("Welcome to this establishment\nHow many people?\n"))
    order = Order()
    challenge_04 = Exercise(order, counter)
    challenge_04.execute()
