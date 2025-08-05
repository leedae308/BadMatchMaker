class Court:
    def __init__(self, court_id):
        self.court_id = court_id
        self.players = []
        self.f_isFull = False

    def add_player(self, player):
        if not self.f_isFull:
            self.players.append(player)

            if len(self.players) >= 4:
                self.f_isFull = True
        else:
            raise Exception(f"Court {self.court_id} is full.")

    def __repr__(self):
        return f"Court {self.court_id}: {self.players}"
