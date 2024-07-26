def add():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("INSERT THE INPORMATION ABOUT THE PATIENT")
    print('')
    PATIENT_ID=int(input("ENTER THE PATIENT ID IN DIGITS:"))
    print('')
    PATIENT_NAME=input("ENTER THE PATIENT NAME :")
    print('')
    AGE=int(input("ENTER THE AGE OF THE PATIENT :"))
    print('')
    DISEASE=input("ENTER THE DISEASE OF THE PATIENT :")
    print('')
    INCHARGE=input("ENTER THE NAME OF THE DOCTOR INCHARGE :")
    print('')
    DATE_OF_ADDMISSION=input("ENTER THE DATE OF ADDMISSION OF THE PATIENT :")
    print('')
    FEE=int(input("ENTER THE AMOUNT OF FEE PER/DAY :"))
    print('')
    ROOM_NUMBER=int(input("ENTER THE ROOM NUMBER :"))
    mycursor.execute("use PATIENT_RECORD")
    mycursor.execute("insert into MED_CARE(PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION)values('%d','%s','%d','%s','%s','%d','%d','%s')"%(PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION))
    print('')
    print("===================================================================================================================================================================")
    print("                                                                    PATIENT ADDED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")





def add_doctor():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("INSERT THE INPORMATION ABOUT THE DOCTOR")
    print('')
    DOCTOR_ID=int(input("ENTER THE DOCTOR ID IN DIGITS:"))
    print('')
    DOCTOR_NAME=input("ENTER THE DOCTOR NAME :")
    print('')
    SPECIALIZATION=input("ENTER THE SPECIALIZATION OF THE DOCTOR :")
    print('')
    DOCTOR_FEE=int(input("ENTER THE FEE OF THE DOCTOR :"))
    print('')
    AVAILABILITY=input("ENTER THE AVAILABILITY OF THE DOCTOR(DAY - DAY) :")
    print('')
    mycursor.execute("use DOCTOR_RECORD")
    mycursor.execute("insert into DOCTOR(DOCTOR_ID,DOCTOR_NAME,SPECIALIZATION,DOCTOR_FEE,AVAILABILITY)values('%d','%s','%s','%d','%s')"%(DOCTOR_ID,DOCTOR_NAME,SPECIALIZATION,DOCTOR_FEE,AVAILABILITY))
    print('')
    print("===================================================================================================================================================================")
    print("                                                                    DOCTOR ADDED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")





def add_STAFF():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("INSERT THE INPORMATION ABOUT THE STAFF")
    print('')
    STAFF_ID=int(input("ENTER THE STAFF ID IN DIGITS:"))
    print('')
    STAFF_NAME=input("ENTER THE STAFF NAME :")
    print('')
    JOB=input("ENTER THE JOB OF THE STAFF :")
    print('')
    STAFF_SALARY=int(input("ENTER THE SALARY OF THE STAFF :"))
    print('')
    mycursor.execute("use STAFF_RECORD")
    mycursor.execute("insert into STAFF(STAFF_ID,STAFF_NAME,JOB,STAFF_SALARY)values('%d','%s','%s','%d')"%(STAFF_ID,STAFF_NAME,JOB,STAFF_SALARY))
    print('')
    print("===================================================================================================================================================================")
    print("                                                                    STAFF ADDED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")





    
    
def delete():
    print("*******************************************************************************************************************************************************************")
    print('')
    s=int(input("ENTER THE PATIENT_ID OF THE PATIENT THAT YOU WANT TO DELETE :"))
    mycursor.execute("use PATIENT_RECORD")
    mycursor.execute("delete from MED_CARE where PATIENT_ID={}".format(s))
    print("===================================================================================================================================================================")
    print("                                                               RECORD DELETED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")

    
    


def delete_DOCTOR():
    print("*******************************************************************************************************************************************************************")
    print('')
    s=int(input("ENTER THE DOCTOR_ID OF THE DOCTOR THAT YOU WANT TO DELETE :"))
    mycursor.execute("use DOCTOR_RECORD")
    mycursor.execute("delete from DOCTOR where DOCTOR_ID={}".format(s))
    print("===================================================================================================================================================================")
    print("                                                              DOCTOR RECORD DELETED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")



def delete_STAFF():
    print("*******************************************************************************************************************************************************************")
    print('')
    s=int(input("ENTER THE STAFF_ID OF THE STAFF THAT YOU WANT TO DELETE :"))
    mycursor.execute("use STAFF_RECORD")
    mycursor.execute("delete from STAFF where STAFF_ID={}".format(s))
    print("===================================================================================================================================================================")
    print("                                                              STAFF RECORD DELETED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")

    

def display():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("===================================================================================================================================================================")
    print("                                                                MEDANTA HOSPITAL PATIENT RECORD TABLE")
    print("===================================================================================================================================================================")

    mydb.commit()
    print('')
    print('')
    print('')
    mycursor.execute("use PATIENT_RECORD")
    mycursor.execute("select * from MED_CARE")
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print("                       PATIENT_ID\tPATIENT_NAME\t    AGE\t         DISEASE\t  INCHARGE\t        FEE\t ROOM_NUMBER\t DATE_OF_ADDMISSION")
    for i in mycursor:
        PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION=i
        print('')
        print('                       ',PATIENT_ID,"\t",'      ',PATIENT_NAME,"\t",'   ',AGE,"\t",DISEASE,"\t",'',INCHARGE,"\t",FEE,"\t",'  ',ROOM_NUMBER,"\t",'   	  ',DATE_OF_ADDMISSION)
        print('')
        print('')

    print('')
    print('')
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")



def display_doctor_records():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("===================================================================================================================================================================")
    print("                                                                MEDANTA HOSPITAL DOCTOR RECORD TABLE")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print('')
    print('')
    mycursor.execute("use DOCTOR_RECORD")
    mycursor.execute("select * from DOCTOR")
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print("                                                 DOCTOR_ID\tDOCTOR_NAME\t    SPECIALIZATION\t   FEE\t  AVAILABILITY")
    for i in mycursor:
        DOCTOR_ID,DOCTOR_NAME,SPECIALIZATION,FEE,AVAILABILITY=i
        print('')
        print('                                                 ',DOCTOR_ID,"\t",'      ',DOCTOR_NAME,"\t",'   ',SPECIALIZATION,"\t"' ',FEE,"\t",'',AVAILABILITY)
        print('')
        print('')
    print('')
    print('')
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")
    





def display_STAFF():
    print("*******************************************************************************************************************************************************************")
    print('')
    print("===================================================================================================================================================================")
    print("                                                                MEDANTA HOSPITAL STAFF RECORD TABLE")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print('')
    print('')
    mycursor.execute("use STAFF_RECORD")
    mycursor.execute("select * from STAFF")
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print("                                                   STAFF_ID\t    STAFF_NAME\t    JOB\t     STAFF_SALARY")
    for i in mycursor:
        STAFF_ID,STAFF_NAME,JOB,STAFF_SALARY=i
        print('')
        print('                                                   ',STAFF_ID,"\t",'      	    ',STAFF_NAME,"\t",'  ',JOB,"\t",STAFF_SALARY)
        print('')
        print('')
    print('')
    print('')
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")







def update():
    print("*******************************************************************************************************************************************************************")
    print('')
    m=input("ENTER THE PATIENT ID :")
    print('')
    dr=input("ENTER THE NEW DOCTOR FEES :")
    mycursor=mydb.cursor()
    mycursor.execute("use PATIENT_RECORD")
    n="update MED_CARE set FEE="+dr+" where PATIENT_ID="+m+';'
    mycursor.execute(n)
    mycursor.execute("select * from MED_CARE where PATIENT_ID="+m)
    print('')
    print("*******************************************************************************************************************************************************************")
    for i in mycursor:
        PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION=i
        print("PATIENT_ID\tPATIENT_NAME\tAGE\t    DISEASE\t INCHARGE\t  	 FEE\tROOM_NUMBER\tDATE_OF_ADDMISSION")
        print(PATIENT_ID,"\t",'      ',PATIENT_NAME,"\t",AGE,"\t"'    ',DISEASE,"\t",INCHARGE,"\t",FEE,"\t"' ',ROOM_NUMBER,"\t",('	 '),DATE_OF_ADDMISSION)
    print('')
    print('')
    print("===================================================================================================================================================================")
    print("                                                                    RECORD UPDATED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")







def search():
    print("*******************************************************************************************************************************************************************")
    print('')
    t=input("ENTER PATIENT ID TO SEARCH :")
    mycursor.execute("use PATIENT_RECORD")
    mycursor.execute("select*from MED_CARE where PATIENT_ID="+t)
    print('')
    print("                       PATIENT_ID\tPATIENT_NAME\t    AGE\t         DISEASE\t  INCHARGE\t        FEE\t ROOM_NUMBER\t DATE_OF_ADDMISSION")
    for i in mycursor:
        PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION=i
        print('')
        print('                       ',PATIENT_ID,"\t",'      ',PATIENT_NAME,"\t",'   ',AGE,"\t",DISEASE,"\t",'',INCHARGE,"\t",FEE,"\t",'  ',ROOM_NUMBER,"\t",'   	  ',DATE_OF_ADDMISSION)
        print('')
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")




def billGENRATION():
    print("*******************************************************************************************************************************************************************")
    print("===================================================================================================================================================================")
    print("                                                                 BILL GENERATION")
    print("===================================================================================================================================================================")
    print('')
    t=input("ENTER PATIENT ID TO GENERATE BILL :")
    mycursor.execute("use PATIENT_RECORD")
    mycursor.execute("select*from MED_CARE where PATIENT_ID="+t)
    u=mycursor.fetchone()
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print("              PATIENT ID:",t)
    print("              AMOUNT OF FEE PER/DAY : ",u[5])
    c=int(input("              ENTER THE NO. OF DAYS PATIENT ADMITED FOR :"))
    m=int(input("              ENTER THE TOTAL DISCOUNT (IF ANY) IN DIGITS :"))
    x=u[5]*c*m/100
    n=int(input("              ENTER ANY ADDITIONAL CHARGES (IF ANY) IN DIGITS :"))
    print('')
    print("              TOTAL AMOUNT PAYABLE : ",u[5]*c-x+n,'Rs/-')
    print('')
    print('')
    print('')
    print('')
    mycursor.execute("select*from MED_CARE where PATIENT_ID="+t)
    print('')
    print("                       PATIENT_ID\tPATIENT_NAME\t    AGE\t         DISEASE\t  INCHARGE\t        FEE\t ROOM_NUMBER\t DATE_OF_ADDMISSION")
    for i in mycursor:
        PATIENT_ID,PATIENT_NAME,AGE,DISEASE,INCHARGE,FEE,ROOM_NUMBER,DATE_OF_ADDMISSION=i
        print('')
        print('                       ',PATIENT_ID,"\t",'      ',PATIENT_NAME,"\t",'   ',AGE,"\t",DISEASE,"\t",'',INCHARGE,"\t",FEE,"\t",'  ',ROOM_NUMBER,"\t",'   	  ',DATE_OF_ADDMISSION)
        print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print("===================================================================================================================================================================")
    print("                                                             BILL GENRATED SUCCESSFULLY")
    print("===================================================================================================================================================================")
    mydb.commit()
    print('')
    print("*******************************************************************************************************************************************************************")
    print('')
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print("")
    print("*******************************************************************************************************************************************************************")

    

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||     MAIN PROGRAM    |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



                                                               ###HOSPITAL MANAGEMENT SYSTEMS###

                                                        ### CREATED BY- AADEE KANCHAN // CLASS : 12th-A ###

                                                                    ## SESSION : 2023/2024 ##
print("*******************************************************************************************************************************************************************")
print('\/\/'*40)
print("===================================================================================================================================================================")
print('                                                                 HOSPITAL MANAGEMENT SYSTEMS                                                     ')     
print('')
print('                                                         CREATED BY- AADEE KANCHAN // CLASS : 12th-A                                                                                                                                                      ')
print('')
print('                                                                     SESSION : 2023/2024                                                                                                              ')
print("===================================================================================================================================================================")
print('\/\/'*40)
print("*******************************************************************************************************************************************************************")


import mysql.connector as obj
mydb=obj.connect(host='localhost',user='root',password='1234')                


if mydb.is_connected():
    print("")
    print("Loding*")
    print("")
    print("Loding**")
    print("")
    print("Loding***")
    print("")
    print("Loding****")
    print("")
    print("Loding*****")
    print("")
    print("===================================================================================================================================================================")
    print("                                                                    CONNECTED SUCESSFULLY")
    print("===================================================================================================================================================================")
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
    print('|| || '*27)
        

#TO CREAT TABLES AND DATABASES IF NOT EXIST
    

import mysql.connector as obj
mydb=obj.connect(host='localhost',user='root',password='1234')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists PATIENT_RECORD")
mycursor.execute("use PATIENT_RECORD")
mycursor.execute("create table if not exists MED_CARE\
                (PATIENT_ID int primary key,\
                PATIENT_NAME varchar(20),\
                AGE int not null,\
                DISEASE varchar(20),\
                INCHARGE varchar(20),\
                FEE int,\
                ROOM_NUMBER int,\
                DATE_OF_ADDMISSION varchar(20))")



import mysql.connector as obj
mydb=obj.connect(host='localhost',user='root',password='1234')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists DOCTOR_RECORD")
mycursor.execute("use DOCTOR_RECORD")
mycursor.execute("create table if not exists DOCTOR\
                (DOCTOR_ID int primary key,\
                DOCTOR_NAME varchar(20),\
                SPECIALIZATION varchar(20),\
                DOCTOR_FEE int,\
                AVAILABILITY varchar(20))")



import mysql.connector as obj
mydb=obj.connect(host='localhost',user='root',password='1234')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists STAFF_RECORD")
mycursor.execute("use STAFF_RECORD")
mycursor.execute("create table if not exists STAFF\
                (STAFF_ID int primary key,\
                STAFF_NAME varchar(20),\
                JOB varchar(20),\
                STAFF_SALARY int)")



#MAIN PROGRAM 


dm=0
while dm==0:
    print('')
    print("===================================================================================================================================================================")
    print("                                                              MEDANTA HOSPITAL MANAGEMENT DEPARTMENT")
    print("===================================================================================================================================================================")
    print("LIST FOR MANAGING RECORDS OF PATIENTS AND DOCTORS/STAFF")
    print("===================================================================================================================================================================")
    print('')
    print(" 1.  ADD A NEW PATIENT")
    print('')
    print(" 2.  DELETE OLD PATIENTS RECORDS")
    print('')
    print(" 3.  DISPLAY THE PATIENTS RECORDS")
    print('')
    print(" 4.  UPDATE THE PATIENTS RECORDS")
    print('')
    print(" 5.  SEARCH THE PATIENTS RECORDS")
    print('')
    print(" 6.  BILL GENRATION")
    print("")
    print("===================================================================================================================================================================")
    print('')
    print(" 7.  ADD A NEW DOCTOR")
    print('')
    print(" 8.  DISPLAY THE RECORDS OF DOCTOR")
    print('')
    print(" 9.  DELETE OLD DOCTOR RECORDS")
    print('')
    print("===================================================================================================================================================================")
    print('')
    print("10.  ADD A NEW STAFF MEMBER")
    print('')
    print("11.  DISPLAY THE RECORDS OF STAFF MEMBERS")
    print('')
    print("12.  DELETE OLD STAFF RECORDS")
    print('')
    print("===================================================================================================================================================================")
    print('')
    print("13.  EXIT")
    print('')
    print("===================================================================================================================================================================")
    ch=int(input("ENTER YOUR CHOICE:"))
    if ch==1:
        add()

    elif ch==2:
        delete()

    elif ch==3:
        display()

    elif ch==4:
        update()

    elif ch==5:
        search()

    elif ch==6:
        billGENRATION()

    elif ch==7:
        add_doctor()
        
    elif ch==8:
        display_doctor_records()

    elif ch==9:
        delete_DOCTOR()

    elif ch==10:
        add_STAFF()

    elif ch==11:
        display_STAFF()

    elif ch==12:
        delete_STAFF()

    elif ch==13:
        exit()

    else:
        print("PLEASE SELECT CORRECT OPTION!!!")
        






    









    
        
        
    
    









    
    
    
    
        
        
    

