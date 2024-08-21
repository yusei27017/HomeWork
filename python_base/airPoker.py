
# 定義撲克牌的花色和點數
poker_suit, poker_rank = ['♦', '♣', '♠', '♥'], ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 生成所有撲克牌的組合
poker_card = [f"{s}{r}" for s in poker_suit for r in poker_rank]
poker_rank_map = {poker_rank[i]: i+1 for i in range(13)}

def poker_combinations(num):
    poker_ans = set()  # 使用集合來存儲已經找到的組合，避免重複
    card_combinations = [[]]

    while card_combinations:
        card_set = card_combinations.pop()
        current_sum = sum(poker_rank_map[card[1:]] for card in card_set)
        
        if len(card_set) == 5 and current_sum == num:
            sorted_set = tuple(sorted(card_set))  # 將組合轉為排序後的元組並加入集合
            poker_ans.add(sorted_set)
            continue
        
        if len(card_set) > 4 or current_sum > num:
            continue
        
        # 確保每次添加的牌保持順序，避免需要額外的排序操作
        last_rank_index = poker_rank_map[card_set[-1][1:]] if card_set else 0
        for select_poker in poker_card:
            if poker_rank_map[select_poker[1:]] >= last_rank_index and select_poker not in card_set:
                new_set = card_set + [select_poker]
                card_combinations.append(new_set)

    return list(poker_ans)

if __name__ == "__main__":
    ans = poker_combinations(15)
    print(ans)
