
y1 = [80,83,83,85]
y2 = [75,75,79,79]
y3 = [74,73,77,78]
y4 = [67,72,74,74]
y5 = [62,63,74,74]
y6 = [60,61,64,65]

y_ = []
y_.append(y1)
y_.append(y2)
y_.append(y3)
y_.append(y4)
y_.append(y5)
y_.append(y6)

a = 6
n = 4
N = a * n

# Y1.
ynumdot = []
for i in range(len(y_)):
	s = 0
	for j in range(len(y_[i])):
		s += y_[i][j]
	s /= len(y_[i])
	ynumdot.append(s)
	print("Y" + str(i + 1) + ". = " + str(s))

# Y..
s = 0
divide_by = 0
for i in range(len(y_)):
	for j in range(len(y_[i])):
		s += y_[i][j]
		divide_by += 1

s /= divide_by
ydotdot = s
print("Y.. = " + str(s))

# Sum of Squares
s = 0
for i in range(len(y_)):
	for j in range(len(y_[i])):
		s += y_[i][j] * y_[i][j]
sum_of_square = s

print("Y^2 = " + str(s))

# SST
sst = sum_of_square - (N * pow(ydotdot, 2))
print("SST = " + str(sum_of_square) + " - " + str(N) + "(" + str(ydotdot) + ")^2 = " + str(sst))

# SSTreatment
numdot_squared = 0
for i in ynumdot:
	numdot_squared += pow(i, 2)
sstreatment = (n * numdot_squared) - (N * pow(ydotdot, 2))

print("SSTreatment = (" + str(n) + " * " + str(numdot_squared) + ") - (" + str(N) + " * " + str(ydotdot) + "^2) = " + str(sstreatment))

# SSError
sserror = sst - sstreatment
print("SSError = SST - SSTreatment = " + str(sserror))

# MS
df_treatment = a - 1
df_error = N - a
df_total = N - 1
print("d.f. Treatment = " + str(df_treatment))
print("d.f. Error = " + str(df_error))
print("d.f. Total = " + str(df_total))
ms_treatment = sstreatment / df_treatment
ms_error = sserror / df_error
ms_total = sst / df_total
print("MS treatment = " + str(ms_treatment))
print("MS error = " + str(ms_error))
print("MS total = " + str(ms_total))

# F
f_treatment = ms_treatment / ms_error
print("F treatment = " + str(f_treatment))