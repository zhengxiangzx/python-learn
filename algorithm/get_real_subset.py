# -*- coding: utf-8 -*-
"""
求一个集合的所有非空子集
通过递归的方式实现
"""


def get_subset(subset, result=[]):
    if len(subset) <= 1:
        return None
    for i in range(len(subset)):
        arr = []
        for num in subset:
            if num != subset[i]:
                arr.append(num)
        get_subset(arr, result)
        # list.count(obj) 用于统计obj元素在list中出现的次数
        if result.count(arr) == 0:
            result.append(arr)
    return result


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    list2 = get_subset(list1)
    list2.sort()
    print(list2)
