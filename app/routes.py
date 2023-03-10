from flask import Flask
     #From the flask module import the Flask class.

app = Flask(__name__)       #Create an instance of Flask into a variable called "app".
                            #From this point forward, app is an "object".


@app.get("/")               #Flask specific decorator to create routes.
def about_me():             #Veiw function. Functions mapped to routs are called veiw functions.
    me = { #on line 8, we are creating a dictionary with our details.                                               
        "first_name": "Edgar",
        "last_name": "Perez",
        "hobbies": "Art",
        "active": True
    }

    return me               #when we return a dictionary from a veiw function. #flask automatically coverts it to JSON.