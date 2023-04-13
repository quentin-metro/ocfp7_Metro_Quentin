import csv


# CONSTANT
BUDGET_MAX = 500
DATA_FILES = "dataset.csv"


def optimized():
    with open(DATA_FILES, 'r') as fichier_csv:
        # Init data from csv file
        csv_reader = csv.reader(fichier_csv, delimiter=' ', quotechar='|')
        actions = []
        for row in csv_reader:
            action = row[0].split(',')
            # action[0] = name, action[1] = price, action[2] = profit
            if action[0].lower() != 'name':
                cost = float(action[1])
                if cost > 0:
                    profit = float(action[2].strip('%')) * 0.01
                    if profit != 0:
                        rapport = (profit * cost) / (1 + cost)
                        new_list = [action[0], cost, profit, rapport]
                        actions.append(new_list)
        actions.sort(reverse=True, key=sortkey)
        # Calculate max profit
        r = calculate_profit(actions)
        total_cost = r[1]
        total_profit = r[2]
        actions_path = r[0]
        print(f'Coût total: {total_cost}')
        print(f'Bénéfice total: {total_profit}')
        print(actions_path)


def sortkey(e):
    return float(e[3])


def calculate_profit(list_action):
    total_cost = 0
    max_profit = 0
    actions_path = []
    for action in list_action:
        new_cost = total_cost + action[1]
        if new_cost <= BUDGET_MAX:
            total_cost = new_cost
            max_profit = max_profit + (action[1] * action[2])
            actions_path.append(action[0])
            if new_cost == BUDGET_MAX:
                break
    return [actions_path, total_cost, max_profit]


optimized()
