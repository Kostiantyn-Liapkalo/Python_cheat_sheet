# The get_random_winners(quantity, participants) function returns a list of unique database identifiers from the participants dictionary in quantity. This is the list of winners!


import random


def get_random_winners(quantity, participants):
    if quantity > len(participants):
        return []
    users = []
    for win in participants.keys():
        users.append(win)
    random.shuffle(users)

    winners = random.sample(users, k=quantity)
    return winners


if __name__ == "__main__":

    participants = {
        "603d2cec9993c627f0982404": "test@test.com",
        "603f79022922882d30dd7bb6": "test11@test.com",
        "60577ce4b536f8259cc225d2": "test2@test.com",
        "605884760742316c07eae603": "vitanlhouse@gmail.com",
        "605b89080c318d66862db390": "elhe2013@gmail.com",
    }
    print(get_random_winners(2, participants))
