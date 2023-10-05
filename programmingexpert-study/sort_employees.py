def sort_employees(employees, sort_by):

    def sort_by_index_zero(iterable):
        return iterable[0]

    def sort_by_index_one(iterable):
        return iterable[1]

    def sort_by_index_two(iterable):
        return iterable[2]
    
    if sort_by == "name":
        return sorted(employees, key=sort_by_index_zero)
    
    if sort_by == "age":
        return sorted(employees, key=sort_by_index_one)
    
    if sort_by == "salary":
        return sorted(employees, key=sort_by_index_two)
        



