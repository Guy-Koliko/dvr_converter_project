from django.shortcuts import render,redirect
from django.conf import settings
import os,re
from datetime import datetime



#===================================#
# this is for the index page       #
#=================================#
def index(request):
    return render(request, 'melcom_one/index.html')
    
#========================================#
# this get the files and pefrom an action#
#========================================#
def getprems(request):
    
    path = settings.MEDIA_ROOT
    if request.method == 'POST':
        starttime = request.POST['starttime']
        endtime = request.POST['endtime']
        channel = request.POST['channel']
        startdates = request.POST['dates']
        enddates = request.POST['edates']
        media = os.listdir(path + '/')
        
        #*********************************#]
        # looping through the media file #
        #********************************#
        filter_file = []
        for l in media:
            #*****************************************#
            # sperating the date from the time       #
            #***************************************#
            aprat = re.split(r'[_.]', l)
            cdate = aprat[3]
            edate = aprat[4]
            rdate = datetime.strptime(cdate, '%Y%m%d%H%M%S')#full start date and time
            ldate = datetime.strptime(edate, '%Y%m%d%H%M%S')#full end date and time
            mdate = str(rdate.date()) #extracted start date 
            ndate =  str(ldate.date()) #extracted end date 
            stime = str(rdate.time())#extrated start time
            etime = str(ldate.time())#extracted end time
            
            
            #********************************************************#
            #take the converted date and time and strip of the(-,:) #
            # and peform some action on it with regx               #
            #*****************************************************# 
            startdatestrip = re.split(r'-',startdates)
            enddatestrip = re.split(r'-',enddates)
            starttimestrip = re.split(r':',starttime)
            endtimestrip = re.split(r':',endtime)
            user_sd_input = ''.join(startdatestrip)
            user_ed_input = ''.join(enddatestrip)
            user_st_input = ''.join(starttimestrip)
            user_et_input = ''.join(endtimestrip)
            
            
            #**************************************************#
            # concatinating the user date and time together   #
            #************************************************#
            user_starttime_date = (user_sd_input + user_st_input).strip()
            user_endtime_date = (user_ed_input + user_et_input).strip()
            
            regx = re.compile(r'(\w+[A-Z]_)([a-z0-9_]{3}_)(\w{4}_)(\d{14})_(\d{14})(\.[a-z0-9]{3})')
            regx_iter = regx.finditer(l)
            
            #************************************#
            # this part takes care of the file  #
            # filtering and rending to the page#
            #**********************************
            for file in regx_iter:
                
                query_st_sd = file.group(4)
                query_et_ed = file.group(2)
                
                if starttime == None and endtime == None and  startdates == None and channel ==None :
                    pass
                elif  (user_starttime_date) <= (query_st_sd) and (user_endtime_date)<= (query_et_ed):
                    filter_file.append(l)
        context = {'data':filter_file}
        return render(request, 'melcom_one/filter.html',context)
             