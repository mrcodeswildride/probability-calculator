print()

favorable_outcomes = int(input("How many favorable outcomes? "))
possible_outcomes = int(input("How many possible outcomes? "))

decimal = favorable_outcomes / possible_outcomes
percent = decimal * 100

print(f"\nThe probability is {percent:.2f}%.")
