"""Examples of row and column data"""

__author__ = "730427471"

row_data: list[dict[str, str]] = [
    {"name": "UNC", "city": "Chapel Hill"},
    {"name": "Duke", "city": "Durham"}
]

col_data: dict[str, list[str]] = {
    "name": ["UNC", "Duke"],
    "city": ["Chapel Hill", "Durham"]
}

print(row_data[1]["city"])
print(col_data["city"][1])
print(row_data[1])