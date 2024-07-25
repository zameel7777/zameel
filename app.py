import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

st.set_page_config(
   page_title="SuperStore Dashboard", 
   page_icon=None, 
   layout="wide",
   initial_sidebar_state = "expanded"
   )


# Add custom CSS for the sidebar width and KPI styling
css = """
<style>

div[data-testid="stMetric"] {
    border: 1px solid #EAEAEA; 
    border-radius: 5px;  
    padding: 10px;
    margin: 5px;
    border-left: 0.5rem solid #FF3345;
    box-shadow: 0 4px 8px 0;
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)


st.write('Hello world!')

st.title('Streamlit :red[Tutorial]')
st.header(':blue[Introduction to Databases]')
st.subheader("🐥💻 Web Applications")
st.text("My First web page in a few lines")

option = st.selectbox(
  'How would you like to be contacted?',
  ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

df = pd.read_csv('Sample Superstore Data.csv')
if st.button('Load data'):
  st.write(df)
else:
  st.info('👆 Click on the button ')

if st.button('Show descriptive statistics analysis'):
  result = df.describe()
  st.write(result)
else:
  st.info('👆 Click on the button ')

sidebar = st.sidebar
with sidebar:
   regions = df['Region'].unique()
   selected_region = st.sidebar.selectbox('Select a Region:', regions)
   df = df[df['Region'] == selected_region]
# KPIS
total_sales = df["Sales"].sum()
total_sales = str(int(total_sales // 1000)) + 'k'
#st.write(total_sales)

total_orders = df["Order ID"].nunique()
#st.write(total_orders)

total_profit = df["Profit"].sum()
total_profit = str(int(total_profit // 1000)) + 'k'
#st.write(total_profit)

total_customers = df["Customer ID"].nunique()
#st.write(total_customers)

#KPI Cards to display
#st.metric(label="Total Sales", value=total_sales)
#st.metric(label="Total Profit", value=total_profit)
#st.metric(label="Number of Orders", value=total_orders)
#st.metric(label="Number of Customers", value=total_customers)



col1, col2, col3, col4= st.columns(4)

with col1:
    st.metric(label="Total Sales", value=total_sales)

with col2:
    st.metric(label="Total Profit", value=total_profit)
   

with col3:
    st.metric(label="Number of Orders", value=total_orders)

with col4:
    st.metric(label="Number of Customers", value=total_customers)

# #Plot 1: Top 10 selling products
# top_product_sales = df.groupby('Product Name')['Sales'].sum()
# top_product_sales = top_product_sales.nlargest(10)
# top_product_sales = pd.DataFrame(top_product_sales).reset_index()
# #Display table
#st.write(top_product_sales)

# #Bar chart
# fig, ax = plt.subplots()
# ax.barh(top_product_sales['Product Name'], top_product_sales['Sales'])
# ax.set_xlabel('Sales Amount')
# ax.set_ylabel('Product Name')
# ax.set_title('Top 10 Selling Products')
# ax.invert_yaxis()  # Invert y-axis to show the highest values at the top

# # Display the plot in Streamlit
# st.pyplot(fig)

# #Plot 2 : Top 10 most profitable products
# top_product_profit = df.groupby('Product Name')['Profit'].sum()
# top_product_profit = top_product_profit.nlargest(10)
# top_product_profit = pd.DataFrame(top_product_profit).reset_index()
# #Bar chart
# fig, ax = plt.subplots()
# ax.barh(top_product_profit['Product Name'], top_product_profit['Profit'])
# ax.set_xlabel('Profit Amount')
# ax.set_ylabel('Product Name')
# ax.set_title('Top 10 Most Profitable Products')
# ax.invert_yaxis()  # Invert y-axis to show the highest values at the top

# # Display the plot in Streamlit
# st.pyplot(fig)

#Place them side by side
col_sales, col_profit = st.columns(2)
# with col_sales:
#    #Plot 1: Top 10 selling products
#     top_product_sales = df.groupby('Product Name')['Sales'].sum()
#     top_product_sales = top_product_sales.nlargest(10)
#     top_product_sales = pd.DataFrame(top_product_sales).reset_index()
#     #Display table
#     #st.write(top_product_sales)

#     #Bar chart
#     fig, ax = plt.subplots()
#     ax.barh(top_product_sales['Product Name'], top_product_sales['Sales'],color = 'red')

#     ax.set_xlabel('Sales Amount')
#     ax.set_ylabel('Product Name')
#     ax.set_title('Top 10 Selling Products')
#     ax.invert_yaxis()  # Invert y-axis to show the highest values at the top

#     # Display the plot in Streamlit
#     st.pyplot(fig)
# with col_profit:
#    #Plot 2 : Top 10 most profitable products
#     top_product_profit = df.groupby('Product Name')['Profit'].sum()
#     top_product_profit = top_product_profit.nlargest(10)
#     top_product_profit = pd.DataFrame(top_product_profit).reset_index()
#     # #Bar chart
#     # fig, ax = plt.subplots()
#     # ax.barh(top_product_profit['Product Name'], top_product_profit['Profit'],color='red')
#     # ax.set_xlabel('Profit Amount')
#     # ax.set_ylabel('Product Name')
#     # ax.set_title('Top 10 Most Profitable Products')
#     # ax.invert_yaxis()  # Invert y-axis to show the highest values at the top
#     # st.pyplot(fig)

#         # Set up Seaborn style
#     sns.set(style="whitegrid")

#     # Plotting the bar chart using Seaborn
#     plt.figure(figsize=(10, 6))
#     sns.barplot(x='Profit', y='Product Name', data=top_product_profit, palette='viridis')
#     plt.xlabel('Sales Amount')
#     plt.ylabel('Product Name')
#     plt.title('Top 10 Selling Products')

#     # Display the plot in Streamlit
#     st.pyplot(plt)

df['Short_Product_Name'] = df['Product Name'].str[:30] + '...'

#Seaborn allows for a lot more customization we will use seaborn for both plots
with col_sales:
    sns.set_style("whitegrid", {'axes.grid': False})
    top_product_sales = df.groupby('Short_Product_Name')['Sales'].sum()
    top_product_sales = top_product_sales.nlargest(10)
    top_product_sales = pd.DataFrame(top_product_sales).reset_index()
    plt.figure(figsize=(15, 10))
    sns.barplot(x='Sales', y='Short_Product_Name', data=top_product_sales, color='red')
    plt.title('Top 10 Selling Products', fontsize=35, pad=30)
    plt.xlabel('Sales', fontsize=35)
    plt.ylabel('Product Name', fontsize=35)
    plt.tick_params(axis='both', which='major', labelsize=30)
    st.pyplot(plt)
with col_profit:
    sns.set_style("whitegrid", {'axes.grid': False})
    top_product_profit = df.groupby('Short_Product_Name')['Profit'].sum()
    top_product_profit = top_product_profit.nlargest(10)
    top_product_profit = pd.DataFrame(top_product_profit).reset_index()
    plt.figure(figsize=(15, 10))
    sns.barplot(x='Profit', y='Short_Product_Name', data=top_product_profit, color='red')
    plt.title('Top 10 Profitable Products', fontsize=35, pad=50)
    plt.xlabel('Profit', fontsize=35)
    plt.ylabel('Product Name', fontsize=35)
    plt.tick_params(axis='both', which='major', labelsize=30)
    st.pyplot(plt)

col_tab , col_stack = st.columns(2)
  #Plot #3  
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Year'] = df['Order Date'].dt.year

sales_by_year = df.groupby(['Year', 'Category'])['Sales'].sum().unstack()

# Custom colors for each category
category_colors = {
    'Furniture': '#FF9797',       
    'Office Supplies': '#A31B1B', 
    'Technology': '#DC4F20'       
}



with col_tab:
    #Pie chart
    fig, ax = plt.subplots(figsize=(12, 10))
    df['Category'].value_counts().plot.pie(autopct="%1.1f%%", ax=ax,colors=['#FF9797', '#A31B1B','#DC4F20'])
    ax.set_title('Distribution of Categories', fontsize=20)
    st.pyplot(fig)
with col_stack:
   tab1,tab2 = st.tabs(["Chart","Data"])
   with tab1:
          # Plot the stacked bar chart with custom colors
    fig, ax = plt.subplots(figsize=(12, 10))
    sales_by_year.plot(kind='bar', stacked=True, ax = ax, color=['#FF9797', '#A31B1B','#DC4F20'])
    ax.set_title('Annual Sales by Category', fontsize=20)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Sales', fontsize=10)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)
   with tab2:
      st.write(sales_by_year)


#Other compontents to test out
st.checkbox('yes')
st.button('Click')
st.radio('Pick your gender',['Male','Female'])
st.selectbox('Pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)