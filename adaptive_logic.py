import math

def probability_correct(ability, difficulty):
    return 1 / (1 + math.exp(-(ability - difficulty)))


def update_ability(ability, difficulty, correct):

    predicted = probability_correct(ability, difficulty)

    learning_rate = 0.1
    result = 1 if correct else 0

    new_ability = ability + learning_rate * (result - predicted)

    return max(0.1, min(1.0, new_ability))