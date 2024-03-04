from flask import Flask, render_template, url_for, request, session, redirect
import mysql.connector
import secrets

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    database="Inventary",
    password="",
    ) 
cursor=connection.cursor()

# SQL commands
commands = [
  """CREATE TABLE IF NOT EXISTS hospital (Id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, password TEXT, mobile TEXT, email TEXT)""",
  """CREATE TABLE IF NOT EXISTS manufacture (Id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, password TEXT, mobile TEXT, email TEXT)""",
  """CREATE TABLE IF NOT EXISTS wholesaler (Id INTEGER PRIMARY KEY AUTO_INCREMENT, name TEXT, password TEXT, mobile TEXT, email TEXT)""",
  """CREATE TABLE IF NOT EXISTS products (Id INTEGER PRIMARY KEY AUTO_INCREMENT, mname TEXT, name TEXT, quantity TEXT, md TEXT, ed TEXT)""",
  """CREATE TABLE IF NOT EXISTS wholesalerorders (Id INTEGER PRIMARY KEY AUTO_INCREMENT, wname TEXT, pid TEXT, quantity TEXT)""",
  """CREATE TABLE IF NOT EXISTS hospitalrorders (Id INTEGER PRIMARY KEY AUTO_INCREMENT, wname TEXT, pid TEXT, quantity TEXT)"""
]

# Execute SQL commands
for command in commands:
  cursor.execute(command)

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    connection = mysql.connector.connect(
    host="127.0.0.1",
    database="Inventary",
    user="root",
    password="",
    ) 
    cursor=connection.cursor()

    cursor.execute("SELECT * FROM hospital")
    result = cursor.fetchall()
    num_hospital = 0
    if result:
        num_hospital = len(result)
    
    cursor.execute("SELECT * FROM manufacture")
    result = cursor.fetchall()
    num_manufacture = 0
    if result:
        num_manufacture = len(result)
    
    cursor.execute("SELECT * FROM wholesaler")
    result = cursor.fetchall()
    num_wholesaler = 0
    if result:
        num_wholesaler = len(result)
    
    cursor.execute("SELECT * FROM products")
    result = cursor.fetchall()
    num_products = 0
    if result:
        num_products = len(result)
    
    cursor.execute("SELECT * FROM wholesalerorders")
    result = cursor.fetchall()
    num_worders = 0
    if result:
        num_worders = len(result)
    
    cursor.execute("SELECT * FROM hospitalrorders")
    result = cursor.fetchall()
    num_horders = 0
    if result:
        num_horders = len(result)
    return render_template('dashboard.html', num_hospital=num_hospital, num_manufacture=num_manufacture, num_wholesaler=num_wholesaler, num_products=num_products, num_worders=num_worders, num_horders=num_horders)

@app.route('/manufacturelog', methods=['GET', 'POST'])
def manufacturelog():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        email = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM manufacture WHERE email = '"+email+"' AND password= '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            session['mname'] = result[1]
            return render_template('manufacture.html')
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')
    return render_template('index.html')

@app.route('/manufacturereg', methods=['GET', 'POST'])
def manufacturereg():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cursor.execute("INSERT INTO manufacture VALUES (NULL, '"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')


@app.route('/wholesalerlog', methods=['GET', 'POST'])
def wholesalerlog():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        email = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM wholesaler WHERE email = '"+email+"' AND password= '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            session['wname'] = result[1]
            return redirect(url_for('wholesaler_order'))
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')

@app.route('/wholesalerreg', methods=['GET', 'POST'])
def wholesalerreg():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cursor.execute("INSERT INTO wholesaler VALUES (NULL, '"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/hospitallog', methods=['GET', 'POST'])
def hospitallog():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        email = request.form['name']
        password = request.form['password']

        query = "SELECT * FROM hospital WHERE email = '"+email+"' AND password= '"+password+"'"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            session['hname'] = result[1]
            return redirect(url_for('wproductlist'))
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')

@app.route('/hospitalreg', methods=['GET', 'POST'])
def hospitalreg():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        cursor.execute("INSERT INTO hospital VALUES (NULL, '"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        name = request.form['name']
        quantity = request.form['quantity']
        md = request.form['md']
        ed = request.form['ed']

        mname = session['mname']
        
        print(name, quantity, md, ed)

        cursor.execute("INSERT INTO products VALUES (NULL, '"+mname+"', '"+name+"', '"+quantity+"', '"+md+"', '"+ed+"')")
        connection.commit()

        return render_template('manufacture.html', msg='Successfully added products')
    
    return render_template('manufacture.html')

@app.route('/product_list')
def product_list():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from products")
    result = cursor.fetchall()

    if result:
        return render_template('productlist.html', result=result)
    else:
        return render_template('productlist.html', msg="Products not found")

@app.route('/wholesaler_order')
def wholesaler_order():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from products")
    result = cursor.fetchall()

    if result:
        return render_template('wholesaler.html', result=result)
    else:
        return render_template('wholesaler.html', msg="Products not found")

@app.route('/wholesaler_order_confirm', methods=['GET', 'POST'])
def wholesaler_order_confirm():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database="Inventary",
        password="",
        ) 
        cursor=connection.cursor()

        pid = request.form['pid']
        quantity = request.form['quantity']
        wname = session['wname']

        cursor.execute("INSERT INTO wholesalerorders VALUES (NULL, '"+wname+"', '"+pid+"', '"+quantity+"')")
        connection.commit()

        return redirect(url_for('wholesaler_order'))
    return redirect(url_for('wholesaler_order'))

@app.route('/wholesaler_order_list')
def wholesaler_order_list():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        database="Inventary",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from wholesalerorders")
    result = cursor.fetchall()
 
    if result:
        rows = []
        for row in result:
            d = []
            d.append(row[0])
            d.append(row[1])
            d.append(row[2])
            d.append(row[3])
            cursor.execute("select * from products where id = '"+row[2]+"'")
            result1 = cursor.fetchone()
            d.append(result1[1])
            d.append(result1[2])
            d.append(result1[4])
            d.append(result1[5])
            rows.append(d)
        return render_template('wholesalerorders.html', result=rows)
    else:
        return render_template('wholesalerorders.html', msg="Orders not found")

@app.route('/worders')
def worders():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from wholesalerorders")
    result = cursor.fetchall()
 
    if result:
        rows = []
        for row in result:
            d = []
            d.append(row[0])
            d.append(row[1])
            d.append(row[2])
            d.append(row[3])
            cursor.execute("select * from products where id = '"+row[2]+"'")
            result1 = cursor.fetchone()
            d.append(result1[1])
            d.append(result1[2])
            d.append(result1[4])
            d.append(result1[5])
            rows.append(d)
        return render_template('worderlist.html', result=rows)
    else:
        return render_template('worderlist.html', msg="Orders not found")

@app.route('/wproductlist')
def wproductlist():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from wholesalerorders")
    result = cursor.fetchall()
 
    if result:
        rows = []
        for row in result:
            d = []
            d.append(row[2])
            d.append(row[1])
            cursor.execute("select * from products where id = '"+row[2]+"'")
            result1 = cursor.fetchone()
            d.append(result1[2])
            d.append(row[3])
            d.append(result1[4])
            d.append(result1[5])
            rows.append(d)
        return render_template('hospital.html', result=rows)
    else:
        return render_template('hospital.html', msg="Orders not found")

@app.route('/hospital_order_confirm', methods=['GET', 'POST'])
def hospital_order_confirm():
    if request.method == 'POST':

        connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
        cursor=connection.cursor()

        pid = request.form['pid']
        quantity = request.form['quantity']
        hname = session['hname']

        cursor.execute("INSERT INTO hospitalrorders VALUES (NULL, '"+hname+"', '"+pid+"', '"+quantity+"')")
        connection.commit()

        return redirect(url_for('wproductlist'))
    return redirect(url_for('wproductlist'))


@app.route('/hospital_order_list')
def hospital_order_list():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        database="Inventary",
        user="root",
        password="",
        ) 
    cursor=connection.cursor()

    cursor.execute("select * from hospitalrorders")
    result = cursor.fetchall()
 
    if result:
        rows = []
        for row in result:
            d = []
            d.append(row[0])
            d.append(row[1])
            d.append(row[2])
            d.append(row[3])
            cursor.execute("select * from products where id = '"+row[2]+"'")
            result1 = cursor.fetchone()
            d.append(result1[1])
            d.append(result1[2])
            d.append(result1[4])
            d.append(result1[5])
            rows.append(d)
        return render_template('hospitalorders.html', result=rows)
    else:
        return render_template('hospitalorders.html', msg="Orders not found")

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
