n = 100
SSxx = 1400
SSxy = 4000
x_bar = 2
y_bar = 10
R_2 = 0.8

SSR = (SSxy - (n * x_bar * y_bar)) ** 2 / (SSxx - (n * (x_bar ** 2)))
print("SSR = ({} - ({} * {} * {}))^2 / ({} - ({} * ({}^2) = {}".format(SSxy, n, x_bar, y_bar, SSxx, n, x_bar, SSR))

SST = SSR / R_2
print("SST = {} / {} = {}".format(SSR, R_2, SST))

SSE = SST - SSR
print("SSE = {} - {} = {}".format(SST, SSR, SSE))

print()

b_1_hat = (SSxy - (n * x_bar * y_bar)) / (SSxx - (n * (x_bar ** 2)))
print("b_1_hat = ({} - ({} * {} * {}) / ({} - ({} * ({}^2) = {}".format(SSxy, n, x_bar, y_bar, SSxx, n, x_bar, b_1_hat))

b_0_hat = y_bar - (b_1_hat * x_bar)
print("b_0_hat = {} - ({} * {}) = {}".format(y_bar, b_1_hat, x_bar, b_0_hat))