import time
import sys
import random
import copy


def Rep(x):
   if( x == 1 ): x = "."
   if( x == 0 ): x = " "
   return x

def RandomFill(Matrix,w,h):
   for j in range(w) :
      for i in range(h)  :
         
         rnd =  random.random()
         if( rnd > 0.7 ):
            Matrix[i][j]  = 1 #str(".")
         else:
            Matrix[i][j]  = 0 #str("0")

   return Matrix



def PropagateTime(M,w,h):

   A = copy.deepcopy(M)
   for i in range (1,w -1):
      for j in range (1,h -1):
         nsum = A[i-1][j] + A[i-1][j-1] + A[i-1][j+1] + A[i][j+1] + A[i][j-1] + A[i+1][j] + A[i+1][j+1] + A[i+1][j-1]

         if(nsum > 4 ):
            M[i][j] = 0
         elif(nsum > 2 ):
            M[i][j] = 1



   return 



#-------------------------------------------------------------------------#





w = 30
h = 30

Matrix = [[0 for x in range(w)]for y in range (h)]
S      = [[0 for x in range(w)]for y in range (h)]


Matrix[15][15] = 1
Matrix[16][15]  = 1
Matrix[14][15]  = 1


Matrix[15][10] = 1
Matrix[16][10]  = 1
Matrix[14][10]  = 1




#RandomFill(Matrix,w,h)



for itest  in range(1,100):
  
   PropagateTime(Matrix,w,h)
   
   for j in range(w) : 
      for i in range(h) : 
         val = Matrix[i][j]
         S[i][j] = Rep(val)   
  

   
   print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in S]))



   for j in range(0,h):
      if(itest != 99):
         sys.stdout.write("\033[F")
         

   time.sleep(0.5)

 


