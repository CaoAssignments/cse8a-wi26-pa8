# CSE 8A PA8 Lab

March 10, 2026

---

## Introduction

Welcome to your PA8 Lab!

Today you will learn about working with **dictionaries** in Python and how to use them to process **CSV files**. Dictionaries are a powerful data structure that allow you to store and retrieve values based on specific keys, rather than numerical indexes. By the end of this lab, you should feel comfortable using dictionaries to solve problems and manipulating real-world data represented as CSVs.

---

## Learning Goals

By the end of this lab, you will be able to:

- Create, access, and modify dictionaries in Python.
- Safely handle missing keys using the `in` keyword.
- Understand how CSV files are represented as lists of dictionaries in Python.
- Write functions to extract, filter, and aggregate data from CSV-like structures.

---

## Part 1: Python Dictionaries (The Basics)

### What Are Dictionaries?

Unlike lists, which use numerical indexes (0, 1, 2...), dictionaries use **keys** to look up **values**. You can think of it like a real-world dictionary: you look up a word (the key) to find its definition (the value).


Here is a code example showing the most common ways you will use a dictionary:

```python
# 1. Creation: Use curly braces {} with key: value pairs
student = {"name": "Alice", "age": 19, "major": "Computer Science"}
empty_dict = {}

# 2. Access: Use square brackets [] and the key
print(student["name"])    # 'Alice'

# 3. Modification & Addition: Assign a value to a key
student["age"] = 20               # Updates an existing key
student["college"] = "Sixth"      # Adds a completely new key

# 4. Check: Safely check if a key exists using the 'in' keyword
if "GPA" in student:
    print(student["GPA"])
else:
    print("GPA not found!")       # This will print, since "GPA" is not a key
```

### Avoiding the `KeyError`

If you try to access or modify a key that does not exist, your program will crash with a KeyError. Always use the in keyword to check or initialize keys before modifying them:

```python
counts = {}
print(counts["apple"])  # This will raise a KeyError since "apple" is not yet a key in the dictionary

item = "apple"
# Correct Initialization Pattern:
if item not in counts:
    counts[item] = 0     # Create the key first if it's missing!

counts[item] += 1        # Now it is safe to add to it
```

### Practice using dictionaries!

In your pa8_lab.py file, write a function that updates a store's inventory: `def update_inventory(inventory, item_name, quantity)`. The function takes in an `inventory` dictionary, an `item_name` string, and a `quantity` integer. The function should update the inventory as follows:
- If the `item_name` is already in the `inventory` dictionary, add the `quantity` to its current value.
- If the `item_name` is NOT in the dictionary, add it as a new key with the `quantity` as its value.

```python
def update_inventory(inventory, item_name, quantity):
    ... #TODO: implement this function

```

Examples:
```python
my_store = {"apple": 5, "banana": 2}

update_inventory(my_store, "apple", 3)
print(my_store)   # {'apple': 8, 'banana': 2}

update_inventory(my_store, "orange", 10)
print(my_store)   # {'apple': 8, 'banana': 2, 'orange': 10}

```

## Part 2: Working with CSV Files

CSV (Comma Separated Values) is a very common format for storing tabular data (like spreadsheets). Consider the following CSV file:

```csv
Name,Role,Age
Alice,Student,19
Bob,Tutor,22
Charlie,Student,20
```

In this CSV, the first line is the header that defines the column names. Each column represents a different attribute of the data (Name, Role, Age), and each subsequent line represents a different record.

To process CSV files in Python, a common way is to represent them as a list of dictionaries, where each dictionary corresponds to a row in the CSV, and the keys of the dictionary are the column names from the header. For example, using the `load_csv` function provided in the `CSE8ACSV.py` file, the above CSV would be represented as:

```python
csv_data = load_csv('example.csv')
print(csv_data)
# Output:
# [{'Name': 'Alice', 'Role': 'Student', 'Age': '19'}, {'Name': 'Bob', 'Role': 'Tutor', 'Age': '22'}, {'Name': 'Charlie', 'Role': 'Student', 'Age': '20'}]
```

To process this data, we use a for loop to look at each row (which is a dictionary) one by one:

```python
for row in csv_data:
    name = row['Name']   # Access the 'Name' column for this row
    role = row['Role']   # Access the 'Role' column for this row
    age = int(row['Age']) # Access the 'Age' column and convert it to an integer
    print(f"{name} is a {role} and is {age} years old.")
```

### Practice processing CSV data!
Download the `tech_diversity.csv` file and put it in the same directory as your `pa8_lab.py` file. This CSV contains data about the diversity of employees at various tech companies. Some of the columns include `'Company'`, `'white'`, `'asian'`, `'hispanic'`, `'black'`, and `'total_female'`. Keep in mind that all values (except the company name) are represented as strings in the CSV file!

In your `pa8_lab.py` file, write a function `get_companies_above_threshold(diversity_data, demographic_key, threshold)` that takes in the dataset (a list of dictionaries), a demographic string (like `'total_female'`), and a threshold float (like `50.0`). The function should return a **list of company names** that have a percentage strictly greater than the given threshold for that demographic.

- **Hint:** Initialize an empty list `[]`. Loop through each row in `diversity_data`. Access the specific demographic value using `row[demographic_key]`, convert it to a `float`, and if it's strictly greater than the `threshold`, append the `'Company'` value to your list.

```python
def get_companies_above_threshold(diversity_data, demographic_key, threshold):
    ... #TODO: implement this function
```

Examples:

```python
tech_data = load_csv("tech_diversity.csv")

print(get_companies_above_threshold(tech_data, "total_female", 50.0))
# ['23andMe']

print(get_companies_above_threshold(tech_data, "black", 7.0))
# ['View', 'HPE', 'PayPal', 'Apple']
```


## Part 3: Lab Quiz (~15 minutes)

Make sure to review the lab activity today! The lab quiz will test material based on what you learned in this lab.
