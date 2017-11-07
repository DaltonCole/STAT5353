from math import sqrt

#x = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5]
#y = [3.0, 3.8, 5.4, 6.9, 8.4, 9.9]

x = [4.5, 4.5, 4.5, 4.0, 4.0, 4.0, 5.0, 5.0, 5.5, 5.0, 0.5, 0.5, 6.0, 6.0, 1.0, 1.0, 1.0]
y = [619, 1049, 1033, 495, 723, 681, 890, 1522, 987, 1194, 163, 182, 764, 1373, 978, 466, 549]


x_2 = [i**2 for i in x]

x_y = [i * j for i,j in zip(x,y)]

y_2 = [i**2 for i in y]


print(x)
print(y)
print(x_2)
print(x_y)
print(y_2)


mean_x = sum(x) / len(x)
mean_y = sum(y) / len(y)
y_bar = mean_y
x_bar = mean_x

n = len(x)

print("n = " + str(n)) 


sum_x_y = sum(x_y)
print("SUM xi*yi = " + str(sum_x_y))

print("n*x_bar*y_bar = " + str(n * mean_x * mean_y))

print("SUM xi^2 = " + str(sum(x_2)))

print("n*x_bar^2 = " + str(n * pow(mean_x, 2)))

b_1_hat = (sum_x_y - (n * mean_x * mean_y)) / (sum(x_2) - (n * pow(mean_x, 2)))
print("B1 = " + str(b_1_hat))

b_0_hat = mean_y - (b_1_hat * mean_x)
print("B0 = " + str(b_0_hat))

print("Y = B0 + B1 X = " + str(b_0_hat) + " + " + str(b_1_hat) + " X")

SST = sum([(i-mean_y)**2 for i in y])
print("SST = " + str(SST))

ssr_formula = lambda i: b_0_hat + (i * b_1_hat)
SSR = sum([(ssr_formula(i) - mean_y) ** 2 for i in x])
print("SSR = " + str(SSR))


SSE = SST - SSR
print("SSE = " + str(SSE))

MST = SST / (len(x) - 1)
print("MST = " + str(MST))

MSR = SSR / 1
print("MSR = " + str(MSR))

MSE = SSE / (len(x) - 2)
print("MSE = " + str(MSE))

f = MSR / MSE
print("F = " + str(f))


print()
SSxx = sum([(i) ** 2 for i in x])
print("SSxx = " + str(SSxx))


"""
t = b_0_hat
print(1/n)
print(mean_x**2/(SSxx - n * mean_x ** 2))
t /= sqrt(pow(MSE, 2) * ((1/n) + (pow(mean_x,2)/ (SSxx - (n * pow(mean_x,2))))))
print("T = " + str(t))
"""

y_2_sum = sum([i*i for i in y])

s_2 = (1/(n-2)) * (y_2_sum - (n * y_bar * y_bar) - (b_1_hat**2 * (SSxx - (n * x_bar**2))))
print("s^2 = " + str(s_2))
s = sqrt(s_2)
print("s = {}".format(s))

s_b0 = s * sqrt((1/n) + (x_bar**2 / (SSxx - (n * x_bar**2))))
print("s_b0 = {}".format(s_b0))

t_b0 = (b_0_hat - 0) / s_b0

print("T for b0=0 : {}".format(t_b0))
print()

s_2_b1_hat = s_2 / (SSxx - (n*(x_bar**2)))
print("s^2_b1_hat = {}".format(s_2_b1_hat))
s_b1_hat = sqrt(s_2_b1_hat)
print("s_b1_hat = {}".format(s_b1_hat))

t_b1 = (b_1_hat - 0) / s_b1_hat
print("T for b1=0 : {}".format(t_b1))
print()

car = 3
s_y_bar = sqrt(s_2 * ((1/n) + ((car - x_bar)**2 / (SSxx - (n * (x_bar**2))))))
print("s_y_bar = {}".format(s_y_bar))

t_alpha_2 = 2.131
L = b_0_hat + (b_1_hat * car) - (t_alpha_2 * s_y_bar)
U = b_0_hat + (b_1_hat * car) + (t_alpha_2 * s_y_bar)
print("L = {}".format(L))
print("U = {}".format(U))