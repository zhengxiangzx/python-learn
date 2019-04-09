# -*- coding: utf-8 -*-

"""
递归的方式实现斐波那契数列
用缓存的方式实现一个斐波那契数列（速度快）
"""


def fib_recursion(n):
    if n < 0:
        return "请输入大于0的数"
    if n == 0 or n == 1:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


# 获取递归的数据
def get_fib(n):
    result = []
    for i in range(1, n + 1):
        result.append(fib_recursion(i))
    return result


# 用缓存的方式获得斐波那契数列，速度快
def fib(n, cache=None):
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    if n == 1 or n == 0:
        return 1
    else:
        cache[n] = fib(n - 2, cache) + fib(n - 1, cache)
        return cache[n]


if __name__ == '__main__':
    num = get_fib(7)
    print(num)
