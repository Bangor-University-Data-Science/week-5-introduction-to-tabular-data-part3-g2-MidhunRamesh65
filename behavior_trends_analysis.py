import pandas as pd
def import_data(filename):
    return pd.read_excel(filename)
data = import_data("Customer_Behavior.xlsx")
data.head("Customer_Behavior.xlsx")

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    
    filtered_df = df.dropna(subset=['CustomerID'])
    
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]
    
    return filtered_df