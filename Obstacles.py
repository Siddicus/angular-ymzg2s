import itertools
import sys
import numpy as np
sys.setrecursionlimit(1000)
############################################################################################################
"""Helper Functions"""

def short_path(arr:[],start:tuple,stop:tuple):    
    if stop[1]==start[1]:      
        
        if stop[0]>start[0]: 
            arr9=[]
            arr2 = [(start[0]+i,start[1]) for i in range(stop[0]-start[0]+1)]
            arr9.append(arr2)
            try:
                
                if 0<=start[1]+1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j+1) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            try:
                
                if 0<=start[1]-1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j-1) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            return arr9
        
        else:
            arr9=[]
            arr2 = [(start[0]-i,start[1]) for i in range(start[0]-stop[0]+1)]
            arr9.append(arr2)
            try:                
                if 0<=start[1]+1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j+1) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            try:                 
                if 0<=start[1]-1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j-1) for i,j in arr2]+[arr2[-1]])
            except IndexError:
                pass
            
            return arr9           

    
    if stop[1]>start[1]:
        
        if stop[0]==start[0]: 
            arr9=[]
            arr2 = [(start[0],start[1]+i) for i in range(stop[1]-start[1]+1)]
            arr9.append(arr2)
            try:
                
                if 0<=start[0]+1<len(arr[0]):                    
                    arr9.append([arr2[0]]+[(i+1,j) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            try:
                
                if 0<=start[0]-1<len(arr[0]):                               
                    arr9.append([arr2[0]]+[(i-1,j) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            return arr9
        
        if stop[0]>start[0]:
            arr9=[]
            arr2 = [(start[0]+i,start[1]) for i in range(stop[0]-start[0]+1)]
            arr3 = [(arr2[-1][0],arr2[-1][1]+i) for i in range(stop[1]-arr2[-1][1]+1)]    
            arr4 = [(start[0],start[1]+i) for i in range(stop[1]-arr2[-1][1]+1)]
            arr5 = [(arr4[-1][0]+i,arr4[-1][1]) for i in range(stop[0]-start[0]+1)]
            try:                
                if 0<=start[1]-1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j-1) for i,j in arr2]+arr3)
            except IndexError:
                pass
                
            if arr9:
                return [arr4+arr5,arr2+arr3,arr9[0]]
            else:
                return  [arr4+arr5,arr2+arr3]
            
        else:
            arr9=[]
            arr2 = [(start[0]-i,start[1]) for i in range(start[0]-stop[0]+1)]
            arr3 = [(arr2[-1][0],arr2[-1][1]+i) for i in range(stop[1]-start[1]+1)]
            arr4 = [(start[0],start[1]+i) for i in range(stop[1]-start[1]+1)]
            arr5 = [(arr4[-1][0]-i,arr4[-1][1]) for i in range(start[0]-stop[0]+1)]
            try:                
                if 0<=start[1]-1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j-1) for i,j in arr2]+arr3)
            except IndexError:
                pass
            if arr9:
                return [arr4+arr5,arr2+arr3,arr9[0]]
            else:
                return  [arr4+arr5,arr2+arr3]
           
    elif stop[1]<start[1]:         
        
        if stop[0]==start[0]: 
            arr9=[]
            arr2 = [(start[0],start[1]-i) for i in range(start[1]-stop[1]+1)]
            arr9.append(arr2)
            try: 
                if 0<=start[0]+1<len(arr[0]):                                
                    arr9.append([arr2[0]]+[(i+1,j) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            try:
                if 0<=start[0]-1<len(arr[0]):                                  
                    arr9.append([arr2[0]]+[(i-1,j) for i,j in arr2]+[arr2[-1]])
            except:
                pass
            return arr9
        if stop[0]>start[0]:
            arr9=[]
            arr2 = [(start[0]+i,start[1]) for i in range(stop[0]-start[0]+1)]
            arr3 = [(arr2[-1][0],arr2[-1][1]-i) for i in range(start[1]+1-stop[1])]    
            arr4 = [(start[0],start[1]-i) for i in range(start[1]+1-stop[1])]
            arr5 = [(arr4[-1][0]+i,arr4[-1][1]) for i in range(stop[0]-start[0]+1)]
            try:                
                if 0<=start[1]+1<len(arr):                     
                    arr9.append([arr2[0]]+[(i,j+1) for i,j in arr2]+arr3)
            except IndexError:
                pass
            if arr9:
                return [arr4+arr5,arr2+arr3,arr9[0]]
            else:
                return  [arr4+arr5,arr2+arr3]             
            
        else: 
            arr9=[]
            arr2 = [(start[0]-i,start[1]) for i in range(start[0]-stop[0]+1)]
            arr3 = [(arr2[-1][0],arr2[-1][1]-i) for i in range(start[1]+1-stop[1])]
            arr4 = [(start[0],start[1]-i) for i in range(start[1]+1-stop[1])]
            arr5 = [(arr4[-1][0]-i,arr4[-1][1]) for i in range(start[0]+1-stop[0])]
            try:                
                if 0<=start[1]+1<len(arr):                    
                    arr9.append([arr2[0]]+[(i,j+1) for i,j in arr2]+arr3)
            except IndexError:
                pass
            if arr9:
                return [arr4+arr5,arr2+arr3,arr9[0]]
            else:
                return  [arr4+arr5,arr2+arr3]


def ver_bool_response(arr,tup,up,start):    
    if up>0 :
        try:
            if arr[tup[1]+1][tup[0]]==0:
                return 2
            else:
                return False             
        except IndexError:
            pass
    
    elif up<0 :
        try:
            if arr[tup[1]-1][tup[0]]==0:           
                return 1
            else:            
                return False
        except IndexError:
            pass
    elif up==0:        
        try:
            if arr[tup[1]+1][tup[0]]==0:                
                return 4
            else:
                return False
        except IndexError:
            pass
        
        try:           
            if arr[tup[1]-1][tup[0]]==0:
                return 3
            else:
                return False
        except IndexError:
            pass

def destination(tup,target):
    if tup==target:
        return True
    else:
        return False
    
def man_dist(start,stop):
    return abs(start[0]-stop[0])+abs(start[1]-stop[1])

def point_short(q_list,look_up,arr,tup,stop,start):
    up =stop[1]-tup[1]
    b = []
    pat = [(sorted(set(i),key=i.index)) for i in short_path(arr,tup,stop)]
    for i in pat:
        j = list(itertools.takewhile(lambda x: look_up[x]==0,i))     
        b.append(j)
    b = list(sorted(b,key=lambda d: len(d),reverse=True))[0]
    
    if ver_bool_response(arr,b[-1],up,start):        
        the_path.append(b)        
        if destination(b[-1],target):
            return the_path
        else:
            return post_short(q_list,look_up,arr,b[-1],target,start)
    else:        
        the_path.append(b[:-1])
        tup_pre = tup
        return bool_cord_response(q_list,arr,b[-1],start,target,tup_pre)
    
def good_point_generator(q_list,bad_point,target,arr,tup_pre):
    k = [val for ind,val in enumerate(q_list) if bad_point in val][0]
    m = {i:man_dist(i,target) for i in k}
    m = list(dict(sorted(m.items(),key = lambda x: x[1])).keys())
    new_point=[i for i in m if ver_bool_response(arr,i,-1,target)]
    new_start = changer(arr,tup_pre)    
    return point_short(q_list,look_up,arr,new_start,new_point[0],start)
  
def post_short(q_list,look_up,arr,tup,target,start):
    up =target[1]-tup[1]
    b = []
    pat = [(sorted(set(i),key=i.index)) for i in short_path(arr,tup,target)]    
    for i in pat:
        j = list(itertools.takewhile(lambda x: look_up[x]==0,i))     
        b.append(j)
    
    b = list(sorted(b,key=lambda d: len(d),reverse=True))   
    vy = list(itertools.chain.from_iterable(the_path))    
    dest= [i for i in b if destination(i[-1],target)]
    if dest:
        return the_path.append(dest[0])    
    else:
        if len(b)>1:
            #choosing the optimum alternative
            if set(b[0]).intersection(set(vy))==0 and set(b[1]).intersection(set(vy))==0:
                b = b[0]                
                if ver_bool_response(arr,b[-1],up,start):
                    the_path.append(b)
                    
                    if destination(b[-1],target):
                        return the_path
                    else:                        
                        return post_short(q_list,look_up,arr,b[-1],target,start)
                else:   
                    the_path.append(b)                   
                    tup_pre=tup
                    return bool_cord_response(q_list,arr,b[-1],start,target,tup_pre)
            elif set(b[0]).intersection(set(vy)) <= set(b[1]).intersection(set(vy)):
                b = b[0]
                
                
                if ver_bool_response(arr,b[-1],up,start):
                    the_path.append(b)        
                    if destination(b[-1],target):                        
                        return the_path
                    else:
                        return post_short(q_list,look_up,arr,b[-1],target,start)
                
                else:   
                    the_path.append(b)                    
                    tup_pre=tup
                    return bool_cord_response(q_list,arr,b[-1],start,target,tup_pre)
            elif set(b[0]).intersection(set(vy)) >set(b[1]).intersection(set(vy)):
                b = b[1]
                
                if ver_bool_response(arr,b[-1],up,start):
                    the_path.append(b)        
                    if destination(b[-1],target):
                        return the_path
                    else:
                        return post_short(q_list,look_up,arr,b[-1],target,start)
                else:
    
                    the_path.append(b)                    
                    tup_pre=tup
                    return bool_cord_response(q_list,arr,b[-1],start,target,tup_pre)                
        else:
            tup_pre=tup
            return good_point_generator(q_list,tup,target,arr,tup_pre)

def changer(arr,tup):
    cy = []
    try:
        if arr[tup[1]][tup[0]+1]==0:
            cy.append((tup[0]+1,tup[1]))
    except:
        pass
    try:
        if arr[tup[1]][tup[0]-1]==0:
            cy.append((tup[0]-1,tup[1]))
    except:
        pass
    try:
        if arr[tup[1]+1][tup[0]]==0:
            cy.append((tup[0],tup[1]+1))
    except:
        pass
    try:
        if arr[tup[1]-1][tup[0]]==0:
            cy.append((tup[0],tup[1]-1))
    except:
        pass    
    return cy[0]

def bool_cord_response(q_list,arr,tup,start,target,tup_pre):    
    po = []
    poo=[]
    up =target[1]-tup[1]    
    for i in range(len(arr[0])-tup[0]):       
        if arr[tup[1]][tup[0]+i]==0:           
            if ver_bool_response(arr,(tup[0]+i,tup[1]),up,start)==2:               
                po.append((tup[0]+i,tup[1]))                
                break
            elif ver_bool_response(arr,(tup[0]+i,tup[1]),up,start)==1:                
                po.append((tup[0]+i,tup[1]))                
                break
            elif ver_bool_response(arr,(tup[0]+i,tup[1]),up,start)==3:               
                po.append((tup[0]+i,tup[1]-1))
                break
            elif ver_bool_response(arr,(tup[0]+i,tup[1]),up,start)==4:               
                po.append((tup[0]+i,tup[1]+1))
                break
            else:
                po.append((tup[0]+i,tup[1]))
        else:            
            break    
    for i in range(tup[0]+1):        
        if arr[tup[1]][tup[0]-i]==0:            
            if ver_bool_response(arr=arr,tup=(tup[0]-i,tup[1]),up=up,start=start)==2:                
                poo.append((tup[0]-i,tup[1]))                
                break
            elif ver_bool_response(arr,(tup[0]-i,tup[1]),up,start)==1:                
                poo.append((tup[0]-i,tup[1]))                
                break
            elif ver_bool_response(arr=arr,tup=(tup[0]-i,tup[1]),up=up,start=start)==3:                
                poo.append((tup[0]-i,tup[1]-1))                
                break
            elif ver_bool_response(arr=arr,tup=(tup[0]-i,tup[1]),up=up,start=start)==4:                
                poo.append((tup[0]-i,tup[1]+1))                
                break
            else:
                poo.append((tup[0]-i,tup[1]))
        else:            
            break
    
    if (len(po)<2 and len(poo)<2 and po==poo):
        pass
    elif len(po)<2:
        po.clear()
    elif len(poo)<2:
        poo.clear()
    by = {}
    if (po and ver_bool_response(arr,po[-1],up,start)):   
        pass
    else:
        po.clear()
    if (poo and ver_bool_response(arr,poo[-1],up,start)):   
        pass
    else:
        poo.clear()
    man_arr = []
    if po:
        by.update({man_dist(po[-1],target):po})
    if poo:
        by.update({man_dist(poo[-1],target):poo})
    
    ni = list(dict(sorted(by.items(),key = lambda x:x[0])).values())    
    if ni:        
        ni = ni[0]
        
        if destination(ni[-1],target):            
            the_path.append(ni)
        else:
            
            the_path.append(ni)            
            return post_short(q_list,look_up,arr,ni[-1],target,start)
        
    else:             
        return good_point_generator(q_list,tup,target,arr,tup_pre)
#####################################################################################################
"""Path_Post_Prcessing Functions"""

def duplicate_consecutive(x):
    qa = []    
    for i in range(len(x)-1):            
        if man_dist(x[i],x[i+1])==0:           
            qa.append(i)    
    for i in sorted(qa, reverse=True):
        del x[i]       
    return duplicate_non_consecutive(x)

def duplicate_non_consecutive(x):
    qa = []    
    for i in range(len(x)-1):
        for j in range(i+2,len(x)):
            if man_dist(x[i],x[j])==0:           
                qa.append((i,j))    
    s = []    
    for i in qa:
        s.append(np.arange(i[0]+1,i[1]+1))
    s = list(itertools.chain.from_iterable(s))
    for i in sorted(s, reverse=True):
        del x[i]
    print(x)
############################################################################################################
"""The Game Begins!"""

#Declaration of grid start and end points

"""Note-> I have inverted the coordinates, so (x,y) of the given digram must be represented as (y,x) below"""

"""Note-> There was some ambiguity if the robot is allowed to move diagonally therefore only the motions across the common edge are allowed in this algorigthm"""
grid =  [ [ 1,0,1,0,0 ], [ 0,0,0,0,1 ], [ 1,0,1,1,0 ], [ 0,0,0,0,0 ], [ 0,1,0,1,0 ] ]
global start
start = (4,2)
global target
target = (4,0)

"""Main calling function as required""" 
def myPathPlanning(grid,start,target):
    global look_up
    look_up={(j,i):grid[i][j] for i in range(len(grid)) for j in range(len(grid[0]))}
    bh = [(i,ind) for ind,value in enumerate(grid) for i,j in enumerate(value) if j==0 ]    
    global q_list
    q_list = []
    for i in range(len(grid[0])):
        q_list.append(list(itertools.takewhile(lambda x: x[1]==i,bh)))
        [bh.remove(g) for g in list(itertools.takewhile(lambda x: x[1]==i,bh))]
    global the_path
    the_path = []
    tup = start
    post_short(q_list=q_list,look_up=look_up,arr=grid,tup=start,target=target,start=start)
    vy = list(itertools.chain.from_iterable(the_path))
    duplicate_consecutive(vy)
##############################################################################################################
"""Calling the myPathPlanning"""
myPathPlanning(grid,start,target)
###############################################################################################################
