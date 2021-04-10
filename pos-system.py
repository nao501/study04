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
    a_list = []
    b_list = []
    c_list = []

    for row in csv.reader(master_deta):
        a_list.append(row[0])
        b_list.append(row[1])
        c_list.append(row[2])
    
    #商品マスター.csvの1行目のセルデータを削除
    del a_list[0]
    del b_list[0]
    del c_list[0]

    #各リストをItem()に入れていく
    for item_code, item_name, price in zip(a_list,b_list,c_list):
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
    
    # マスター検索
    for item in item_master:
        for item_order in order.item_order_list:
            if item.item_code == item_order:
                print("商品コード" +item.item_code +":"+ item.item_name + '￥'+str(item.price)+'円')
    for item in item_master:
        if item.item_code == order_code:
            print("\n選んだ商品は商品コード" +item.item_code +":"+ item.item_name + '￥'+str(item.price)+'円')
              
            
  
   


if __name__ == "__main__":
    main()