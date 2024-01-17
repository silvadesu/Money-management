class MoneyManagement:
    def __init__(self):
        self.asset=0
        self.month=[]
    def record(self,month,amount,detail):
        content=({"詳細":detail,"金額":amount})
        self.asset+=amount
        self.month.append(content)
    def detail_of_month(self,month):
        for table in self.month:
            print(table)
    def show_asset(self):
        print(self.asset)
        
money_management=MoneyManagement()

def Menu():
    menu=input("機能を選択(1:収入、2:支出、3:月別詳細、4:残高表示)")
    if menu=="1":
        plus=input("収入を入力")
        amount=float(plus)
        month=float(input("月を入力"))
        detail=input("詳細を入力")
        money_management.record(month,amount,detail)
    elif menu=="2":
        minus=input("支出を入力")
        amount=-float(minus)
        month=float(input("月を入力"))
        detail=input("詳細を入力")
        money_management.record(month,amount,detail)
    elif menu=="3":
        month=float(input("月を入力"))
        money_management.detail_of_month(month)
    elif menu=="4":
        money_management.show_asset()
    else:
        print("エラーが起こりました。")

Menu()
