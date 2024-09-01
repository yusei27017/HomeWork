import airPoker, random

def hand_aanalysis(hand_comb):
    '''
    應用題
    隨機給出五張手排點數之和 
    例如: 點數合為6,其poker組合為 ('♠2', '♠A', '♣A', '♥A', '♦A'), ('♠A', '♣2', '♣A', '♥A', '♦A')
    ('♠A', '♣A', '♥2', '♥A', '♦A'), ('♠A', '♣A', '♥A', '♦2', '♦A')
    只有四總poker組合 拿到鐵支機率為100% 接下來隨機input點數之和請寫個function計算 同花順 鐵支 三條的機率各為何?
    '''    
    print(hand_comb)


if __name__ == "__main__":
    random_num = random.randint(8, 63)
    poker_comb = airPoker.poker_combinations(random_num)

    hand_aanalysis(poker_comb)