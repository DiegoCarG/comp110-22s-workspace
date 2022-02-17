"""An example of for in syntax."""

names: list[str] = ["Diego", "Adam", "Max", "Adrian"]

# Example of iterating through names using a while loop
i:int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1 

# The following for..in is the same as the while loop above
for name in names:
    print(name)

for x in [1, 2, 3]:
    print(x)