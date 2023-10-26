def change_money(player_money,amount):
	"""Increases the players money by 1
	
	Parameters
	----------
	player_money:int
		current money of player
	amount: int
		amount to change money by, can be
		positive or negative

	Returns
	-------
	Money changed by amount
	"""
	player_money += amount
	return player_money

def more_money(player_money):
	"""Increases the players money by 1
	
	Parameters
	----------
	player_money:int
		current money of player

	Returns
	-------
	Money increased by 1
	"""
	player_money = player_money + 1
	return player_money


####Main Code####

current_money = 100
print(current_money)
current_money = more_money(current_money)
print(current_money)

current_money = 100
print(current_money)
current_money = change_money(current_money,-20)
print(current_money)
