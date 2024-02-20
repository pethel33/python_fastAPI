from fastapi import FastAPI

app = FastAPI()


#student resource data name,age,sex,height
#create student resoucrce in a class collection, 
#dic of name and object --- name: student
class Student:
    def _init_(self, name: str, age: int, sex: str, height: float):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        
#dict in memory storage
students = {}
        
# #define home route
@app.get('/home')
def home():
    return{'message': 'success'}



#create student 
@app.post('/students')
def create_student(name: str, age: str, sex:str, height:str):
    id_ = len(students) + 1
    new_student = {
        'id': id_,       
        'name': name,
        'age': age,
        'sex': sex,
        'height': height
    }
    
    #database of students
    students[id_] = new_student
    return{'message': 'students created successfully', 'data': new_student}

#get the all student, retrive all student created from data base using the get method, return the sudents data dict
#the endpoint is students 
#customize data in array gotten using foreach loop
@app.get('/students')
def get_all():
    #create an empty array, use the forloop and append the data 
    student_arr = []
    for stud in students:
        student_arr.append(students[stud])
    return{'message': 'students gotten sucessfully', 'data': student_arr}
    
    
#get only one student not all, using the get method with a pat parameter
#path and pre parameter -- /{id} and ?{id}
    
@app.get('/students/{id}')
def get_one_student(id: int):
    student = students[id]
    return{
        'message': 'one student fetched succesffuly', 'data': student
    }
    
#update student
#get student by id
#student gotten to new changes
    #return update message 
@app.put('/students/{id}')
def update_student(id: int, name: str):
    student = students[id]
    student['name'] = name
    return{
        'message': 'updated sucessfully',
        'data': student
    }
    
#delete
#using status code message
#500 status code is from server
#400 is from client
@app.delete('/students/{id}')
def delete_student(id: int, name: str):
    student = students[id]
    name = student['name']
    del students[id]
    return{
        'message': 'student successfully deleted',
        'data': student
    }
    
        
        
