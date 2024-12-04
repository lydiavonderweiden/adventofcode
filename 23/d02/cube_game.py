def clean_up(liste):
    games = []
    for l in liste:
        game_index= int(l[0].strip("Game "))
        turns = l[1].split(';')
        list_turns = []
        for t in turns:
            draw = t.split(',')
            dict_draw = {}
            for d in draw: 
                d = d.strip()
                match d.split():
                    case [amount, "green"]: dict_draw['green'] = int(amount)
                    case [amount, "red"]: dict_draw['red'] = int(amount)
                    case [amount, "blue"]: dict_draw['blue'] = int(amount)
            list_turns.append(dict_draw)
        games.append((game_index, list_turns))
                
    return games

def check_valid(games):
    red = 12
    blue = 14
    green = 13
    id_valid = []
    for game in games:
        id = game[0]
        valid = True
        for draw in game[1]:
            if 'green' in draw and draw['green'] > green: 
                valid = False
                break
            if 'blue' in draw and draw['blue'] > blue: 
                valid = False
                break
            if 'red' in draw and draw['red'] > red:
                valid = False
                break
        if valid: id_valid.append(id)

    return id_valid

def check_power(games):
    power_sets = []
    for game in games:
        red = 0
        blue = 0
        green = 0
        for draw in game[1]:
            if 'green' in draw and draw['green'] > green: green = draw['green']
            if 'blue' in draw and draw['blue'] > blue: blue = draw['blue']
            if 'red' in draw and draw['red'] > red: red = draw['red']
        power = red*blue*green
        power_sets.append(power)

    return power_sets

if __name__ == "__main__":
    with open("input") as file:
        liste = [l.strip("\n").split(':') for l in file.readlines()]

    games = clean_up(liste)
    id_valid = check_valid(games)
    power_sets =check_power(games)
    print(sum(power_sets))
    