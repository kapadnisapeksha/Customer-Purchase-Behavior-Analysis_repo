# Import necessary libraries
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display all columns when printing DataFrame
pd.set_option('display.max_columns', None)

# Import the dataset
#this is my file path where the data set is located in my PC .plz change according to your data set location
df = pd.read_csv(r"C:/Users/DELL/OneDrive/Desktop/Assement Attempt 1/Customer Purchase Behavior Analysis/customer_data.csv")

# Display the shape of the DataFrame
print('DataFrame Shape:')
#FILL THE CODE HERE
print(df.shape)

# Display the first 5 rows of the DataFrame
print('First 5 Rows of Data:')
#FILL THE CODE HERE
print(df.head(5))


# Display columns and their types
print('Columns and Data Types:')
#FILL THE CODE HERE
print(df.dtypes)

# Data Cleaning

# Drop the 'index' column
#FILL THE CODE HERE
print(df.drop('index',axis=1))
    
# Cast 'Year' as type string and handle potential floating point issues
#FILL THE CODE HERE
df['Year']=df["Year"].astype(str)
    
# Convert 'Date' from object to datetime
#FILL THE CODE HERE
df['Date'] = pd.to_datetime(df['Date'])

    
# Define age groups
age_groups = {
    (0, 18): "0-18",
    (19, 30): "19-30",
    (31, 40): "31-40",
    (41, 50): "41-50",
    (51, 60): "51-60",
    (61, 70): "61-70",
    (71, float("inf")): "71 & above"
}

# Create a new column for age groups based on 'Customer Age'
#FILL THE CODE HERE

df['Age Group']=pd.cut(df['Customer Age'],bins=[0,18,30,40,50,60,70,float("inf")],labels= ['0-18', '19-30', '31-40', '41-50', '51-60', '61-70', '71 & above'])
# Calculate profit margin. Create a new column in the DF by name margin. Margin is computed as Revenue-Cost
#FILL THE CODE HERE
df['Margine']=df['Revenue'] - df['Cost']
    
# Drop rows with null values
#FILL THE CODE HERE
df=df.dropna()

# Data Exploration

# Examine the distribution of numerical variables in a tabular form
#FILL THE CODE HERE
print(df.describe())

# Demographic Analysis

# Age Distribution
# Define the order for age groups
age_order = ["0-18", "19-30", "31-40", "41-50", "51-60", "61-70", "71 & above"]

# Create a sorting column to maintain order
#FILL THE CODE HERE


# Sort the DataFrame based on the sorting column
#FILL THE CODE HERE


# Plot age distribution (Use sns.histplot)
#FILL THE CODE HERE

# Plot 1 Details
plt.title("Distribution of Customer Age")
plt.xlabel("Customer Age")
plt.ylabel("Count")
plt.savefig('agedistribution.jpg')
plt.clf()

# Gender Distribution (Use sns.histplot())
#FILL THE CODE HERE

# Plot 2 Details
plt.title("Distribution of Customer Gender")
plt.xlabel("Customer Gender")
plt.ylabel("Count")
plt.savefig('genderdistribution.jpg')
plt.clf()

# Country Distribution (Use sns.histplot())
#FILL THE CODE HERE

# Plot 3 Details
plt.title("Distribution of Customer Country")
plt.xlabel("Customer Country")
plt.ylabel("Count")
plt.savefig('countrydistribution.jpg')
plt.clf()

# State Distribution (Use sns.histplot())
#FILL THE CODE HERE

# Plot 4 Details
plt.title("Distribution of Customer State")
plt.xlabel("Customer State")
plt.ylabel("Count")
plt.savefig('statedistribution.jpg')
plt.clf()

# Purchase Behavior Analysis
# Product Category Preferences by Age Group
# Group the DataFrame by 'Age Group' and 'Product Category'
#FILL THE CODE HERE


# Pivot the data for heatmap
#FILL THE CODE HERE


# Create heatmap for product category preferences by age group
# Use annot=False, cmap="YlGnBu", cbar=True
#FILL THE CODE HERE

# Plot 5 Details
plt.xlabel("Product Category")
plt.ylabel("Age Group")
plt.title("Product Category Preferences by Age Group")
plt.savefig('productcatpref.jpg')
plt.clf()

# Subcategory Preferences by Age Group
# Group the DataFrame by 'Age Group' and 'Sub Category'

# Create bar chart for subcategory preferences by age group
plt.figure(figsize=(10, 6))
#FILL THE CODE HERE

# Plot 6 Details
plt.title("Product Preferences by Age Group")
plt.xlabel("Sub Category")
plt.ylabel("Count")
plt.legend(title="Age Group")
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.savefig('subcatpref.jpg')
plt.clf()

# Financial Metrics Analysis
# Compute the average unit price and quantity purchased by different age groups and create a dataframe
#FILL THE CODE HERE


# Create bar chart for Average Unit Price by Age Group
#FILL THE CODE HERE

# Plot 7 Details
plt.title("Comparison of Average Unit Price by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Unit Price")
plt.savefig('agevsprice.jpg')
plt.clf()

# Create bar chart for Average Quantity by Age Group
#FILL THE CODE HERE

# Plot 8 Details
plt.title("Comparison of Average Quantity by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Average Quantity")
plt.savefig('agevsquantity.jpg')
plt.clf()

# Distribution of Revenue by Age
# Group total revenue by customer age
#FILL THE CODE HERE


# Plot a Scatter Plot - total revenue by customer age
#FILL THE CODE HERE

# Plot 9 Details
plt.xlabel('Age')
plt.ylabel("Total Revenue")
plt.title('Total Revenue by Age')
plt.savefig('agevsrevenue.jpg')
plt.clf()

# Profitability Assessment

# Calculate the average margin by product category and subcategory
#FILL THE CODE HERE


# Sort the DataFrame by margin and select the top 10 products
#FILL THE CODE HERE


# Create horizontal bar chart for mean margin by subcategory for top 10 products
#FILL THE CODE HERE

# Plot 10 Details
plt.title("Mean Margin by Sub Category")
plt.xlabel("Product Margin")
plt.ylabel("Sub Category")
plt.savefig('profitability.jpg')
plt.clf()

# Temporal Trends

# Revenue Trend

# Sort DataFrame by date
#FILL THE CODE HERE


# Plot revenue trend over time. Use sns.lineplot
#FILL THE CODE HERE

# Plot 11 Details
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Revenue Trends Over Time")
plt.savefig('revenuetrend.jpg')
plt.clf()

# Monthly Revenue Comparison by Year
# Filter data by year
year1 = df[df["Year"] == "2015"]
year2 = df[df["Year"] == "2016"]

# Define the order of months
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# Group data by month and sum revenue
monthly_rev2015 = year1.groupby('Month')['Revenue'].sum().reindex(months_order).reset_index()
monthly_rev2016 = year2.groupby('Month')['Revenue'].sum().reindex(months_order).reset_index()

# Plot 2 separate line plots to compare monthly revenue for 2015 and 2016
#FILL THE CODE HERE

# Plot 12 Details
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Revenue Trend for 2015 and 2016")
plt.savefig('monthlyrevenue.jpg')
plt.clf()

# Geographic Analysis

# Average Revenue generated by Country
labels = ['France', 'Germany', 'United Kingdom', 'United States']
sizes = df.groupby("Country")["Revenue"].mean()

# Create pie chart for average revenue generated by country. Set autopct='%1.1f%%'
#FILL THE CODE HERE

# Plot 13 Details
plt.title("Percentage of the Average Revenue Generated by Country")
plt.savefig("AvRevenueByCountry.jpg")
plt.clf()

# Average Unit Price per Product by Country
# Group data by country and product category to calculate mean unit price
#FILL THE CODE HERE


# Create bar chart for average unit price per product by country
#FILL THE CODE HERE

# Plot 14 Details
plt.xlabel("Country")
plt.ylabel("Mean Unit Price")
plt.title("Comparison of Mean Unit Price by Country")
plt.savefig("AvUnitPricePerProductByCountry.jpg")
plt.clf()

