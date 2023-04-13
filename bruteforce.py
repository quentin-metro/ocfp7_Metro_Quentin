import csv


# CONSTANT
BUDGET_MAX = 500
DATA_FILES = "dataset.csv"


def bruteforce():
    with open(DATA_FILES, 'r') as fichier_csv:
        # Init data from csv file
        csv_reader = csv.reader(fichier_csv, delimiter=' ', quotechar='|')
        actions = []
        for row in csv_reader:
            action = row[0].split(',')
            # action[0] = name, action[1] = price, action[2] = profit
            if action[0] != 'name':
                actions.append(action)
        # Calculate max profit
        r = calculate_profit(actions, 0)
        total_cost = r[1]
        total_profit = r[2]
        actions_path = r[0]
        print(f'Coût total: {total_cost}')
        print(f'Bénéfice total: {total_profit}')
        print(actions_path)


def sortkey(e):
    return float(e[1])


def calculate_profit(list_action, total_cost):
    max_profit = 0
    actions_path = []
    best_cost = 0
    for action in list_action:
        new_cost = total_cost + float(action[1])
        if new_cost <= BUDGET_MAX:
            # Handle profit format ("%")
            total_profit = float(action[1]) * (1 + float(action[2].strip('%'))/100)
            # Check if last element of the list
            if len(list_action) > 1:
                new_list = list_action.copy()
                new_list.remove(action)
                r = calculate_profit(new_list, new_cost)
                # If better take r else ignore this iteration
                if r[1] <= BUDGET_MAX and (total_profit + r[2]) > max_profit:
                    actions_path = r[0]
                    best_cost = r[1]
                    max_profit = total_profit + r[2]
                    actions_path.append(action[0])
            else:
                actions_path.append(action[0])
                max_profit = total_profit
                best_cost = new_cost
    if best_cost != 0:
        total_cost = best_cost
    r = [actions_path, total_cost, max_profit]
    return r


bruteforce()
