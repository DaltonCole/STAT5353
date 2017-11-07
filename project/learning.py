import csv 		# Convert to spreadsheet format
import sys
import numpy
#from jarcard_similarity import jarcard_similarity
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
	cluster = KMeansClusterer(c, distance=euclidean_distance, repeats=10, avoid_empty_clusters=True)
	assigned = cluster.cluster(data, assign_clusters=True)
	print(assigned)

	if c == 2:
		# Find majority class
		majority_a = [0,0]
		majority_b = [0,0]
		for original, a in zip(answer, assigned):
			if original == 0 and a =0 0:
				majority_a[0] += 1
			elif original == 0 and a != 0:
				majority_a[1] += 1
			elif original != 0 and a == 0:
				majority_b[0] += 1
			elif original != 0 and a != 0:
				majority_b[1] += 1
		
	# SSE
	#total_sse, sse = SSE(data, assigned, c)
	#print(total_sse)
	#print(sse)
	#print()

	

quit()
euclidean_k_clusters = KMeansClusterer(NUM_CLUSTERS, distance=euclidean_distance, repeats=1000)
assigned_clusters_euclidean = euclidean_k_clusters.cluster(article_word_frequency, assign_clusters=True)
print((assigned_clusters_euclidean))

### SSE
euclidean_total_SSE, euclidean_SSE = SSE(article_word_frequency, assigned_clusters_euclidean, NUM_CLUSTERS)
print(euclidean_total_SSE)
print(euclidean_SSE)

### How correct were we?
correct = [0] * 5
for a_type in range(len(article_type_numeric)):
	for ty, cluster in zip(article_type_numeric[a_type], assigned_clusters_euclidean):
		if ty == cluster:
			correct[a_type] += 1
print(correct)
print(max(correct), '%')

#################################################### Cosine Kmeans ####################################################
print("COSINE")
cosine_k_clusters = KMeansClusterer(NUM_CLUSTERS, distance=cosine_distance, repeats=1000)
assigned_clusters_cosine = cosine_k_clusters.cluster(article_word_frequency, assign_clusters=True)
print(assigned_clusters_cosine)

cosine_total_SSE, cosine_SSE = SSE(article_word_frequency, assigned_clusters_cosine, NUM_CLUSTERS)
print(cosine_total_SSE)
print(cosine_SSE)

### How correct were we?
correct = [0] * 5
for a_type in range(len(article_type_numeric)):
	for ty, cluster in zip(article_type_numeric[a_type], assigned_clusters_cosine):
		if ty == cluster:
			correct[a_type] += 1
print(correct)
print(max(correct), '%')


#################################################### Jarcard Kmeans ####################################################
print("JARCARD")
jarcard_k_clusters = KMeansClusterer(NUM_CLUSTERS, distance=jarcard_similarity, repeats=25)
assigned_clusters_jarcard = jarcard_k_clusters.cluster(article_word_frequency, assign_clusters=True)
print(assigned_clusters_jarcard)

jarcard_total_SSE, jarcard_SSE = SSE(article_word_frequency, assigned_clusters_jarcard, NUM_CLUSTERS)
print(jarcard_total_SSE)
print(jarcard_SSE)

### How correct were we?
correct = [0] * 5
for a_type in range(len(article_type_numeric)):
	for ty, cluster in zip(article_type_numeric[a_type], assigned_clusters_jarcard):
		if ty == cluster:
			correct[a_type] += 1
print(correct)
print(max(correct), '%')