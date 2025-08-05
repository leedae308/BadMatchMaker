from structure.matchmaker import MatchMaker

mm=MatchMaker(num_courts=4, f_mixTiers=True)
mm.load_players_from_csv('players.csv')
mm.assign_matches()
mm.print_courts()
