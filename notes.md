Here are your **clean, structured, interview-ready OOP notes**—organized for quick revision and conceptual clarity.

---

# 🧠 Object-Oriented Programming (OOP) — Structured Notes

## 1. Class vs Object

**Class**

* Blueprint or template for creating objects
* Defines attributes (variables) and behaviors (methods)
* No real-world existence

```python
class Car:
    pass
```

**Object**

* Instance of a class (real-world entity)
* Occupies memory

```python
car1 = Car()
```

---

## 2. Encapsulation (Data Hiding)

* Bundling **data + methods** together
* Restricting direct access to internal state
* Achieved using **private variables + getters/setters**

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Private

    def get_balance(self):  # Getter
        return self.__balance

    def set_balance(self, amount):  # Setter
        if amount >= 0:
            self.__balance = amount
```

**Key Insight**

* Protects invariants (e.g., balance cannot be negative)
* Reduces unintended side effects

---

## 3. Inheritance (Code Reuse)

* Child class reuses properties of parent class
* Represents **"is-a" relationship**

```python
class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"
```

**Types**

* Single
* Multiple
* Multilevel
* Hierarchical

---

## 4. Abstraction (Interface Design)

* Hide implementation details
* Show only essential behavior
* Achieved using **abstract base classes (ABC)**

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
```

**Why important**

* Forces contract-based design
* Useful in large systems (APIs, frameworks)

---

## 5. Polymorphism

### Method Overriding (Runtime Polymorphism)

* Same method name, different implementation

```python
class Dog(Animal):
    def sound(self):
        return "Woof!"
```

### Method Overloading (Not native in Python)

* Achieved using `*args`, `**kwargs`

```python
def add(*args):
    return sum(args)
```

**Key Idea**

* Same interface → different behavior

---

## 6. Constructor

* Special method to initialize objects
* Runs automatically when object is created

```python
class Example:
    def __init__(self):
        self.value = 10
```

---

## 7. Method Types

### Instance Method

* Works with object
* Accesses instance variables

```python
def instance_method(self):
    pass
```

### Class Method

* Works with class
* Uses `cls`

```python
@classmethod
def class_method(cls):
    pass
```

### Static Method

* Independent utility function
* No access to class or instance

```python
@staticmethod
def static_method():
    pass
```

---

## 8. Composition (Has-A Relationship — Strong)

* Class contains another class object
* Strong coupling

```python
class Engine:
    pass

class Car:
    def __init__(self):
        self.engine = Engine()
```

---

## 9. Aggregation (Has-A Relationship — Weak)

* Objects exist independently
* Loose coupling

```python
class Department:
    pass

class University:
    def __init__(self, dept):
        self.department = dept
```

---

## 10. Access Modifiers

| Type      | Syntax  | Access Level       |
| --------- | ------- | ------------------ |
| Public    | `var`   | Anywhere           |
| Protected | `_var`  | Class + Subclasses |
| Private   | `__var` | Only inside class  |

---

## 11. Getter & Setter

* Controlled access to private variables

```python
class Example:
    def __init__(self):
        self.__value = 0

    def get_value(self):
        return self.__value

    def set_value(self, val):
        if val > 0:
            self.__value = val
```

---

## 🔥 High-Value Insights (Interview + Performance Thinking)

* Prefer **composition over inheritance** (better flexibility)
* Use **encapsulation** to maintain invariants → critical in large systems
* Avoid deep inheritance chains → increases complexity and cache misses in large systems
* Use **polymorphism** to reduce branching (`if-else explosion`)
* Static methods are slightly faster (no object/context binding)

---

## 🧩 Mental Model

* **Class** → Blueprint
* **Object** → Instance
* **Encapsulation** → Protection
* **Inheritance** → Reuse
* **Abstraction** → Interface
* **Polymorphism** → Flexibility

---

If you want next step: I can convert this into a **real production-level file-organizer agent project using OOP + watchdog + concurrency + system-level optimizations** (aligned with your performance engineering goal).
