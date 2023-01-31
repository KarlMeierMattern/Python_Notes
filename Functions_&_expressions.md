If, elif, else

if: condition
	print()
elif: condition
	print()
else:
	print()


While loops
While loop creates a repeated if statement.
Repeats an action until a condition is met.

while condition:
	expression

For loops
For each variable in a sequence execute an expression.
I.e. can iterate through a list or an array.

for var in seq:
	expression

To control how many times the for loop iterates use the range() function:
for x in range(10):
	expression


Task 2
# List of characters to remove
chars_to_remove = ['+',",","$"]
# List of column names to clean
cols_to_clean = ["Installs","Price"]

# Loop for each column in cols_to_clean
for col in cols_to_clean:
    # Loop for each char in chars_to_remove
    for char in chars_to_remove:   
        # Replace the character with an empty string
        apps[col] = apps[col].apply(lambda x: x.replace(char, ''))


### Functions

max() is a function as you can call it on a list

fam = [4,6,10,3,9]
I.e. max(fam)

round(number, decimal places) 
By default it rounds to zero decimal places

len() - can call on a string or list (will count number of elements in the list)