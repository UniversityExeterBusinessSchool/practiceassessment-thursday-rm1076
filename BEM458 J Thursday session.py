#######################################################################################################################################################
# 
# Name: Rakesh Mohankumar
# SID: 740098081
# Exam Date: 27-03-2025
# Module: Programming for Business Analytics (BEMM458_J_2_202425)
# Github link for this assignment:  https://github.com/UniversityExeterBusinessSchool/practiceassessment-thursday-rm1076.git
#
# ######################################################################################################################################################
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# Write your search code here and provide comments. 

# Now we need to search for words 'order' & 'minor' from cx feedback- 
# And we need to store the start and end position is the list.

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""


# My first letter of SID number - 7 , last digit - 1  (740098081)
key_comments = {
    7: 'resolve',
    1: 'order'
}

# Now creating empty list to store the positions 
my_list = []

# Loop through key_comments
for key in key_comments:
    word = key_comments[key]
    start = customer_feedback.find(word)         # to find the starting position of the word
    end = start + len(word)                      # to find the ending, we use starting position + length of the word 
    my_list.append((start, end))                 # add (start, end) as tuple

print(my_list)

# result: [(123, 130), (13, 18)]
# 'resolve' starting at 123rd position and ending at 130th position  
# 'order' starting at 13th position and ending at 18th position   


##########################################################################################################################################################

# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here: 74
# Insert last two digits of ID number here: 81

# Write your code for Operating Profit Margin
def operating_profit_margin(operating_profit, revenue):
    return (operating_profit / revenue) * 100

# Write your code for Revenue per Customer
def revenue_per_customer(total_revenue, total_customers):
    return total_revenue / total_customers

# Write your code for Customer Churn Rate
def churn_rate(customers_lost, total_customers_start):
    return (customers_lost / total_customers_start) * 100

# Write your code for Average Order Value
def average_order_value(total_revenue, number_of_orders):
    return total_revenue / number_of_orders

# Call your designed functions here

opm = operating_profit_margin(74, 200)
rpc = revenue_per_customer(7400, 81)
ccr = churn_rate(8, 81)
aov = average_order_value(7400, 81)

# to print the result
print("Operating Profit Margin:", opm)  # result: 37.0
print("Revenue per Customer:", rpc)    # result: 91.36...
print("Customer Churn Rate:", ccr)     # result: 9.87...
print("Average Order Value:", aov)     # result: 91.36...


##########################################################################################################################################################

# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here

from sklearn.linear_model import LinearRegression
import numpy as np

# writing price and demand in array format first
prices = np.array([20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]).reshape(-1, 1)
demand = np.array([300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 85])

# now in order to train the model
model = LinearRegression()
model.fit(prices, demand)

# to predict the demand when the price is at 52, we use
predicted_demand = model.predict([[52]])
print("Demand at £52:", predicted_demand[0])  # result - 158.17

# to find the best price for oour maximum revenue, we use 
max_revenue = 0
best_price = 0

for val in range(20, 71):
    d = model.predict([[val]])[0]
    revenue = val * d
    if revenue > max_revenue:
        max_revenue = revenue
        best_price = val

print("The best price to maximize revenue is :", best_price)  # result: 40


##########################################################################################################################################################

# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
# max-value = integer(input("Enter your Student ID: ")) - it cannot have '-' for variable

# here we are asking the student id number and we should use int. I am commenting the given code and entering correct code below
max_value = int(input("Enter your Student ID: "))  # forexample 740098081

# random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# to generate 100 random nos between 1 & my student ID 
random_numbers = [random.randint(1, max_value) for i in range(100)] # - here range should not start from 0 since we have to start from 1


# Plotting the numbers in a line chart
# plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
#no 0 instead o
# plt.title(Line Chart of 100 Random Numbers)
# plt.xlabel="Index"
# plt.ylabel="Random Number"
# plt.legend('---')
# plt.grid(True)
# plt.show()


# in order to plot the random numbers 
plt.plot(random_numbers, marker='o', markerfacecolor='green', markeredgecolor='red', linestyle='--', label='Random Numbers', color='blue')
plt.title("Line Chart of 100 Random Numbers")
plt.xlabel("Index")
plt.ylabel("Random Number")
plt.legend()
plt.grid(True)
plt.show()

