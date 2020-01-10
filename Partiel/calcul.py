total = 0
for i in range(1,1000):
    calc = pow(i,i)
    total = total + calc
print(abs(total) % 10000000000)
#merci a https://www.wolframalpha.com/input/?i=sum+n%5En%2C+n%3D1+to+1000 pour la verification
#https://www5b.wolframalpha.com/Calculate/MSP/MSP309222336e38iib2714a00004i267c27b46i473d?MSPStoreType=image/gif&s=8