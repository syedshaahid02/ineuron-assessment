#1.Min_Sum
nums = [1,4,3,2]
nums.sort()
res=0
for i in range(0,len(nums),1):
    res+=1
print(res)
#2.Candies
candyType = [1,1,2,2,3,3]
un = len(set(candyType))
can_eat =len(candyType)//2
print(min(un,can_eat))
#3.Harmonic sequence

#4.Flower bed
if n==0: return True
flowerbed = [0]+flowerbed+[0]
for i in range(1,len(flowerbed)-1):
    if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
        flowerbed[i]=1
        n-=1
    if n<=0:
        return True
#5.Maximum 3 number in nums
big_3 = heapq.nlargest(3,nums)
small_3 = heapq.nsmallest(2,nums)

return max(big_3[0]*big_3[1]*big_3[2],small_3[0]*small_3[1]*big_3[0])
#6.Binaray Search 
l,r= 0, len(nums)-1
while l<=r:
    mid= (l+r)//2
    if target==nums[mid]:
        return target
    elif target>nums[mid]:
        l =mid+1
    elif target<nums[mid]:
        r = mid-1
return -1
#7.Monotonic array
inc =des = True
for i in range(1,len(nums)):
    if nums[i]>nums[i-1]:
        des = False
    if nums[i]<nums[i-1]:
        inc = False
return inc or des
