# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
from math import sqrt
class Triangle():
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2        
        self.c1 = c1
        self.c2 = c2
##        print('a1=',self.a1,'a2=', self.a2,'b1=', self.b1,'b2=', self.b2,'c1=', self.c1,'c2=', self.c2)
##        print (sqrt((self.c1-self.b1)**2+(self.c2-self.b2)**2),sqrt((self.c1-self.a1)**2+(self.c2-self.a2)**2),sqrt((self.b1-self.a1)**2+(self.b2-self.a2)**2))
    def area(self):
        return abs((self.b2-self.a2)*(self.c1-self.a1) - (self.b1-self.a1)*(self.c2-self.a2))/2
    def altitude(self,topnum):
        #S=1/2*a*h => h=2*S*a
        if topnum not in (1,2,3):
            print('Введите номер вершины, из которой выходит высота: 1, 2, 3')
            return
        if topnum == 1:
            a = sqrt((self.c1-self.b1)**2+(self.c2-self.b2)**2)
        elif topnum == 2:
            a = sqrt((self.c1-self.a1)**2+(self.c2-self.a2)**2)
        elif topnum == 3:
            a = sqrt((self.b1-self.a1)**2+(self.b2-self.a2)**2)
        return 2*self.area()*a
    def perimeter(self):
        return sqrt((self.c1-self.b1)**2+(self.c2-self.b2)**2) + sqrt((self.c1-self.a1)**2+(self.c2-self.a2)**2) +sqrt((self.b1-self.a1)**2+(self.b2-self.a2)**2)
    
triangle1 = Triangle(0,0,1,0,0.5,0.866)
print (triangle1.area())
print (triangle1.altitude(2))
print (Triangle.perimeter(triangle1))


        
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
class Quadrangle():
    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):
        self.a1 = a1
        self.a2 = a2
        self.b1 = b1
        self.b2 = b2        
        self.c1 = c1
        self.c2 = c2
        self.d1 = d1
        self.d2 = d2
        self.ab = abs(sqrt((self.a1-self.b1)**2+(self.a2-self.b2)**2))
        self.bc = abs(sqrt((self.b1-self.c1)**2+(self.b2-self.c2)**2))
        self.cd = abs(sqrt((self.c1-self.d1)**2+(self.c2-self.d2)**2))
        self.ad = abs(sqrt((self.a1-self.d1)**2+(self.a2-self.d2)**2))
    def side_lengths(self):
        return 'AB={} BC={} CD={} AD={}'.format(self.ab, self.bc, self.cd, self.ad)
    def perimeter(self):
        return self.ab + self.bc + self.cd + self.ad
    
class Trapeze(Quadrangle):
    def __init__(self, a1, a2, b1, b2, c1, c2, d1, d2):
        Quadrangle.__init__(self, a1, a2, b1, b2, c1, c2, d1, d2)
    def check(self):
        isparal_ab_cd =  ((self.b2-self.a2)*(self.c1-self.d1) - (self.b1-self.a1)*(self.c2-self.d2) == 0)
        isparal_bc_ad =  ((self.c2-self.b2)*(self.d1-self.a1) - (self.c1-self.b1)*(self.d2-self.a2) == 0)
        if isparal_bc_ad:
            return (self.b1-self.a1)*(self.d1-self.a1) + (self.b2-self.a2)*(self.d2-self.a2) == (self.c1-self.d1)*(self.a1-self.d1) + (self.c2-self.d2)*(self.a2-self.d2)
        if isparal_ab_cd:
            return (self.a1-self.d1)*(self.c1-self.a1) + (self.a2-self.d2)*(self.c2-self.a2) == (self.b1-self.c1)*(self.d1-self.c1) + (self.b2-self.c2)*(self.d2-self.c2) 
    def area(self):
        if self.check():
            triangle1 = Triangle(self.a1,self.a2,self.b1,self.b2,self.c1,self.c2)
            triangle2 = Triangle(self.a1,self.a2,self.d1,self.d2,self.c1,self.c2)
            return triangle1.area() + triangle2.area()
        else:
            return '?'

trap1 = Trapeze(0,0,1,1,4,1,5,0)
print('Трапеция равнобедренная' if trap1.check() else 'Четырехугольник не является равнобедренной трапецией')
print (trap1.side_lengths())
print('Периметр ' + str(trap1.perimeter()))
print('Площадь {}'.format(trap1.area()))
