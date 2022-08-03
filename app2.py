from flask import Flask, render_template, request
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine

app = Flask(__name__)

@app.route("/")
@app.route("/index2.html")
def index2():
    error=""
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
        query="SELECT TID, namet\
               FROM TEAM\
               ORDER BY TID"

        team = con.execute(query)
     
        con.close()

        return render_template('index2.html', team = team)

    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)


@app.route("/submitted2.html", methods=["GET", "POST"])
def submitted2():
    error=""

    if('CID' not in request.args or'Name' not in request.args or 
        'Surname' not in request.args or 'Nation' not in request.args):
            error += 'Insert the missing fields. '
            return render_template('error.html', error_message=error)


    CID = request.args.get('CID')
    Name = request.args.get('Name')
    Surname = request.args.get('Surname')
    Nation = request.args.get('Nation')
    TID = request.args.get('TID')   
    BirthYear = (int)(request.args.get('BirthYear'))
    

    if (CID=="" or Name=="" or Surname=="" or Nation=="" ):
        error += 'Insert the missing fields. '
        return render_template('error.html', error_message=error)

   
    error=""
    dialect = "mysql"
    username="root"
    password=""
    host="127.0.0.1"
    dbname = "cyclists"
    #Connection object creation
    engine = create_engine("%s://%s:%s@%s/%s"%(dialect,username,password,host,dbname))

    try:
        con = engine.connect()    

        query = "INSERT INTO cyclist(CID, Name, Surname, Nationality, TID, BirthYear)\
                VALUES ('%s','%s','%s','%s','%s','%s')"%(CID,Name,Surname,Nation, TID, BirthYear)
        con.execute(query)

        con.close()
	
        return render_template('submitted2.html')
    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)



@app.route("/index3.html")
def index3():
    error=""
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
        query="SELECT CID\
               FROM cyclist"

        cyclist = con.execute(query)

        query="SELECT  SID\
               FROM stage"

        stage = con.execute(query)

        query="SELECT Edition\
               FROM stage"

        edition = con.execute(query)
     
        con.close()

        return render_template('index3.html', cyclist = cyclist, stage = stage, edition = edition )

    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)



@app.route("/submitted3.html", methods=["GET", "POST"])
def submitted3():
    error=""
    if('CID' not in request.args or 'SID' not in request.args or 
       'Edition' not in request.args or 'cyclist_position' not in request.args):
        error += 'Insert missing1 field. '
        return render_template('error.html', error_message=error)


    CID = request.args.get('CID')
    SID = request.args.get('SID')
    Edition = request.args.get('Edition')
    cyclist_position = request.args.get('cyclist_position')
    
    if (CID=="" or SID=="" or Edition=="" or cyclist_position==""):
        error += 'Insert the missing2 fields. '
        return render_template('error.html', error_message=error)

    error=""
    dialect = "mysql"
    username="root"
    password=""
    host="127.0.0.1"
    dbname = "cyclists"
    #Connection object creation
    engine = create_engine("%s://%s:%s@%s/%s"%(dialect,username,password,host,dbname))

    try:
        con = engine.connect()    

        query = "INSERT INTO individual_ranking(CID,SID, Edition,Location )\
                VALUES ('%s','%s','%s','%s')"%(CID,SID, Edition,cyclist_position )
        con.execute(query)

        con.close()
	
        return render_template('submitted3.html')
    except SQLAlchemyError as e:

        error = str(e.__dict__['orig'])
        return render_template('error.html', error_message=error)



app.run(debug=True, port=8080)
