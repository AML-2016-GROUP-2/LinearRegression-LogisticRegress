from numpy import loadtxt, zeros, ones, array, linspace, logspace
from pylab import scatter, show, title, xlabel, ylabel, plot, contour



#Load the dataset
data = loadtxt('ex1data1.txt', delimiter=',')

#Plot the data
scatter(data[:, 0],data[0:], marker='o', c='b')
title('Profits distribution')
xlabel('Population of City in 10,000s')
ylabel('Profit in $10,000s')
show()

#seting up data 
X = data[:, 0]
y = data[:, 1]

print X
print "y here",y

#number of training samples
m = y.size

#Add a column of ones to X (interception data)
it = ones(shape=(m, 2))
it[:, 1] = X
print "here is it",it
#Initialize theta parameters
theta = zeros(shape=(2, 1))
print theta
#Some gradient descent settings
iterations = 1500
alpha = 0.01

predictions = it.dot(theta).flatten()
print predictions
