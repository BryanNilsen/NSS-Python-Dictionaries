stockDict = {'GM': 'General Motors',
             'CAT': 'Caterpillar', 'BP': "British Petroleum"}

purchases = [
    ('GM', 100, '10-sep-2001', 48),
    ('CAT', 100, '1-apr-1999', 24),
    ('GM', 200, '1-jul-1998', 56),
    ('BP', 200, '1-jul-1998', 56)
]


# # loop through purchases (list of tuples)
# for purchase in purchases:
#     # declare variable company and set equal to 0 index value (company initials)
#     company = purchase[0]

#     # now loop through stockDict (dictionary)
#     for stock in stockDict:
#         # if the company initials (previously declared company variable) exists in stockDict, then grab the company full name
#         if company == stock:
#             company = stockDict[stock]

#     #perform cost calculation on purchase values at indexes 1 and 3
#     cost = str('${:,.2f}'.format(purchase[1] * purchase[3]))

#     print("I purchased " + company + " stock for " + cost + ".")

#     print("I purchased {0} stock for {1}.".format(company, cost))




# for purchase in purchases:
#     company = purchase[0]
#     for stock in stockDict:
#         if company == stock:
#             company = stockDict[stock]
#     cost = str('${:,.2f}'.format(purchase[1] * purchase[3]))
#     print("I purchased {0} stock for {1}.".format(company, cost))


report = {}
for purchase in purchases:
  abbrev = purchase[0]
  full_name = stockDict[abbrev]
  no_of_shares = purchase[1]
  purch_date = purchase[2]
  purch_price = purchase[3]
  full_purch_price = no_of_shares * purch_price
  print(f"I purchased {full_name} stock on {purch_date} for {full_purch_price}")

  try:
    report[abbrev].append(purchase)
  except KeyError:
    report[abbrev] = list()
    report[abbrev].append(purchase)

for abbrev, purchases in report.items():
  print(f"------- {abbrev} -------")
  total_portfolio_stock_value = 0
  for purchase in purchases:
    total_portfolio_stock_value += purchase[1] * purchase[3]
    print(f"     {purchase}")
  print(f"Total value of stock in portfolio: ${total_portfolio_stock_value}\n\n")



