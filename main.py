import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
 
sales = pd.read_csv('cleaned_store_sales.csv')

revenue_by_date = sales.groupby('price')['units_sold'].sum()
print(revenue_by_date)

corr = sales.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show() 