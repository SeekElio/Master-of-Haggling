#游戏设计师 FANG xifan
'''
【游戏目标】
玩家扮演顾客与商人讨价还价 在5次之内与商人达成交易即可获胜

【游戏元素】
场景：集市
角色：顾客（玩家） 商人（电脑）

【游戏流程】
1.开始游戏 商人随机选择物品
*画面:价格，成本，出价输入框
2.玩家输入价格进行报价
3.商人进行决策 根据报价进行反馈 并且调整心理价格
*画面:商人提示“太高了”“太低了”
4.玩家第二次输入价格进行报价
*画面:价格，成本，建议出价，出价输入框
5.如此往复4次
6.如果在5次内成交,游戏胜利;如果5次仍未达成游戏,游戏结束。
'''

'''
创建一个角色Customer
3个属性:出价，剩余次数，推荐出价
4个功能：为商品出价，提示剩余次数，设置建议价格，输出建议价格
'''
class Customer:
    def _init_(self,bid,remaining_times,suggested_bid):
        self.bid = bid
        self.remaining_times = remaining_times
        self.suggested_bid = suggested_bid
'''
创建一个角色Merchant
1个属性:保留价格
2个功能：设置保留价格，获取保留价格
'''
class Merchant:
    def _init_(self,reservation_price):
        self.reservation_price = reservation_price
'''
创建一个父级抽象类（ADT class）创建接口
并在其子类中实现具体逻辑
'''
class Product:
    def _init_(self,cost,price):
        self.cost = cost
        self,price = price
#class Name(Product):

isTransactionContinue = True       
customer = Customer()
merchant = Merchant()



#前端设计师 Sze-To TSZ KIN




#后端设计师 ZHANG jiayuan





#美术设计师 LAW kahei




#测试者 CHI xuanyi