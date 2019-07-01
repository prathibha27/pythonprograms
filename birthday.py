birthday={'navya' : '29 dec' , 'pragna' :'25 oct ' , 'spoo':'18 dec' , 'trupti': '16 may' }
while True :
  print("enter the name ")
  name=input('>>')
  if name=='':
    break

  if name in birthday:
       print (birthday[name] + " is the DOB of "+ name)

  else :
    print ("sorry I dont know when is their birthday , do tell me , I ll remember ")
    bday =input('>>')
    birthday[name]=bday
    print("birthday updated to the database")
 

       
       
 
