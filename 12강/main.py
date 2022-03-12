class Animal:
    def eat(self):
        print('먹는다')
    
    def move(self):
        print('움직인다')
    
class Dog(Animal):
    def bark(self):
        print('멍멍')       
    def shake(self):
        print('꼬리를 흔든다')   

dog = Dog()
dog.eat()
dog.move()
dog.bark()
dog.shake()   

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print('먹는다')
    def move(self):
        print('움직인다')

class Dog(Animal):
    def __init__(self, name, age, owner):
        super().__init__(name, age)
        self.owner = owner
    def bark(self):
        print('멍멍')
    def bark(self):
        print('꼬리를 흔든다')
    def __str__(self):
       sentence = '이름:{}, 나이:, 주인:{}'.format(self.name, self.age, self.owner)
       
       return sentence


animal = Animal('동물', 1)
animal.eat()
dog = Dog('코코', 2, '홍길동')
print(dog.name, dog.age, dog.owner)
print(dog)

dog = Dog('코코', 2, '홍길동')
print(dog.name, dog.age, dog.owner)
print(dog)

class Animal:
    def __init__(self, age):
        self.age = age

    def eat(self):
        print('먹는다')
    
    def move(self):
        print('움직인다')

class Bird(Animal):
    def __init__(self, age):
        super().__init__(age)
    def fly(self):
        print('날다')       
    def 쪼다(self):
        print('쪼다가 입이 뿌러지다')   

bird = Bird(1)
bird.eat()
bird.move()  
bird.fly()
bird.쪼다()

class Human:
    def __init__(self, age):
        self.age = age

    def hit(self):
        print('떄리다')       
    def speak(self):
        print('말하다')   

class Teacher(Human):
    
    def __init__(self, sc):
        super().__init__(age)
    def hithit(self):
        print('학생을 때리다')       
    def homework(self):
        print('숙제를 많이내준다')

class Student(Human):

    def ㅋㅋ(self):
        print('장난치다')       
    def ㅇㅇ(self):
        print('수업을 듣다')

teacher = Teacher()
teacher.hit()
teacher.speak()
teacher.hithit()
teacher.homework()

student = Student()
student.hit()
student.speak()
student.ㅋㅋ()
student.ㅇㅇ()
