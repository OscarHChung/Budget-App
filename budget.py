class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
  
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ""):
    enough_funds = self.check_funds(amount)
    if(enough_funds):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for i in self.ledger:
      balance = balance + i["amount"]
    return balance

  def transfer(self, amount, other_category):
    enough_funds = self.check_funds(amount)
    if(enough_funds):
      self.withdraw(amount, "Transfer to %s" % other_category.name)
      other_category.deposit(amount, "Transfer from %s" % self.name)
      return True
    else:
      return False

  def __str__(self):
    output = self.name.center(30, "*") + "\n"
    for i in self.ledger:
      output += f"{i['description'][:23].ljust(23)}{format(i['amount'], '.2f').rjust(7)}\n"
    output += f"Total: {format(self.get_balance(), '.2f')}"
    return output





def create_spend_chart(categories):
  category_names = []
  category_spent = []
  category_percentages = []

  for category in categories:
    category_names.append(category.name)
    total = 0
    for item in category.ledger:
      if item['amount'] < 0:
        total -= item['amount']
    category_spent.append(round(total, 2))
  
  for amount in category_spent:
    category_percentages.append((round((amount / sum(category_spent)), 2))*100)
  
  graph = "Percentage spent by category\n"
  graph_percentages = range(100, -1, -10)

  for percentage in graph_percentages:
    graph += str(percentage).rjust(3) + "| "
    for cat_perc in category_percentages:
      if cat_perc >= percentage:
        graph += "o  "
      else:
        graph += "   "
    graph += "\n"
  
  graph += "    ----" + ("---" * (len(category_names) - 1)) + "\n     "

  longest_name = 0

  for name in category_names:
    if len(name) > longest_name:
      longest_name = len(name)

  for i in range(longest_name):
    for name in category_names:
      if len(name) > i:
        graph += name[i] + "  "
      else:
        graph += "   "
    if i < longest_name-1:
      graph += "\n     "

  return(graph)
