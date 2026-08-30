# CarDekho Market Trends Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
# Update the path if running locally
# df = pd.read_csv('data/car_data.csv')

# Expected columns:
# Car_Name, Year, Selling_Price, Present_Price, Kms_Driven,
# Fuel_Type, Seller_Type, Transmission, Owner

# Example analysis after loading df:
# print(df.shape)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# Price trend by manufacturing year
# yearly_price = df.groupby('Year')['Selling_Price'].mean()
# yearly_price.plot(kind='line', marker='o', title='Average Selling Price by Year')
# plt.xlabel('Manufacturing Year')
# plt.ylabel('Average Selling Price')
# plt.tight_layout()
# plt.show()

# Fuel distribution
# sns.countplot(data=df, x='Fuel_Type')
# plt.title('Fuel Type Distribution')
# plt.tight_layout()
# plt.show()

# Price distribution
# sns.histplot(df['Selling_Price'], kde=True)
# plt.title('Selling Price Distribution')
# plt.tight_layout()
# plt.show()
