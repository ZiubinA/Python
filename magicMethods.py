import copy

class C:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value == other.value
    
    def __call__(self, number):
        print(f"multipling {number} on {self.value}")
        return number * self.value

class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        
        num = self.current
        self.current -= 1

        return num



x5 = C(5)
result = x5(10)
print(f"result = {result}")
print(f"is x5 calleble? {callable(x5)}")

print("Test countDown")
manual_timer = Countdown(3)

for i in manual_timer:
        print(i)
#try:
    
#print(next(manual_timer))
#print(next(manual_timer))
#print(next(manual_timer))
#print(next(manual_timer))
#except StopIteration:
#    print("Iterator ended")
    

original = [1, 2 , [100, 200]]

shallow = copy.copy(original)
print(f"befor changes:{original} copy{shallow}")

shallow[2][0] = 999
print(f"after changes:{original} copy{shallow}")

original = [1, 2, [100, 200]]
deep = copy.deepcopy(original)

print(f"befor changes:{original} copy{deep}")
deep[2][0] = 999
print(f"after changes:{original} copy{deep}")

class SmartList:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        new_data = self.value + other.value
        return SmartList(new_data)
    
    def __mul__(self, n):
        new_data = self.value * n
        return SmartList(new_data)
    
    def __delitem__(self, index):
        del self.value[index]

obj1 = SmartList([1, 2])
obj2 = SmartList([3, 4])

print("1. test add")
result_plus = obj1 + obj2
print(f"result: {result_plus}") 

print("\n2. test mul")
result_mul = obj1 * 3
print(f"result: {result_mul}") 

print("\n3. test del")
print(f"before del: {result_plus}")
del result_plus[0]
print(f"after del: {result_plus}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("age must be real number")
        if value < 0:
            raise ValueError("age cannot be minuse")
        
        self._age = value
    
    @age.deleter
    def age(self):
        del self._age

print("1. create human")
p = Person("Ivan", 20)
print(f"name: {p.name}, age: {p.age}")

print("\n2. change age")
p.age = 25  
print(f"new age: {p.age}")

print("\n3. try minuse")
try:
    p.age = -5  
except ValueError as e:
    print(f"catch error: {e}")

print("4. try string")
try:
    p.age = "twenty"
except ValueError as e:  
    print(f"error: {e}")
except TypeError as e:   
    print(f"error type: {e}")

print("\n5. delet age")
del p.age
try:
    print(p.age)
except AttributeError:
    print("age deleted (AttributeError)")