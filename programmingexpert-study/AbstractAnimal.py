class AbstractAnimal:

    def sleep(self):
        print("ZzzZzz")
    
    def animal_sound(self):
        raise NotImplementedError("You must provide an implementation for animal_sound()")
    
    def wake_up(self):
        self.animal_sound()
        print("I am awake!")

class Lion(AbstractAnimal):

    def animal_sound(self):
        print ("Roar!")

leo = Lion()
leo.sleep()
leo.wake_up()

