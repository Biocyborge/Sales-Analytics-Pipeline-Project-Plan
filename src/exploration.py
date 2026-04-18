from extract import extracter
from itertools import combinations

def explore():
    cust_df = extracter()

    priority_keywords = ["id","_id","key","_key"]

    for i,j in cust_df.items():
        #print(f"{i} columns:")
        #print(j.columns.to_list())
        #print()
        features = { i: j.columns.to_list() }
        print(features)
    for (f1, cols1),(f2, cols2) in combinations(features.items(), 2):
        in_common = set(cols1).intersection(cols2)
        print(f1,f2,in_common)
    for col in in_common:
        if any( k in col.lower() for k in priority_keywords):
            print(f"Most likely joins on: {col}")


    

    return


explore()