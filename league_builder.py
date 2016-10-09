"""A module which loads a .csv of soccer players, sorts them into teams according to their experience,
and generates a text file letter to their parents, informing them of their new team and the time/date
of their first practice.
"""

import csv


def main_function():

	exp_players = []
	new_players = []
	sharks = []
	dragons = []
	raptors = []
	teams = [sharks, dragons, raptors]

	# import the csv data into a list of dicts.
	with open("soccer_players.csv","r") as csvfile:
		player_reader = csv.DictReader(csvfile)
		for row in player_reader:
			new_player = {"name": row["Name"], "guardian": row["Guardian Name(s)"],
						  "experience": row["Soccer Experience"].lower(), "team": ""}
			if new_player["experience"] == "yes":
				exp_players.append(new_player)
			else:
				new_players.append(new_player)

	# divvy out the experienced players first
	for player in exp_players:
		if len(sharks) <= len(dragons) and len(sharks) <= len(raptors):
			player["team"] = "Sharks"
			sharks.append(player)
		elif len(dragons) <= len(sharks) and len(dragons) <= len(raptors):
			player["team"] = "Dragons"
			dragons.append(player)
		else:
			player["team"] = "Raptors"
			raptors.append(player)

	# Assign the remaining players randomly
	for player in new_players:
		if len(sharks) <= len(dragons) and len(sharks) <= len(raptors):
			player["team"] = "Sharks"
			sharks.append(player)
		elif len(dragons) <= len(sharks) and len(dragons) <= len(raptors):
			player["team"] = "Dragons"
			dragons.append(player)
		else:
			player["team"] = "Raptors"
			raptors.append(player)

	for team in teams:
		for player in team:
			write_letter(player["name"], player["team"], player["guardian"])


def write_letter(player, team, guardian):
	practice_date = ""
	if team.lower == "dragons":
		practice_date = "March 17, at 1pm"
	elif team.lower == "sharks":
		practice_date = "March 17, at 3pm"
	else:
		practice_date = "March 18, at 1pm"

	filename = player.replace(" ", "_").lower() + ".txt"

	with open(filename, "w") as file:
		file.write("Dear {},\n\n".format(guardian) +
				   "We are excited to tell you that {} has been ".format(player) +
				   "accepted into the {},  on the County Soccer League! ".format(team) +
				   "To participate in the league, your child will need the following:\n" +
				   "\t - Soccer Cleats\n" +
				   "\t - Shin Guards\n" +
				   "\t - A practice soccer ball (Standard size & weight)\n" +
				   "For assistance in obtaining these items, please call (555) 555-5555. " +
				   "Bring these items to your first practice, on {}. ".format(practice_date) +
				   "We look forward to seeing you there!")

	print("{} successfully created!".format(filename))


if __name__ == "__main__":
	main_function()
