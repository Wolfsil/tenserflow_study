# -*- coding: utf-8 -*-
"""1.넘파이

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FoYbmcyUroKRoyEUt98HBBqlyFAvPC6Y

# Python 기초와 Numpy

이 튜토리얼은 Justin Johnson에 의해 최초로 작성되고, Volodymyr Kuleshov, Isaac Caswell, 그리고 Kevin Zakka에 의해 수정된 버전을 이 수업에 맞게 다시 수정한 것이다.

##학습목표

- Python 기초
  - 기본 데이터 타입과 연산 
  - 컨테이너(container): List, Dictionary, Set, Tuple
  - Function과 Class
- Numpy
  - Basic usage
  - Array indexing
  - Array math
  - Broadcasting
- Matplotlib: Plotting, Subplots, Images

## Python 버전에 대하여

* 파이썬의 두 가지 버전 Python 2.7과 Python 3.x가 동시에 사용되어 왔지만 2020년 1월에 Python 2에 대한 지원이 공식적으로 종료

* 우리 수업에서는 Python 3.6 혹은 3.7을 사용

* 커맨드라인에 다음의 명령어로 현재 시스템에 설치된 파이썬 버전을 확인할 수 있음: `python --version`.
"""

!python --version

"""## 기본 데이터 타입 

다른 프로그래밍 언어들처럼 파이썬에도 정수, 실수, 불리언, 문자열 같은 기본 자료형이 있다.

####Numbers

파이썬의 정수형(Integers)과 실수형(floats) 데이터 타입은 다른 언어와 거의 유사하다.
"""

x = 3
print(x, type(x))     # `type`함수를 이용하여 데이터의 타입을 확인할 수 있다.

print(x + 1)   # Addition
print(x - 1)   # Subtraction
print(x * 2)   # Multiplication
print(x ** 2)  # Exponentiation

x += 1
print(x)
x *= 2
print(x)

y = 2.5
print(type(y))
print(y, y + 1, y * 2, y ** 2)

print(int(y))       # 정수로 타입 캐스팅    (int)y
print(float(x))     # 실수로 타입 캐스팅

print(int(y)/x)     # 피연산자가 둘 다 정수지만 결과는 실수이다.
print((int(y)//x))  # //는 몫을 구하는 연산이다.
print(int(y) % x)   # %는 나머지를 구하는 연산이다.

"""- 다른 언어들과는 달리 파이썬에는 증감 단항연산자(`x++`, `x--`)
가 없으며, 
- 지수연산자 `**`가 제공된다. 
- 또한 Python 3에서는 나눗셈에서 피연산자가 모두 정수인 경우에도 결과는 실수가 된다.
- 몫을 구하는 연산자는 `//`이며, 나머지 연산자는 `%`이다.
- 파이썬은 long 정수형과 복소수 데이터 타입도 지원한다. 자세한 사항은 [문서](https://docs.python.org/3.7/library/stdtypes.html#numeric-types-int-float-long-complex)를 참조하라.

####Booleans

논리연산자는 기호(`&&`, `||`, `~`) 대신 영어 단어(`and`, `or`, `not`)를 사용한다.
"""

t, f = True, False
print(type(t))

print(t and f) # Logical AND;
print(t or f)  # Logical OR;
print(not t)   # Logical NOT;
print(t != f)  # Logical XOR;

"""####Strings
파이썬은 문자열을 표현하고 처리하는 다양한 기능을 지원한다:
"""

word = "it's"
print(word)
hello = 'hello'   # String literals can use single quotes
world = "world"   # or double quotes; it does not matter
print(hello, len(hello))

hw = hello + ' ' + world  # String concatenation
print(hw)

hw12 = 'The concatenated string is {} jhdfg {}sdf{}.'.format(hello, world, 12)  # string formatting printf("%d%s%f", 4, "hello", 0.25)
print(hw12)

"""문자열 객체에는 유용한 메소드들이 많다; 예를 들어:"""

s = "hello"
print(s.capitalize())  # Capitalize a string
print(s.upper())       # Convert a string to uppercase; prints "HELLO"
print(s.rjust(7))      # Right-justify a string, padding with spaces
print(s.center(7))     # Center a string, padding with spaces
print(s.replace('l', '(ell)'))  # Replace all instances of one substring with another
print('  world '.strip())  # Strip leading and trailing whitespace

"""문자열 내에서 substring을 검색하는 다양한 메서드들을 제공한다."""

print('lm' in s)
print(s.find('lm'))
print(s.idex('elm'))

"""문자열을 분할하는 다양한 기능을 제공한다."""

str = '1,2,3,4'
print(str.split(','))
print(str.split(',', maxsplit=2))
print('1,2,,3,'.split(','))

"""모든 문자열 메소드는 [문서](https://docs.python.org/3.7/library/stdtypes.html#string-methods)에서 찾아볼 수 있다.

##컨테이너 (container)

파이썬은 다음과 같은 컨테이너 타입을 지원한다. 
- 리스트(list)
- 딕셔너리(dictionary)
- 집합(set)
- 튜플(tuple)

## 리스트(List)

### 리스트의 생성과 기본 연산들

리스트는 파이썬에서 배열 같은 존재이다. 하지만 배열과 달리 **크기 변경이 가능**하고 **서로 다른 자료형**일지라도 하나의 리스트에 저장될 수 있다:
"""

empty = []        # Create an empty list
print(len(empty)) # the length of a list
xs = [3, 1, 2]    # Create a list of length 3
print(len(xs))
print(xs, xs[0])
print(xs[1])
print(xs[-1])     # Negative indices count from the end of the list; prints "2"
print(xs[-2])
print(xs[-3])

"""리스트에 저장된 값을 변경하거나, 리스트에 새로운 원소를 추가(`append`, `insert`)하고 삭제(`pop`, `remove`)하는 여러 방법들을 제공한다."""

xs[2] = 'foo'    # Lists can contain elements of different types
print(xs)

xs.append('bar') # Add a new element to the end of the list
print(xs)

xs.insert(1, 'orange')      # 특정 위치에 원소 삽입하기
print(xs)

xs = [3, 'orange', 1, 'foo', 'bar', 10]
x = xs.pop()     # Remove and return the last element of the list
print(x, xs)

xs.remove(1)
print(xs)
xs.remove(xs[1])
print(xs)
xs.remove('bar')
print(xs)

"""리스트를 복사하여 새로운 리스트를 만들 수 있다."""

thislist = ["apple", "banana", "cherry"]
newlist = thislist
newlist[0] = 'orange'
print(thislist)

mylist = thislist.copy()
mylist[0] = 'melon'
print(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

"""두개 이상의 리스트를 하나의 리스트로 합칠 수 있다."""

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1 += list2
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

"""리스트의 리스트는 2차원 배열과 같은 역할을 한다."""

ys = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]  # 4*3 크기의 이차원 배열처럼 사용한다.
print(len(ys))
print(ys)
print(ys[1])
print(ys[1][2])
# print(ys[1, 2])       # Error

for r in ys:
  print(r)

for r in ys:
  for v in r:
    print(v)

"""좀 더 자세한 사항은 [문서](https://docs.python.org/3.7/tutorial/datastructures.html#more-on-lists)를 참조하라.

### 리스트 슬라이싱(slicing)

리스트의 한 원소 접근하는 것 이외에도, 파이썬은 리스트를 잘라낸 일부분에 접근하는 간결한 문법을 제공한다. 이를 **슬라이싱**이라고 한다. 

슬라이싱의 기본 형태는 `x[start:end:step]`이다. `start는 슬라이싱을 시작할 위치, `end는 끝낼(exclusive) 위치, 그리고 `step`은 몇개씩 건너뛸지를 지정한다. `step`은 생략될 수 있고, 그 경우 `step=1`로 간주된다.
"""

# nums = [0, 1, 2, 3, 4]
nums = list(range(5))    # range is a built-in function that creates a list of integers
print(nums)         # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])    # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])     # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])     # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])      # Get a slice of the whole list; prints ["0, 1, 2, 3, 4]"
print(nums[:-2])    # Slice indices can be negative; prints ["0, 1, 2, 3]"

nums[2:4] = [8, 9] # Assign a new sublist to a slice
print(nums)         # Prints "[0, 1, 8, 9, 4]"

print(nums[::2])
print(nums[-1::-1])

"""리스트를 치환하면 새로운 리스트가 생성되지 않지만, 리스트를 슬라이싱하면 새로운 리스트가 생성된다."""

a = [1, 2, 3, 4]
b = a             # a와 b는 동일한 리스트 객체를 참조한다.
c = a[:]          # c는 a의 복사본을 참조한다. 즉, a와 c는 별개의 리스트 객체이다.
b[0] = 0
c[1] = 0
print(a)
print(b)
print(c)

"""### 원소의 존재 검사와 반복문

아래와 같이 리스트에 특정 원소가 존재하는지 검사할 수 있고, 또한 반복문에서 리스트의 요소들을 반복해서 조회할 수 있다.
"""

animals = ['cat', 'dog', 'monkey']
if 'dog' in animals:
  print("Yes, 'dog' is in the list.")
  
for animal in animals:
    print(animal)

"""만약 반복문 내에서 리스트 각 요소의 인덱스에 접근하고 싶다면, `enumerate` 함수를 사용하라:"""

animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))

"""
### 리스트의 정렬

"""

cars = ['Ford', 'BMW', 'Volvo']
print(cars)
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
print(cars)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
result = sorted(cars)
print(result)
print(cars)

"""물론 Python은 custom comparator를 이용하는 보다 generic한 정렬 기능을 제공한다. 그 내용은 생략한다.

### 예제

Python으로 직접 정수 리스트를 정렬하는 Quicksort 알고리즘을 구현해보자.
"""

def partition(arr):
    x = arr[len(arr)-1]             # pivot element
    i = -1                          # position of the last element that is less than or equal to pivot
    for j in range(len(arr)-1):     # iterate over elements except pivot
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]     # swap
    arr[i+1], arr[len(arr)-1] = arr[len(arr)-1], arr[i+1]     
    return i+1

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    q = partition(arr)
    left = arr[:q]
    right = arr[q+1:]

    return quicksort(left) + [arr[q]] + quicksort(right)

data = [ 3, 6, 8, 10, 1, 2, 1 ]
print(quicksort(data))

"""### <font color=”blue”> **실습 과제 1** 
1. 정수 리스트를 정렬하는 삽입정렬(insertion sort) 알고리즘을 Python으로 구현하라.
2. 정수 리스트를 정렬하는 합병정렬(merge sort) 알고리즘을 Python으로 구현하라.
</font>

### List Comprehension

예를 들자면 하나의 리스트에 저장된 모든 숫자의 제곱으로 구성되는 다른 리스트를 구성하는 다음의 코드를 보라:
"""

nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)

"""리스트 comprehension을 이용해 이 코드를 간단하게 만들 수 있다:


"""

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)

"""또한 리스트 comprehensions에 조건을 추가할 수도 있다:"""

nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)

words = ['hello', 'python', 'and', 'numpy', 'they', 'are', 'really', 'fun']
selected = [str for str in words if 'e' in str]
print(selected)
longstrs = [str.capitalize() for str in words if len(str) > 4]
print(longstrs)

"""### Quicksort Revisited"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

print(quicksort([3,6,8,10,1,2,1]))

"""### <font color=”blue”> **실습 과제 2**  
 </font>

중고 자동차 재고를 저장한 [파일](https://www.dropbox.com/s/k9py88enkkdiand/cars.csv?dl=0) `cars.csv`를 읽어 온다. Python은 csv 파일을 쉽게 읽고 처리하기 위한 다양한 라이브러리를 제공하지만 일단 여기에서는 단순한 텍스트 파일로 다루어보자.
"""

from google.colab import drive
drive.mount('/content/drive')

f = open('/content/drive/My Drive/데이터 사이언스/cars.csv', 'r')   # 파일을 open한다.
head = f.readline()           # 파일의 첫 라인을 읽는다. 첫 라인은 테이블의 head이다.
print(head)                   # Brand,Price,Body,Mileage,EngineV,Engine Type,Registration,Year,Model
data = f.readlines()          # 파일의 나머지 모든 라인을 읽어온다. 라인들의 리스트로 저장된다.
f.close()

print(len(data))              # 4345
print(type(data[0]), data[0]) # 각 라인들은 하나의 String이고, 각 스트링은 9개의 필드가 콤마(,)로 구분된 형태이다.







"""<font color=”blue”> **문제**:
1. 제조사가 Volkswagen인 가솔린(Gas) 차들 중에서 형태가 Sedan인 자동차를 개수는?
2. 제조사가 BMW인 자동차들만 하나의 리스트에 저장한 후 제조년도에 대한 오름차순으로 정렬하여 출력하라. </font>

## 딕셔너리(Dictionary)

**자바의** ‘맵(map)’과 유사하게 파이썬의 ‘딕셔너리’는 (key, value) 쌍을 저장한다.
"""

d = {'cat': 'cute', 'dog': 'furry'}  # Create a new dictionary with some data
print(d['cat'])       # Get an entry from a dictionary; prints "cute"
print('cat' in d)     # Check if a dictionary has a given key; prints "True"

d['fish'] = 'wet'    # Set an entry in a dictionary
print(d['fish'])      # Prints "wet"
print(d)

# print(d['monkey'])  # KeyError: 'monkey' not a key of d
print(d.get('monkey'))

print(d.get('monkey', 'N/A'))  # Get an element with a default; prints "N/A"
print(d.get('fish', 'N/A'))    # Get an element with a default; prints "wet"

del d['fish']        # Remove an element from a dictionary
print(d.get('fish', 'N/A')) # "fish" is no longer a key; prints "N/A"

"""딕셔너리는 key를 이용하여 쉽게 반복(iterate)할 수 있다."""

d = {'person': 2, 'cat': 4, 'spider': 8}
for animal, legs in d.items():
    print('A {} has {} legs'.format(animal, legs))

"""리스트 comprehensions과 유사한 딕셔너리 comprehensions을 통해 손쉽게 딕셔너리를 만들 수 있다."""

nums = [0, 1, 2, 3, 4]
even_num_to_square = {x: x ** 2 for x in nums if x % 2 == 0}
print(even_num_to_square)

"""딕셔너리에 관한 더 세부적인 사항은 [문서](https://docs.python.org/2/library/stdtypes.html#dict)를 참조하라.

## 집합(Set)

집합은 순서가 없는 서로 다른 원소들의 모임이다
"""

animals = {'cat', 'dog'}
print('cat' in animals)   # Check if an element is in a set; prints "True"
print('fish' in animals)  # prints "False"

animals.add('fish')      # Add an element to a set
print('fish' in animals)
print(len(animals))       # Number of elements in a set;

animals.add('cat')       # Adding an element that is already in the set does nothing
print(len(animals))       
animals.remove('cat')    # Remove an element from a set
print(len(animals))

"""집합의 원소들간에는 순서가 없으므로 다음과 같이 집합의 원소들을 iterate할 때 항상 동일한 순서로 iterate되다고 가정해서는 않된다. """

animals = {'cat', 'dog', 'fish'}
for idx, animal in enumerate(animals):
    print('#{}: {}'.format(idx + 1, animal))

"""리스트와 마찬가지로 다음과 같이 set comprehension을 지원한다."""

from math import sqrt
print({int(sqrt(x)) for x in range(30)})

"""## 튜플(Tuple)

튜플은 immutable한 리스트이다. 즉, 한 번 생성된 튜플은 값을 변경할 수 없다. 그점을 제외하고 튜플은 리스트와 매우 유사하지만 중요한 차이가 한가지 있다. **튜플은 딕셔너리의 key로 사용될 수 있지만 리스트는 그렇지 않다.**
"""

d = {(x, x + 1): x for x in range(10)}  # Create a dictionary with tuple keys
t = (5, 6)       # Create a tuple
print(type(t))
print(d[t])       
print(d[(1, 2)])

t[0] = 1

"""## <font color=”blue”> **실습 과제 3**  
 </font>

1. 실습과제2에서는 데이터를 string의 리스트로 저장하였다. 각 스트링은 여러 개의 필드들이 콤마로 구분된 
형태였다. 파일의 첫 번째 줄의 헤드 정보를 이용하여 데이터를 딕셔너리의 리스트로 변환하여 저장하라. 각각의 딕셔너리는 하나의 자동차를 표현하고, Brand, Price, Body, Mileage, EngineV, Engine Type, Registration, Year, Model의 9개의 키를 사용하라.
2. 가격이 `$`20,000~`$`50,000 범위이고, 제조 년도가 2000년 이후이며, 형태가 sedan이면서 가솔린(Gas)을 연료로 사용하는 모든 차량들을 검색하여 가격이 낮은 것 부터 높은 순으로 정렬하여 출력하라.
3. 모든 차량 제조사의 이름을 저장하는 집합(set)을 생성하고 출력하라.

## 함수(Function)

키워드 def를 사용하여 다음과 같이 함수를 정의한다.
"""

def sign(x):
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'

for x in [-1, 0, 1]:
    print(sign(x))

"""다음과 같이 optional argument와 그것의 default 값을 지정할 수 있다. """

def hello(name, loud=False):
    if loud:
        print('HELLO, {}'.format(name.upper()))
    else:
        print('Hello, {}!'.format(name))

hello('Bob')
hello('Fred', loud=True)

"""## 클래스(Class)

Python에서는 다음과 같이 클래스를 정의한다.
"""

class Greeter:

    # Constructor
    def __init__(self, name):
        self.name = name  # Create an instance variable

    # Instance method
    def greet(self, loud=False):
        if loud:
          print('HELLO, {}'.format(self.name.upper()))
        else:
          print('Hello, {}!'.format(self.name))

g = Greeter('Fred')  # Construct an instance of the Greeter class
g.greet()            # Call an instance method; prints "Hello, Fred"
g.greet(loud=True)   # Call an instance method; prints "HELLO, FRED!"

"""##Numpy 배열

- Numpy는 파이썬이 계산과학분야에 이용될때 핵심 역할을 하는 라이브러리이다.
- Python의 리스트가 배열과 유사한 역할을 할 수 있지만 리스트는 처리속도가 느리다. 고성능이 필요한 상황에는 Numpy 배열이 적합하다.
- Numpy는 **동일한 자료형의 데이터를 저장**하는 다차원 배열을 제공한다

### 설치와 import하기

Colab에는 이미 설치되어 있다. PC에서 Numpy 패키지는 다음의 명령으로 설치할 수 있다.

`$ pip install numpy`

Numpy를 사용하려면 먼저 다음과 같이 `numpy` 패키지를 import해야 한다.
"""

import numpy as np
print(np.__version__)

"""### 배열의 생성, 그리고 rank와 shape

파이썬의 리스트를 이용해 Numpy 배열을 초기화 할 수 있다.

배열의 원소들은 정수들의 튜플로 색인(indexing) 된다. 

배열은 `ndim`, `shape`, `dtype`등의 속성을 지닌다. `ndim` 혹은 rank는 배열이 몇 차원인지를 의미하고, `shape는` 는 각 차원 별 크기를 나타내는 튜플이다. `dtype은` 배열에 저장된 데이터의 타입이다.
"""

a = np.array([1, 2, 3])   # rank 1인 배열의 생성
print(a)
print(a[0], a[1], a[2])   # []를 이용해 배열의 각각의 값에 접근

print(type(a))

print(a.ndim)             # 모든 배열은 rank를 나타내는 속성 ndim을 가짐
print(a.shape)            # 모든 배열은 shape이라는 속성을 가짐
print(a.dtype)            # 모든 배열은 데이터 타입을 나타내는 dtype 속성을 가짐

a[0] = 5                  # 배열의 값을 변경
print(a)

b = np.array([[1,2,3],[4,5,6]])   # rank 2인 배열의 생성
print(b)
print(b.ndim)
print(b.shape)
l = [[1,2,3],[4,5,6]]
print(l[0][0])

print(b[0, 0], b[0, 1], b[1, 0])        # 다차원 배열에서 각각의 값에 접근
print(b[(0, 0)], b[(0, 1)], b[(1, 0)])  # 다차원 배열에서 각각의 값에 접근

c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(c.ndim)
print(c.shape)
print(c)
print(c[0, 1, 2], c[(0, 1, 2)])

"""*Numpy는* 배열을 생성하고 특정한 값으로 초기화하는 다양한 함수를 제공한다."""

a = np.zeros((2,2))   # 0으로 채워진 2*2 크기의 2차원 배열을 생성
print(a)
print(a.dtype)        # 데이터 타입은 실수가 된다.

b = np.ones((1,2))    # 모든 원소가 1인 1*2 크기의 2차원 배열
                      # b는 첫번째 차원의 길이가 1인 2차원 배열이다. 이것은 1차원 배열과는 다르다.
print(b)              # 이 배열이 어떻게 출력되는지 확인하라.

c = np.full((2,2), 7) # Create a constant array
print(c)

d = np.eye(3)        # Create a 2x2 identity matrix
print(d)

e = np.random.random((2,2)) # Create an array filled with random values
print(e)

"""Numpy 배열에는 **동일한 타입**의 값들이 저장된다. Numpy는 배열이 생성될 때 자료형을 스스로 추측한다. 하지만 배열을 생성할 때 명시적으로 특정 자료형을 지정할 수도 있다."""

x = np.array([1, 2])  # Let numpy choose the datatype
y = np.array([1.0, 2.0])  # Let numpy choose the datatype
z = np.array([1, 2], dtype=np.int32)  # Force a particular datatype
w = np.array([1, 2], dtype=np.float32)  # Force a particular datatype

print(x.dtype, y.dtype, z.dtype, w.dtype)

"""### 배열 reshape

Numpy배열은 원소의 개수가 유지되는 경우 자유롭게 다른 shape으로 변경할 수 있다. 가령 (3, 4) 크기의 2차원 배열은 (2, 6) 크기의 2차원 배열이나, 길이가 12인 1차원 배열, 혹은 (2, 2, 3) 크기의 3차원배열로도 쉽게 변형할 수 있다.
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print(arr)

arr1 = np.reshape(arr, (12))    # arr1 = arr.reshape(12) 
print(arr1)

arr2 = np.reshape(arr, (2, 6))  # arr1 = arr.reshape(2, 6)
print(arr2)

arr3 = np.reshape(arr, (2, 2, 3))
print(arr3)

# arr4 = np.reshape(arr, (3, 3))

"""배열 reshape은 배열을 복사하여 새로운 배열을 생성하는게 아니라 존재하는 배열에 대한 새로운 view를 제공할 따름이다."""

arr3[0, 0, 0] = 99
print(arr)

"""배열 reshape에서 어짜피 원소의 개수는 보존되어야 하므로 모든 차원의 크기를 명시할 필요가 없다. 즉, 자동으로 계산할 수 있는 경우에는 크기를 명시하는 대신 -1로 대신할 수 있다."""

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

wrongreshape = arr.reshape(2, -1, -1)

"""가장 자주 사용하는 reshape은 다차원 배열을 1차원 배열로 reshape하는 경우이다. Numpy는 이를 위한 몇가지 방법을 제공한다."""

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)
print(newarr)

print(np.ravel(arr))
print(arr.ravel())
# print(np.flatten(arr))
print(arr.flatten())

"""### 배열 슬라이싱(slicing)

파이썬 리스트와 유사하게 Numpy 배열도 슬라이싱이 가능하다. Numpy 배열은 다차원인 경우가 많기에, 각 차원별로 어떻게 슬라이스할건지 명확히 해야 한다.
"""

# Create the following rank 2 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])

# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
print(b)

"""Numpy 배열의 슬라이싱은 새로운 배열을 생성하지 않는다. 다만 기존 배열에 대한 새로운 view를 제공할 뿐이다. 따라서 슬라이스된 배열의 값을 수정하면 원래 배열의 값도 수정된다. """

print(a[0, 1])
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(a)

"""정수 인덱스와 슬라이스 인덱스를 섞어서 함께 사용할 수 있다. 이 경우 배열의 rank가 감소하게 될 것이다. """

# Create the following rank 2 array with shape (3, 4)
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(a)

row_r1 = a[1, :]    # Rank 1 view of the second row of a  
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a

print(row_r1, row_r1.shape)
print(row_r2, row_r2.shape)

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape)
print()
print(col_r2, col_r2.shape)

"""### 배열 합치기

#### Concatenate 함수로 배열 합치기

Numpy는 둘 이상의 배열을 **특정 축(axis)을 따라서** 합치는 `concatenate` 메서드를 제공한다. 배열들은 동일한 rank를 가져야 하며, 합쳐질 축을 제외한 나머지 축으로는 동일한 길이를 가져야 한다. 만들어진 배열은 입력된 배열과 동일한 rank를 가진다.
"""

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5])

arr = np.concatenate((arr1, arr2))

print(arr)

"""배열을 합칠 축을 지정할 수 있다. 축이 지정되지 않으면 디폴트로 `axis=0`으로 간주된다."""

arr1 = np.array([[1, 2], 
                 [3, 4]])
arr2 = np.array([[5, 6], 
                 [7, 8]])
arr3 = np.concatenate((arr1, arr2), axis=0)
print(arr3)

arr4 = np.concatenate((arr1, arr2), axis=1)
print(arr4)

"""#### Stack 함수로 배열 쌓기

`stack` 함수는 배열들을 새로운 축으로 합치는 일을 한다. 예를 들어 1차원 배열들을 합쳐서 2차원 배열을 만들거나, 2차원 배열들을 여러 개 합쳐서 3차원 배열을 합치거나 등이다. 합쳐질 배열들은 모두 동일한 shape이어야 한다.
"""

arr1 = np.array([1, 
                 2, 
                 3])
arr2 = np.array([4, 
                 5, 
                 6])
arr3 = np.stack((arr1, arr2), axis=0)
print(arr3)
arr4 = np.stack((arr1, arr2), axis=1)
print(arr4)

"""### 정수 배열 인덱싱(Integer Array Indexing)

배열에서 하나의 **단일한 원소를 엑세스할 경우에 tuple로 인덱싱**한다.  

하지만 배열을 다른 정수 배열(들)로(혹은 정수 배열로 암묵적으로 변환될 수 있는 리스트로) 인덱싱할 수 있다. 이것은 **배열에 저장된 여러 개의 값을 한꺼번에 뽑아내어서 다른 하나의 배열을 생성**하려는 목적이다.

배열을 슬라이싱하면 결과로 얻어지는 배열은 원본 배열의 연속적인 부분 배열이거나 혹은 일정한 규칙을 따라서(가령 한 칸씩 건너서 등) 잘라낸 형태이다. 
그러나 정수 배열 인덱싱을 하면 불규칙적으로 원본 배열의 일부를 뽑내거나 원본과 다른 배열을 만들 수도 있다.

**중요**: 슬라이싱은 단지 원본 배열에 대한 새로운 view를 생성하는 것에 지나지 않지만, 정수배열인덱싱은 새로운 배열 객체를 생성한다.

#### 1차원 배열에 대한 정수 배열 인덱싱

인덱스로 사용된 배열의 각 값은 그 자리에 올 원래 배열의 값의 위치를 표시한다.
"""

x = np.arange(10, 1, -1)  # x = np.array([10,  9,  8,  7,  6,  5,  4,  3,  2])
print(x)

print(x[np.array([3, 3, 1, 8])])
print(x[[3, 3, 1, 8]])    # 리스트는 배열로 암묵적으로 변환가능하므로 동일하다.

"""음수 인덱스도 물론 사용 가능하다."""

print(x[np.array([3, 3, -3, 8])])

"""1차원 배열을 다차원 배열로 인덱싱할 수도 있다. 이 경우 **리턴되는 결과는 항상 인덱스 배열과 동일한 shape**의 배열이며, 값은 인덱스 배열에 의해서 지정한 값들이다."""

print(x[np.array([[1,1],[2,3]])])     # 1차원 배열을 2차원 배열로 인덱싱한 경우

"""#### 다차원 배열에 대한 정수 배열 인덱싱

다차원 배열이 배열로 인덱싱될 때는 좀 더 규칙이 복잡해진다. 우선 가장 간단한 경우는 **원래 배열의 차원의 개수, 즉 rank개의 인덱스 배열로 제공되고, 모든 인덱스 배열들이 동일한 shape을 가지는 경우**이다. 

이 경우 결과는 인덱스 배열과 동일한 shape을 가진다. 또한 결과 배열의 값은 각각의 차원에 대해서 그 차원에 대응하는 인덱스 배열의 값을 인덱스로 하는 값이다.
"""

y = np.arange(35).reshape(5,7)
print(y)
print(y[np.array([0,2,4]), np.array([0,1,2])])
# print(y[[0,2,4], [0,1,2]])

print(y[np.array([[0, 1], [2, 3]]), np.array([[4, 5], [2, 3]])])

"""인덱스 배열들이 서로 동일한 shape이 아닐 경우에는 그들을 동일한 shape으로 만들기 위해서 broadcast를 시도한다. 아직 broadcast에 대해 다루지 않았으므로 이 부분은 생략한다.

원래 **배열의 rank보다 적은 개수의 인덱스 배열**을 사용하여 인덱싱할 수도 있다.
"""

print(y[np.array([0, 4, 1, 0])])

"""이 경우 인덱스 배열에 있는 값에 해당하는 행(row)들을 선택하여 새로운 배열을 만들어서 반환한다. 이 기능은 주어진 배열의 특정 행만을 뽑아서 새로운 배열을 구성할 때 유용하다.

이 외에도 배열인덱싱을 활용하는 많은 use case들이 있다. 상세한 사항은 [문서](https://numpy.org/doc/stable/reference/arrays.indexing.html)를 참조하라.

### 불리언 배열 인덱싱(Boolean array indexing)

불리언 배열 인덱싱을 통해 배열 속 요소를 취사선택할 수 있다. 불리언 배열 인덱싱은 특정 조건을 만족하게 하는 요소만 선택하고자 할 때 자주 사용된다.
"""

import numpy as np

a = np.array([[1, 2], 
              [3, 4], 
              [5, 6]])

bool_idx = (a > 2)  # Find the elements of a that are bigger than 2;
                    # this returns a numpy array of Booleans of the same
                    # shape as a, where each slot of bool_idx tells
                    # whether that element of a is > 2.

print(bool_idx)

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])

# We can do all of the above in a single concise statement:
print(a[a > 2])

"""### 배열 연산(Array math)

Numpy 배열에 대한 사칙연산 등의 기본적인 수학 연산이나 함수는 배열의 각 요소별로(elementwise) 동작한다.
"""

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

"""즉, `*`은 행렬 곱이 아니라 요소별 곱이다. Numpy에선 벡터의 내적, 벡터와 행렬의 곱을 위해서는 `*`대신 ‘dot’함수를 사용해야 한다. ‘dot’은 Numpy 모듈 함수로서도 배열 객체의 인스턴스 메소드로서도 이용 가능하다."""

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

print(x.dot(y))
print(x.dot(v))

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

"""`@`연산자는 numpy의 `dot` 연산자와 동일하다."""

print(v @ w)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))
print(x @ v)

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)

"""Numpy는 `sum`, `max`, `min`, `mean`, `std` 등의 많은 유용한 함수들을 제공한다. """

x = np.array([[1,2],
              [3,4]])

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

print(np.max(x))
print(np.max(x, axis=1))
print(np.min(x))
print(np.min(x, axis=0))

print(np.mean(x))
print(np.mean(x, axis=0))

print(np.std(x))
print(np.std(x, axis=1))

"""행렬에서 자주 사용되는 연산의 하나는 전치행렬을 구하는 것이다. 행렬을 전치하기 위해선, 간단하게 배열 객체의 ‘T’ 속성을 사용하면 된다."""

print(x)
print("transpose\n", x.T)

v = np.array([[1,2,3]])
print(v )
print("transpose\n", v.T)

"""### Broadcasting

브로트캐스팅은 Numpy에서 shape이 다른 배열 간에도 산술 연산이 가능하게 하는 메커니즘이다. 종종 작은 배열과 큰 배열이 있을 때, 큰 배열을 대상으로 작은 배열을 여러 번 연산하고자 할 때가 있다. 예를 들어, 배열의 모든 원소에 스칼라 값을 더하거나 곱하거나, 혹은 행렬의 각 행에 상수 벡터를 더하고 싶은 경우 등이 있다.

Numpy 브로드캐스팅을 이용한다면 다음과 같이 간단하게 할 수 있다.
"""

import numpy as np

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x + 2)      # add a scalar to an array
print(x * 2)      # multiply a scalar

v = np.array([1, 0, 1])
y = x + v         # Add v to each row of x using broadcasting
print(y)

"""x의 shape가 (4, 3)이고 v의 shape가 (3,)라도 브로드캐스팅으로 인해 y = x + v는 문제없이 수행된다; 이때 ‘v’는 ‘v’의 복사본이 차곡차곡 쌓인 shape (4, 3)처럼 간주되어 ‘x’와 동일한 shape가 되며 이들 간의 요소별 덧셈연산이 y에 저장된다.

두 배열의 브로드캐스팅은 아래의 규칙을 따른다:

1. 두 배열이 동일한 rank를 가지고 있지 않다면, 낮은 rank의 배열의 shape앞에 1을 연속적으로 추가하여 두 배열의 rank를 동일하게 만든다.
2. 특정 차원에서 두 배열이 동일한 크기를 갖거나, 두 배열 중 하나의 크기가 1이라면 그 두 배열은 그 차원에서 compatible하다고 한다.
3. 두 행렬이 모든 차원에서 compatible하다면, 브로드캐스팅이 가능하다.
4. 브로드캐스팅이 이뤄지면, 두 배열 shape의 요소별 최대값으로 이루어진 shape이 두 배열의 shape으로 간주된다.
5. 차원에 상관없이 크기가 1인 배열과 1보다 큰 배열이 있을 때, 크기가 1인 배열은 자신의 차원 수만큼 복사되어 쌓인 것처럼 간주한다.

더 자세한 설명은 [scipy문서](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)나 [scipy위키](http://wiki.scipy.org/EricsBroadcastingDoc)를 참조하라.

##Matplotlib

Matplotlib는 **plotting 라이브러리**이다. 여기서는 `matplotlib.pyplot` 모듈에 관한 간략하게 소개한다. 먼저 아래와 같이 `import`한다.
"""

import matplotlib.pyplot as plt

"""다음과 같이 특별한 iPython command를 실행함으로써 Jupyter Notebook이나 Colab에서 inline으로 챠트들을 디스플레이할 수 있다."""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""###Plotting

`matplotlib`에서 가장 중요한 기능은 2차원 데이터를 그래프로 그릴 수 있게 해주는 `plot`이다.
"""

import numpy as np
# Compute the x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
print(x)
y = np.sin(x)
print(y)

# Plot the points using matplotlib
plt.plot(x, y)

"""아래와 같이 여러 개의 함수를 한 번에 디스플레이 할 수 있다. 또한 타이틀이나 범례(legend)를 달거나 축 라벨(axis label)을 붙일 수도 있다."""

y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])

"""###Subplots

`subplot`함수를 통해 하나의 그림 위에 여러 개의 차트를 나타낼 수 있다.
"""

# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(2, 1, 1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()

"""`subplot` 함수에 대한 자세한 설명은 [문서](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot)를 참조하라.

### 이미지(image) 디스플레이 하기

`pyplotlib`의 `imshow`함수를 사용해 이미지를 디스플레이 할 수 있다.
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
# from scipy.misc import imread, imresize
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread

img = imread('/content/drive/My Drive/DataScience2020/assets/cat.jpg')
print(type(img))
print(img.shape)

img_tinted = img * [1, 0.95, 0.9]

# 원본 이미지 나타내기
plt.subplot(1, 2, 1)
plt.imshow(img)

# 색변화된 이미지 나타내기
plt.subplot(1, 2, 2)

# imshow를 이용하며 주의할 점은 데이터의 자료형이
# uint8이 아니라면 이상한 결과를 보여줄 수도 있다는 것이다.
# 그러므로 이미지를 나타내기 전에 명시적으로 자료형을 uint8로 형변환 해준다.

plt.imshow(np.uint8(img_tinted))
plt.show()

from PIL import Image
from urllib.request import urlopen

# url = 'https://newevolutiondesigns.com/images/freebies/colorful-background-14.jpg'
url = 'https://github.com/ohheum/DS2020/blob/master/assets/cat.jpg?raw=true'
img = Image.open(urlopen(url))
plt.imshow(img)
plt.show()