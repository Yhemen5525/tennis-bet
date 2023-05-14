import itertools

# function to calculate total odds for a bet
def calculate_total_odds(bet):
    total_odds = 1
    for odds in bet.values():
        total_odds *= odds
    return total_odds

# function to generate all possible bets given a list of matches and their odds
def generate_possible_bets(matches):
    possible_bets = []
    for bet_combination in itertools.product(*matches):
        bet = {}
        for match in bet_combination:
            player_name, odds = match.split(" (")
            player_name = player_name.strip()
            odds = float(odds[:-1])
            bet[player_name] = odds
        possible_bets.append(bet)
    return possible_bets

# sample data
matches = [
    ["Player A (1.24)", "Player B (3.40)"],
    ["Player C (1.93)", "Player D (1.91)"],
    ["Player E (1.50)", "Player F (2.75)"],
     ["Player w (1.70)", "Player F (3.75)"]
]



# generate all possible bets
possible_bets = generate_possible_bets(matches)

# calculate total odds for each possible bet
for bet in possible_bets:
    total_odds = calculate_total_odds(bet)
    print(bet, "Total Odds:", round(total_odds, 3))
