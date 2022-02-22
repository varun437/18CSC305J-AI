import math
 
def minimax (cd, idx,maxt, scr,td):
 
    if (cd == td):
        return scr[idx]
    
    if (maxt):
        return max(minimax(cd + 1, idx * 2,False, scr, td),
              minimax(cd + 1, idx * 2 + 1,False, scr, td))
     
    else:
        return min(minimax(cd + 1, idx * 2,True, scr, td),
              minimax(cd + 1, idx * 2 + 1,True, scr, td))
     
scr = [3, 5, 2, 9, 12, 5, 23, 23]
 
td = math.log(len(scr), 2)
 
print("value is : ", end = "")
print(minimax(0, 0, True, scr, td))
