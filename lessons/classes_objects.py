"""Example of a class and object instatiation."""


class Pizza:
    """Models the idea of a Pizza."""

    def __init__(self, size: str, toppings: int, extra_cheese: bool):
        """Constructor definition for intialization of attributes"""
        self.size = size
        self.toppings = toppings
        self.extra_cheese = extra_cheese



    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        if self.extra_cheese:
            total += 0

        total *= tax

        return total
    

    def __str__(self) -> str:
        """Produce a str representation of a point for humans."""
        return f"({self.size}, {self.toppings}, {self.extra_cheese})"

    def __repr__(self) -> str:
        """Produce a str representation of a Point for Python!"""
        return f"Point({self.size}, {self.toppings}"



a_pizza: Pizza = Pizza("large", 3, False)
print(Pizza)
print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")

another.pizza: Pizza = Pizza("small", 0, False)
another_pizza.extra_cheese = true
print(a_pizza.size)