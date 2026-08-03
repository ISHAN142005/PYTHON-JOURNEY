print("--- 1. Variable Assignment & Data Types ---")

base_score = 50
bonus_multiplier = 1.5
is_active = True

print("Base Score (int):", base_score)
print("Bonus Multiplier (float):", bonus_multiplier)

print("\n--- 2. User Inputs & Type Conversion ---")

user_input1 = input("Enter a whole number: ")
user_input2 = input("Enter a decimal number: ")

num_a = int(user_input1)
num_b = float(user_input2)
print("You entered:", num_a, "and", num_b)

print("\n--- 3. Math Operations & Type Coercion ---")

addition_result = num_a + num_b
print(f"Addition Result ({num_a} + {num_b}) = {addition_result}")
print("Notice the result type is:", type(addition_result))

print("\n--- 4. Operator Precedence & Associativity ---")

math_expression = num_a + num_b * 10 - 4 / 2

print(f"Expression: {num_a} + {num_b} * 10 - 4 / 2")
print("Result of expression:", math_expression)
print(
    "Explanation: Python multiplied and divided first, then added and subtracted from left to right."
)
