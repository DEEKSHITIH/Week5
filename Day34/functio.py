# Define the calculate_area function
def calculate_area(length, width):
    return length * width


rectangle_length = 3
rectangle_width = 5
rectangle_area = calculate_area(rectangle_length, rectangle_width)
print(f"Rectangle Area: {rectangle_area} ")


myinfo = {
    "name": "DEEKSHITH",
    "age": 19,
    "location": "HYDERABAD"
}

# Define the print_person_info function
def print_myinfo_info(myinfo_dict):
    print(f"Name: {myinfo_dict['name']}")
    print(f"Age: {myinfo_dict['age']} years")
    print(f"location: {myinfo_dict['location']}")

# Print the person's information
print("\n MY Information:")
print_myinfo_info(myinfo)
