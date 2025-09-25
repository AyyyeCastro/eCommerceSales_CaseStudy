import pandas as pd

#### Data prepartion layer ####
def prepare_data(df):
    """ Cleans & prepares the data once, rather than redudantly in each function."""
    print("Preparing data...")

    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    
    df['order_month'] = df['order_date'].dt.to_period('M')
    df['profit_margin'] = (df['absolute_profit'] / df['total_price']) * 100
    
    return df

#### Data analysis functions ####
def getAvgAbsoluteProfit(df):
    """Creates a .CSV, on the average absolute profit by category."""
    averages = df.groupby('category')['absolute_profit'].describe()
    avgAbsProfit_df = averages.reset_index()
    avgAbsProfit_df.to_csv('manipulated_csv/average_absoluteProfit_by_category.csv', index=False)
    print("Generated: average_absoluteProfit_by_category.csv")

def getAvgProfitMarginByCategory(df):
    """Creates a .CSV, on the average profit margin by category."""
    averages = df.groupby('category')['profit_margin'].describe()
    avgProfitMargin_df = averages.reset_index()
    avgProfitMargin_df.to_csv('manipulated_csv/average_ProfitMargin_by_category.csv', index=False)
    print("Generated: average_ProfitMargin_by_category.csv")

def getAvgProfitMarginByPaymentMethod(df):
    """Creates a .CSV, on the average profit margin by payment method."""
    averages = df.groupby('payment_method')['profit_margin'].describe()
    avgProfitMargin_df = averages.reset_index()
    avgProfitMargin_df.to_csv('manipulated_csv/average_ProfitMargin_by_paymentMethod.csv', index=False)
    print("Generated: average_ProfitMargin_by_paymentMethod.csv")

def getAvgProfitMarginByRegion(df):
    """Creates a .CSV, on the average profit margin by region."""
    averages = df.groupby('region')['profit_margin'].describe()
    avgProfitMargin_df = averages.reset_index()
    avgProfitMargin_df.to_csv('manipulated_csv/average_ProfitMargin_by_region.csv', index=False)
    print("Generated: average_ProfitMargin_by_region.csv")

def getAvgProfitMarginByMonth(df):
    """Creates a .CSV, on the average profit margin by month."""
    averages = df.groupby('order_month')['profit_margin'].describe()
    monthly_profit_df = averages.reset_index()
    monthly_profit_df.to_csv('manipulated_csv/average_ProfitMargin_by_month.csv', index=False)
    print("Generated: average_ProfitMargin_by_month.csv")

def getAvgDeliveryTimeByCategory(df):
    """Creates a .CSV, on the average delivery time by category."""
    averages = df.groupby('category')['delivery_time_days'].describe()
    avgDT_df = averages.reset_index()
    avgDT_df.to_csv('manipulated_csv/average_deliveryTimeDays_by_category.csv', index=False)
    print("Generated: average_deliveryTimeDays_by_category.csv")

def getCategoryReturnCount(df):
    """Creates a .CSV, on the total return count by category."""
    returns_df = df[df['returned'] == 'Yes']
    returnCount = returns_df['category'].value_counts()
    categoricalReturns_df = returnCount.reset_index()
    categoricalReturns_df.to_csv('manipulated_csv/total_returnCount_by_category.csv', index=False)
    print("Generated: total_returnCount_by_category.csv")

def getRegionalReturnCount(df):
    """Creates a .CSV, on the total return count by region."""
    returns_df = df[df['returned'] == 'Yes']
    returnCount = returns_df['region'].value_counts()
    regionalReturns_df = returnCount.reset_index()
    regionalReturns_df.to_csv('manipulated_csv/total_returnCount_by_region.csv', index=False)
    print("Generated: total_returnCount_by_region.csv")

def getTotalSalesByRegion(df):
    """Creates a .CSV, on the total sale count by region."""
    returns_df = df[df['returned'] == 'No']
    returnCount = returns_df['region'].value_counts()
    RegionalSales_df = returnCount.reset_index()
    RegionalSales_df.to_csv('manipulated_csv/total_SaleCount_by_region.csv', index=False)
    print("Generated: total_SaleCount_by_region.csv")

def getTotalSalesByMonth(df):
    """Creates a .CSV, on the total sale count by month."""
    sales_df = df[df['returned'] == 'No']
    monthly_sales = sales_df.groupby('order_month').size()
    monthly_sales_df = monthly_sales.reset_index(name='sale_count')
    monthly_sales_df.to_csv('manipulated_csv/total_sales_by_month.csv', index=False)
    print("Generated: total_sales_by_month.csv")

def getTotalSalesByCategory(df):
    """Creates a .CSV, on the total sale count by category."""
    returns_df = df[df['returned'] == 'No']
    returnCount = returns_df['category'].value_counts()
    RegionalSales_df = returnCount.reset_index()
    RegionalSales_df.to_csv('manipulated_csv/total_SaleCount_by_category.csv', index=False)
    print("Generated: total_SaleCount_by_category.csv")


def getAvgReturnRateByRegion(df):
    """Creates a .CSV, on the return rate percentage for each region (based on regions total sales)"""
    total_orders = df.groupby('region').size()
    returns_df = df[df['returned'] == 'Yes']
    total_returns = returns_df.groupby('region').size()
    regional_stats_df = pd.DataFrame({
        'total_orders': total_orders,
        'total_returns': total_returns
    })
    
    regional_stats_df['total_returns'] = regional_stats_df['total_returns'].fillna(0)
    
    regional_stats_df['return_rate_pct'] = (
        regional_stats_df['total_returns'] / regional_stats_df['total_orders']
    ) * 100
    
    regional_stats_df = regional_stats_df.reset_index()
    regional_stats_df.to_csv('manipulated_csv/average_return_rate_by_region.csv', index=False)
    print("Generated: return_rate_by_region.csv")

def getAvgProfitMarginByCategoryAndGender(df):
    """Creates a .CSV on the avg profit margin for each gender within each category."""
    averages = df.groupby(['category', 'customer_gender'])['profit_margin'].mean()
    
    result_df = averages.reset_index()
    result_df.to_csv('manipulated_csv/average_profitMargin_by_categoryAndgender.csv', index=False)
    print("Generated: average_profit_margin_by_category_gender.csv")

def groupCategoryByAge(df):
    """Creates a .CSV, on customer age statistics by category."""
    averages = df.groupby('category')['customer_age'].describe()
    avgAge_df = averages.reset_index()
    avgAge_df.to_csv('manipulated_csv/average_age_by_category.csv', index=False)
    print("Generated: average_age_by_category.csv")

def groupCategoryByGender(df):
    """Creates a .CSV, on the total gender count by category."""
    averages = df.groupby('category')['customer_gender'].value_counts()
    avgAge_df = averages.reset_index()
    avgAge_df.to_csv('manipulated_csv/total_genderCount_by_category.csv', index=False)
    print("Generated: total_gender_by_category.csv")

#### run program ####
def main():
    raw_df = pd.read_csv('raw_csv/ecommerce_sales_34500.csv')
    prepared_df = prepare_data(raw_df)


    # getAvgAbsoluteProfit(prepared_df)
    # getAvgProfitMarginByCategory(prepared_df)
    # getAvgProfitMarginByPaymentMethod(prepared_df)
    # getAvgProfitMarginByRegion(prepared_df)
    # getAvgProfitMarginByMonth(prepared_df)
    # getAvgDeliveryTimeByCategory(prepared_df)
    # getCategoryReturnCount(prepared_df)
    # getRegionalReturnCount(prepared_df)
    # getTotalSalesByRegion(prepared_df)
    # getTotalSalesByMonth(prepared_df)
    # getAvgReturnRateByRegion(prepared_df)
    # groupCategoryByAge(prepared_df)
    # groupCategoryByGender(prepared_df)
    # getAvgProfitMarginByCategoryAndGender(prepared_df)
    # getTotalSalesByCategory(prepared_df)

    print("--- Complete ---")

if __name__ == "__main__":
    main()