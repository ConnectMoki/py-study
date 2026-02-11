def hano(n, a, b, c):
    """
    参数:
        n: 起始盘子的数量
        a: 起始柱子
        b: 辅助柱子
        c: 目标柱子
    """
    if(n == 1):
        print(a, "-->", c)
    else: 
        hano(n-1, a, c, b)
        print(a, "-->", c)
        hano(n-1, b, a, c)
        
