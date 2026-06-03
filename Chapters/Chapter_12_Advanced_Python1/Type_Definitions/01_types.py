'''
In Python, type definitions usually refer to specifying the expected types of variables, function parameters, and return values using type hints.

Variable Type Hints
name: str = "Sameer"
age: int = 25
height: float = 5.9
is_student: bool = True
Function Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}"

Here:

name: str means name should be a string.
-> str means the function returns a string.
Multiple Types

Using the Union type (or | in Python 3.10+):

from typing import Union

def square(num: Union[int, float]) -> float:
    return num * num

Or:

def square(num: int | float) -> float:
    return num * num
Lists, Dictionaries, and Tuples
numbers: list[int] = [1, 2, 3]

scores: dict[str, int] = {
    "Alice": 90,
    "Bob": 85
}

point: tuple[int, int] = (10, 20)
Custom Type Aliases
type UserId = int  # Python 3.12+

user_id: UserId = 123

Before Python 3.12:

UserId = int
Defining a Custom Class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
Typed Dictionaries
from typing import TypedDict

class Employee(TypedDict):
    name: str
    age: int

emp: Employee = {
    "name": "Sameer",
    "age": 25
}
Important Note

Type hints:

Improve readability.
Help IDEs and tools catch errors.
Are not enforced at runtime by Python itself.

Example:

def add(a: int, b: int) -> int:
    return a + b

add("3", "4")  # Python will run this and return "34"

'''

n : int = 5 #int type definition

name: str = 'Harry' #string type definition

def sum(a: int, b: int) -> int:
    return a + b

