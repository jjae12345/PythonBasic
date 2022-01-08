def 시리얼먹기():
    print("준비물을 준비합니다.")
    print("시리얼을 그릇에 넣습니다.")
    print("우유를 시리얼에 담긴 그릇에 떠서 먹습니다")
    print("숟가락으로 시리얼과 우유를 떠서 먹습나다.")

시리얼먹기()

def 시리얼먹기(우유, 시리얼 ,그릇 ,숟가락):
    # print("준비물을 준비합니다.")
    print("{}을 {}에 넣습니다.".format(시리얼, 그릇))
    print("{}을 {}에 넣습니다".format(시리얼 ,그릇))
    print("{}를 {}이 담긴 {}에 따릅니다.".format(우유, 시리얼, 그릇))
    print("{}으로 {}과 {}를 떠서 먹습니다.".format(숟가락, 시리얼, 우유))
    return "{} 1리터, {} 500그램 남았습니다.".format(우유, 시리얼)

A = 시리얼먹기("서울우유", "콘푸로스트", "밥그릇", "쇠숫가락")     
print(A)


def 망고먹기():
    print("준비물을 준비합니다.")
    print("망고를 접시에 놓습니다.")
    print("망고를 깝니다")
    print("입으로 먹습니다.")

def hello():
    print("안녕하세요")

hello()

def messege():
    print("A")
    print("B")

messege()
print("C")
messege()

def say1(name):
    string = '안녕하세요? ' + name + '님'
    return string

def say2(name):
    string = '안녕하세요? ' + name + '님'
    print(string)  


name = "홍길동"
say1(name)
say2(name)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a // b


a = 6
b = 3
print(add(b, a))
print(sub(b, a))
print(mul(b, a))
print(div(b, a))








