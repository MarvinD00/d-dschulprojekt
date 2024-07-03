import random

class StorySegment:
	def __init__(self, description, choices):
		self.description = description
		self.choices = choices

	def display(self):
		print(self.description)
		for index, choice in enumerate(self.choices, 1):
			print(f"{index}. {choice['text']}")

	def get_choice(self):
		choice = input("Choose an option: ")
		try:
			choice_index = int(choice) - 1
			if 0 <= choice_index < len(self.choices):
				return self.choices[choice_index]
			else:
				print("Invalid choice. Try again.")
				return self.get_choice()
		except ValueError:
			print("Invalid input. Enter a number.")
			return self.get_choice()