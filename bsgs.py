'''

3411390473 = 3**x mod 1788512386
def BSGS(πΌ,π½,π) 
    N = ββπβ1β 
    bshash = empty hash table 
    for j = 0 to N-1 
        bshash[πΌπ (πππ π)] = j  
    end 
    for k = 0 to N-1 
        gs = π½πΌβππ (πππ π) 
        if gs is a key in bshash then 
            j = bshash[g] 
            return π+ππ (πππ π) 
        end 
    end 
end
'''
#Huseyn Mammadov
import math
def bsgs(a,b,p):
    N = int(math.ceil(math.sqrt(p-1)))
    bshash = {}
    for i in range(N):
        #o = (a**i)%p
        bshash[pow(a,i,p)] = i
    giant = pow(a,N*(p-2),p)
    for j in range(N):
        last = (b*pow(giant,j,p))%p
        if last in bshash:
            return j*N+bshash[last]
    return None

a = bsgs(3,1788512386,3411390473)
if __name__=='__main__':
   
   print(a) 

#1783590054