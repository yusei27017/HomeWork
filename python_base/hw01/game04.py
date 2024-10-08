import random
poker = ['♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
'♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
'♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
'♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K', 'Joker']

def stats_rank(deck):
    '''
    請輸出統計 例如在排組中梅花有 xx點 方塊有 oo點 黑桃有 ..
    統計任何數據形式都行 我要一眼就知道每個花色最後有多少點。
    特殊規則 如果抽到Joker下次抽到牌的花色點數必須清零
    例如 
    下一張抽到 Joker 那再下一張抽到 方塊10 則方塊10作廢以外
    方塊總點數再抽到 方塊10 的情況下 必須歸零 繼續抽下張 
    下一張抽到 Joker 那再下一張抽到 黑桃A 則黑桃A作廢以外
    黑桃總點數再抽到 黑桃A 的情況下 必須歸零 繼續抽下張 
    '''
    return

def rank_sort(deck):
    '''
    請替牌組排序 ♠>♥>♦>♣ , A>K>Q>J>10>9>8>7>6>5>4>3>2
    特殊規則 如果抽到Joker最大
    output 請給我 list
    '''
    return []

if __name__ == "__main__":
    random.shuffle(poker)
    poker_len = random.randint(5, 23)
    deck = poker[:poker_len]
    # 1
    stats_ans = stats_rank(deck)
    # 2
    sort_ans = rank_sort(deck)


