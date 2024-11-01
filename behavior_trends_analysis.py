import pandas as pd
def import_data(filename):
    return pd.read_excel(filename)
data = import_data("Customer_Behavior.xlsx")
data.head("Customer_Behavior.xlsx")

def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    
    filtered_df = df.dropna(subset=['CustomerID'])    
    filtered_df = filtered_df[(filtered_df['Quantity'] >= 0) & (filtered_df['UnitPrice'] >= 0)]    
    return filtered_df

def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    
    loyal_customers_df = df.groupby('CustomerID', as_index=False).size()    
    loyal_customers_df.columns = ['CustomerID', 'PurchaseCount']     
    loyal_customers_df = loyal_customers_df[loyal_customers_df['PurchaseCount'] >= min_purchases]    
    return loyal_customers_df
def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:    
    
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])    
    df['TotalRevenue'] = df['Quantity'] * df['UnitPrice']    
    df['Quarter'] = df['InvoiceDate'].dt.to_period('Q')    
    quarterly_revenue_df = df.groupby('Quarter', as_index=False)['TotalRevenue'].sum()    
    quarterly_revenue_df.columns = ['quarter', 'total_revenue']
    return quarterly_revenue_df

def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    
    product_demand_df = df.groupby('ProductID', as_index=False)['Quantity'].sum()    
    product_demand_df.columns = ['ProductID', 'TotalQuantitySold']   
    product_demand_df = product_demand_df.sort_values(by='TotalQuantitySold', ascending=False)    
    top_n_products = product_demand_df.head(top_n)    
    return top_n_products

def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    
    product_summary_df = df.groupby('ProductID', as_index=False).agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    )    
    product_summary_df.rename(columns={'ProductID': 'product'}, inplace=True)    
    return product_summary_df

def answer_conceptual_questions() -> dict:
    
    answers = {
        "Q1": {"A"},  
        "Q2": {"B"},  
        "Q3": {"C"},  
        "Q4": {"A"},  
        "Q5": {"A"},    
        
    }
    return answers