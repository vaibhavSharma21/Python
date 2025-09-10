'''1st pattern'''
# 1
# 2  3
# 4  5  6
# 7  8  9  10
# 11 12 13 14 15

# n = int(input("enter the number :"))
# temp = 0
# for i in range(0,n):
#     for j in range(0,i+1):
#         temp += 1
#         print(temp,end="  ")
#     print()

#------------------------------------------------------------------------------

#      *
#     ***
#    *****
#   *******
#  *********

# n = int(input("enter the number :"))
# for i in range(0,n):       # yha 0 or 1 pe ek hi output aa rahi hain
#     for j in range(0,n-i-1):
#         print(" ",end = " ")
#     for j in range(0,((2*i)+1)):
#         print("*",end=" ")
#     print()    

#------------------------------------------------------------------------

#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***
#      * 

# n = int(input("enter the number : ")) 
# for i in range(0,(n//2)+1):
#       ## spaces
#       for j in range(0,(n//2)-i):
#             print(" ",end = " ")
#       ## stars
#       for j in range(0,(2*i)+1):
#             print("*",end = " ")
#       print()
# for i in range((n//2)+1,n):
#       ## spaces
#       for j in range(0,i-(n//2)):
#             print(" ",end=" ")
#       ## stars
#       for j in range(0,2*(n-i)-1):
#             print("*",end = " ")
#       print()
  

#---------------------------------------------------------------

#      *
#     *-*
#    *---*
#   *-----*
#  *-------*

    

#---------------

# n = int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         if j==1 or j==2*i-1:
#            print("*",end=" ")
#         else:
#             print("-",end=" ")   
#     print()          

#---------------------------------------------------------------------
# 12345
# 1234
# 123
# 12
# 1

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,(n-i)+2):
#         print(j,end=" ")
#     print()    

#-----------------------------------------------------------------------------------

# 12345
# 2345
# 345
# 45
# 5

# n = int(input("enter ther number :"))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()    

#-----------------------------------------------------------------------------------

# 54321
# 5432
# 543
# 54
# 5

# n = int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range(n,i-1,-1):  #yha agar hum i rakhte toh hmara 1 print nahihota isliye humne i-1 rakha
#         print(j,end=" ")
#     print()    

#-------------------------------------------------------------------------------

# 54321
# 4321
# 321
# 21
# 1

# n = int(input("enter the number"))
# for i in range(1,n+1):
#     for j in range((n-i)+1,0,-1):  
#         print(j,end=" ")
#     print()    

#--------------------------------------------------------------------------------

# 1
# 21
# 321
# 4321
# 54321

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()    

#------------------------------------------------------------------------------------

# 1
# 12
# 123
# 1234
# 12345

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()    

#----------------------------------------------------------------------------------


# 5
# 54
# 543
# 5432
# 54321

n = int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(n,n-i,-1):
        print(j,end=" ")
    print()    

#----------------------------------------------------------------------------------


# 5
# 45
# 345
# 2345
# 12345

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(n+1-i,n+1):
#         print(j,end=" ")
#     print() 

#----------------

# n = int(input("enter the number:"))
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()    


#---------------------------------------------------------------------------------

# 12345
#  1234
#   123
#    12
#     1

# n = int(input("enter the number:"))
# for i in range(1,n+1):
      #space
#     for j in range(1,i):
#         print(" ",end=" ")
       #numbers
#     for j in range(1,n+2-i):
#         print(j,end=" ")  
#     print()

#----------------------------------------------------------------------------


# 12345
#  2345
#   345
#    45
#     5

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     #    space
#     for j in range(1,i):
#         print(" ",end=" ")
#         # numbers
#     for j in range(i,n+1):
#         print(j,end=" ")  
#     print()


#---------------------------------------------------------------------------------

# 54321
#  5432
#   543
#    54
#     5

# n = int(input("entr the number:"))
# for i in range(1,n+1):
#     #    space
#     for j in range(1,i):
#         print(" ",end=" ")
#     #    numbers
#     for j in range(n,i-1,-1):
#         print(j,end=" ")    
#     print()

#---------------------------------------------------------------------


# 54321
#  4321
#   321
#    21
#     1

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     #space
#     for j in range(1,i):
#        print(" ",end=" ")
#     #numbners
#     for j in range(n+1-i,0,-1):
#         print(j,end=" ")
#     print()

#----------------------------------------------------------------------------------

#     1
#    21
#   321
#  4321
# 54321

# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()          

#----------------------------------------------------------------------------------

#     1
#    12
#   123
#  1234
# 12345


# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()          

#----------------------------------------------------------------------------------

#     5
#    54
#   543
#  5432
# 54321

# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(n,n-i,-1):
#         print(j,end=" ")
#     print()          

#----------------------------------------------------------------------------------

#     5
#    45
#   345
#  2345
# 12345

# n = int(input("enter the number :"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range((n+1)-i,n+1):
#         print(j,end=" ")
#     print()       

#----------------------------------------------------------------------------------

# 1
# 2  3
# 4  5  6 
# 7  8  9  10
# 11 12 13 14 15

# n = int(input("enter the number:"))
# temp =  0
# for i in range(1,n+1):
#     temp = temp + 1
#     for j in range(temp,temp+i):
#       print(j,end=" ")
#       temp = j
#     print()  
        
#----------------------------------------------------------------------------------

# 1
# 3  5
# 7  9  11
# 13 15 17 19

# n = int(input("enter the number :"))
# temp = -1
# for i in range(1,n+1):
#     temp = temp + 2
#     for j in range(temp,(i*i)+i,2):
#       print(j,end=" ")
#       temp = j
#     print()    

#----------------------------------------------------------------------------------


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# n = int(input("enter the number"))
# for i in range(1,2*n):
#     if i<=5:
#       for j in range(1,i+1):
#         print("*",end=" ")
#     else:
#        for j in range(0,2*n-i):
#           print("*",end=" ")
#     print()
#       

#-----------------------------------------------------------------------------------

# *
# **
# ***
# ****
# *****
#  ****
#   ***
#    **
#     *

# n = int(input("enter the number:"))
# for i in range(1,2*n):
#     if i<=n:
#       for j in range(0,i):
#          print("*",end=" ") 
#     else:    #space
#       for j in range(0,i-n):
#          print(" ",end=" ") 
#              #star
#       for j in range(0,2*n-i):
#          print("*",end=" ")   
#     print()

#-----------------------------------------------------------------------------------


#      *
#     **
#    ***
#   ****
#  *****
#  ****
#  ***
#  **
#  *

# n = int(input("enter the number:"))
# for i in range(1,2*n):
#     if i<=n:
#       for j in range(0,n-i):
#           print(" ",end=" ")
#       for j in range(0,i):
#           print("*",end=" ")
#     else:    
#       for j in range(0,2*n-i):
#           print("*",end=" ")
#     print()    

#-----------------------------------------------------------------------------------


# *****
#  ****
#   ***
#    **
#     *
#    **
#   ***
#  ****
# *****

# n = int(input("enter the number:"))
# for i in range(1,2*n):
#     if i<=n:
#       for j in range(1,i):
#         print(" ",end=" ")
#       for j in range(0,n+1-i): 
#         print("*",end=" ") 
#     else:
#       for j in range(0,(2*n-1)-i):
#         print(" ",end=" ")   
#       for j in range(0,i+1-n):
#         print("*",end=" ")       
#     print()   

#-----------------------------------------------------------------------------------


#      *
#     ***
#    *****
#   *******
#  *********

# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(0,n-i):
#         print(" ",end=" ")
#     for j in range(0,2*i-1):
#         print("*",end=" ")
#     print()        

#-----------------------------------------------------------------------------------


#      *
#     ***
#    *****
#   *******
#  *********
#   *******
#    *****
#     ***   
#      *


# n = int(input("enter the number :"))
# for i in range(1,2*n):
#     if i<=n:
#       for j in range(0,n-i):
#         print(" ",end=" ")
#       for j in range(0,2*i-1):
#         print("*",end=" ")  
#     else:      
#       for j in range(0,i-n):
#         print(" ",end=" ")    
#       for j in range(0,2*(2*n-i)-1):
#         print("*",end=" ")    
#     print()    

#-------------------------------------------------------------------------------------


#      *
#     *-*
#    *---*
#   *-----*
#  *-------*
#   *-----*
#    *---*
#     *-*
#      *

# n = int(input("enter the number :"))
# for i in range(1,2*n):
#     if i<=n:
#       for j in range(0,n-i):
#         print(" ",end=" ")
#       for j in range(0,2*i-1):
#         if j==0 or j==2*i-2:
#           print("*",end=" ") 
#         else:
#           print("-",end=" ") 
#     else:      
#       for j in range(0,i-n):
#         print(" ",end=" ")    
#       for j in range(0,2*(2*n-i)-1):
#         if j==0 or j==2*(2*n-i)-2:
#           print("*",end=" ") 
#         else:
#           print("-",end=" ")
#     print()    


