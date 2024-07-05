import pandas as pd

ARC_DATA = [
    {'arc_id': 1, 'arc_name': 'First Selection'},
    {'arc_id': 2, 'arc_name': 'Second Selection'},
    {'arc_id': 3, 'arc_name': 'World Five'},
    {'arc_id': 4, 'arc_name': 'Third Selection'},
    {'arc_id': 5, 'arc_name': 'U20 Match'},
    {'arc_id': 6, 'arc_name': 'Neo Egoist League'}
]

TEAM_DATA = [
    {'team_id': 1, 'arc_id': 1, 'team_name': 'Team Z'},
    {'team_id': 2, 'arc_id': 1, 'team_name': 'Team Y'},
    {'team_id': 3, 'arc_id': 1, 'team_name': 'Team X'},
    {'team_id': 4, 'arc_id': 1, 'team_name': 'Team W'},
    {'team_id': 5, 'arc_id': 1, 'team_name': 'Team V'},

    {'team_id': 6, 'arc_id': 2, 'team_name': 'Team White'},
    {'team_id': 7, 'arc_id': 2, 'team_name': 'Team Red'},

    {'team_id': 8, 'arc_id': 3, 'team_name': 'Team World Five'},

    {'team_id': 9, 'arc_id': 4, 'team_name': 'Team A'},
    {'team_id': 10, 'arc_id': 4, 'team_name': 'Team B'},
    {'team_id': 11, 'arc_id': 4, 'team_name': 'Team C'},

    {'team_id': 12, 'arc_id': 5, 'team_name': 'Blue Lock Eleven'},
    {'team_id': 13, 'arc_id': 5, 'team_name': 'Japan U-20'},

    {'team_id': 14, 'arc_id': 6, 'team_name': 'Bastard München'},
    {'team_id': 15, 'arc_id': 6, 'team_name': 'FC Barcha'},
    {'team_id': 16, 'arc_id': 6, 'team_name': 'Manshine City'},
    {'team_id': 17, 'arc_id': 6, 'team_name': 'Ubers'},
    {'team_id': 18, 'arc_id': 6, 'team_name': 'Paris X Gen'}
]

arc_df = pd.DataFrame(ARC_DATA)
arc_df.to_csv('arcs.csv', index=False)

teams_df = pd.DataFrame(TEAM_DATA)
teams_df.to_csv('teams.csv', index=False)