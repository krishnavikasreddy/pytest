
def sort(numbers,start,end):
	if(numbers[start]>numbers[end]):
		temp=numbers[end]
		numbers[end]=numbers[start]
		numbers[start]=temp

def MergeSort(numbers,start,end):
	if((end-start)>1):
		middle=int(round(((start+end)-0.1)/2))
		MergeSort(numbers,start,middle)
		MergeSort(numbers,middle+1,end)
		merge(numbers,start,end,middle)
	else:
		sort(numbers,start,end)
		



def merge(numbers,start,end,middle):
	i=start
	j=middle+1
	k=i
	result=[]
	print(numbers)
	while(i<=middle and j<=end):
		if(numbers[i]<numbers[j]):
			result.append(numbers[i])
			i=i+1
		else:
			result.append(numbers[j])
			j=j+1
	print(result)

numbers=[9,1,4,8,2,7,6,3]
MergeSort(numbers,0,len(numbers)-1)


