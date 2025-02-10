import pickle
ExpenseList=[
             {
                 'Month':9,
                 'Date':20,
                 'Number':5000,
                 'Category':1,
                 'title':"Bought clothes"
             },
             #{
                 
             #}
             ]
with open('collab-test/ExpenseData.pkl', 'wb') as data:
    pickle.dump(ExpenseList,data)