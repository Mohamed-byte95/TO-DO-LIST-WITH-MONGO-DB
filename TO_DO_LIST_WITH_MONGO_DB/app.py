# PYMONGO FOR HANDLING THE DATA BASE 
from pymongo import MongoClient
#FLASK LIBRAY TO CREATE THE SERVER AND CONTROL THE WEBSITE AND DIFFERENT TEMPLATES 
from flask import Flask ,render_template , url_for , request , redirect
#TO READ THE OBJECT ID OF THE DOCUMENTS WITHIN THE COLLECTION 
from bson.objectid import ObjectId


app = Flask(__name__)
#CREATING A CONNECTION TO THE DATA BASE SERVER 
client = MongoClient('localhost',27017)

#CREATE A ROUTE TO THE MAIN PATH 
@app.route("/",methods=["GET","POST"])


#THIS IS A HANDLER TO REDNER OUR HOME PAGE TO THE INDEX PAGE 
def index():
    #CHECK IF THE THE REQUEST IS POST
    if request.method== 'POST':
        #RETIRVE DATA FROM THE FORM 
        content = request.form['content']
        degree = request.form['Degree']
        #INSERT RAW DATA INTO THE COLLECTION OF THE DATABASE
        todos.insert_one({"content":content,"Degree":degree})
        return redirect(url_for('index'))
    #GET ALL THE TODOS STORED INSIDE THE DATABASE 
    all_todos = todos.find()
    return render_template("index.html",todos=all_todos) 

#DEFINE A NEW ROUTE FOR THE DELETE
@app.post("/<id>/delete/")

#DEFINE A HANDLER FOR DELETING ELEMENTS FROM THE DATA BASE 
def delete(id):
    todos.delete_one({"_id":ObjectId(id)})
    return redirect(url_for('index'))

#FETCH THE DATA FROM THE DATA BASE 

@app.route("/<id>/update/" , methods = ["GET","POST"])

@app.post("/<id>/update/" )
def update_item(id):
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['Degree']
        print(id)
        todos.update_one({"_id":ObjectId(id)},{"$set": {"content": content,"Degree":degree}})
        return redirect(url_for('index'))
    elif request.method == 'GET':
        #FIND THE SELECTED ITEM IN THE DATA BASE 
        
        update_item = todos.find_one({"_id":ObjectId(id)})
        importance = update_item['Degree']
        #SHOW DATE THE DATA INTO THE TEMPLATE 
        return render_template("index.html" , item = update_item['content'],deg=importance)


#CREATING MONGO_DB
db = client.TODO_DB

#CREATING  TODOS COLLECTION
todos = db.todos

#MAIN FUNCTION 
if __name__== "__main__":
    app.run(debug=True)

