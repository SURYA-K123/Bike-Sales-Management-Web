from flask import Flask, render_template, redirect, url_for, request, session
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Surya@4111",
  database="BIKE"
)


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def authenticate():
    username = request.form['u']
    password = request.form['p']
    cursor = mydb.cursor()
    cursor.execute("SELECT CATEGORY FROM USER WHERE USER_NAME='" +username + "' AND PASSWORD='" +password +"'")
    data = cursor.fetchone()
    if data is None:
        return "Username or password is wrong"
    elif data[0]=="user":
        return redirect(url_for('bikesmodel'))
    else:
        return redirect(url_for('vbranch'))

@app.route("/logout")
def logout():
    return redirect(url_for('my_form'))

    

@app.route("/addbikepage")
def addbikepage():
    return render_template("addbike.html")


@app.route("/editbikedetails", methods = ['POST'])
def editbikedetails():
    mycursor = mydb.cursor()
    id = request.form['id']
    brand =request.form['brand']
    model = request.form['model']
    image = request.form['image']
    price = request.form ['price']
    mileage = request.form['mileage']
    ec = request.form['ec']
    ftc  = request.form['ftc']
    gears = request.form['gears']
    ft = request.form['ft']
    brake = request.form['brake']
    mt = request.form['mt']
    mp = request.form['mp']
    sql = "UPDATE BIKE SET brand = %s, model_name = %s, image_path = %s, price = %s, mileage = %s, engine_capacity = %s, fuel_tank_capacity = %s, gears = %s, fuel = %s, brakes = %s, max_torque = %s, max_power = %s WHERE bike_id = %s"
    val = (brand, model, image, price, mileage, ec, ftc, gears, ft, brake, mt, mp,id)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('bikesadmin'))


@app.route("/addbikedetails", methods = ['POST'])
def addbikedetails():
    mycursor = mydb.cursor()
    brand =request.form['brand']
    model = request.form['model']
    image = request.form['image']
    price = request.form ['price']
    mileage = request.form['mileage']
    ec = request.form['ec']
    ftc  = request.form['ftc']
    gears = request.form['gears']
    ft = request.form['ft']
    brake = request.form['brake']
    mt = request.form['mt']
    mp = request.form['mp']
    sql = "INSERT INTO BIKE (brand, model_name, image_path, price, mileage, engine_capacity, fuel_tank_capacity, gears, fuel, brakes, max_torque, max_power) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (brand, model, image, price, mileage, ec, ftc, gears, ft, brake, mt, mp)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for('bikesadmin'))



@app.route('/vbranch')
def vbranch():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Branch")
    branch = cursor.fetchall()
    return render_template("vbranch.html", data=branch)


@app.route('/openeditbike', methods=['POST'])
def openaddbike():
    id = request.json['id']
    return redirect(url_for("editbike",id = id))


@app.route("/editbike/<string:id>")
def editbike(id):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM bike WHERE Bike_ID=%s"
    val = (id,)
    mycursor.execute(sql, val)
    res = mycursor.fetchone()
    mycursor.close()
    return render_template("editbike.html", datas=res)


@app.route("/addbike", methods=['POST'])
def addbike():
    if request.method == 'POST':
        MODEL_NAME = request.form['MODEL_NAME']
        PRICE = request.form['PRICE']
        MILEAGE = request.form['MILEAGE']
        mycursor = mydb.cursor()
        sql = "INSERT INTO bike (MODEL_NAME, MILEAGE, PRICE) VALUES (%s, %s, %s)"
        val = (MODEL_NAME, MILEAGE, PRICE)
        mycursor.execute(sql, val)
        mydb.commit()        
        return redirect(url_for("index"))
    return render_template("addbike.html")


@app.route("/deletebike/<string:id>", methods=['POST'])
def deletebike(id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM bike WHERE BIKE_ID=%s"
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
    return render_template("adminbike.html")


@app.route("/openaddbranch")        #hkhkhkkbjk
def openaddbranch():
    return render_template("addbranch.html")


@app.route("/addbranch", methods=['GET','POST'])    #dgfhjsdfgh
def addbranch():
    if request.method == 'POST':
        branchname = request.form['branchname']
        branchmanager = request.form['branchmanager']
        branchnumber = request.form['branchphone']
        branchlocation = request.form['branchlocation']
        stock = request.form['stock']
        mycursor = mydb.cursor()
        sql = "INSERT INTO branch (branchname, branchmanager,branch_location,branch_phone, stock) VALUES (%s, %s, %s, %s, %s)"
        val = (branchname, branchmanager, branchlocation,branchnumber,stock)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect(url_for("vbranch"))
    return render_template("addbranch.html")





@app.route("/editbranchpage/<datas>")    #kfgsdjdvsjdm
def editbranchpage(datas):
    branchid = datas
    mycursor = mydb.cursor()
    sql = "SELECT * FROM branch WHERE branchid = %s"
    val = (branchid,)
    mycursor.execute(sql, val)
    res = mycursor.fetchone()
    return render_template("editbranch.html",data=res)


@app.route("/editbranch", methods=['POST'])    #dfdfdf
def editbranch():
    branchid = request.json['id']
    return redirect(url_for("editbranchpage",datas=branchid))


@app.route("/update", methods =['POST'])   #fsdkfgsdjfg
def update():
    mycursor = mydb.cursor()
    branchid = int(request.form['branchid'])
    branchname = request.form['branchname']
    branchmanager = request.form['branchmanager']
    branchlocation = request.form['branchlocation']
    branchnumber = request.form['branchphone']
    stock = int(request.form['stock'])
    sql = "UPDATE BRANCH SET branchname = %s, branchmanager = %s, stock = %s, branch_location=%s, branch_phone=%s WHERE branchid = %s"
    val = (branchname, branchmanager, stock, branchlocation,branchnumber,branchid)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()
    return redirect(url_for("vbranch"))

@app.route("/deletebranch/<string:branchid>", methods=['POST'])  #fdfdff
def deletebranch(branchid):
    mycursor = mydb.cursor()
    sql = "DELETE FROM branch WHERE branchid=%s"
    val = (branchid,)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect(url_for("vbranch"))

@app.route('/bikesmodel')
def bikesmodel():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE")
    bike = mycursor.fetchall()
    return render_template("home.html", data=bike)


@app.route('/bikesec')
def bikesec():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE")
    bike = mycursor.fetchall()
    return render_template("enginecapacity.html", data=bike)


@app.route('/bikespr')
def bikespr():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE")
    bike = mycursor.fetchall()
    return render_template("pricerange.html", data=bike)


@app.route('/bikesadmin')   #vjmsjdfgjf
def bikesadmin():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE")
    bike = mycursor.fetchall()
    return render_template("adminbike.html", data=bike)


@app.route('/search_model', methods=['POST'])
def search_post():
    model = request.form['model']
    return redirect(url_for("fn", model=model))


@app.route('/fn/<model>')
def fn(model):
    mycursor = mydb.cursor()
    sql = "SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE WHERE MODEL_NAME = %s OR BRAND = %s "
    mycursor.execute(sql, (model, model))
    bikes = mycursor.fetchall()
    isbike = False
    if len(bikes)>=1:
        isbike = True
    return render_template("search.html", data=bikes, ispresent = isbike)

@app.route('/search_ec', methods=['POST'])
def search_ec():
    ec = request.form['ec']
    return redirect(url_for("search_ec_disp", ec=ec))


@app.route('/search_ec_disp/<ec>')
def search_ec_disp(ec):
    my_string = ec
    digits_only = "".join(filter(str.isdigit, my_string))
    engine = int(digits_only)
    mycursor = mydb.cursor()
    sql = "SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE WHERE ENGINE_CAPACITY >=%s"
    mycursor.execute(sql, (engine,))
    bikes = mycursor.fetchall()
    isbike = False
    if len(bikes)>=1:
        isbike = True
    return render_template("search.html", data=bikes, ispresent = isbike)


@app.route('/search_pr', methods=['POST'])
def search_pr():
    pr1 = request.form['pr1']
    pr2 = request.form['pr2']
    return redirect(url_for("search_pr_disp", pr1=pr1, pr2= pr2))


@app.route("/viewbranchbike",methods = ['POST'])
def viewbranchbike():
    branchid=request.form['bid']
    return redirect(url_for("viewthebike", bid=branchid))

@app.route("/viewthebike/<bid>")
def viewthebike(bid):
    mycursor = mydb.cursor()
    sql = "SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE WHERE BIKE_ID IN(SELECT BIKE_ID FROM BIKE WHERE BRANCH_ID1=%s OR BRANCH_ID2=%s)"
    val = (bid,bid)
    mycursor.execute(sql,val)
    bikes = mycursor.fetchall()
    print(bikes)
    return render_template("branchbike.html", data=bikes) 


@app.route('/search_pr_disp/<pr1>/<pr2>')
def search_pr_disp(pr1,pr2):
    sprice = pr1
    eprice = pr2
    mycursor = mydb.cursor()
    sql = "SELECT BIKE_ID,IMAGE_PATH,MODEL_NAME,BRAND,PRICE FROM BIKE WHERE PRICE >= %s AND PRICE <= %s"
    mycursor.execute(sql, (sprice,eprice,))
    bikes = mycursor.fetchall()
    isbike = False
    if len(bikes)>=1:
        isbike = True
    return render_template("search.html", data=bikes, ispresent = isbike)


@app.route('/send-message', methods=['POST'])
def receive_message():
    message = request.json['message']
    return redirect(url_for("details", message=message))


@app.route('/details/<message>')
def details(message):
    mycursor = mydb.cursor()
    id = int(message)
    sql = "SELECT * FROM BIKE WHERE bike_id = %s"
    mycursor.execute(sql, (id,))
    bikes = mycursor.fetchall()
    return render_template("detail.html",data=bikes)




@app.route("/billing")
def billing():
    return render_template("billing.html")

@app.route("/billingexecution" ,methods=['POST'])
def billingexecution():
    name = request.form['name'] 
    model = request.form['model']
    dob = request.form['dob']
    date = request.form['date']
    pn = request.form['pn']
    mail = request.form['mail']  
    mycursor = mydb.cursor()
    sql = "INSERT INTO BILLING (bill_time) VALUES (%s)"
    val = (date,)
    mycursor.execute(sql, val)
    bill_id = mycursor.lastrowid
    sql2 = "SELECT BIKE_ID FROM BIKE WHERE MODEL_NAME = %s" 
    mycursor.execute(sql2,(model,))
    id1 = mycursor.fetchone()
    id=id1[0]
    print(id)
    sql1= "INSERT INTO CUSTOMER (CUSTOMER_NAME,DOB,PHONE_NUMBER,EMAIL,BIKE_ID,BILL_ID) VALUES(%s,%s,%s,%s,%s,%s)"
    val1=(name,dob,pn,mail,id,bill_id)
    mycursor.execute(sql1,val1)
    mydb.commit()
    return redirect(url_for("finalbill",id = id))


@app.route("/finalbill/<id>")
def finalbill(id):
    cursor = mydb.cursor()
    query = "SELECT * FROM BIKE WHERE BIKE_ID = (SELECT BIKE_ID FROM CUSTOMER WHERE BILL_ID =%s)"
    cursor.execute(query, (id,))
    result = cursor.fetchone()
    q1 = "SELECT BILL_TIME FROM BILLING WHERE BILL_ID = %s"
    cursor.execute(q1,(id,))
    date = cursor.fetchone()
    return render_template("bill.html", data=result,billno = id, today=date[0])



if __name__ == '__main__':
    app.run(debug=True)
