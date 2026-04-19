from extract import extracter
from itertools import combinations

def explore(): #initial exploritory analysis
    cust_df = extracter() # extract data
    print()
    print("Data Tables with possible Joins")
    features = {} #features

    for i,j in cust_df.items(): # create a dictionary of features to iterate through
        #print(f"{i} columns:")
        #print(j.columns.to_list())
        #print()
        features[i] =  j.columns.to_list()
        #print(features)
         
    for (f1, cols1),(f2, cols2) in combinations(features.items(), 2): # find those that match
        in_common = set(cols1).intersection(cols2)
        if len(in_common) > 0:
            print()
            print(f" Table: {f1}, Table: {f2}, Table: {in_common}") #print tables with possible matches
            
            priority_keywords = ["id","_id","key","_key","product"]

        for col in in_common:
            if any(k in col for k in priority_keywords):
                print(f"Most likely joins on: {col}")
            else:
                print(f"common column {col}")
    
    
    return


explore()