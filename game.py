import random
from storySegment import StorySegment

class Game:
	def __init__(self):
		# Add the state and inventory attributes here
		self.state = {
			'worked': False,
			"lost_items": False,
			"injured": False,
			"help_failure": False,
			"escape_failure": False,
		}

		self.inventory = []

		# Add the story_segments (see storySegment.py)
		self.story_segments = {
			"start": StorySegment(
				# Add the description for the segment
				"Du wachst in einem unbekannten Wald auf. Du hast keine Erinnerung daran, wie du hierher gekommen bist. Vor dir sind zwei Wege: einer führt zu einem Dorf, der andere in die Tiefen des Waldes.",
				[
					# Add the choices for the segment
					# text = displayed text for each choice
					# next = key for the next segment
					# action = function to call for the choice
					{"text": "Zum Dorf gehen", "next": "village_entrance"},
					{"text": "In den Wald gehen", "next": "deep_forest"},
				]
			),
			"village_entrance": StorySegment(
				"Du erreichst das Dorf und siehst eine Menschenmenge. Sie scheinen aufgeregt. Was tust du?",
				[
					{"text": "Die Menschenmenge untersuchen", "next": "crowd"},
					{"text": "Weiter ins Dorf gehen", "next": "village_center"},
				]
			),
			"deep_forest": StorySegment(
				"Du gehst tiefer in den Wald hinein. Plötzlich hörst du ein seltsames Geräusch. Was tust du?",
				[
					{"text": "Das Geräusch untersuchen", "next": "strange_noise"},
					{"text": "In eine andere Richtung gehen", "next": "lost_forest"},
				]
			),
			"crowd": StorySegment(
				"Die Menschenmenge hat sich um einen verletzten Dorfbewohner versammelt. Was tust du?",
				[
					{"text": "Dem Verletzten helfen", "next": "help_injured"},
					{"text": "Ignorieren und weitergehen", "next": "village_center"},
				]
			),
			"village_center": StorySegment(
				"Im Zentrum des Dorfes siehst du einen Laden und ein Gasthaus. Wo gehst du hin?",
				[
					{"text": "Zum Laden gehen", "next": "shop"},
					{"text": "Zum Gasthaus gehen", "next": "inn"},
					{"text": "Das Dorf verlassen", "next": "deep_forest"},
				]
			),
			"strange_noise": StorySegment(
				"Du folgst dem Geräusch und entdeckst eine Gruppe von Banditen. Sie sehen dich und greifen an! Was tust du?",
				[
					{"text": "Kämpfen", "action": self.fight_bandits},
					{"text": "Weglaufen", "next": "running_away"},
				]
			),
			"running_away": StorySegment(
				"Du rennst so schnell du kannst, aber die Banditen sind schneller. Sie fangen dich und bringen dich zu ihrem Lager.",
				[
					{"text": "Einen Fluchtplan schmieden", "next": "escape_attempt"},
					{"text": "Auf Hilfe warten", "next": "rescue_attempt"},
				]
			),
			"help_injured": StorySegment(
				"Du hilfst dem Verletzten und gewinnst das Vertrauen der Dorfbewohner. Sie erzählen dir von einem geheimen Schatz im Wald. Was tust du?",
				[
					{"text": "Nach dem Schatz suchen", "next": "treasure_hunt"},
					{"text": "Im Dorf bleiben", "next": "village_center"},
				]
			),
			"shop": StorySegment(
				"Im Laden findest du nützliche Gegenstände. Da du kein Geld hast kannst du nichts kaufen.",
				[
					{"text": "Mit dem Ladenbesitzer reden", "next": "shop_owner"},
					{"text": "Den Laden verlassen", "next": "village_center"},
				]
			),
			"shop_owner": StorySegment(
				"Der Ladenbesitzer bietet dir einen job an, um Geld zu verdienen. Was tust du?",
				[
					{"text": "Den Job annehmen", "action": self.accept_job},
					{"text": "Den Job ablehnen", "next": "village_center"},
				]
			),
			"job_acceptance": StorySegment(
				"Du arbeitest im Laden und verdienst Geld für nützliche Gegenstände. Was kaufst du?",
				[
					{"text": "Heiltrank", "action": self.buy_healing_potion},
					{"text": "Karte des Waldes", "action": self.buy_map},
					{"text": "Den Laden verlassen", "next": "village_center"},
				]
			),
			"inn": StorySegment(
				"Im Gasthaus triffst du auf einen mysteriösen Fremden. Er bietet dir Informationen über den Wald an. Was tust du?",
				[
					{"text": "Mit dem Fremden sprechen", "next": "speak_stranger"},
					{"text": "Den Fremden ignorieren", "next": "village_center"},
				]
			),
			"lost_forest": StorySegment(
				"Du hast dich im Wald verlaufen. Du findest einen alten, verlassenen Turm. Was tust du?",
				[
					{"text": "Den Turm betreten", "next": "enter_tower"},
					{"text": "Den Turm ignorieren", "next": "wander_forest"},
				]
			),
			"enter_tower": StorySegment(
				"Du betrittst den Turm und ein mysteriöser Wächter erscheint. Er stellt dir drei Rätsel. Beantworte sie richtig, um weiterzukommen. Eine falsche Antwort führt zu einem Kampf.",
				[
					{"text": "Rätsel 1 beantworten", "next": "riddle_1"},
				]
			),
			"riddle_1": StorySegment(
				"Rätsel 1: Ich spreche ohne Mund und höre ohne Ohren. Ich habe keinen Körper, aber ich werde durch den Wind lebendig. Was bin ich?",
				[
					{"text": "", "action": self.riddle1},
				]
			),
			"riddle_2": StorySegment(
				"Rätsel 2: Ich werde immer größer, je mehr du wegnimmst. Was bin ich?",
				[
					{"text": "", "action": self.riddle2},
				]
			),
			"riddle_3": StorySegment(
				"Rätsel 3: Je mehr du nimmst, desto mehr lässt du zurück. Was bin ich?",
				[
					{"text": "", "action": self.riddle3},
				]
			),
			"treasure_room": StorySegment(
				"Du hast alle Rätsel richtig beantwortet! Der Wächter verschwindet und ein Schatz öffnet sich vor dir.",
				[
					{"text": "Schatz nehmen", "next": "end"},
				]
			),
			"treasure_hunt": StorySegment(
				"Du folgst den Hinweisen und entdeckst einen verborgenen Schatz. Plötzlich hörst du ein Knurren hinter dir.",
				[
					{"text": "Umdrehen und kämpfen", "next": "wolf_fight"},
					{"text": "Mit dem Schatz weglaufen", "next": "escape_treasure"},
				]
			),
			"speak_stranger": StorySegment(
				"Der Fremde erzählt dir, dass es einen versteckten Schatz im Wald gibt. Was tust du?",
				[
					{"text": "Dem Fremden glauben und in den Wald gehen", "next": "treasure_hunt"},
					{"text": "Den Fremden ignorieren", "next": "village_center"},
				]
			),
			"treasure_guardian": StorySegment(
				"Ein riesiger Wolf bewacht den Schatz. Was tust du?",
				[
					{"text": "Den Wolf bekämpfen", "next": "wolf_fight"},
					{"text": "Den Schatz zurücklassen", "next": "escape_woods"},
				]
			),
			"escape_treasure": StorySegment(
				"Du rennst mit dem Schatz weg, aber der Wolf verfolgt dich.",
				[
					{"text": "Den Wolf bekämpfen", "next": "wolf_fight"},
				]
			),
			"wolf_fight": StorySegment(
				"Du kämpfst gegen den riesigen Wolf.",
				[
					{"text": "Würfeln", "action": self.fight_wolf},
				]
			),
			"back_to_town": StorySegment(
				"Du kehrst zurück ins Dorf und befindet dich wieder am Anfang deiner Reise.",
				[
					{"text": "Zum Laden gehen", "next": "shop"},
					{"text": "Zum Gasthaus gehen", "next": "inn"},
					{"text": "Das Dorf verlassen", "next": "deep_forest"},
				]
			),
			"escape_plan": StorySegment(
				"Du schmiedest einen Fluchtplan und versuchst, aus dem Lager zu entkommen.",
				[
					{"text": "Die Flucht versuchen", "next": "escape_attempt"},
				]
			),
			"rescue_attempt": StorySegment(
				"Je nach deinem Würfelergebnis wirst du entweder gerettet oder musst weiter auf Hilfe warten.",
				[
					{"text": "Würfeln", "action": self.wait_help},
				]
			),
			"bandit_camp": StorySegment(
				"Du wirst zu einem Banditenlager gebracht und gefangen gehalten. Was tust du?",
				[
					{"text": "Einen Fluchtplan schmieden", "next": "escape_attempt"},
					{"text": "Auf Hilfe warten", "next": "rescue_attempt"},
				]
			),
			"escape_attempt": StorySegment(
				"Je nach deinem Würfelergebnis entkommst du oder wirst wieder eingefangen.",
				[
					{"text": "Würfeln", "action": self.escape_attempt},
				]
			),
			"forest_mastery": StorySegment(
				"Du beherrschst nun die Kräfte des Waldes und bist in der Lage, deine Reise mit neuen Fähigkeiten fortzusetzen.",
				[
					{"text": "Spiel beenden", "next": "end"},
				]
			),
			"secret_paths": StorySegment(
				"Die geheimen Pfade führen dich zu verborgenen Schätzen und uralten Geheimnissen.",
				[
					{"text": "Die Schätze erkunden", "next": "treasure_hunt"},
					{"text": "Die Geheimnisse enthüllen", "next": "ancient_secrets"},
				]
			),
			"boss_fight": StorySegment(
				"Du hast eine falsche Antwort gegeben und der Wächter greift dich an! Du musst strategisch kämpfen, um zu überleben.",
				[
					{"text": "Kampf beginnen", "action": self.fight_boss},
				]
			),
			"end": StorySegment(
				"Du hast das Spiel beendet. Du kehrst mit dem Schatz ins Dorf zurück und wirst als Held gefeiert.",
				[
					{"text": "Spiel beenden", "action" : self.end_game},
				]
			),
		}
	
	# Add the game functions here
	# each of these returns a key for the next segment, depending on outcome / choice / previous actions

	# fight functions
	def fight_boss(self):
		boss_defeated = False
		while boss_defeated == False:
			boss_hp = 100
			player_hp = 100
			while boss_hp > 0 and player_hp > 0:
				player_damage = random.randint(1, 25)
				boss_damage = random.randint(1, 15)
				boss_hp -= player_damage
				player_hp -= boss_damage
				print(f"Du greifst den Wächter an und verursachst {player_damage} Schaden. Der Wächter hat noch {boss_hp} HP.")
				print(f"Der Wächter greift dich an und verursacht {boss_damage} Schaden. Du hast noch {player_hp} HP.")
			if boss_hp <= 0:
				boss_defeated = True
				print("Du hast den Wächter besiegt und kannst deine Reise fortsetzen.")
				return "treasure_room"
			else:
				print("Du wurdest vom Wächter besiegt. Deine Reise endet hier.")
				return "end"

	def fight_bandits(self):
		roll = random.randint(1, 20)
		if roll <= 10:
			self.state["lost_items"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest von den Banditen besiegt und hast einige Gegenstände verloren.")
			self.lose_items()
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Nach einem schweren Kampf besiegst du die Banditen und setzt deine Reise fort.")
			return "lost_forest"
		
	def fight_wolf(self):
		if self.state["injured"] == True:
			if self.check_inventory("Heiltrank") == True:
				self.remove_from_inventory("Heiltrank")
				self.state["injured"] = False
				print ("Du hast einen Heiltrank benutzt, der deine Verletzungen geheilt hat.")
			else:
				print ("Du bist verletzt und kannst nicht kämpfen.")
				return "lost_forest"
		roll = random.randint(1, 20)
		if roll <= 10:
			self.state["injured"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest vom Wolf verletzt und fliehst zurück ins dorf.")
			return "back_to_town"
		elif roll <= 20:
			print(f"Du hast eine {roll} gewürfelt. Nach einem schweren Kampf besiegst du den Wolf und setzt deine Reise fort.")
			return "lost_forest"
		
	# other functions

	def buy_healing_potion(self):
		self.add_to_inventory("Heiltrank")
		return "village_center"
	
	def buy_map(self):
		self.add_to_inventory("Karte des Waldes")
		return "village_center"
	
	def wait_help(self):
		roll = random.randint(1, 20)
		if roll <= 5:
			self.state["help_failure"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest nicht gerettet.")
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Du wurdest gerettet und kannst deine Reise fortsetzen.")
			return "lost_forest"

	def escape_attempt(self):
		roll = random.randint(1, 20)
		if roll <= 5:
			self.state["escape_failure"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest wieder eingefangen.")
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Du bist erfolgreich entkommen und kannst deine Reise fortsetzen.")
			return "lost_forest"
	
	def accept_job(self):
		if self.state["worked"] == False:
			self.state["worked"] = True
			return "job_acceptance"
		else:
			print ("Du hast bereits im Laden gearbeitet, tu etwas anderes!.")
			return "shop"

	def riddle1(self):
		answer = input("Antwort: ")
		if answer.lower() == "echo" or answer.lower() == "hall":
			print("Richtig! Hier ist das nächste Rätsel.")
			return "riddle_2"
		else:
			print("Falsch! Du musst kämpfen.")
			return "boss_fight"
		
	def riddle2(self):
		answer = input("Antwort: ")
		if answer.lower() == "loch":
			print("Richtig! Hier ist das letzte Rätsel.")
			return "riddle_3"
		else:
			print("Falsch! Du musst kämpfen.")
			return "boss_fight"
	
	def riddle3(self):
		answer = input("Antwort: ")
		if answer.lower() == "fußspuren" or answer.lower() == "fußabdrücke":
			print("Richtig! Du hast alle Rätsel gelöst.")
			return "treasure_room"
		else:
			print("Falsch! Du musst kämpfen.")
			return "boss_fight"

	# helper functions for the inventory

	def check_inventory(self, item_str):
		if item_str in self.inventory:
			return True
		else:
			return False
		
	def add_to_inventory (self, item):
		self.inventory.append(item)
		print(f"Du hast {item} gefunden und deinem Inventar hinzugefügt.")
		print (f"Inventar: {self.inventory}")

	def remove_from_inventory (self, item):
		self.inventory.remove(item)
		print(f"Du hast {item} verloren.")
	
	def lose_items(self):
		if self.state["lost_items"] == True:
			if len(self.inventory) > 0:
				for i in range(2):
					random_item = random.choice(self.inventory)
					self.remove_from_inventory(random_item)
			else:
				print ("Du hast keine Gegenstände zu verlieren.")
		print (f"Inventar: {self.inventory}")

	# end game function to not get error in while loop of play function

	def end_game(self):
		exit()

	# main play function / game loop
	# this is where the game starts and the player progresses through the story segments

	def play(self):
		current_segment = self.story_segments["start"]
		while True:
			current_segment.display()
			if not current_segment.choices:
				break
			choice = current_segment.get_choice()
			if "next" in choice:
				next_segment_key = choice["next"]
			elif "action" in choice:
				next_segment_key = choice["action"]()

			current_segment = self.story_segments[next_segment_key]

if __name__ == "__main__":
	# Create an instance of the Game class and start the game
	game = Game()
	game.play()