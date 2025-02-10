import pickle
ExpenseList=[]
with open('ExpenseData.pkl', 'rb') as data:
    ExpenseList.append(data)
#def add_expense() #include the filter
def main():
    print("Wellcome to Expense Tracker system.\nYou could enter the following numbers\n1. Add new Expense\n2. Delet the expense\n3. View the Expense\n4. Calculate the Expense\n5. Quit and Save")
main()