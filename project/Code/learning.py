import csv 		# Convert to spreadsheet format
import sys
import numpy
from jarcard_similarity import jarcard_similarity
from sum_of_squares import SSE
from nltk.cluster.kmeans import KMeansClusterer # Kmeans
from nltk.cluster.util import cosine_distance, euclidean_distance # Distances (cosine, euclidean)
import matplotlib.pyplot as plt

#################################################### Extract csv data ####################################################
### article_word_frequency is the word frequency in each article (only numbers)
### article_type is the type of every article
### words is what each index corresponds to

# Every row in the csv file
rows = []

# Read every row in data files file
with open('./heart-disease/processed.cleveland.data', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rows.append(row)
with open('./heart-disease/processed.hungarian.data', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rows.append(row)
with open('./heart-disease/processed.switzerland.data', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rows.append(row)
with open('./heart-disease/processed.va.data', 'r') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		rows.append(row)

# All rows without missing data
no_missing_data =[]

for row in rows:
	if '?' not in row:
		no_missing_data.append(row)


data_points = len(rows) - 1

# Different cluster sizes to test
cluster_sizes = [2, 3, 5]

# Answer key
heart_attack_rate = []
for row in no_missing_data:
	heart_attack_rate.append(row[-1])


# Remove answer from no_missing_data
for i in range(len(no_missing_data)):
	no_missing_data[i] = no_missing_data[i][0:-1]

# Convert to numpy array
data = numpy.array(no_missing_data, dtype=float)
answer = numpy.array(heart_attack_rate, dtype=float)

############################## Euclidean Kmeans ##############################
print("EUCLIDEAN")

for c in cluster_sizes:
	# Make cluasters
	cluster = KMeansClusterer(c, distance=euclidean_distance, repeats=1, avoid_empty_clusters=True)
	assigned = cluster.cluster(data, assign_clusters=True)
	
	if c == 2:
		# Find majority class
		majority_a = [0,0]
		majority_b = [0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a != 0:
				majority_a[1] += 1
			elif original != 0 and a == 0:
				majority_b[0] += 1
			elif original != 0 and a != 0:
				majority_b[1] += 1
		print(majority_a)
		print(majority_b)

		s = 0
		s += max(majority_a)
		s += max(majority_b)

		print("Number correct for c=2: {}".format(s))

	if c == 3:
		# Find majority class
		majority_a = [0,0,0]
		majority_b = [0,0,0]
		majority_c = [0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1

			elif original == 4 and a == 0:
				majority_c[0] += 1
			elif original == 4 and a == 1:
				majority_c[1] += 1
			elif original == 4 and a == 2:
				majority_c[2] += 1


			elif a == 0:
				majority_b[0] += 1
			elif a == 1:
				majority_b[1] += 1
			elif a == 2:
				majority_b[2] += 1

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print("Number correct for c=3: {}".format(max(majority_a) + max(majority_b) + max(majority_c)))

	if c == 5:
		# Find majority class
		majority_a = [0,0,0,0,0]
		majority_b = [0,0,0,0,0]
		majority_c = [0,0,0,0,0]
		majority_d = [0,0,0,0,0]
		majority_e = [0,0,0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1
			elif original == 0 and a == 3:
				majority_a[3] += 1
			elif original == 0 and a == 4:
				majority_a[4] += 1

			elif original == 1 and a == 0:
				majority_b[0] += 1
			elif original == 1 and a == 1:
				majority_b[1] += 1
			elif original == 1 and a == 2:
				majority_b[2] += 1
			elif original == 1 and a == 3:
				majority_b[3] += 1
			elif original == 1 and a == 4:
				majority_b[4] += 1

			elif original == 2 and a == 0:
				majority_c[0] += 1
			elif original == 2 and a == 1:
				majority_c[1] += 1
			elif original == 2 and a == 2:
				majority_c[2] += 1
			elif original == 2 and a == 3:
				majority_c[3] += 1
			elif original == 2 and a == 4:
				majority_c[4] += 1

			elif original == 3 and a == 0:
				majority_d[0] += 1
			elif original == 3 and a == 1:
				majority_d[1] += 1
			elif original == 3 and a == 2:
				majority_d[2] += 1
			elif original == 3 and a == 3:
				majority_d[3] += 1
			elif original == 3 and a == 4:
				majority_d[4] += 1

			elif original == 4 and a == 0:
				majority_e[0] += 1
			elif original == 4 and a == 1:
				majority_e[1] += 1
			elif original == 4 and a == 2:
				majority_e[2] += 1
			elif original == 4 and a == 3:
				majority_e[3] += 1
			elif original == 4 and a == 4:
				majority_e[4] += 1

			

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print(majority_d)
		print(majority_e)
		print("Number correct c=5: {}".format(max(majority_a) + max(majority_b) + max(majority_c) + max(majority_d) + max(majority_e)))


	print()


#################################################### Cosine Kmeans ####################################################
print("COSINE")

for c in cluster_sizes:
	# Make cluasters
	cluster = KMeansClusterer(c, distance=cosine_distance, repeats=1, avoid_empty_clusters=True)
	assigned = cluster.cluster(data, assign_clusters=True)
	
	if c == 2:
		# Find majority class
		majority_a = [0,0]
		majority_b = [0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a != 0:
				majority_a[1] += 1
			elif original != 0 and a == 0:
				majority_b[0] += 1
			elif original != 0 and a != 0:
				majority_b[1] += 1
		print(majority_a)
		print(majority_b)

		s = 0
		s += max(majority_a)
		s += max(majority_b)

		print("Number correct for c=2: {}".format(s))

	if c == 3:
		# Find majority class
		majority_a = [0,0,0]
		majority_b = [0,0,0]
		majority_c = [0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1

			elif original == 4 and a == 0:
				majority_c[0] += 1
			elif original == 4 and a == 1:
				majority_c[1] += 1
			elif original == 4 and a == 2:
				majority_c[2] += 1


			elif a == 0:
				majority_b[0] += 1
			elif a == 1:
				majority_b[1] += 1
			elif a == 2:
				majority_b[2] += 1

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print("Number correct for c=3: {}".format(max(majority_a) + max(majority_b) + max(majority_c)))

	if c == 5:
		# Find majority class
		majority_a = [0,0,0,0,0]
		majority_b = [0,0,0,0,0]
		majority_c = [0,0,0,0,0]
		majority_d = [0,0,0,0,0]
		majority_e = [0,0,0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1
			elif original == 0 and a == 3:
				majority_a[3] += 1
			elif original == 0 and a == 4:
				majority_a[4] += 1

			elif original == 1 and a == 0:
				majority_b[0] += 1
			elif original == 1 and a == 1:
				majority_b[1] += 1
			elif original == 1 and a == 2:
				majority_b[2] += 1
			elif original == 1 and a == 3:
				majority_b[3] += 1
			elif original == 1 and a == 4:
				majority_b[4] += 1

			elif original == 2 and a == 0:
				majority_c[0] += 1
			elif original == 2 and a == 1:
				majority_c[1] += 1
			elif original == 2 and a == 2:
				majority_c[2] += 1
			elif original == 2 and a == 3:
				majority_c[3] += 1
			elif original == 2 and a == 4:
				majority_c[4] += 1

			elif original == 3 and a == 0:
				majority_d[0] += 1
			elif original == 3 and a == 1:
				majority_d[1] += 1
			elif original == 3 and a == 2:
				majority_d[2] += 1
			elif original == 3 and a == 3:
				majority_d[3] += 1
			elif original == 3 and a == 4:
				majority_d[4] += 1

			elif original == 4 and a == 0:
				majority_e[0] += 1
			elif original == 4 and a == 1:
				majority_e[1] += 1
			elif original == 4 and a == 2:
				majority_e[2] += 1
			elif original == 4 and a == 3:
				majority_e[3] += 1
			elif original == 4 and a == 4:
				majority_e[4] += 1

			

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print(majority_d)
		print(majority_e)
		print("Number correct c=5: {}".format(max(majority_a) + max(majority_b) + max(majority_c) + max(majority_d) + max(majority_e)))


	print()

#################################################### Jarcard Kmeans ####################################################
print("JARCARD")

for c in cluster_sizes:
	# Make cluasters
	cluster = KMeansClusterer(c, distance=jarcard_similarity, repeats=1, avoid_empty_clusters=True)
	assigned = cluster.cluster(data, assign_clusters=True)
	
	if c == 2:
		# Find majority class
		majority_a = [0,0]
		majority_b = [0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a != 0:
				majority_a[1] += 1
			elif original != 0 and a == 0:
				majority_b[0] += 1
			elif original != 0 and a != 0:
				majority_b[1] += 1
		print(majority_a)
		print(majority_b)

		s = 0
		s += max(majority_a)
		s += max(majority_b)

		print("Number correct for c=2: {}".format(s))

	if c == 3:
		# Find majority class
		majority_a = [0,0,0]
		majority_b = [0,0,0]
		majority_c = [0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1

			elif original == 4 and a == 0:
				majority_c[0] += 1
			elif original == 4 and a == 1:
				majority_c[1] += 1
			elif original == 4 and a == 2:
				majority_c[2] += 1


			elif a == 0:
				majority_b[0] += 1
			elif a == 1:
				majority_b[1] += 1
			elif a == 2:
				majority_b[2] += 1

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print("Number correct for c=3: {}".format(max(majority_a) + max(majority_b) + max(majority_c)))

	if c == 5:
		# Find majority class
		majority_a = [0,0,0,0,0]
		majority_b = [0,0,0,0,0]
		majority_c = [0,0,0,0,0]
		majority_d = [0,0,0,0,0]
		majority_e = [0,0,0,0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a == 0:
				majority_a[0] += 1
			elif original == 0 and a == 1:
				majority_a[1] += 1
			elif original == 0 and a == 2:
				majority_a[2] += 1
			elif original == 0 and a == 3:
				majority_a[3] += 1
			elif original == 0 and a == 4:
				majority_a[4] += 1

			elif original == 1 and a == 0:
				majority_b[0] += 1
			elif original == 1 and a == 1:
				majority_b[1] += 1
			elif original == 1 and a == 2:
				majority_b[2] += 1
			elif original == 1 and a == 3:
				majority_b[3] += 1
			elif original == 1 and a == 4:
				majority_b[4] += 1

			elif original == 2 and a == 0:
				majority_c[0] += 1
			elif original == 2 and a == 1:
				majority_c[1] += 1
			elif original == 2 and a == 2:
				majority_c[2] += 1
			elif original == 2 and a == 3:
				majority_c[3] += 1
			elif original == 2 and a == 4:
				majority_c[4] += 1

			elif original == 3 and a == 0:
				majority_d[0] += 1
			elif original == 3 and a == 1:
				majority_d[1] += 1
			elif original == 3 and a == 2:
				majority_d[2] += 1
			elif original == 3 and a == 3:
				majority_d[3] += 1
			elif original == 3 and a == 4:
				majority_d[4] += 1

			elif original == 4 and a == 0:
				majority_e[0] += 1
			elif original == 4 and a == 1:
				majority_e[1] += 1
			elif original == 4 and a == 2:
				majority_e[2] += 1
			elif original == 4 and a == 3:
				majority_e[3] += 1
			elif original == 4 and a == 4:
				majority_e[4] += 1

			

		print(majority_a)
		print(majority_b)
		print(majority_c)
		print(majority_d)
		print(majority_e)
		print("Number correct c=5: {}".format(max(majority_a) + max(majority_b) + max(majority_c) + max(majority_d) + max(majority_e)))


	print()