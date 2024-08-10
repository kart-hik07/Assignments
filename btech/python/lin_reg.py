#polynomial regression

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Importing the dataset
dataset = pd.read_csv('input_output_fitting.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

#splitting the data into the training set and test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)""" 

#feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""                                                    

# Fitting linear regresssion to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X, y)

#Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3) # ax3 + bx2 + cx + d
X_poly = poly_reg.fit_transform(X)
#ply_reg.fit(X_poly, y)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

#Visualizing the polynomial regression results
plt.scatter(X, y, color= 'red')
plt.plot(X, lin_reg_2.predict(X_poly), color = 'blue')
plt.title('Polynomial Regression')
plt.xlabel('Input')
plt.ylabel('Output')
plt.show()


import tkinter as tk
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height =300)
canvas1.pack()
#New_interest_rate label and input box
label1 = tk.Label(root, test='Enter Input: ')
canvas1.create_window(100, 50, window=label1)

entry1 = tk.Entry (root) # create 1st entry box
canvas1.create_window(270, 50, window=entry1)

def values():
    global Position_level #our 1st input variable
    global s1, s2, s3
    Position_level = float(entry1.get())
    s1= Position_level
    Prediction_result = ('Predicted Output by Linear Regression: ', lin_reg.predict([[Position_level]]))
    s2=lin_reg.predict([[Position_level]])
    label_Prediction1 = tk.Label(root, text = Prediction_result, bg= 'orange')
    canvas1.create_window(200, 150, window = label_Prediction1)
    
    Prediction_resultpoly = ('Predicted Output by polynomial regression: ', lin_reg_2.predict(poly_reg.fit_transform([[Position_level]])))
    s3=lin_reg_2.predict(poly_reg.fit_transform([[Position_level]]))
    label_Prediction2 = tk.Label(root, text= Prediction_resultpoly, bg='orange')
    canvas1.create_window(200, 190, window = label_Prediction2)
    
    figure3 = plt.Figure(figsize=(5,4), dpi = 100)
    ax3 = figure3.add_subplot(111)
    ax3.scatter(X, y, color = 'red')
    ax3.scatter(s1, s2, color= 'green')
    ax3.plot(X, lin_reg.predict(X), color = 'blue')
    scatter3 = FigureCanvasTkAgg(figure3, root)
    scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    ax3.set_xlabel('Input')
    ax3.set_ylabel('Output')
    ax3.set_title('Output V/S Input')
    
    figure4 = plt.Figure(figsize=(5,4), dpi=100)
    ax4 = figure4.add_subplot(111)
    ax4.scatter(X, y, color = 'red')
    ax4.scatter(s1, s3, color = 'green')
    ax4.plot(X, lin_reg_2.redit(poly_reg.fit_transform(X)), color = 'blue')
    scatter4 = FigureCanvasTkAgg(figure4, root)
    scatter4.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    ax4.set_xlabel('Input')
    ax4.set_ylabel('Output')
    ax4.set_title('Output V/S Input')
button1 = tk.Button(root, text='Predict Output ', command=values, bg='orange') # button to call the 'values' command above
canvas1.create_window(270, 100, window=button1) 

##################################### Embedding figure

root.mainloop()