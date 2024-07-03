import openai
from openai import OpenAI

messages=[
	{
		"role": "system",
		"content": "You are the narrator of a story, the user will be the player. You can start by describing the setting and the player's role in the story. The player will be able to make choices and you will respond to them. You can type 'end' to finish the story.",
	}
]
chat = client.chat.completions.create(
	messages=messages,
	model="gpt-3.5-turbo",
)

start = chat.choices[0].message.content
print(f"Narrator: {start}")
messages.append({"role": "assistant", "content": start})

while True:
	print("\n")
	message = input("You : ")
	if message:
		messages.append(
			{"role": "user", "content": message},
		)
	chat = client.chat.completions.create(
		messages=messages,
		model="gpt-3.5-turbo",
	)
	reply = chat.choices[0].message.content
	print(f"Narrator: {reply}")
	messages.append({"role": "assistant", "content": reply})
