import pickle
ExpenseList=[
             {
                 'Title':"Bought clothes",
                 'Date':9.20,
                 'Number':5000,
                 'Category':1
             },
             #{
                 
             #}
             ]
with open('collab-test/ExpenseData.pkl', 'wb') as data:
    pickle.dump(ExpenseList,data)