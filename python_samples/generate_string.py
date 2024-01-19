def generate_string(string, frequency):
    current = 0
    while current < len(string):
        yield string[current] * frequency
        current += 1


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string
        self.frequency = frequency

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        self.current += 1
        if self.current - 1 < len(self.string):  #  -1 is used to correct the index
            return self.string[self.current - 1] * self.frequency
        else:
            raise StopIteration


string = 'hello'
frequency = 10
gen = "".join(list(generate_string(string, frequency)))
gen2 = "".join(list(GenerateString(string, frequency)))

print(gen)
print(gen2)