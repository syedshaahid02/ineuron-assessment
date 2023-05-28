#LANGUAGE---PYTHON
#1.Two sum 
#intution prefix sum
nums = [2,7,11,15]
target = 9
lookup ={}#valto index
for i,n in enumerate(nums):
    diff = target-n
    if diff in lookup:
        print([lookup[diff],i])
    lookup[n] =i
#2.Remove element
#intution swapping
nums = [3,2,2,3]
val =3
k =0 
for i in range(len(nums)):
    if nums[i]!=val:
        nums[k]=nums[i]
        k+=1
print(k)
#3.search position
#intution: Binary Search
nums = [1,3,5,6]
target = 5
l,r =0,len(nums)-1
while l<=r:
    mid = (l+r)//2
    if target == nums[mid]:
        return mid
    elif target<nums[mid]:
        r= mid-1
    elif target>nums[mid]:
        l=mid+1
return l

#4.larger interger by one
digits = [1,2,3]
res =""
for nums in digits:
    res+=str(nums)
    tmp = str(int(res)+1)
    result = [int(i) for i in tmp]
return result
#5.merge sorted array
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
last_position = m+n-1
while m>0 and n>0:
    if nums1[m-1]>nums2[n-1]:
        nums1[last_position]=nums1[m-1]
        m-=1
    else:
        nums1[last_position]= nums2[n-1]
        n-=1
        last_position -=1
while n>0:
    nums1[last_position]=nums2[n-1]
    n,last_position = n-1,last_position-1
return nums1
#6.duplicate numbers
nums = [1,2,3,1]
nums =sorted(nums)
l,r=0,1
while r<len(nums):
    if nums[l]==nums[r]:
        return True
    l,r=l+1,r+1
return False
#7.Move zeroes
nums = [0,1,0,3,12]
for i in range(len(nums)):
    if nums[i]==0:
        nums.remove(nums[i])
        nums.append(0)
return nums
#8.duplicate number and missing number
nums = [1,2,2,4]
duplicate_num= -1
missing_num = -1
lookup ={}
for i in range(len(nums)):
    lookup[s[i]] = 1+ lookup.get(s[i],0)
for i in range(1,len(nums)+1):
    if i not in lookup.keys():
        missing_num = i
    elif lookup[i]==2:
        duplicate_num = lookup[s[i]]
return [missing_num,duplicate_num]