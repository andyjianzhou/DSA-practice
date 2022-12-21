import math
class Solution:
    def intToRoman(self,num):
        d={1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
        numofdigits=math.floor(math.log(num))+1
        numofzeros=numofdigits-1
        numral=""
        for i in range(numofdigits):
            place=pow(10,(numofzeros-i))
            firstnum=num//place
            if firstnum==4:
                numral += d[place]
                numral +=d[place*5]
            elif firstnum==9:
                numral += d[place]
                numral +=d[place*10]
            else:
                if firstnum>4:
                    numral += d[place*5]
                for j in range(firstnum%5):
                    numral += d[place]
            num -= firstnum*place
        return numral

# This question sucks