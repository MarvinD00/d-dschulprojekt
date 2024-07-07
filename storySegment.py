import random

class StorySegment:
	# each story segment consists of a description and a list of choices
	def __init__(self, description, choices):
		self.description = description
		self.choices = choices

	# display the description and choices
	def display(self):
		print(self.description)
		for index, choice in enumerate(self.choices, 1):
			print(f"{index}. {choice['text']}")

	# get the choice from the user
	# if the input is invalid, ask the user to try again
	# return the choice
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