class Superhero:
    def __init__(self, name, secret_identity, power, weakness, catchphrase):
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.weakness = weakness
        self.catchphrase = catchphrase
        self.is_flying = False

    def reveal_identity(self):
        print(f"By day, I am {self.secret_identity}...")

    def use_power(self):
        print(f"{self.name} uses their amazing power of {self.power}!")

    def taunt_villain(self):
        print(f'"{self.catchphrase}!" shouts {self.name}.')

    def fly(self):
        if "flight" in self.power.lower():
            self.is_flying = True
            print(f"{self.name} soars through the sky!")
        else:
            print(f"{self.name} can't fly... sadly.")

    def land(self):
        if self.is_flying:
            self.is_flying = False
            print(f"{self.name} gently lands.")
        else:
            print(f"{self.name} is already on the ground.")

    def describe(self):
        print(f"Meet {self.name}, secretly known as {self.secret_identity}! "
              f"Their incredible power is {self.power}, but they are vulnerable to {self.weakness}. "
              f"You'll often hear them exclaim, '{self.catchphrase}'.")

# Creating instances of the Superhero class
superman = Superhero("Superman", "Clark Kent", "Flight, Super Strength, Heat Vision", "Kryptonite", "Truth, Justice, and the American Way!")
wonder_woman = Superhero("Wonder Woman", "Diana Prince", "Super Strength, Speed, Lasso of Truth", "Piercing Weapons", "For Justice!")

superman.describe()
wonder_woman.use_power()
superman.fly()
wonder_woman.taunt_villain()
superman.land()