class Player:
    def __init__(self, name, tier, gender):
        self.name = name
        self.tier = int(tier)
        self.gender = gender

    def __repr__(self):
        return f"Player(name='{self.name}', tier='{self.tier}', gender='{self.gender}')"
