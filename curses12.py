head = [1,1]
body = [[1,1],[2,1],[3,1],[4,1],[5,1]]
print body
for z in range(len(body)-1,0,-1):
	body[z] = body[z-1]
print body