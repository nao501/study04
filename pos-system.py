from os import error
from numpy.lib.twodim_base import mask_indices
import pandas as pd
import csv
### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
    
    
### メイン処理
def main():

    # マスタ登録
    item_master=[]
    #商品マスター.csvからデータを読み込み
    master_deta = open("商品マスター.csv",'r')
    item_code_list = []
    tem_name_list = []
    price_list = []

    for row in csv.reader(master_deta):
        item_code_list.append(row[0])
        tem_name_list.append(row[1])
        price_list.append(row[2])
    
    #商品マスター.csvの1行目のセルデータを削除
    del item_code_list[0]
    del tem_name_list[0]
    del price_list[0]

    #各リストをItem()に入れていく
    for item_code, item_name, price in zip(item_code_list,tem_name_list,price_list):
        item_master.append(Item(item_code, item_name, price))


    #item_master.append(Item("001","りんご",100))
    #item_master.append(Item("002","なし",120))
    #item_master.append(Item("003","みかん",150))
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    order.add_item_order("004")
    # オーダー表示
    order.view_item_list()
    # オーダー登録
    order_code = input("商品コードを入力してください：")
    order_count = int(input("個数を入力してください："))
    
    # マスター検索
    for item in item_master:
        for item_order in order.item_order_list:
            if item.item_code == item_order:
                print(f"商品コード{item.item_code}:{item.item_name}￥{item.price}円")
    for item in item_master:
        if item.item_code == order_code:
            item_price = int(item.price)*order_count
            print(f"\n選んだ商品は商品コード{item.item_code}:{item.item_name}￥{item.price}円\n")
            print(f"個数：{order_count}個,合計金額{item_price}円")

            customer_money =int(input("金額を入力してください："))
            return_money = customer_money-item_price
            
            if return_money <0:
                error_money =item_price-customer_money
                print(f"{error_money}円不足しています")
            elif return_money == 0:
                print("ちょうど頂きます")
            else:
                print(f"{return_money}円お返しです。")
  
   


if __name__ == "__main__":
    main()