class Group:
    def __init__(self, name, members=[]):
        self.name = name
        self.members = members

    def add(self, name):
        self.members.append(name)

    def delete(self, name):
        if name in self.members:
            self.members.remove(name)
        else:
            raise Exception("Member not in group.")

    def get_members(self):
        return sorted(self.members)

    def merge(self, group):
        merged_members = self.members + group.members
        merged_group = Group(self.name + '&' + group.name, merged_members)
        return merged_group
    
g1 = Group('A-Team', ['Tim', 'Joe'])
g2 = Group("tunnelbees", ['a', 'b', 'c'])
g1.add('Sally')
g1.add('Billy')
members = g1.get_members()
print(members)
g1.delete('Joe')
members = g1.get_members()
print(members)
g3 = g1.merge(g2)
print(g3.name)
print(g3.get_members())
#g1.delete('Joe')