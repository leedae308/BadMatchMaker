#structure/matchmaker.py

from structure.player import Player
from structure.court import Court
import random

class MatchMaker:
    def __init__(self, num_courts, f_mixTiers = False):
        self.players = []
        self.tiered_players = {}
        self.courts = [Court(i+1) for i in range(num_courts)]
        self.history = {}
        self.f_mixTiers = f_mixTiers

    def load_players_from_csv(self, filepath):
        import csv
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                player = Player(row['Name'], row['Tier'], row['Gender'])
                self.players.append(player)
            self._group_players_by_tier()

    def _group_players_by_tier(self):
        self.tiered_players={}
        for player in self.players:
            self.tiered_players.setdefault(player.tier, []).append(player)

    def assign_matches(self):
        if self.f_mixTiers:
            self._assign_mixed_tier_matches()
        else:
            self._assign_tier_separated_matches()

    def _assign_mixed_tier_matches(self):
        t1 = self.tiered_players.get(1, [])
        t2 = self.tiered_players.get(2, [])
        t3 = self.tiered_players.get(3, [])

        half = len(t2) // 2
        t2_group1 = t2[:half]
        t2_group2 = t2[half:]

        group1 = t1 + t2_group1
        group2 = t3 + t2_group2

        random.shuffle(group1)
        random.shuffle(group2)

        for group in [group1, group2]:
            while len(group) >= 4:
                court = self._get_available_court()
                if not court:
                    print("모든 코트가 가득 찼습니다.")
                    return
                for _ in range(4):
                    court.add_player(group.pop())
        print(f"group1 남은 인원: {len(group1)}명")
        print(f"group2 남은 인원: {len(group2)}명")

    def _assign_tier_separated_matches(self):
        for tier, players in self.tiered_players.items():
            random.shuffle(players)
            while len(players) >= 4:
                court = self._get_available_court()
                if not court:
                    print("모든 코트가 가득 찼습니다.")
                    return
                for _ in range(4) :
                    court.add_player(players.pop())

    def _get_available_court(self):
        for court in self.courts:
            if not court.f_isFull:
                return court
        return None

    def print_courts(self):
        for court in self.courts:
            print(court)