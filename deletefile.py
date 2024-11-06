'''
This code is use for deleting a file with the dates,without deleting current and yestaday date it will delete other date folders.
'''
import os
import shutil
from datetime import datetime,date,timedelta


path = "D:/pyt-practice/GFG/smalltest/"
list_dir = os.listdir(path)
yestaday = date.today() - timedelta(days=1)
today = date.today()
# It store current & yestaday date
need_dates = [today,yestaday]      

for iter in list_dir:    
    list_strdir = str(iter)
    #It will splite the folder name into date,other.
    split_list = list_strdir.rsplit("-",1)
    #It will convert a string formate date to datetime formate.  
    nd_dtformat = datetime.strptime((split_list[0]),'%Y-%m-%d').date() 
    if nd_dtformat not in  need_dates:
        # It will attach a path and folder name in single string variable.
        path_local = os.path.join(path,iter) 
        # It will remove the folder without current & yestaday date.
        shutil.rmtree(path_local) 
        print("deleting dir complete")
        
        
        
        
        
        
        
        
        
        
        
        
        
        #y = date.today()
        #yestaday = date.today() - timedelta(days=3)
        #print(y,"tday")
        #print(yestaday,"yest")
        #breakpoint()
        #print("there is not 4 folders ,there is less then 4")

    
 
