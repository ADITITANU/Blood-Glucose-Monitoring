

# Function to find minimum operation required to 
# make all array elements equal 
def minDelete(arr, n): 
	max_freq = 1
	arr.sort() # sort array for binary search 

	# Iterating the whole array 
	i = 0
	while i < n: 
		
		# index of first occ of arr[i] 
		first_index = arr.index(arr[i]) 
		
		# find the last occ of arr[i] 
		j = n - 1
		while j >= 0 and arr[j] != arr[i]: 
			j -= 1
		last_index = j 
		fre = last_index - first_index + 1 # finding frequency 
		# Finding maximum frequency from all array elements 
		max_freq = max(max_freq, fre) 

		i = last_index + 1 # assign i to next index 

	return n - max_freq # return answer 

# Drive code 
arr = [4, 3, 4, 4, 2, 4] 
n = len(arr) 

# Function call 
print(minDelete(arr, n))

        # code here


