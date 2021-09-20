import datetime
import random
import string 
import json 
from datetime import date
import time
#Take 20 sample Contacts
contacts=[ 'mohith','nag','priya','venkatesh','sriya','neha','chandu','sai','gayatri','Anusha','harish','varshini','vishnavi']
#loading json file
f=open('data.json','r+') 
data=json.load(f)
# sending a file  
def send_file():
    print("...sending...")
    user1='me'
    user2=random.choice(contacts)
    print("Enter file to send to {}:".format(user2))
    to_send=input()
    today=date.today()
    d4 = today.strftime("%b-%d-%Y")
    try:
        data['container'][d4]['sent'].append(to_send)
    except:
        data['container'][d4]={'sent':[to_send],'received':[]}

    finally:   
        time.sleep(1)
        print("...File sent succesfully...")
        json.dump(data,f)
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data,f,indent=4)
        f.truncate()
#receiving a file
def receive_file():
    user1=random.choice(contacts)
    user2='me'
    types=['.doc','.pdf','.xls','.ppt']
    received=''.join((random.choice(string.ascii_lowercase) for x in range(8)))+random.choice(types)
    today=date.today()
    d4 = today.strftime("%b-%d-%Y")
    try:
        data['container'][d4]['received'].append(received)
    except:
        data['container'][d4]={ 'sent':[],'received':[received]}
    finally:
        time.sleep(1)
        print("....File named {} Received...".format(received))
        json.dump(data,f)
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()
#display list
def display():
    print("1.Single date\n2.Rangeof dates \n3.Exit")
    choice=input("Enter Choice:")
    if choice =='1':
        date1 = datetime.date(int(input("year:")), int(input("month:")), int(input("date:")))
        key=date1.strftime('%b-%d-%Y')
        try:
            print("Sent files on {} are {}".format(key,data['container'][key]['sent']))
            print("received files on {} are {}".format(key,data['container'][key]['received']))
        except :
            print("No files found on given date")
    elif choice=='2':
        sentlist=[]
        receivedlist=[]
        date1 = datetime.date(int(input("from year:")), int(input("from month in num:")), int(input("from date:")))
        date2 = datetime.date(int(input("To year:")), int(input("To month in num :")), int(input("To date:")))
        day = datetime.timedelta(days=1)
        while date1 <= date2:
            key=date1.strftime('%b-%d-%Y')
            try:
                sentlist.append(data['container'][key]['sent'])
                receivedlist.append(data['container'][key]['received'])
            except:
                pass
                    
                
                
            date1 = date1 + day 
        if sentlist!=[] or  receivedlist!=[]:
            print("sent files :",sentlist)
            print("received files:",receivedlist)
        else:
            print("!!!!!!!!No files found!!!!!!!!")
        
    else:
        exit(0)


#Driver Code
while True:
    print("******\n1:Send File \n2:Receive File\n3:FilterByDate\nothers:exit\n******")
    choice=input("Enter Choice:")
    if choice=='1':
        send_file()
    elif choice=='2':
        receive_file()
    elif choice=='3':
        display()
        
    else:
        exit(0)




