''' FreeCoderCamp Python Programming Course final projects Budget Class '''


class Category:

  def __init__(self,name):
    self.name=name
    self.ledger=[]
    self.sum=0

  def check_funds(self,amount):
    if amount>self.sum:
      return False
    else:
      return True

  def deposit(self,amount,description=""):
    thing={"amount": amount, "description": description}
    self.ledger.append(thing)
    self.sum=self.sum+amount

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      thing={"amount": (-1)*amount, "description": description}
      self.ledger.append(thing)
      self.sum=self.sum-amount
      return True
    else:
      return False

  def get_balance(self):
    return self.sum

  def transfer(self,amount,cate):
    if self.check_funds(amount):
      useful="Transfer to "+cate.name
      thing={"amount": (-1)*amount, "description":useful}
      self.ledger.append(thing)
      self.sum=self.sum-amount
      cate.deposit(amount,"Transfer from "+str(self.name))
      return True
    else:
      return False

  def __str__(self):
    x=len(self.name)
    y=int((30-x)/2)
    print("*"*y+str(self.name)+"*"*y)
    for j in self.ledger:
      temp=[]
      for i in j.keys():
        temp.append(j[i])
      x1=len(str(temp[0]))
      y1=len(str(temp[1]))
      useful=abs(30-x1-y1)
      if y1>30:
        h=30-x1-1
        useful=1
        print(str(temp[1][0:h]),end="")
        print(" "*useful,end="")
        print(str(temp[0]))
      else:
        print(str(temp[1]),end="")
        print(" "*useful,end="")
        print(str(temp[0]))
    print("Total: ",end="")
    print(self.sum)
    return ""

def create_spend_chart(c):
  final=""
  final=final+"Percentage spent by category\n" #print("Percentage Spent by category")
  #getting percentages
  respective_percentages=[]
  for i in c:
    spending=0
    given=0
    for j in i.ledger:
      if j["amount"] < 0:
        spending = spending+((-1)*(j["amount"]))
      elif j["amount"] > 0:
        given = given + j["amount"]
    respective_percentages.append(round((spending/given)*10)*10)

  #printing format
  y_axis=list(range(0,110,10))
  y_axis.sort(reverse=True)
  for i in y_axis:
    v=3-len(str(i))
    u=" "*v
    final=final+u+str(i)+"| "   #print(u+str(i)+"|",end=" ")
    for j in range(len(respective_percentages)):
      if respective_percentages[j] >= i:
        final=final+"o" #print("o",end="")
      else:
        final=final+" " #print(" ",end="")
      final=final+"  " #print("  ",end="")
    final=final+"\n"   #print("")
  final=final+"    "  #print("    ",end="")
  for k in range(len(respective_percentages)):
    final=final+"---" #print("---",end="")
  final=final+"-\n"  #print("-")

  #doing the vertical x_axis
  #finds longest category name
  temp=[]
  temp2=[]
  for i in c:
    temp.append(len(i.name))
  m=max(temp)

  for i in c:
    temp2.append(i.name+" "*(m-len(i.name)))

  for k in range(m):
    final=final+"    " #print("    ",end="")
    for g in temp2:
      final=final+" "+g[k]+" " #print(" "+g[k]+" ",end="")
    final=final+"\n"   #print("")

  return final
