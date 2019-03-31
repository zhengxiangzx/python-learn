# # -*- coding: utf-8 -*-
# import math
#
#
# # 冒泡排序
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         for j in range(0, len(arr) - i):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
#
# # 归并排序
# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
#     middle_num = math.floor(len(arr) / 2)
#     left_num, right_num = arr[0:middle_num], arr[middle_num::]
#     return merge(merge_sort(left_num), merge_sort(right_num))
#
#
# def merge(left_num, right_num):
#     result = []
#     while left_num and right_num:
#         if left_num[0] >= right_num[0]:
#             result.append(right_num.pop(0))
#         else:
#             result.append(left_num.pop(0))
#     while left_num:
#         result.append(left_num.pop(0))
#     while right_num:
#         result.append(right_num.pop(0))
#     return result
#
#
# # def quick_sort(arr):
# #     if len(arr) < 2:
# #         return arr
# #     for num in arr[1::]:
# #         if num >= arr[0]:
# #
# #     pass
#
#
# def partition():
#     pass
#
# if __name__ == '__main__':
#     arr_list = [17, 6, 27, 9, 15]
#     result1 = merge_sort(arr_list)
#     print(result1)
#     # middle = math.ceil(len(arr_list) / 2)
#     # for i in range(0, len(arr_list), 2):
#     #     left_num, right_num = arr_list[i:i + 1], arr_list[i + 1: i + 2]
#     #     if left_num and right_num:
#     #         if left_num > right_num:
#     #             print(left_num, right_num)
#     # print(arr_list[middle])
#     # print(arr_list[0:middle])
#     # print(middle)


string =["event_time_selected_timezone", "event_type", "re_targeting_conversion_type", "is_retargeting", "app_id", "platform", "attribution_type",
            "event_time", "event_name", "currency", "selected_currency", "revenue_in_selected_currency", "cost_per_install", "click_time_selected_timezone",
            "click_time", "install_time_selected_timezone", "install_time", "agency", "campaign", "media_source", "af_sub1", "af_sub2",
            "af_sub3", "af_sub4", "af_sub5", "af_siteid", "click_url", "fb_campaign_id", "fb_campaign_name", "fb_adset_id", "fb_adset_name",
            "fb_adg roup_id", "fb_adgroup_name", "country_code", "city", "ip", "wifi", "language", "appsflyer_device_id", "customer_user_id",
            "android_id", "imei", "advertising_id", "mac", "device_brand", "device_model", "os_version", "sdk_version", "app_version", "operator",
            "carrier", "http_referrer", "app_name", "download_time", "download_time_selected_timezone", "af_cost_currency", "af_cost_value",
            "af_cost_model", "af_c_id", "af_adset", "af_adset_id", "af_ad", "af_ad_id", "af_ad_type", "af_channel", "af_keywords", "bundle_id",
            "attributed_touch_type", "attributed_touch_time", "device_type", "device_name", "idfa", "idfv", "fb_adgroup_id"]

print(string.index("install_time_selected_timezone"))