students = {
    "Name": ["Alice", "Jwanil"],
    "Roll No": [101, 102],
    "Age": [19, 20],
    "Grade": ["A", "B+"]
}

# Find how many items we have (assuming all lists are the same length)
num_items = len(students["Name"])

print(f"{'Name':<7} | {'Roll No:':<10} | {'Age:':<6} | {'Grade:'}")

for i in range(num_items):
    # Access the i-th item from each list
    name = students["Name"][i]
    roll = students["Roll No"][i]
    age = students["Age"][i]
    grade = students["Grade"][i]
    
    print(f"{name:<7} | {roll:<10} | {age:<6} | {grade}")
