from random import randint, uniform
import sys
import math
import heapq
from requests import get


my_name = "seonhong"
age = 31
dead = False


def say_hello(user_name, user_age):
    print("hellow", user_name, "how are you")
    print("your", user_age, "years old")



def plus(a=0,b=0):
    print(a + b)

def minus(a=0,b=0):
    print(a - b)

def divide(a=0,b=0):
    print(a/b)

def multiply(a=0,b=0):
    print(a*b)

def square(a=0,b=0):
    print(a**b)


def tax_calc(Money):
    return Money * 0.5

def pay_tax(tax):
    print("thank you for paying", tax)

# to_pay = tax_calc(1000)

# pay_tax(to_pay)

a = "nico"

b = 5

c = 10

if a == "nico" and b == 10:
    print("True!")


password_correct = True

if password_correct:
    print("if is True")
else:
    print("Wrong password")


winner = 10

if winner > 10:
    print("winner is bigger than 10")
elif winner < 10:
    print("winner is less than 10")
else:
    print("winner is 10")


# age = input("how old are you?")

# print("user answer", age)



pc_choice = randint(1, 50)

distance = 0

""" while distance < 20:
    print("I'M running :", distance, "km")
    distance = distance + 1 """

# playing = True

# while playing:
#     user_choice = int(input("Choose number : "))
#     if user_choice < pc_choice:
#         print("you loose pc_choice : ", pc_choice)
#     elif user_choice == pc_choice:
#         print("draw pc_choice :", pc_choice)
#     elif user_choice > pc_choice:
#         print("your win")
#         playing = False

""" print("plz put in number?")
write = sys.stdin.readline()
print(write) """

heap = []

heapq.heappush(heap, 15)
heapq.heappush(heap, 10)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)

""" 
print(heap)

heapq.heappop(heap)

print(heap)
 """
""" 
heap2 = []
values = [1, 5, 3, 4, 2]

for i in values:
    heapq.heappush(heap2, -i)

print(heap2)

for i in range(5):
    print(-heapq.heappop(heap2)) """

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

results = {}

for each in websites:
    if not each.startswith("https://"):
        each = f"https://{each}"
    response = get(each)
    if response.status_code == 200:
        results[each] = "OK"
    else:
        results[each] = "FAILED"

    print(results)

test



