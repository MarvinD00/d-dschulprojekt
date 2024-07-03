import random
from storySegment import StorySegment

class Game:
	def __init__(self):
		self.state = {
			"path_blocked": False,
			"lost_items": False,
			"injured": False,
			"entered_at_night": False,
			"help_failure": False,
			"escape_failure": False,
		}

		self.story_segments = {
			"start": StorySegment(
				"Du wachst in einem unbekannten Wald auf. Du hast keine Erinnerung daran, wie du hierher gekommen bist. Vor dir sind zwei Wege: einer führt zu einem Dorf, der andere in die Tiefen des Waldes.",
				[
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
					{"text": "Weglaufen", "next": "running_away"},
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
				"Du versuchst wegzulaufen, aber der Weg ist blockiert. Du musst dich entscheiden, wohin du gehst.",
				[
					{"text": "Zurück zum Startpunkt", "next": "start"},
					{"text": "In eine andere Richtung rennen", "next": "lost_forest"},
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
			"treasure_hunt": StorySegment(
				"Du folgst den Hinweisen und entdeckst einen verborgenen Schatz. Plötzlich hörst du ein Knurren hinter dir.",
				[
					{"text": "Umdrehen und kämpfen", "next": "treasure_guardian"},
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
			"enter_tower": StorySegment(
				"Im Turm findest du alte Schriftrollen und magische Artefakte. Plötzlich beginnt der Turm zu zittern.",
				[
					{"text": "Die Artefakte untersuchen", "next": "artifact_inspection"},
					{"text": "Den Turm verlassen", "next": "wander_forest"},
				]
			),
			"wander_forest": StorySegment(
				"Du wanderst weiter durch den Wald und findest schließlich den Weg zurück zum Startpunkt.",
				[
					{"text": "Zurück zum Startpunkt", "next": "start"},
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
			"artifact_inspection": StorySegment(
				"Die verborgene Macht in den Artefakten gibt dir unglaubliche Fähigkeiten. Was tust du?",
				[
					{"text": "Die Macht nutzen", "next": "forest_mastery"},
					{"text": "Die Macht zurücklassen", "next": "wander_forest"},
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
			"use_power": StorySegment(
				"Die verborgene Macht in den Artefakten gibt dir unglaubliche Fähigkeiten. Was tust du?",
				[
					{"text": "Die Macht nutzen", "next": "forest_mastery"},
					{"text": "Die Macht zurücklassen", "next": "wander_forest"},
				]
			),
			"back_to_town": StorySegment(
				"Du kehrst zurück ins Dorf und wirst von den Dorfbewohnern versorgt. Deine Reise endet hier.",
				[]
			),
			"speak_spirits": StorySegment(
				"Die Geister des Waldes offenbaren dir geheime Pfade und versteckte Schätze. Was tust du?",
				[
					{"text": "Den Pfaden folgen", "next": "secret_paths"},
					{"text": "Im Dorf bleiben", "next": "village_center"},
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
			"ancient_secrets": StorySegment(
				"Du enthüllst die uralten Geheimnisse des Waldes und erhältst Wissen und Macht, die dir auf deiner Reise helfen werden.",
				[
					{"text": "Spiel beenden", "next": "end"},
				]
			),
			"end": StorySegment(
				"Deine Reise endet hier. Vielen Dank fürs Spielen!",
				[]
			),
		}
	

	def enter_at_night(self):
		self.state["entered_at_night"] = True

	def fight_bandits(self):
		roll = random.randint(1, 20)
		if roll <= 10:
			self.state["lost_items"] = True
			print (self.state["lost_items"])
			print(f"Du hast eine {roll} gewürfelt. Du wurdest von den Banditen besiegt und hast einige Gegenstände verloren.")
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Nach einem schweren Kampf besiegst du die Banditen und setzt deine Reise fort.")
			return "lost_forest"
		
	def fight_wolf(self):
		roll = random.randint(1, 20)
		if roll <= 10:
			self.state["injured"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest vom Wolf verletzt und fliehst.")
			return "wolf_fight_outcome"
		elif roll <= 20:
			print(f"Du hast eine {roll} gewürfelt. Nach einem schweren Kampf besiegst du den Wolf und setzt deine Reise fort.")
			return "lost_forest"
		
	def wait_help(self):
		roll = random.randint(1, 20)
		if roll <= 5:
			self.state["help_failure"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest nicht gerettet und hast einige Gegenstände verloren.")
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Du wurdest gerettet und kannst deine Reise fortsetzen.")
			return "lost_forest"

	def escape_attempt(self):
		roll = random.randint(1, 20)
		if roll <= 5:
			self.state["escape_failure"] = True
			print(f"Du hast eine {roll} gewürfelt. Du wurdest wieder eingefangen und hast einige Gegenstände verloren.")
			return "bandit_camp"
		else:
			print(f"Du hast eine {roll} gewürfelt. Du bist erfolgreich entkommen und kannst deine Reise fortsetzen.")
			return "lost_forest"
		
	def play(self):
		current_segment = self.story_segments["start"]
		while True:
			current_segment.display()
			if not current_segment.choices:
				break
			choice = current_segment.get_choice()
			if "action" in choice:
				next_segment_key = choice["action"]()
			else:
				next_segment_key = choice["next"]
			current_segment = self.story_segments[next_segment_key]

if __name__ == "__main__":	
	game = Game()
	game.play()