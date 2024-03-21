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


class Shape:
    def __init__(self, vertex: list[Point]):
        self.vertex = vertex


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
    
"""
example_1 = Triangle([Point(2, 1), Point(5, 4), Point(6, 1)])
example_2 = Equilateral_Triangle([Point(2, 1), Point(4, 4.4641), Point(6, 1)])
example_3 = Isosceles_Triangle([Point(3, 1), Point(4, 5), Point(5, 1)])
example_4 = Scalene_Triangle([Point(3, 1), Point(2, 2.5), Point(6, 0.5)])
example_5 = Rectangle_Triangle([Point(3, 1), Point(3, 5), Point(5, 1)])
example_6 = Tetragon([Point(6, 4), Point(5, -3), Point(-2, -1), Point(-4, 2)]) 
example_7 = Rectangule([Point(-3, 2), Point(7, 2), Point(7, -4), Point(-3, -4)]) 
example_8 = Square([Point(-5, -2), Point(3, -2), Point(3, -10), Point(-5, -10)]) 
"""

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

if __name__ == "__main__": 
    print("\n""\t""Hi there!""\n")
    while True:
        sides = int(input("If you wanna know the components of a Triangle,""\t\t""please write 3""\n""If you wanna know the components of a Quadrilateral,""\t""please write 4""\n""If you wanna end this program,""\t\t\t\t""please write 0""\n"))
        if sides == 0: break
        else: Exercise(sides).execute()
    print("\n""\t""Have a Nice day, see you again!")