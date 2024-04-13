nums=[1,2,3,4]
mult=1
answer=[1]*len(nums)
pre=1
post=1
for i in range(len(nums)):
    answer[i]=pre
    pre=pre*nums[i]
for i in range(len(nums)-1,-1,-1) :
    answer[i]*=post
    post*=nums[i]
print(answer)    


        



     
