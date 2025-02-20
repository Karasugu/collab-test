import pickle

#create the list
ExpenseList=[]

#open saved data in ExpenseList
with open('collab-test/ExpenseData.pkl', 'rb') as data:
    ExpenseList = pickle.load(data)

#add function, asks for 5 inputs   
def AddExpense(): 
    
    #create a title for the event
    def InputTitle():
        while True:
            Title = str(input("What is the title of this expense?"))
            if Title == "":
                print("Name cannot be empty")  # Ensure event name is not empty
            elif len(Title) >= 50:
                print("please enter less than 50 characters") # Ensure event name is not too long
            else:
                return Title
            
    #ask for month
    def InputMonth():
        while True:
            try:
                Month = int(input("What month are you going to choose?\n1 for January\n2 for February\n3 for March\netc\n"))
                if Month >= 13 or Month <= 0: # Ensure input is between 1-12
                    print("Please choose a valid month")
                else:
                    return Month
            except ValueError:
                print("Please choose a valid month") # Ensure input is a valid number
                
    #ask for date
    def InputDate():
        while True:
            try:
                Month = InputMonth()  # Get the month
                Date = int(input("What date are you going to choose?"))
                # Check for valid date based on the month
                if (Month in [1, 3, 5, 7, 8, 10, 12] and 1 <= Date <= 31) or \
                   (Month in [2, 4, 6, 9, 11] and 1 <= Date <= 30): 
                    return float(Date) * 0.01 + Month
                else:
                    print("Please choose a valid date")
            except ValueError:
                print("Please choose a valid date") # Ensure input is a valid number
                
    #ask for amount of expense            
    def InputNumber():
        while True:
            try:
                Number = float(input("What is the number of expenses?"))
                if Number <= 0:
                    print("Please do not enter a nagative number or 0")
                else:
                    return Number
            except:
                print("Please choose a number")
    def InputCategory():
        while True:
            try:
                print("1.FOOD\n2.CLOTHING\n3.HOUSING\n4.TRANSPORT\n5.ENTERTAINMENT")
                Category = int(input("Enter the number 1-5:"))
                if Category < 1 or Category > 5:
                    print("please enter 1-5")
                else:
                    return Category
            except ValueError:
                print("please choose a valid number")

    ExpenseList.append({'Title':InputTitle(),'Date':InputDate(),'Number':InputNumber(),'Category':InputCategory()})
    print("Expense save succefully")
    def SortKey(i):
        return i['Date']
    ExpenseList.sort(key=SortKey)
<<<<<<< HEAD
#def DeleteExpense():
    
    
#def ViewExpense():
   #Allows the user to view each category of reminders
#   print("Expense Categories:")
 #  print("1. FOOD")
  # print("2. CLOTHING")
   #print("3. HOUSING")
   #print("4. TRANSPORT")
   #print("5. ENTERTAINMENT")
   #print("6. ALL")
    #The user selects which category of reminders they would like to view. They can also view all reminders at once.
   #see_my_expenses = print("Which category of expenses would you like to view?(1-6): ")
   #if see_my_expenses == 1:
   #  return 1 in Category
   #if see_my_expenses == 2:
   #  return 2 in Category
   #if see_my_expenses == 3:
   #  return 3 in Category
   #if see_my_expenses == 4:
   #  return 4 in Category
   #if see_my_expenses == 5:
   #  return 5 in Category
   #if see_my_expenses == 6:
   #  print(ExpenseList)
=======
def DeleteExpense():
    
    
def ViewExpense():
   #Allows the user to view each category of reminders
   print("Expense Categories:")
   print("1. FOOD")
   print("2. CLOTHING")
   print("3. HOUSING")
   print("4. TRANSPORT")
   print("5. ENTERTAINMENT")
   print("6. ALL")
    #The user selects which category of reminders they would like to view. They can also view all reminders at once.
   see_my_expenses = print("Which category of expenses would you like to view?(1-6): ")
   if see_my_expenses == 1:
     return 1 in Category
   if see_my_expenses == 2:
     return 2 in Category
   if see_my_expenses == 3:
     return 3 in Category
   if see_my_expenses == 4:
     return 4 in Category
   if see_my_expenses == 5:
     return 5 in Category
   if see_my_expenses == 6:
     print(ExpenseList)
>>>>>>> 4c085e06edceb56df5f054fdc0b0c3f1a1bb9703
    
def QuitSave():
    with open('collab-test/ExpenseData.pkl', 'rb') as data:
        pickle.dump(ExpenseList,data)
    return "The data has been saved. The funtion has been closed"
def main():
    while True:
        try:
<<<<<<< HEAD
            choice=int(input("Welcome to Expense Tracker system.\nYou could enter the following numbers\n1. Add new Expense\n2. Delet the expense\n3. View the Expense\n4. Quit and Save"))
=======
            choice=input(int("Welcome to Expense Tracker system.\nYou could enter the following numbers\n1. Add new Expense\n2. Delet the expense\n3. View the Expense\n4. Quit and Save"))
>>>>>>> 4c085e06edceb56df5f054fdc0b0c3f1a1bb9703
            if choice == 1:
                AddExpense()
            elif choice == 2:
                DeleteExpense()
            elif choice == 3:
                ViewExpense()
            elif choice == 4:
                return QuitSave()
            else:
                print("Please choose from the list")
        except:
            print("Please enter a integer from the list")
    #print(ExpenseList)
main()
