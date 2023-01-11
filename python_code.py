
from itertools import product


def get_newspaper_combinations(budget):
    news_papers = {"TOI": [3, 3, 3, 3, 3, 5, 6], 
                  "Hindu": [2.5, 2.5, 2.5, 2.5, 2.5, 4, 4],
                  "ET": [4, 4, 4, 4, 4, 4, 10],
                  "BM": [1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5],
                  "HT": [2, 2, 2, 2, 2, 4, 4]}
    
    
    
    comb = [combination for length in range(1, len(news_papers)+1)
                    for combination in product(news_papers, repeat=length)]
    
    
    
    comb = [{k: v for sub_combination in combination for k, v in sub_combination.items()} for combination in comb]
    
    

    valid_final = []
    for combination in comb:
        total_cost = sum([sum(subscription) for subscription in comb.values()])
        if total_cost <= budget:
            valid_final.append(combination)
    return valid_final

main_value = float(input("Enter the weekly budget for subscriptions: "))
combs = get_newspaper_combinations(main_value)
for combination in combs:
    print(combination)
