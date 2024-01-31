# Example 1.1 : 
i = 1          
while i < 6:   
  print(i)     # 1 2 3 4 5 6
  i += 1       
               
  
# Example 1.2 : Break statement can stop loop in certain condition
i = 1
while i < 6:
  print(i)  # 1 2 3
  if i == 3:          
    break             
  i += 1              


# Example 1.3 : Continue statement can skip current iteration and conitinue with next iteration
i = 0            
while i < 6:  
  i += 1
  if i == 3:
    continue
  print(i)    # 1 2 4 5 6


# Example 1.4 : With else statement we can run block of code since condition is no longer true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")    # 1 2 3 4 5 i is no longer less than 6
