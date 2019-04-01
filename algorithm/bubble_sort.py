# -*- coding: utf-8 -*-
import math


# 冒泡排序
def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 归并排序
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle_num = math.floor(len(arr) / 2)
    left_num, right_num = arr[0:middle_num], arr[middle_num::]
    return merge(merge_sort(left_num), merge_sort(right_num))


def merge(left_num, right_num):
    result = []
    while left_num and right_num:
        if left_num[0] >= right_num[0]:
            result.append(right_num.pop(0))
        else:
            result.append(left_num.pop(0))
    while left_num:
        result.append(left_num.pop(0))
    while right_num:
        result.append(right_num.pop(0))
    return result


# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#     for num in arr[1::]:
#         if num >= arr[0]:
#
#     pass


def partition():
    pass


if __name__ == '__main__':
    arr_list = [17, 6, 27, 9, 15]
    result1 = bubble_sort(arr_list)
    print(result1)
