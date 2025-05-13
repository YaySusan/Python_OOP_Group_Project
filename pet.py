class Pet: # Create the pet class
    def __init__(self, name): # Initialize the instance
        self.name = "Waffles" # Stored the pet's name to call upon later
        self.hunger = 5 # The pet's starting hunger level is 5, middle point between 0 and 10
        self.energy = 5 # The pet's starting energy level is 5, middle point between 0 and 10
        self.happiness = 5 # The pet's starting energy level is 5, middle point between 0 and 10
        self.tricks = []         # list to store tricks learned


    def eat(self): # Method which reduces the pet's hunger by 3 points and increases its happiness by 1 point if fed food
        self.hunger = max(0, self.hunger - 3) # When the pet is fed, its hunger level decreases by 3 points
        self.happiness = min(10, self.happiness +1) # When the pet is fed, its happiness level increases by 1 point.


    def sleep(self):
        self.energy = min(self.energy + 5, 10)

    def play(self):
        self.energy = max(self.energy - 2, 0)
        self.happiness = min(self.happiness + 2, 10)
        self.hunger = min(self.hunger + 1, 10)

    def get_status(self):
        print(f"Pet: {self.name}")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        if self.tricks:
            print(f"Tricks learned: {', '.join(self.tricks)}")
        else:
            print("No tricks learned yet.")

    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows the trick: {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
