class Pet: # Create the pet class
    def __init__(self, name): # Initialize the instance
        self.name = "Waffles" # Stored the pet's name to call upon later
        self.hunger = 5 # The pet's starting hunger level is 5, middle point between 0 and 10
        self.energy = 5 # The pet's starting energy level is 5, middle point between 0 and 10
        self.happiness = 5 # The pet's starting energy level is 5, middle point between 0 and 10

    def eat(self): # Method which reduces the pet's hunger by 3 points and increases its happiness by 1 point if fed food
        self.hunger = max(0, self.hunger - 3) # When the pet is fed, its hunger level decreases by 3 points
        self.happiness = min(10, self.happiness +1) # When the pet is fed, its happiness level increases by 1 point.
        print(f"{self.name} ate some food. The pet is less hungry and is happier. Yay!") # Prints out a message telling the user that the pet has been fed

