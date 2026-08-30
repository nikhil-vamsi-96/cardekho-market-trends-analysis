import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CarDekho dataset
# df = pd.read_csv('data/car_data.csv')

def plot_market_trends(df):
    """Create the main portfolio charts used in the project."""
    df = df.copy()
    df['Depreciation'] = df['Present_Price'] - df['Selling_Price']
    df['Vehicle_Age'] = 2026 - df['Year']

    # 1. Average selling price by manufacturing year
    yearly = df.groupby('Year')['Selling_Price'].mean()
    yearly.plot(marker='o', figsize=(9, 5), title='Average Selling Price by Manufacturing Year')
    plt.xlabel('Manufacturing Year')
    plt.ylabel('Average Selling Price (Lakhs)')
    plt.tight_layout()
    plt.show()

    # 2. Selling price vs kilometres driven
    plt.figure(figsize=(9, 5))
    sns.scatterplot(data=df, x='Kms_Driven', y='Selling_Price')
    plt.title('Selling Price vs Kilometres Driven')
    plt.xlabel('Kilometres Driven')
    plt.ylabel('Selling Price (Lakhs)')
    plt.tight_layout()
    plt.show()

    # 3. Average depreciation by vehicle age
    age_dep = df.groupby('Vehicle_Age')['Depreciation'].mean()
    age_dep.plot(marker='o', figsize=(9, 5), title='Average Price Depreciation vs Vehicle Age')
    plt.xlabel('Vehicle Age (Years)')
    plt.ylabel('Average Depreciation (Lakhs)')
    plt.tight_layout()
    plt.show()

    # 4. Fuel type distribution
    plt.figure(figsize=(8, 5))
    df['Fuel_Type'].value_counts().plot(kind='bar')
    plt.title('Vehicles by Fuel Type')
    plt.xlabel('Fuel Type')
    plt.ylabel('Number of Vehicles')
    plt.tight_layout()
    plt.show()

    # 5. Transmission distribution
    plt.figure(figsize=(8, 5))
    df['Transmission'].value_counts().plot(kind='bar')
    plt.title('Vehicles by Transmission Type')
    plt.xlabel('Transmission')
    plt.ylabel('Number of Vehicles')
    plt.tight_layout()
    plt.show()

    # 6. Seller type distribution
    plt.figure(figsize=(8, 5))
    df['Seller_Type'].value_counts().plot(kind='bar')
    plt.title('Vehicles by Seller Type')
    plt.xlabel('Seller Type')
    plt.ylabel('Number of Vehicles')
    plt.tight_layout()
    plt.show()

    # 7. Previous-owner distribution
    plt.figure(figsize=(8, 5))
    df['Owner'].value_counts().sort_index().plot(kind='bar')
    plt.title('Vehicles by Number of Previous Owners')
    plt.xlabel('Owner Category')
    plt.ylabel('Number of Vehicles')
    plt.tight_layout()
    plt.show()

# Example:
# df = pd.read_csv('data/car_data.csv')
# plot_market_trends(df)
