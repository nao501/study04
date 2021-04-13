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
    def __init__(self,item_master,order_count):
        self.item_order_list=[]
        self.order_count_list = []
        self.item_master=item_master
        self.order_count = order_count

    def add_item_order(self,item_code,order_count):
        self.item_order_list.append(item_code)
        self.order_count_list.append(order_count)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
    
    
### メイン処理
def main():

    # マスタ登録
    item_master=[]
    order_count=[]
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
    
    # オーダー登録
    order=Order(item_master,order_count)

    while True:
        text_order = input("商品コードを入力してください\n終了の際は000と入力してください：")
        if text_order == "000":
            break
        else:
            text_count = int(input("個数を入力してください："))
            order.add_item_order(text_order,text_count)
    
    # マスター検索
    for item in item_master:
        for item_order,order_count in zip(order.item_order_list,order.order_count_list):
            if item.item_code == item_order:
                print(f"商品コード{item.item_code}:{item.item_name}￥{item.price}円/{order_count}個")
                order_price = int(item.price)*order_count
        total_price = order_price +int(item.price)
        
    print(f"合計金額は{total_price}円")

  
    customer_money =int(input("支払い金額を入力してください："))
    return_money = customer_money-total_price
            
    if return_money <0:
        error_money =total_price-customer_money
        print(f"{error_money}円不足しています")
    elif return_money == 0:
        print("ちょうど頂きます")
    else:
        print(f"{return_money}円お返しです。")
  
   


if __name__ == "__main__":
    main()