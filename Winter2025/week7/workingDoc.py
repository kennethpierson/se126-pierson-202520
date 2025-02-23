# Create a 2D list (plane seating arrangement)
seats = [
    ['A', 'B', 'C', 'D'],  # Row 1
    ['A', 'B', 'C', 'D'],  # Row 2
    ['A', 'B', 'C', 'D'],  # Row 3
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D'],
    ['A', 'B', 'C', 'D']
    # Add more rows as needed
]

# Create a dictionary to keep track of seat availability
# True means seat is taken, False means seat is available
seat_availability = {}

# Initialize all seats as available
for row in range(len(seats)):
    for col in range(len(seats[row])):
        seat_availability[(row, col)] = False  # False means the seat is available

# Function to print the seat map
def print_seats():
    for row in range(len(seats)):
        print(f"Row {row + 1}: ", end="")
        for col in range(len(seats[row])):
            seat_status = "X" if seat_availability[(row, col)] else 'O'  # 'X' for taken, 'O' for available
            print(seat_status, end=" ")
        print()

# Function to ask the user for seat input
def select_seat():
    seat_selected = False  # Flag to track if a valid seat was selected

    while not seat_selected:
        print_seats()  # Display available seats
        row = int(input("Enter row number: ")) - 1  # Subtract 1 to match index
        col = input("Enter seat (A-F): ").upper()

        # Convert seat column letter to column index
        col_index = {'A': 0, 'B': 1, 'C': 2, 'D': 3}.get(col, -1)

        if col_index == -1 or row < 0 or row >= len(seats) or seat_availability[(row, col_index)]:
            print("Invalid seat or seat already taken. Please choose another one.")
        else:
            seat_availability[(row, col_index)] = True  # Mark the seat as taken
            print(f"You have selected row {row + 1} seat {col}.")
            seat_selected = True  # Exit the loop once a valid seat is selected

# Main loop
continue_selecting = True
while continue_selecting:
    select_seat()
    again = input("Do you want to select another seat? (y/n): ").lower()
    if again != 'y':
        continue_selecting = False
