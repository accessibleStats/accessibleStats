import tkinter as tk
from numpy import sqrt

# Finding z score from sample mean, pop mean, pop standard deviation, and number of observations
def findzscore():
    x_bar = float(x_barnum.get())
    mu = float(mu_num.get())
    standard = float(pop_standard_num.get())
    obs = float(obs_num.get())
    z_score = (x_bar - mu) / (standard/sqrt(obs))
    display.insert(0, z_score)

window=tk.Tk()
window.geometry("500x500")


# Labels for user input
x_barLabel=tk.Label(window, text="Enter the sample mean (x-bar):")
mu_Label=tk.Label(window, text="Enter the mean of the population mean (mu):")
pop_standard_label=tk.Label(window, text="Enter the population standard deviation (sigma):")
obs_Label=tk.Label(window, text="Enter the number of observations (n):")
display_Label=tk.Label(window, text="The Z score is:")

# Entry boxes for user input
x_barnum=tk.Entry(window)
mu_num=tk.Entry(window)
pop_standard_num=tk.Entry(window)
obs_num=tk.Entry(window)

# Button to generate Z score
Zbtn=tk.Button(window, text="Calculate Z", command=findzscore)

# Box to display Z score
display=tk.Entry(window)

#Locations
x_barLabel.grid(row=0, column=0)
x_barnum.grid(row=0, column=1)
mu_Label.grid(row=1, column=0)
mu_num.grid(row=1, column=1)
pop_standard_label.grid(row=2, column=0)
pop_standard_num.grid(row=2, column=1)
obs_Label.grid(row=3, column=0)
obs_num.grid(row=3, column=1)
Zbtn.grid(row=4, column=1)
display_Label.grid(row=5, column=0)
display.grid(row=5, column=1)

# run
window.mainloop()