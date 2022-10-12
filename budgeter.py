

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_data():
  row_list = []
  import csv

  with open('data.csv', newline='') as data:
   reader = csv.DictReader(data)
   for row in reader:
     output = row['date'], row['transaction'], row['amount'], row['note']
     row_list.append(output)

   return row_list

def view_previous_entries(entries):
   entries = load_data()
   for entry in entries:
       print(entry[0], entry[1], entry[2], entry[3])

def display_profit_loss(entries):
   expense = 0
   income = 0
   entries = load_data()
   for entry in entries:
       if entry[1] == 'Expense':
           expense += int(entry[2])
       elif entry[1] == 'Income':
           income += int(entry[2])

   profit_loss = income - expense

   if profit_loss >= 0:
       print(f'The total income is {income}.\n',f'The total expense is {expense}.\n',f'The current profit is ${profit_loss}.')
   elif profit_loss < 0:
       print(f'The total income is {income}.\n',f'The total expense is {expense}.\n', f'The current loss is ${profit_loss}')  
 
def add_new_entry(entries):
   
    import csv
    
    with open('data.csv','a', newline='') as data:
      new_entry = {'date':'','transaction':'','amount':'','note':''}
      new_entry['date'] = input('Date of transaction (YYYY-MM-DD):')
      income = input('Was this Income (Y/N)):')
      if income == 'Y':
          new_entry['transaction'] = 'Income'
      else:
          new_entry['transaction'] = 'Expense'

      new_entry['amount'] = int(input('Amount:'))
      while new_entry['amount'] <= 0:
        try:
           new_entry['amount'] = int(input('Please enter a number greater than O: '))
        except ValueError as err:
           print('That was not good input, please try again!')
      
      new_entry['note'] = input('Describe the transaction):')

      writer = csv.DictWriter(data, FIELDNAMES)

      writer.writerow(new_entry)


def get_menu_choice():
  choice = None
  
  while choice == None:
    try:
      choice = int(input('> '))
    except ValueError as err:
      print('That was not a valid entry, please try again!')
      continue

    if choice < 1 or choice > 4:
      print('That was not a valid choice, please try again!')
      choice = None

  return choice

def print_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Exit\n')

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_data()

  while True:
    print_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      break

main()
