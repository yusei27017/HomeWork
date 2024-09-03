import random

'''
費波那契數列是一個數學序列，其中每一個數字都是前兩個數字之和。這個數列通常從 1 開始，接下來的數字如下：
- 第一個數是 1
- 第二個數也是 1
- 第三個數是 1 + 1 = 2
- 第四個數是 1 + 2 = 3
- 第五個數是 2 + 3 = 5
- 第六個數是 3 + 5 = 8

如此繼續下去。用公式表示的話，如果費波那契數列的第(n)個數為(F(n))，那麼：
F(n) = F(n-1) + F(n-2)
其中 (F(1) = 1) 且 (F(2) = 1)。這個數列有許多有趣的性質，並且在自然界和各種科學領域中都可以看到它的應用。
'''

def calcu_fibonacci(num):
    '''
    給一個數,請返回費波那契數列中距離該數最近的數
    例如：num = 6 out->5 num = 7 out->8
    '''
    fibonacci_array = [1, 1]
    fibonacci_num = 1
    while fibonacci_num < num:
        fibonacci_num = fibonacci_array[-1] + fibonacci_array[-2]
        fibonacci_array.append(fibonacci_num)

    if fibonacci_array[-1] - num < num - fibonacci_array[-2]:
        return fibonacci_array[-1]
    return fibonacci_array[-2]


if __name__ == "__main__":
    randnum = random.randint(1, 5000)
    print(randnum)
    ans = calcu_fibonacci(randnum)
    print(ans)



