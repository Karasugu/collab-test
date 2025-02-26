import pickle

#create the list
ExpenseList=[]

#open saved data 
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
                #ensure added expense is positive. Give user instruction and return to input
                if Number <= 0:
                    print("Please do not enter a nagative number or 0")
                else:
                    return Number
            #run when error occurred
            except:
                print("Please choose a number")
    #sorts the expenses into 5 categories         
    def InputCategory():
        while True:
            try:
                print("1.FOOD\n2.CLOTHING\n3.HOUSING\n4.TRANSPORT\n5.ENTERTAINMENT")
                Category = int(input("Enter the number 1-5:"))
                #run when user input != value of 1-5. Give user instruction and return to input
                if Category < 1 or Category > 5:
                    print("please enter 1-5")
                else:
                    return Category
            #run when error occurred    
            except ValueError:
                print("please choose a valid number")
                
    #add expenses as dictionary into ExpenseList
    ExpenseList.append({'Title':InputTitle(),'Date':InputDate(),'Number':InputNumber(),'Category':InputCategory()})
    print("Expense save succefully")
    def SortKey(i):
        return i['Date']
    ExpenseList.sort(key=SortKey)
    #auto save after action is complete
    Save()

#Delete function
def DeleteExpense():
    TitleDelete = input("What title of the expense you want to delete")
    global ExpenseList
    #find the dictionary to delete through the Title
    for f in ExpenseList:
        if TitleDelete == f['Title']:
            ExpenseList = [e for e in ExpenseList if e['Title'] != TitleDelete]
            #auto save after successfully deleted
            Save()
            print("Successfully deleted the expense")
        else:
            continue
    #run when the delete action fails (Title not found)    
    else:
        print("Expense not found")
    
def ViewExpense():
    #Allows the user to view each category of reminders
    print("Expense Categories:")
    print("1. FOOD")
    print("2. CLOTHING")
    print("3. HOUSING")
    print("4. TRANSPORT")
    print("5. ENTERTAINMENT")
    print("6. ALL")
    #The user selects which category of reminders they would like to view. They can also view all reminders at once (6).
    while True:
        try:
            UserChoice = int(input("Which category of expenses would you like to view?(1-6): "))
            #if user input is between 1-5, find the corrisponding Category
            if 1<=UserChoice<=5:
                TemList = [a for a in ExpenseList if a['Category'] == UserChoice]
            #if user input 6 (all), find ExpenseList
            elif UserChoice == 6:
                TemList = [c for c in ExpenseList]
            #run if user input is invalid
            else:
                print("please choose from the list")
            #print the found Catergory (TemList)
            print(TemList)
            #display totle amound of money spend in the found Catergory
            print("Totally $",sum(b['Number'] for b in TemList))
            break
        #run when error occured
        except ValueError:
            print("please choose a valid number")

#save function    
def Save():
    #save data in ExpenseList into ExpenseData.pkl so data carry on
    with open('collab-test/ExpenseData.pkl', 'wb') as data:
        pickle.dump(ExpenseList,data)
    return ("The data has been saved. The funtion has been closed")
def main():
    while True:
        #try:
            choice=int(input("Welcome to Expense Tracker system.\nYou could enter the following numbers\n1. Add new Expense\n2. Delet the expense\n3. View the Expense"))
            if choice== 1:
                AddExpense()
            elif choice == 2:
                DeleteExpense()
            elif choice == 3:
                ViewExpense()
            else:
                print("Please choose from the list")
        #except:
            #print("Please enter a integer from the list")
    print(ExpenseList)
main()
