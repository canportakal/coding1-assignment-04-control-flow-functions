def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: The output is 3, then 4. The loop sets number to 1, 2, 3 in turn.
# The if condition is not True for 1, so that iteration is skipped. For 2 and 3 the condition is True, so
# add_one(2) and add_one(3) are called, giving 3 and 4, which uv run python assignment.py displays.

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add_one(2) returns 3. return sends a value back to the code that
# called the function, so it can be stored or used, and it ends the function.
# It shows nothing on screen. print only displays a value in the console and
# gives nothing back for further use. In the loop, add_one returns the number
# and print displays it. Without print, nothing would appear.
