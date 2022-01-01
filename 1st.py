from math import ceil as c
from math import fabs as fs


# import 할 때 필요한것들만 import 하는 것이 효율적이다.

# a_string = "hello"
# a_number = 3
# a_float = 3.14
# a_boolean = True
# print(a_boolean) # var

# day = ["mon","tue","wed","thur","fri"] #list
# print("mon" in day) # "mon" 이 day라는 리스트안에 속하는가? = True
# print(day[2]) # day라는 리스트의 3번째 항목 출력 (숫자는 0부터 카운트)
# print(len(day)) # day리스트의 길이 (항목 갯수)
# day.append("sun") # day리스트에 sun항목 뒤에 추가
# print(day)
# day.reverse() # 리스트 순서 뒤집기
# print(day)

# day = ("0mon","tue","wed","thur","fri") # tuple
# print(type(day))

# HSH1 ={              #dic
#   "name" : "HSH",
#   "age" : 23,
#   "leng" : "Kor",
#   "fav_color" : "blue, purple"
# }
# print(HSH1["age"])

# def hello(a):
#   print("hello",a)

# hello("HSH")

# def minus(a,b=2):
#   print(a-b)

# minus(6,4)
# minus(7)

# def plus(a,b):
#   if type(a) is str or type(b) is str:
#     return int(a) + int(b)
#   elif type(a) is int or type(b) is int:
#     return a + b 
#   else:
#     return
# result = plus(2, "3")

# def say_hello(name, age):
#   return f"Hello {name} you are {age} years old"

# hello = say_hello("HSH", "23")
# print(hello)
# print(plus(2,"7"))

# days = ("m","t","w","th","f")
# for day in days:
#   if day == "t":
#     break
#   print(day)
print(c(1.2325)) # 2
print(fs(-124.412)) # |-124.412| 