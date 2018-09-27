#q.1 Take students name and marks from the user
import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['student']
#q.2 Append the values in 2 columns
for i in range(10):
    try:
        name = input("Enter the name: ") 
        marks = int(input('Enter your Marks: '))
        if(marks<0 or marks >100):  
            raise ValueError('Invalid entry of marks')
            i=i-1
        else:#q.3 create a database of students
            collection.insert_one({'Name':name,'Marks':marks})  
            i=i+1
    except  ValueError as msg:
        print(msg)
#q.4 print the names of all the students who scored more than 80 marks
db=collection.find({"Marks":{"$gt":80}})
for data in db:
    print(data)
