#! /usr/local/env python3
# -*- coding: utf-8 -*-
# Author: v.stone@163.com


import random
import sys
from math import ceil


class MenuItem(object):
    def __init__(self):
        self.staple_list = [
            [
                {u"名称": u"大米饭", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"杂粮饭", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"馒头", u"数量": u"1个", u"克重": u"80g", u"图片": u""},
                {u"名称": u"花卷", u"数量": u"1个", u"克重": u"80g", u"图片": u""},
            ], [
                {u"名称": u"全麦切片面包", u"数量": u"2片", u"克重": u"70g", u"图片": u""},
            ], [
                {u"名称": u"杂粮稠粥", u"数量": u"1碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"杂粮米糊", u"数量": u"1碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"素菜包", u"数量": u"1个", u"克重": u"80g", u"图片": u""},
                {u"名称": u"瘦肉包", u"数量": u"1个", u"克重": u"80g", u"图片": u""},
            ], [
                {u"名称": u"纯燕麦片", u"数量": u"1份", u"克重": u"50g", u"图片": u"", u"备注": u"桂格或捷森"},
            ], [
                {u"名称": u"杂粮稀粥", u"数量": u"1碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"杂粮薄米糊", u"数量": u"1碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"少油大饼", u"数量": u"2块", u"克重": u"", u"图片": u"", u"备注": u"扑克牌大小为1块"},
            ], [
                {u"名称": u"家乐氏玉米片", u"数量": u"1份", u"克重": u"40g", u"图片": u""},
                {u"名称": u"ICA 等坚果果干 混合麦片", u"数量": u"1份", u"克重": u"40g", u"图片": u""},
            ], [
                {u"名称": u"面条", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"米线", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"米粉", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"馅饼", u"数量": u"1个", u"克重": u"", u"图片": u"", u'备注': u'少油，手掌大小'},
            ], [
                {u"名称": u"Weet-bix 麦片", u"数量": u"3块", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"玉米", u"数量": u"2/3根", u"克重": u"150g", u"图片": u""},
            ], [
                {u"名称": u"煎饼", u"数量": u"半个", u"克重": u"", u"图片": u"", u"备注": u"面粉 50g，无薄脆、油 条、香肠"},
            ], [
                {u"名称": u"纯五谷杂粮粉", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"凉皮", u"数量": u"半碗", u"克重": u"", u"图片": u""},
                {u"名称": u"少油炒粉", u"数量": u"半碗", u"克重": u"", u"图片": u""},
                {u"名称": u"少油炒饭", u"数量": u"半碗", u"克重": u"", u"图片": u""},
                {u"名称": u"少油炒面", u"数量": u"半碗", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"小笼包", u"数量": u"3个", u"克重": u"", u"图片": u""},
                {u"名称": u"蒸饺", u"数量": u"5个", u"克重": u"", u"图片": u""},
                {u"名称": u"烧卖", u"数量": u"2个", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"含坚果杂粮粉", u"数量": u"1份", u"克重": u"40g", u"图片": u""},
            ], [
                {u"名称": u"意面", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"通心粉", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"粽子", u"数量": u"1个", u"克重": u"90g", u"图片": u""},
            ], [
                {u"名称": u"桂格燕麦饼干", u"数量": u"1袋", u"克重": u"35g", u"图片": u""},
            ], [
                {u"名称": u"粉丝", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
                {u"名称": u"粉条", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"紫薯", u"数量": u"1个", u"克重": u"200g", u"图片": u""},
            ], [
                {u"名称": u"焙朗早餐饼", u"数量": u"4块", u"克重": u"", u"图片": u"", u'备注': u'5片/小袋规格'},
            ], [
                {u"名称": u"肠粉", u"数量": u"半碗", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"土豆", u"数量": u"1个", u"克重": u"250g", u"图片": u""},
            ], [
                {u"名称": u"太平苏打饼干", u"数量": u"1.5袋", u"克重": u"37.5g", u"图片": u""},
            ], [
                {u"名称": u"胡辣汤", u"数量": u"1碗", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"蒸山药", u"数量": u"1段", u"克重": u"300g", u"图片": u""},
            ], [
                {u"名称": u"无奶油蛋糕", u"数量": u"1块", u"克重": u"40g", u"图片": u""},
            ], [
                {u"名称": u"水饺", u"数量": u"5个", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"蒸藕", u"数量": u"1段", u"克重": u"280g", u"图片": u""},
            ], [
                {u"名称": u"板栗", u"数量": u"8颗", u"克重": u"80g", u"图片": u""},
            ], [
                {u"名称": u"馄饨", u"数量": u"8个", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"蒸胡萝卜", u"数量": u"3根", u"克重": u"450g", u"图片": u""},
            ], [
                {u"名称": u"BOLTHOUSE 水果胡萝卜", u"数量": u"", u"克重": u"250g", u"图片": u""},
            ], [
                {u"名称": u"汤圆", u"数量": u"3个", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"蒸芋头", u"数量": u"", u"克重": u"210g", u"图片": u""},
            ], [
                {u"名称": u"葡萄干", u"数量": u"", u"克重": u"50g", u"图片": u""},
                {u"名称": u"蔓越莓干", u"数量": u"", u"克重": u"50g", u"图片": u""},
            ], [
                {u"名称": u"寿司", u"数量": u"4块", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"煮南瓜", u"数量": u"3碗", u"克重": u"880g", u"图片": u""},
            ], [
                {u"名称": u"水果 2 个", u"数量": u"2个", u"克重": u"", u"图片": u""},
            ]
        ]
        self.breakfast_list = [
            [
                {u"名称": u"水煮蛋", u"数量": u"2个", u"克重": u"", u"图片": u""},
                {u"名称": u"茶叶蛋", u"数量": u"2个", u"克重": u"", u"图片": u""},
                {u"名称": u"蒸蛋羹", u"数量": u"2个", u"克重": u"", u"图片": u""},
                {u"名称": u"少油煎蛋", u"数量": u"2个", u"克重": u"", u"图片": u""},
            ], [
                {u"名称": u"无糖酸奶", u"数量": u"1盒", u"克重": u"", u"图片": u""},
                {u"名称": u"脱脂奶", u"数量": u"1盒", u"克重": u"", u"图片": u""},
                {u"名称": u"无糖豆浆", u"数量": u"1杯", u"克重": u"500g", u"图片": u""},
            ], [
                {u"名称": u"叶菜", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"黄瓜", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"西红柿", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"圣女果", u"数量": u"6颗", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"绿豆芽", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"芹菜", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"海带丝", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
                {u"名称": u"绿豆芽", u"数量": u"1份", u"克重": u"150g", u"图片": u"", u'备注': u'可不吃'},
            ]
        ]
        self.morning_tea_list = [
            [
                {u"名称": u"核桃", u"数量": u"2颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"碧根果", u"数量": u"2颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"腰果", u"数量": u"5颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"杏仁", u"数量": u"5颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"巴旦木", u"数量": u"8颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"扁桃仁", u"数量": u"8颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"花生", u"数量": u"15颗", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"瓜子仁", u"数量": u"1把", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"黑芝麻", u"数量": u"1把", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"枣夹核桃", u"数量": u"1个", u"克重": u"10g", u"图片": u"", u"备注": u"若不饿，可不吃"},
            ], [
                {u"名称": u"圣女果", u"数量": u"6颗", u"克重": u"150-450g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"番茄", u"数量": u"1个", u"克重": u"150-450g", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"黄瓜", u"数量": u"1根", u"克重": u"150-450", u"图片": u"", u"备注": u"若不饿，可不吃"},
            ]
        ]
        self.meat_list = [
            {u"名称": u"去皮鸡肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"去皮鸭肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"去皮鹅肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"鸡胸肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"鱼肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"虾肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"虾肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"瘦牛肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"瘦羊肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"瘦猪肉", u"数量": u"1份", u"克重": u"100g", u"图片": u""},
            {u"名称": u"卤牛肉", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"去皮卤鸡腿", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"天猫超市即食鸡胸肉", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"科尔沁酱卤牛腱肉", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"草原旭日风干牛肉干", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"光合力量鸡胸肉干丝", u"数量": u"1份", u"克重": u"50g", u"图片": u""},
            {u"名称": u"丽仕三文鱼罐头", u"数量": u"1份", u"克重": u"", u"图片": u""},
            {u"名称": u"丽仕金枪鱼罐头", u"数量": u"1份", u"克重": u"", u"图片": u""},
        ]
        self.bean_list = [
            {u"名称": u"黄豆", u"数量": u"1份", u"克重": u"30g", u"图片": u""},
            {u"名称": u"千张", u"数量": u"1份", u"克重": u"45g", u"图片": u""},
            {u"名称": u"豆干", u"数量": u"1份", u"克重": u"90g", u"图片": u""},
            {u"名称": u"北豆腐", u"数量": u"1份", u"克重": u"120g", u"图片": u""},
            {u"名称": u"南豆腐", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
            {u"名称": u"内脂豆腐", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
            {u"名称": u"无糖豆浆", u"数量": u"1份", u"克重": u"500g", u"图片": u""},
        ]
        self.vegetable_list_level_1 = [
            {u"名称": u"菜心", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"生菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"黄瓜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"娃娃菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"西红柿", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"冬瓜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"彩椒", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"柿子椒", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"油麦菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"蒿子杆", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"大白菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"莴笋", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"空心菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"西葫芦", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"芹菜梗", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"芦笋", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"海带", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"白萝卜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"小白菜", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"紫甘蓝", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
            {u"名称": u"绿豆芽", u"数量": u"2份", u"克重": u"300-600g", u"图片": u""},
        ]
        self.vegetable_list_level_2 = [
            {u"名称": u"茄子", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"油菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"茭白", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"青椒", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"韭黄", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"韭菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"菜花", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"荠菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"香菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"菠菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"茼蒿", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"苋菜", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"鲜香菇", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"鲜木耳", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
            {u"名称": u"金针菇", u"数量": u"1份", u"克重": u"150-300g", u"图片": u""},
        ]
        self.vegetable_list_level_3 = [
            {u"名称": u"西兰花", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"豆角", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"苦菊", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"芹菜叶", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"豌豆苗", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"扁豆", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"蒜苗", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
            {u"名称": u"杏鲍菇", u"数量": u"1份", u"克重": u"150g", u"图片": u""},
        ]
        self.lunch_list = [
            # 植物油 10g
            self.meat_list + self.bean_list,
            self.vegetable_list_level_1 + self.vegetable_list_level_2 + self.vegetable_list_level_3
        ]
        self.afternoon_tea_list = [
            [
                {u"名称": u"苹果", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"梨", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"桃子", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"橙子", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"香蕉", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"西瓜", u"数量": u"1份", u"克重": u"300g", u"图片": u""},
                {u"名称": u"芒果", u"数量": u"1份", u"克重": u"350g", u"图片": u""},
                {u"名称": u"火龙果", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"樱桃", u"数量": u"20颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"车厘子", u"数量": u"20颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"哈密瓜", u"数量": u"1份", u"克重": u"260g", u"图片": u""},
                {u"名称": u"香瓜", u"数量": u"1份", u"克重": u"300g", u"图片": u""},
                {u"名称": u"蓝莓", u"数量": u"40颗", u"克重": u"150g", u"图片": u""},
                {u"名称": u"猕猴桃", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"奇异果", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"菠萝", u"数量": u"1/4份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"橘子", u"数量": u"1份", u"克重": u"200g", u"图片": u""},
                {u"名称": u"葡萄", u"数量": u"15颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"提子", u"数量": u"15颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"石榴", u"数量": u"半个", u"克重": u"120g", u"图片": u""},
                {u"名称": u"柚子", u"数量": u"2瓣", u"克重": u"215g", u"图片": u""},
                {u"名称": u"草莓", u"数量": u"12颗", u"克重": u"250g", u"图片": u""},
                {u"名称": u"番石榴", u"数量": u"2/3个", u"克重": u"170g", u"图片": u""},
                {u"名称": u"西柚", u"数量": u"半个", u"克重": u"250g", u"图片": u""},
                {u"名称": u"木瓜", u"数量": u"半个", u"克重": u"310g", u"图片": u""},
                {u"名称": u"金桔", u"数量": u"8颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"李子", u"数量": u"5颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"布朗", u"数量": u"5颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"青枣", u"数量": u"5颗", u"克重": u"200g", u"图片": u""},
                {u"名称": u"红枣", u"数量": u"2颗", u"克重": u"", u"图片": u""},
            ]
        ]
        self.dinner_list = [
            self.meat_list,
            self.vegetable_list_level_1,
        ]
        self.night_list = [
            [
                {u"名称": u"圣女果", u"数量": u"6颗", u"克重": u"", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"番茄", u"数量": u"1个", u"克重": u"", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"黄瓜", u"数量": u"1根", u"克重": u"", u"图片": u"", u"备注": u"若不饿，可不吃"},
                {u"名称": u"丸善魔芋丝", u"数量": u"1袋", u"克重": u"", u"图片": u"", u"备注": u"若不饿，可不吃"},
            ]
        ]


class MenuDayItem(object):
    def __init__(self):
        self.menu = {
            u"早餐": list(),
            u"上午茶": list(),
            u"中餐": list(),
            u"下午茶": list(),
            u"晚餐": list(),
            u"晚上点心": list(),
        }
        self.times = {
            u"早餐": '08:00',
            u"上午茶": '10:00',
            u"中餐": '12:00',
            u"下午茶": '15:00',
            u"晚餐": '18:00',
            u"晚上点心": '21:00',
        }


class Menu(object):
    def __init__(self):
        self.items = MenuItem()
        self.menu_day = dict()
        self.times = dict()
        self.menu_week = list()
        self.menu_month = list()
        self.staples = list()
        self.shopping_items = dict()
        self.shopping_list = list()

    def get_staple(self):
        while True:
            _staples = random.choice(self.items.staple_list)
            if _staples != self.staples:
                self.staples = _staples
                break
            print(u'类别重复了，重新搭配')
        _staple = random.choice(_staples)
        # _staples.remove(_staple)
        return _staple

    def get_breakfast(self):
        menu_name = u'早餐'
        menu_day_item = MenuDayItem()
        self.menu_day = menu_day_item.menu
        self.times = menu_day_item.times
        self.menu_day[menu_name].append(self.get_staple())
        for items in self.items.breakfast_list:
            self.menu_day[menu_name].append(random.choice(items))
        return True

    def get_morning_tea(self):
        menu_name = u'上午茶'
        for items in self.items.morning_tea_list:
            self.menu_day[menu_name].append(random.choice(items))
        pass

    def get_lunch(self):
        menu_name = u'中餐'
        self.menu_day[menu_name].append(self.get_staple())
        for items in self.items.lunch_list:
            self.menu_day[menu_name].append(random.choice(items))
        return True

    def get_afternoon_tea(self):
        menu_name = u'下午茶'
        for items in self.items.afternoon_tea_list:
            self.menu_day[menu_name].append(random.choice(items))
        return True

    def get_dinner(self):
        menu_name = u'晚餐'
        for items in self.items.dinner_list:
            self.menu_day[menu_name].append(random.choice(items))
        return True

    def get_night(self):
        menu_name = u'晚上点心'
        for items in self.items.night_list:
            self.menu_day[menu_name].append(random.choice(items))
        return True

    def add_into_shopping_list(self, shopping_item):
        item_name = shopping_item[u'名称']
        if shopping_item[u'克重']:
            item_unit = shopping_item[u'克重'].lower()[-1]
            item_count = shopping_item[u'克重'].lower().split(item_unit)[0].split('-')
        else:
            item_unit = shopping_item[u'数量'].lower()[-1]
            item_count = shopping_item[u'数量'].lower().split(item_unit)[0].split('-')
        if self.shopping_items.get(item_name) is None:
            self.shopping_items[item_name] = [0, 0, item_unit]
        if len(item_count) == 0:
            item_count = [0, 0]
        elif len(item_count) == 1:
            if item_count[0] == u'半':
                item_count[0] = 0.5
                item_count.append(0.5)
            elif '/' in item_count[0]:
                item_count.append(eval(item_count[0]))
            else:
                item_count.append(item_count[0])
        self.shopping_items[item_name][0] += ceil(float(item_count[0]))
        self.shopping_items[item_name][1] += ceil(float(item_count[1]))
        return True

    def summarize_shopping_list(self):
        print('\n===== 采购清单 =====')
        for shopping_item in self.shopping_items:
            item_min, item_max, item_unit = self.shopping_items[shopping_item]
            if item_min == item_max:
                print('%s\t%s%s' % (shopping_item, item_min, item_unit))
                self.shopping_list.append({
                    u"名称": shopping_item,
                    u"采购量": '%s%s' % (item_min, item_unit)
                })
            else:
                print('%s\t%s-%s%s' % (shopping_item, item_min, item_max, item_unit))
                self.shopping_list.append({
                    u"名称": shopping_item,
                    u"采购量": '%s-%s%s' % (item_min, item_max, item_unit)
                })
        return self.shopping_list

    def daily_menu(self, week_day=None):
        if week_day:
            print(u'\n===== %s菜单 =====' % week_day)
        else:
            print(u'\n===== 一日菜单 =====')
        self.get_breakfast()
        self.get_morning_tea()
        self.get_lunch()
        self.get_afternoon_tea()
        self.get_dinner()
        self.get_night()
        for stage in self.menu_day.keys():
            print('\n%s - %s:' % (self.times[stage], stage))
            for item in self.menu_day[stage]:
                if item.get(u'名称'):
                    item_comment = '(%s)' % item.get(u'备注') if item.get(u'备注') else ''
                    print('\t%s\t%s\t%s\t%s' % (item[u'数量'], item[u'名称'], item[u'克重'], item_comment))
                    self.add_into_shopping_list(shopping_item=item)
        return self.menu_day

    def weekly_menu(self):
        # print(u'\n===== 一周菜单 =====')
        for week_day in [u'周一', u'周二', u'周三', u'周四', u'周五', u'周六', u'周日']:
            self.daily_menu(week_day)
            self.menu_week.append(self.menu_day)
        return self.menu_week

    def monthly_menu(self):
        # print(u'\n===== 一个月菜单 =====')
        for month_day in range(1, 31):
            self.daily_menu('%s号' % month_day)
            self.menu_month.append(self.menu_day)
        return self.menu_month


def main():
    hmenu = Menu()
    if sys.argv[1:] and sys.argv[1] == "-w":
        hmenu.weekly_menu()
    elif sys.argv[1:] and sys.argv[1] == "-m":
        hmenu.monthly_menu()
    else:
        hmenu.daily_menu()
    hmenu.summarize_shopping_list()
    return True


if __name__ == '__main__':
    print(u'健康餐随机搭配程序')
