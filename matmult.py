def mult_scalar(matrix, scale):
	newValue = matrix
	
	for i in range(len(newValue)): #list number
		for j in range(len(newValue[i])): #value
			newValue[i][j] *= scale
	
	return newValue

def mult_matrix(a, b):

    if len(a[0]) == len(b):
        resultMatrix = []
    for i in range(len(a)): #every row in a
        prodResult = []
        for j in range(len(b[0])): #every column in b
            product = 0
            for k in range(len(b)): #every row in b
                product += a[i][k] * b[k][j]
            prodResult.append(product)
        resultMatrix.append(prodResult)
    
        return resultMatrix
    else:
        return None

def multiply(v, G):
    result = []
    for i in range(len(G[0])):
        total = 0
        for j in range(len(v)):
            total += v[j] * G[j][i]
        result.append(total)
    return result

def euclidean_dist(a,b):
    distance = 0
    sums = []
    for i in range(len(a)): #for every list
        for j in range(len(a[0])): #for every value in each list
            sum = (a[i][j] - b[i][j])**2
            sums.append(sum)
    tot = 0
    for k in sums:
        tot += k
	
    distance += tot ** (1/2)
    return distance