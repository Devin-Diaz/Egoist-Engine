
PLAYER_HREFS = []

with open('player_hrefs.txt', 'r') as file:
    for line in file:
        parsed_line = line.strip().replace("\n", "")
        PLAYER_HREFS.append(parsed_line)


