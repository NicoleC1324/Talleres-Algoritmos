t=1
sum=0
for t in range(97,1004):
    if(t%2==0):
      sum=sum+t
      t+=1
    print(sum)