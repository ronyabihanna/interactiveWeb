from flask import Flask, render_template, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    dialect = "mysql"
    username="root"
    password=""
    host="127.0.0.1"
    dbname = "cyclists"
    #Connection object creation
    engine = create_engine("%s://%s:%s@%s/%s"%(dialect,username,password,host,dbname))

    try:
        con = engine.connect()

        #QUERY SQL
        query="SELECT CID, name, surname\
               FROM CYCLIST\
               ORDER BY CID"

        cyclist = con.execute(query)

     
        con.close()

        return render_template('index.html', cyclist = cyclist)

    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)


@app.route("/submitted.html", methods=["GET", "POST"])
def submitted():

    error=""

    if('cyclist_ID' not in request.args or 'SID' not in request.args):
        error += 'insert the missing field'
        return render_template('error.html', error_message=error)

    dialect = "mysql"
    username = "root"
    psw = ""
    host="127.0.0.1"
    dbname = "cyclists"

    try: 
        engine = create_engine(f"{dialect}://{username}:{psw}@{host}/{dbname}")
        con = engine.connect()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)

    if request.method == "GET":
        SID = request.args.get("SID")
      
    else:
        SID = request.form["SID"]

    query = f"SELECT c.name, surname, namet, t.tid\
             FROM CYCLIST c, TEAM t, INDIVIDUAL_RANKING i\
             WHERE t.tid = c.tid and i.CID = c.CID and sid = '{SID}'"

    result = con.execute(query)
    header = result.keys()

    return render_template("submitted.html", header=header, values=result, SID=SID)


app.run(debug=True, port=8080)
