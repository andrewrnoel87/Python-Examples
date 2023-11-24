def counter(start):
    count = start
    def increment(value):
        nonlocal count
        count += value
        return count
    return increment
count = counter(2)
print(count(1))

class Counter:
    def __init__(self, start):
        self.count = start
    def count_increment(self, value):
        self.count += value
        return self.count

count = Counter(2)
print(count.count_increment(1))
