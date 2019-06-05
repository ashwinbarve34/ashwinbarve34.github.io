from flask import Flask, render_template, request, url_for
from profile3 import savings, main, tax, percentage, nmi, hnmi, annual, month, housing, transportation, utilities, entertainment, grocery
from profile3 import fitness, remain, grocery1, transportation1, utilities1, entertainment1, housing1, fitness1, os, left, listed

checkFruits = 0
checkMilk = 0
checkBeverages = 0
checkSweet = 0
checkMeat = 0
checkNuts = 0
checkSpices = 0
checkBasic = 0
checkInternet = 0
checkMaid = 0
checkPhone = 0
checkSports = 0
checkGym = 0
checkRestaurant = 0
checkTrip = 0
checkParty = 0
checkMovies = 0
checkTaxi = 0
checkFiat = 0
checkAudi = 0
checkScooty = 0
checkPass = 0
checkRent = 0
checkMortgage = 0
checkTwo = 0
checkThree = 0
count = 0

app = Flask(__name__)

 
@app.route('/', methods=["GET", "POST"])
def front_page():
    global profession
    global age
    global salary
    global gmi
    if request.method == "POST":
        if request.form["action"] == "START":
            name = request.values.get('name')
            result = main(name)
            profession = result[0];
            salary = result[1];
            gmi = result[2];
            naam = result[3];
            job = result[4];
            age = result[5];
            return '''
                <html>
                    <div style="border:4px green; background-color:green; height:15%; text-align:center;">
                        <ul>
                            <li style="display:inline"><a style="color:white; font-size:20px; padding-right:10%;" href="/">Home</a></li>
                            <li style="display:inline"><a style="color:white; font-size:20px; padding-right:10%;" href="/">News</a></li>
                            <li style="display:inline"><a style="color:white; font-size:20px; padding-right:10%;" href="/">Contact</a></li>
                            <li style="display:inline"><a style="color:white; font-size:20px; padding-right:10%;" href="/tax">About</a></li>
                        </ul>
                    </div>
                    <div style="background-color: white;">
                        <body>
                            <h3 style="text-align:center; font-size:160%; font-family:verdana;">{naam}</h3>
                            <div style="text-align:center;">
                                <img src="https://pixabay.com/get/54e0d7444c53a514f6da8c7dda6d49214b6ac3e45654784c77287dd494/african-2027619_1280.png" alt="Boy" height="200" width="175">
                            </div>
                            <br />
                            <div class="boxed" style="border:3px green; padding:8px; background-color: #228B22; margin-top:3%; margin-left:15%; margin-right:15%; font-size:100%;">
                                <p style="color:white; font-size:20px; text-align:center;">My profession is {profession}</p>
                                <p style="color:white; font-size:20px; text-align:center;">Age: {age}</p>
                                <p style="color:white; font-size:20px; text-align:center;">My salary is Rs. {salary}</p>
                                <p style="color:white; font-size:100%; text-align:center;">My gross monthly income is Rs. {gmi}</p>
                                <h4 style="color:white;">Job Description:</h4>
                                <p style="color:white;">{job}</p>                            
                                <br />
                                <p style="text-align:center; font-family:verdana; font-size:100%; color:white;"> Gross salary looks good! But you cannot avoid the taxes. Click below to calculate your taxes.</p>
                                <div style="text-align:center;">
                                    <a style="color:white; font-size:20px;" href="/tax">Taxes</a>
                                </div>
                            </div>
                        </body>
                    </div>
                </html>
            '''.format(naam=naam, profession=profession, salary=salary, gmi=gmi, job=job, age=age)

    return '''
        <html>
            <div style="border:4px green; background-color:green; height:12%; text-align:center; width:100%; overflow:auto;">
                <ul>
                    <li style="display:inline;"><a style="color:white; font-size:17px; width:25%; padding:12px;" href="/">Home</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:17px; width:25%; padding:12px;" href="/">News</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:17px; width:25%; padding:12px;" href="/">Contact</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:17px; width:25%; padding:12px;" href="/tax">About</a></li>
                </ul>
            </div>
            <body>
                <form method="post" action=".">
                    <center style="color:green;text-align:center;font-size:300%;padding-top:10%;">BUDGET CENTER</center>
                    <br />
                    <center style="color:black;text-align:center;">Please enter your first name</center>
                    <center><input name="name" /></center>
                    <br />
                    <center style="color:green;"><input type="submit" name="action" value="START" /></center>
                </form>
            </body>
        </html>
    '''

@app.route('/tax', methods=["GET", "POST"])
def tax_page():
    result1 = annual()
    result2 = month()
    errors = ""
    if request.method == "POST":
        if request.form["action"] == "Calculate":
            gai = None
            gmi = None
            try:
                gai = float(request.form["gai"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["gai"])
            try:
                gmi = float(request.form["gmi"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["gmi"])
            if gai is not None and gmi is not None:
                result = tax(gai, gmi)
                federal = result[0];
                mt = result[1];
                nmi = result[2];
                return '''
                    <html>
                        <div style="border:4px green; background-color:green; height:15%; text-align:right;">
                            <ul>
                                <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Home</a></li>
                                <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">News</a></li>
                                <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Contact</a></li>
                                <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/tax">About</a></li>
                            </ul>
                        </div>
                        <body>
                            <h1 style="text-align:center; font-size:160%; font-family:verdana;">Net Monthly Income Calculation:</h1>
                            <div class="boxed" style="border:3px green; padding:8px; background-color: #228B22; margin-top:3%; margin-left:25%; margin-right:25%; font-size:100%;">
                                <h4 style="color:white; font-size:20px; text-align:center;">Your federal tax is Rs. {federal}</h4>
                                <h4 style="color:white; font-size:20px; text-align:center;">Your total monthly tax is Rs. {mt}</h4>
                                <h4 style="color:white; font-size:20px; text-align:center;">Your net monthly income is Rs. {nmi}</h4>
                            </div>
                            <br />
                            <div class="boxed" style="border:3px green; padding:8px; background-color: #228B22; margin-top:3%; margin-left:15%; margin-right:15%; font-size:100%;">
                                <p style="color:white; font-size:20px; text-align:center;">Now let's save some money before budgeting our expenses!</p>
                                <div style="text-align:center;">
                                    <a style="color:white; font-size:20px;" href="/savings">Savings</a>
                                </div>
                            </div>
                        </body>
                    </html>
                '''.format(federal=federal, mt=mt, nmi=nmi)
    
    return '''
        <html>
            <div style="border:4px green; background-color:green; height:15%; text-align:right;">
                <ul>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Home</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">News</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Contact</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/tax">About</a></li>
                </ul>
            </div>
            <body>
                <h1 style="text-align:center; font-size:160%; font-family:verdana;">Net Monthly Income Calculation:</h1>
                <h4 style="text-align:center; font-size:120%; font-family:verdana;">Your Gross Annual Income is Rs. {result1}</h4>
                <h4 style="text-align:center; font-size:120%; font-family:verdana;">Your Gross Monthly Income is Rs. {result2}</h4>
                <div class="boxed" style="border:3px green; padding:8px; background-color: #228B22; margin-top:3%; margin-left:25%; margin-right:25%; font-size:100%;">
                    <p style="color:white; font-size:20px; text-align:center;">Enter you gross annual income:
                    <form method="post" action="/tax">
                        <p style="text-align:center;"><input name="gai" /></p>
                        <p style="color:white; font-size:20px; text-align:center;">Enter your gross monthly income:</p>
                        <p style="text-align:center;"><input name="gmi" /></p>
                        {errors}
                        <p style="text-align:center;"><input type="submit" name="action" value="Calculate" /></p>
                    </form>
                </div>
            </body>
        </html>
    '''.format(result1=result1, result2=result2, errors=errors)

@app.route('/savings', methods=["GET", "POST"])
def save_page():
    result2 = hnmi()
    errors = ""
    if request.method == "POST":
        if request.form["action"] == "Next":
            ts = None
            rs = None
            es = None
            os = None
            try:
                ts = float(request.form["ts"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["ts"])
            try:
                rs = float(request.form["rs"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["rs"])
            try:
                es = float(request.form["es"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["es"])
            try:
                os = float(request.form["os"])
            except:
                errors += "<p>{!r} is not a number.</p>\n".format(request.form["os"])
            if ts is not None and rs is not None and es is not None and os is not None:
                result = savings(ts, rs, es, os)
                result1 = nmi()
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="text-align:center; color:white; font-size:100%; font-family:verdana;">{result}</p>
                            <p style="text-align:center; color:white; font-size:100%; font-family:verdana;">Your net monthy income after savings is Rs. {result1}</p>
                            <br />
                            <div style="text-align:center;">
                                <a style="font-size:20px; color:white;" href="/budget">BUDGET</a>
                            </div>
                        </body>
                    </html>
                '''.format(result=result, result1=result1)
    
    return '''
        <html>
            <div style="border:4px green; background-color:green; height:15%; text-align:right;">
                <ul>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Home</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">News</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/">Contact</a></li>
                    <li style="display:inline;"><a style="color:white; font-size:20px; padding-right:20px;" href="/tax">About</a></li>
                </ul>
            </div>
            <body>
                <h1 style="text-align:center; font-size:160%; font-family:verdana;">Total savings plan for this month:</h1>
                <h3 style="text-align:center; font-size:130%; font-family:verdana;">Your net monthly income is Rs. {result2}</h3>
                <p style="text-align:center; font-size:100%; font-family:verdana;">The first budget decision you will make today is paying yourself first.</p>
                <form method="post" action="/savings">
                    <div class="boxed" style="border:3px green; padding:8px; background-color: #228B22; margin-top:3%; margin-left:15%; margin-right:15%; font-size:100%;">
                        <h4 style="color:white; font-size:20px; text-align:center;">Enter the total you will save this month: (15% is recommended)</h4>
                        <p style="color:white; text-align:center;"><input name="ts" /></p>
                        <br />
                        <h4 style="color:white; font-size:20px; text-align:center;">Determine how you will divide the total savings amount into each savings type below:</h4>
                        <p style="color:white; font-size:20px; text-align:center;">(Note: The sum of the amounts in each type should equal the total savings amount)</p>
                        <br />
                        <p style="color:white; font-size:20px; text-align:center;">Retirement Funds:</p>
                        <p style="color:white; text-align:center;"><input name="rs" /></p>
                        <p style="color:white; font-size:20px; text-align:center;">Emergency Funds:</p>
                        <p style="color:white; text-align:center;"><input name="es" /></p>
                        <p style="color:white; font-size:20px; text-align:center;">Other savings:</p>
                        <p style="color:white; text-align:center;"><input name="os" /></p>
                        {errors}
                        <p style="color:white; text-align:center;"><input type="submit" name="action" value="Next" /></p>
                    </div>
                </form>
            </body>
        </html>
    '''.format(result2=result2, errors=errors)

@app.route('/budget', methods=["GET", "POST"])
def budget_page():
    global count
    if count == 0:
        return '''
            <html>
                <head>
                    <title>BUDGET</title>
                </head>
                <frameset cols = "200, *">
                    <frame src = "/category_page.html" name = "category_page" />
                    <frame src = "/main_page.html" name = "main_page" />
                </frameset>

            </html>
        '''
    else:
        return '''
        <html>
            <head>
                <title>REPORT CARD</title>
            </head>
            <frameset rows = "30%, *">
                <frameset cols = "50%, 50%">
                    <frame src= "/profile_final" name = "pro_page" />
                    <frame src= "/salary_final" name = "sal_page" />
                </frameset>
                <frameset cols = "200, 200, 200, 200, 200, *">
                    <frame src = "/grocery_final" name = "gro_page" />
                    <frame src = "/entertainment_final" name = "ent_page" />
                    <frame src = "/transportation_final" name = "tra_page" />
                    <frame src = "/housing_final" name = "hou_page" />
                    <frame src = "/fitness_final" name = "fit_page" />
                    <frame src = "/utilities_final" name = "uti_page" />
                </frameset>
            </frameset>
        </html>
    '''

@app.route('/category_page.html', methods=["GET", "POST"])
def category_page():
    return '''
        <html>
            <body bgcolor = "white">
                <a style="font-size:20px;" href = "/grocery" target = "main_page">Grocery</a>
                <br />
                <br />
      
                <a style="font-size:20px;" href = "/entertainment" target = "main_page">Entertainment</a>
                <br />
                <br />
      
                <a style="font-size:20px;" href = "/utilities" target = "main_page">Utilities</a>
                <br />
                <br />

                <a style="font-size:20px;" href = "/fitness" target = "main_page">Fitness</a>
                <br />
                <br />

                <a style="font-size:20px;" href = "/housing" target = "main_page">Housing</a>
                <br />
                <br />

                <a style="font-size:20px;" href = "/transportation" target = "main_page">Transportation</a>
            </body>
	</html>
    '''

@app.route('/main_page1.html', methods=["GET", "POST"])
def main_page1():
    result = left()
    global count
    count = count + 1;
    return '''
        <html>
            <body bgcolor = "#228B22">
                <h3 style="color:white;font-size:25px;">Congratulations! Please click the link below to see your financial report card!</h3>
                <p style="color:white;font-size:20px;">Your total amount in savings is Rs. {result}</p>
                <a style="color:white; font-size:20px;" href="/budget", target="_top">Report Card</a>
            </body>
        </html>
    '''.format(result=result)

@app.route('/main_page.html', methods=["GET", "POST"])
def main_page():
    result = remain()
    global count
    if request.method == "POST":
        if request.form["action"] == "FINISH":
            if result == "Congratulations!":
                count = count + 1;
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <h3 style="color:white;font-size:25px;">Congratulations! Please click the link below to see your financial report card!</h3>
                            <a style="color:white; font-size:20px;" href="/budget" target="_top">Report Card</a>
                        </body>
                    </html>
                '''
            elif result < 0:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <h3 style="color:white;font-size:25px;">Sorry. You have exceeded the amount left to allocate. Please re-allocate to proceed.</h3>
                            <br />
                            <p style="color:white; font-size:20px;">Amount left to allocate is Rs. {result}</p>
                            <br />
                            <form method="post" action="/main_page.html">
                                <input type="submit" name="action" value="BACK" />
                            </form>
                        </body>
                    </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <h3 style="color:white;font-size:25px;">You still have some amount left to allocate.</h3>
                            <br />
                            <p style="color:white; font-size:20px;">Amount left to allocate is Rs. {result}</p>
                            <br />
                            <p style="color:white; font-size:20px;">Would you like to allocate the remaining amount to your total savings or would you like to re-allocate the remaining amount to different categories?</p>
                            <br />
                            <form method="post" action="/main_page1.html">
                                <input type="submit" name="action" value="ADD TO SAVINGS" />
                            </form>
                            <br />
                            <form method="post" action="/main_page.html">
                                <input type="submit" name="action" value="RE-ALLOCATE" />
                            </form>
                        </body>
                    </html>
                '''.format(result=result)
    return '''
        <html>
            <body bgcolor = "#228B22">
                <h3 style="color:white;font-size:25px;">Click on each expense category from the column on the left.</h3>
                <p style="color:white;font-size:20px;">For each category you will need to first answer a question related to each category before proceeding to shop.</p>
                <p style="color:white;font-size:20px;">Amount left to allocate is Rs. {result}</p>
                <br />
                <br />
                <p style="color:white;font-size:20px;">Once you are done shopping, please click the FINISH button below</p>
                <form method="post" action="/main_page.html">
                    <input type="submit" name="action" value="FINISH" />
                </form>
            </body>
	</html>
    '''.format(result=result)

#-----------------------------------------ENTERTAINMENT---------------------------ENTERTAINMENT---------------------------------------|

@app.route('/entertainment', methods=["GET", "POST"])
def entertainment_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            ent = request.values.get('ent')
            result = entertainment(ent)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/entertainment">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/entertainment1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">ENTERTAINMENT</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">Everyone likes to spend money on activities that bring entertainment like watching movies, dining at restaurants, etc.</p>
                <p style="color:white; font-size:25px;">If not spent wisely, this category can easily disrupt one's monthly budget. A few activities like vacation trips, shopping expensive items require proper planning.<br>
                A proper monthly budget helps to save enough money to enjoy these activities. As an exercise, try to spend on this category at the last today!</p>
                <p style="color:white; font-size:20px;">How many activities are mentioned above that require proper planning?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/entertainment">
                    <p><input name="ent" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/entertainment1', methods=["GET", "POST"])
def entertainment1_page():
    result = remain()
    global checkRestaurant
    global checkMovies
    global checkTrip
    global checkParty
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'restaurant' in option:
            checkRestaurant = 1
        else:
            checkRestaurant = 0
        if 'movies' in option:
            checkMovies = 1
        else:
            checkMovies = 0
        if 'trip' in option:
            checkTrip = 1
        else:
            checkTrip = 0
        if 'party' in option:
            checkParty = 1
        else:
            checkParty = 0
        
        result1 = entertainment1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">ENTERTAINMENT</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/50e0d6434d54b108feda8460825668204022dfe056587748742d78dc/theatre-603076_1920.jpg" alt="Entertainment" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/entertainment1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="restaurant_div">{checkRestaurant}
                        </div>
                        <br />
                        <div id="movies_div">{checkMovies}
                        </div>
                        <br />
                        <div id="trip_div">{checkTrip}
                        </div>
                        <br />
                        <div id="party_div">{checkParty}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <script>
                        if ('{checkRestaurant}' == 1)
                            document.getElementById("restaurant_div").innerHTML = '<input type="checkbox" name="item" value="restaurant" checked/> Restaurant Rs.3000';
                        else
                            document.getElementById("restaurant_div").innerHTML = '<input type="checkbox" name="item" value="restaurant" /> Restaurant Rs.3000';
                    </script>
                    <script>
                        if ('{checkMovies}' == 1)
                            document.getElementById("movies_div").innerHTML = '<input type="checkbox" name="item" value="movies" checked/> Movies Rs.2000';
                        else
                            document.getElementById("movies_div").innerHTML = '<input type="checkbox" name="item" value="movies" /> Movies Rs.2000';
                    </script>
                    <script>
                        if ('{checkTrip}' == 1)
                            document.getElementById("trip_div").innerHTML = '<input type="checkbox" name="item" value="trip" checked/> Trip to Mahabaleshwar Rs.4000';
                        else
                            document.getElementById("trip_div").innerHTML = '<input type="checkbox" name="item" value="trip" /> Trip to Mahabaleshwar Rs.4000';
                    </script>
                    <script>
                        if ('{checkParty}' == 1)
                            document.getElementById("party_div").innerHTML = '<input type="checkbox" name="item" value="party" checked/> Weekend Party Rs.3500';
                        else
                            document.getElementById("party_div").innerHTML = '<input type="checkbox" name="item" value="party" /> Weekend Party Rs.3500';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkRestaurant=checkRestaurant, checkMovies=checkMovies, checkTrip=checkTrip, checkParty=checkParty)

#--------------------------------------------------GROCERY------------------------------GROCERY---------------------------------|

@app.route('/grocery', methods=["GET", "POST"])
def grocery_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            gro = request.values.get('gro')
            result = grocery(gro)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/grocery">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/grocery1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">GROCERY</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">The monthly cost of this category depends on two factors. Firstly, your family size and secondly, the number of times you cook food at home.</p>
                <p style="color:white; font-size:25px;">The grocery expense increases as the number of family members increases. The cost will reduce if you don't cook at home much.<br>
                However, this comes at a cost of increased expense of eating at restaurants. Cooking food at home is always a cheaper and healthier option than eating outside.<br>
                Some people subscribe to tiffin service to enjoy home cooked food at affordable price.</p>
                <p style="color:white; font-size:20px;">The cost of Grocery depends on how many factors?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/grocery">
                    <p><input name="gro" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/grocery1', methods=["GET", "POST"])
def grocery1_page():
    result = remain()
    global checkFruits
    global checkMilk
    global checkBeverages
    global checkSweet
    global checkMeat
    global checkNuts
    global checkSpices
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'milk' in option:
            checkMilk = 1
        else:
            checkMilk = 0
        if 'fruits' in option:
            checkFruits = 1
        else:
            checkFruits = 0
        if 'tea' in option:
            checkBeverages = 1
        else:
            checkBeverages = 0
        if 'sweet' in option:
            checkSweet = 1
        else:
            checkSweet = 0
        if 'meat' in option:
            checkMeat = 1
        else:
            checkMeat = 0
        if 'nuts' in option:
            checkNuts = 1
        else:
            checkNuts = 0
        if 'spices' in option:
            checkSpices = 1
        else:
            checkSpices = 0
        
        result1 = grocery1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">GROCERY</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/57e2d64b4857ae14f6d1867dda6d49214b6ac3e45654784c762f79d496/vegetables-1238252_1920.jpg" alt="Grocery" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/grocery1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="milk_div">{checkMilk}
                        </div>
                        <br />
                        <div id="fruits_div">{checkFruits}
                        </div>
                        <br />
                        <div id="tea_div">{checkBeverages}
                        </div>
                        <br />
                        <div id="sweet_div">{checkSweet}
                        </div>
                        <br />
                        <div id="meat_div">{checkMeat}
                        </div>
                        <br />
                        <div id="nuts_div">{checkNuts}
                        </div>
                        <br />
                        <div id="spices_div">{checkSpices}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <script>
                        if ('{checkMilk}' == 1)
                            document.getElementById("milk_div").innerHTML = '<input type="checkbox" name="item" value="milk" checked/> Milk and Dairy - Rs.120';
                        else
                            document.getElementById("milk_div").innerHTML = '<input type="checkbox" name="item" value="milk" /> Milk and Dairy - Rs.120';
                    </script>
                    <script>
                        if ('{checkFruits}' == 1)
                            document.getElementById("fruits_div").innerHTML = '<input type="checkbox" name="item" value="fruits" checked/> Fruits and Vegetables - Rs.100';
                        else
                            document.getElementById("fruits_div").innerHTML = '<input type="checkbox" name="item" value="fruits" /> Fruits and Vegetables - Rs.100';
                    </script>
                    <script>
                        if ('{checkBeverages}' == 1)
                            document.getElementById("tea_div").innerHTML = '<input type="checkbox" name="item" value="tea" checked/> Tea Coffe and Drinks - Rs.120';
                        else
                            document.getElementById("tea_div").innerHTML = '<input type="checkbox" name="item" value="tea" /> Tea Coffee and Drinks - Rs.120';
                    </script>
                    <script>
                        if ('{checkSweet}' == 1)
                            document.getElementById("sweet_div").innerHTML = '<input type="checkbox" name="item" value="sweet" checked/> Baking and Sweets - Rs.120';
                        else
                            document.getElementById("sweet_div").innerHTML = '<input type="checkbox" name="item" value="sweet" /> Baking and Sweets - Rs.120';
                    </script>
                    <script>
                        if ('{checkMeat}' == 1)
                            document.getElementById("meat_div").innerHTML = '<input type="checkbox" name="item" value="meat" checked/> Fish and Meat - Rs.120';
                        else
                            document.getElementById("meat_div").innerHTML = '<input type="checkbox" name="item" value="meat" /> Fish and Meat - Rs.120';
                    </script>
                    <script>
                        if ('{checkNuts}' == 1)
                            document.getElementById("nuts_div").innerHTML = '<input type="checkbox" name="item" value="nuts" checked/> Nuts and Dried Fruits - Rs.120';
                        else
                            document.getElementById("nuts_div").innerHTML = '<input type="checkbox" name="item" value="nuts" /> Nuts and Dried Fruits - Rs.120';
                    </script>
                    <script>
                        if ('{checkSpices}' == 1)
                            document.getElementById("spices_div").innerHTML = '<input type="checkbox" name="item" value="spices" checked/> Spices and Seasonings - Rs.120';
                        else
                            document.getElementById("spices_div").innerHTML = '<input type="checkbox" name="item" value="spices" /> Spices and Seasonings - Rs.120';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkMilk=checkMilk, checkFruits=checkFruits, checkBeverages=checkBeverages, checkSweet=checkSweet, checkMeat=checkMeat, checkNuts=checkNuts, checkSpices=checkSpices)
                    

#-----------------------------------UTILITIES--------------------------------------UTILITIES-------------------------------|

@app.route('/utilities', methods=["GET", "POST"])
def utilities_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            ele = request.values.get('ele')
            result = utilities(ele)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/utilities">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/utilities1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">UTILITIES</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">Utilities is the most common forgotten expense while budgeting. However, one just cannot run away from this bill.</p>
                <p style="color:white; font-size:25px;">The basic utilities people have to pay for are gas, water, sewer, and electricity. The amount usually differs as per the usage of the utility.<br>
                The size of the house also decides the monthly bill for these utilities. Additional utilities include phone, internet and cable services.<br>
                People can live without these services. However, in today's world, they are becoming part of the basic utilities.
                <br />
                <p style="color:white; font-size:20px;">How many basic utilities do people have to pay for?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/utilities">
                    <p><input name="ele" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/utilities1', methods=["GET", "POST"])
def utilities1_page():
    result = remain()
    global checkBasic
    global checkPhone
    global checkInternet
    global checkMaid
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'basic' in option:
            checkBasic = 1
        else:
            checkBasic = 0
        if 'phone' in option:
            checkPhone = 1
        else:
            checkPhone = 0
        if 'internet' in option:
            checkInternet = 1
        else:
            checkInternet = 0
        if 'maid' in option:
            checkMaid = 1
        else:
            checkMaid = 0
        
        result1 = utilities1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">UTILITIES</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/55e1d044495ba914f6d1867dda6d49214b6ac3e45654784f742e7bdc93/beverage-3157395_1920.jpg" alt="Utility" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/utilities1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="basic_div">{checkBasic}
                        </div>
                        <br />
                        <div id="phone_div">{checkPhone}
                        </div>
                        <br />
                        <div id="internet_div">{checkInternet}
                        </div>
                        <br />
                        <div id="maid_div">{checkMaid}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <br />
                    <p>*Basic Utilities include electricity, water, garbage, heating, cooling</p>
                    <script>
                        if ('{checkBasic}' == 1)
                            document.getElementById("basic_div").innerHTML = '<input type="checkbox" name="item" value="basic" checked/> *Basic Rs.1200';
                        else
                            document.getElementById("basic_div").innerHTML = '<input type="checkbox" name="item" value="basic" checked/> *Basic Rs.1200';
                    </script>
                    <script>
                        if ('{checkPhone}' == 1)
                            document.getElementById("phone_div").innerHTML = '<input type="checkbox" name="item" value="phone" checked/> Phone Rs.600';
                        else
                            document.getElementById("phone_div").innerHTML = '<input type="checkbox" name="item" value="phone" /> Phone Rs.600';
                    </script>
                    <script>
                        if ('{checkInternet}' == 1)
                            document.getElementById("internet_div").innerHTML = '<input type="checkbox" name="item" value="internet" checked/> Internet Rs.2500';
                        else
                            document.getElementById("internet_div").innerHTML = '<input type="checkbox" name="item" value="internet" /> Internet Rs.2500';
                    </script>
                    <script>
                        if ('{checkMaid}' == 1)
                            document.getElementById("maid_div").innerHTML = '<input type="checkbox" name="item" value="maid" checked/> Housemaid Rs.2000';
                        else
                            document.getElementById("maid_div").innerHTML = '<input type="checkbox" name="item" value="maid" /> Housemaid Rs.2000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkBasic=checkBasic, checkPhone=checkPhone, checkInternet=checkInternet, checkMaid=checkMaid)

#-------------------------------------------HOUSING----------------------------HOUSING------------------------------------|

@app.route('/housing', methods=["GET", "POST"])
def housing_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            hou = request.values.get('hou')
            result = housing(hou)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/housing">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/housing1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">HOUSING</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">Everyone lives in a house which they have either bought or rented out.</p>
                <p style="color:white; font-size:25px;">Renting a house is less stressful and an easy option. It is the best option for risk averse individuals.<br>
                The price of a house usually appreciates overtime thereby providing the owner of the house a good return on investment.<br>
                However, the price can depreciate as well making it a risky investment for some.</p>
                <br />
                <p style="color:white; font-size:20px;">How many housing options are mentioned above?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/housing">
                    <p><input name="hou" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/housing1', methods=["GET", "POST"])
def housing1_page():
    result = remain()
    global checkRent
    global checkMortgage
    global checkTwo
    global checkThree
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'rent' in option:
            checkRent = 1
        else:
            checkRent = 0
        if 'mortgage' in option:
            checkMortgage = 1
        else:
            checkMortgage = 0
        if 'two' in option:
            checkTwo = 1
        else:
            checkTwo = 0
        if 'three' in option:
            checkThree = 1
        else:
            checkThree = 0
        
        result1 = housing1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">HOUSING</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/57e3d040495aa514f6d1867dda6d49214b6ac3e45654784f742f73dd96/house-1353389_1920.jpg" alt="House" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/housing1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="rent_div">{checkRent}
                        </div>
                        <br />
                        <div id="mortgage_div">{checkMortgage}
                        </div>
                        <br />
                        <div id="two_div">{checkTwo}
                        </div>
                        <br />
                        <div id="three_div">{checkThree}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <script>
                        if ('{checkRent}' == 1)
                            document.getElementById("rent_div").innerHTML = '<input type="checkbox" name="item" value="rent" checked/> Rent (1BHK in Bavdhan) Rs.11000';
                        else
                            document.getElementById("rent_div").innerHTML = '<input type="checkbox" name="item" value="rent" /> Rent (1BHK in Bavdhan) Rs.11000';
                    </script>
                    <script>
                        if ('{checkMortgage}' == 1)
                            document.getElementById("mortgage_div").innerHTML = '<input type="checkbox" name="item" value="mortgage" checked/> EMI (1BHK in Aundh) Rs.20000';
                        else
                            document.getElementById("mortgage_div").innerHTML = '<input type="checkbox" name="item" value="mortgage" /> EMI (1BHK in Aundh) Rs.20000';
                    </script>
                    <script>
                        if ('{checkTwo}' == 1)
                            document.getElementById("two_div").innerHTML = '<input type="checkbox" name="item" value="two" checked/> EMI (2BHK in Kothrud) Rs.35000';
                        else
                            document.getElementById("two_div").innerHTML = '<input type="checkbox" name="item" value="two" /> EMI (2BHK in Kothrud) Rs.35000';
                    </script>
                    <script>
                        if ('{checkThree}' == 1)
                            document.getElementById("three_div").innerHTML = '<input type="checkbox" name="item" value="three" checked/> EMI (3BHK in Karvenagar) Rs.50000';
                        else
                            document.getElementById("three_div").innerHTML = '<input type="checkbox" name="item" value="three" /> EMI (3BHK in Karvenagar) Rs.50000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkRent=checkRent, checkMortgage=checkMortgage, checkTwo=checkTwo, checkThree=checkThree)

#---------------------------------------FITNESS-------------------------------FITNESS----------------------------------------|

@app.route('/fitness', methods=["GET", "POST"])
def fitness_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            pho = request.values.get('pho')
            result = fitness(pho)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/fitness">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/fitness1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">FITNESS</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">Exercise is an important part of our daily routine. A fit body helps us to improve our concentration levels and productivity in our daily work.</p>
                <p style="color:white; font-size:25px;">There are different mediums available in India for people to keep themselves fit. Some people go to fitness centers (Gyms) while some prefer to play sports.<br>
                There are two popular ways of payment for gym memberships in India. First way is to pay a monthly or annual membership. Second way is to pay on a per-use basis.<br>
                Annual membership option is usually cheaper over a period of 12 years. However, the pay-per-use option guarantees maximum utilization of the service.</p>
                <br />
                <p style="color:white; font-size:20px;">How many methods of payment are mentioned above?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/fitness">
                    <p><input name="pho" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/fitness1', methods=["GET", "POST"])
def fitness1_page():
    result = remain()
    global checkGym
    global checkSports
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'sports' in option:
            checkSports = 1
        else:
            checkSports = 0
        if 'gym' in option:
            checkGym = 1
        else:
            checkGym = 0
        
        result1 = fitness1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">FITNESS</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/54e4d3464e55a414f6d1867dda6d49214b6ac3e45654784f742f7dd09f/dumbbells-2465478_1920.jpg" alt="Fitness" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/fitness1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="sports_div">{checkSports}
                        </div>
                        <br />
                        <div id="gym_div">{checkGym}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <script>
                        if ('{checkSports}' == 1)
                            document.getElementById("sports_div").innerHTML = '<input type="checkbox" name="item" value="sports" checked/> Sports Rs.700';
                        else
                            document.getElementById("sports_div").innerHTML = '<input type="checkbox" name="item" value="sports" /> Sports Rs.700';
                    </script>
                    <script>
                        if ('{checkGym}' == 1)
                            document.getElementById("gym_div").innerHTML = '<input type="checkbox" name="item" value="gym" checked/> Gym Rs.1400';
                        else
                            document.getElementById("gym_div").innerHTML = '<input type="checkbox" name="item" value="gym" /> Gym Rs.1400';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkSports=checkSports, checkGym=checkGym)


#----------------------------------------TRANSPORT-----------------------------------TRANSPORT------------------------------------|

@app.route('/transportation', methods=["GET", "POST"])
def transportation_page():
    if request.method == "POST":
        if request.form["action"] == "Next":
            tra = request.values.get('tra')
            result = transportation(tra)
            wrong = "Sorry. Your answer is wrong. Please try again."
            if result == wrong:
                return '''
                <html>
                    <body bgcolor = "#228B22">
                        <p style="color:white; font-size:20px;">{result}</p>
                        <a style="color:white; font-size:20px;" href="/transportation">BACK</a>
                    </body>
                </html>
                '''.format(result=result)
            else:
                return '''
                    <html>
                        <body bgcolor = "#228B22">
                            <p style="color:white; font-size:20px;">{result}</p>
                            <a style="color:white; font-size:20px;" href="/transportation1">CONTINUE</a>
                        </body>
                    </html>
                '''.format(result=result)

    return '''
        <html>
            <body bgcolor = "#228B22">
                <p style="color:white; font-size:40px;">TRANSPORTATION</p>
                <p style="color:white; font-size:20px;">(Please read the passage below and answer the question that follows to proceed)</p>
                <p style="color:white; font-size:25px;">In most parts of India, people either own a private car or two-wheeler, use public transport or travel by rickshaw or taxi.</p>
                <p style="color:white; font-size:25px;">Owning a private vehicle is the most convenient option. Howvwer, they increase the traffic on roads. Recently, Ola and Uber cab services have made urban transportation somewhat better.<br>
                Public transportation helps to reduce private vehicles on roads thereby reducing traffic and air pollution. Petrol and maintenance costs are additional expenses of owning a car</p>
                <br />
                <p style="color:white; font-size:20px;">In how many ways do people travel in most parts of India?</p>
                <p style="color:white; font-size:20px;">Enter your answer:
                <form method="post" action="/transportation">
                    <p><input name="tra" /></p>
                    <p><input type="submit" name="action" value="Next" /></p>
                </form>
            </body>
        </html>
    '''

@app.route('/transportation1', methods=["GET", "POST"])
def transportation1_page():
    result = remain()
    global checkTaxi
    global checkPass
    global checkFiat
    global checkAudi
    global checkScooty
    if request.method == "POST":
        option = (request.form.getlist('item'))
        if 'taxi' in option:
            checkTaxi = 1
        else:
            checkTaxi = 0
        if 'pass' in option:
            checkPass = 1
        else:
            checkPass = 0
        if 'fiat' in option:
            checkFiat = 1
        else:
            checkFiat = 0
        if 'audi' in option:
            checkAudi = 1
        else:
            checkAudi = 0
        if 'scooty' in option:
            checkScooty = 1
        else:
            checkScooty = 0
        
        result1 = transportation1(option)

        return '''
            <html>
                <body bgcolor = "#228B22">
                    <p style="color:white; font-size:20px;">{result1}</p>
                    <a style="color:white; font-size:20px;" href="/main_page.html">CONTINUE</a>
                </body>
            </html>
        '''.format(result1=result1)
    
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:25px;">TRANSPORTATION</p>
                    <marquee behavior="slide" direction="left" style="font-size:20px;">Amount left to allocate is Rs. {result}</marquee>
                    <br />
                    <img src="https://pixabay.com/get/50e7d440435bb108feda8460825668204022dfe056587748752c7dd6/traffic-671399_1920.jpg" alt="Transport" height="400" width="360" style="float: left; margin-right: 15px; margin-bottom:5px;" />
                    <form action="/transportation1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <br />
                        <br />
                        <div id="taxi_div">{checkTaxi}
                        </div>
                        <br />
                        <div id="pass_div">{checkPass}
                        </div>
                        <br />
                        <div id="fiat_div">{checkFiat}
                        </div>
                        <br />
                        <div id="audi_div">{checkAudi}
                        </div>
                        <br />
                        <div id="scooty_div">{checkScooty}
                        </div>
                        <br />
                        <input type="submit">
                    </form>
                    <script>
                        if ('{checkTaxi}' == 1)
                            document.getElementById("taxi_div").innerHTML = '<input type="checkbox" name="item" value="taxi" checked/> Taxi (Rickshaw/Uber/Ola) Rs.1700';
                        else
                            document.getElementById("taxi_div").innerHTML = '<input type="checkbox" name="item" value="taxi" /> Taxi (Rickshaw/Uber/Ola) Rs.1700';
                    </script>
                    <script>
                        if ('{checkPass}' == 1)
                            document.getElementById("pass_div").innerHTML = '<input type="checkbox" name="item" value="pass" checked/> Monthly Pass (bus/train) Rs.1400';
                        else
                            document.getElementById("pass_div").innerHTML = '<input type="checkbox" name="item" value="pass" /> Pass (bus/train) Rs.1400';
                    </script>
                    <script>
                        if ('{checkFiat}' == 1)
                            document.getElementById("fiat_div").innerHTML = '<input type="checkbox" name="item" value="fiat" checked/> EMI (for economy car) Rs.20000';
                        else
                            document.getElementById("fiat_div").innerHTML = '<input type="checkbox" name="item" value="fiat" /> EMI (for economy car) Rs.20000';
                    </script>
                    <script>
                        if ('{checkAudi}' == 1)
                            document.getElementById("audi_div").innerHTML = '<input type="checkbox" name="item" value="audi" checked/> EMI (for luxury car) Rs.40000';
                        else
                            document.getElementById("audi_div").innerHTML = '<input type="checkbox" name="item" value="audi" /> EMI (for luxury car) Rs.40000';
                    </script>
                    <script>
                        if ('{checkScooty}' == 1)
                            document.getElementById("scooty_div").innerHTML = '<input type="checkbox" name="item" value="scooty" checked/> EMI (for two-wheeler) Rs.10000';
                        else
                            document.getElementById("scooty_div").innerHTML = '<input type="checkbox" name="item" value="scooty" /> EMI (for two-wheeler) Rs.10000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(result=result, checkTaxi=checkTaxi, checkPass=checkPass, checkFiat=checkFiat, checkAudi=checkAudi, checkScooty=checkScooty)

#------------------------------------FINAL------------------------------------------FINAL----------------------------------------------|

@app.route('/grocery_final', methods=["GET", "POST"])
def gro_page():
    global checkFruits
    global checkMilk
    global checkBeverages
    global checkSweet
    global checkMeat
    global checkNuts
    global checkSpices
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">GROCERY</p>
                    <form action="/grocery1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="milk_div">{checkMilk}
                        </div>
                        <br />
                        <div id="fruits_div">{checkFruits}
                        </div>
                        <br />
                        <div id="tea_div">{checkBeverages}
                        </div>
                        <br />
                        <div id="sweet_div">{checkSweet}
                        </div>
                        <br />
                        <div id="meat_div">{checkMeat}
                        </div>
                        <br />
                        <div id="nuts_div">{checkNuts}
                        </div>
                        <br />
                        <div id="spices_div">{checkSpices}
                        </div>
                    </form>
                    <script>
                        if ('{checkMilk}' == 1)
                            document.getElementById("milk_div").innerHTML = '<input type="checkbox" name="item" value="milk" checked/> Milk and Dairy - Rs.120';
                        else
                            document.getElementById("milk_div").innerHTML = '<input type="checkbox" name="item" value="milk" /> Milk and Dairy - Rs.120';
                    </script>
                    <script>
                        if ('{checkFruits}' == 1)
                            document.getElementById("fruits_div").innerHTML = '<input type="checkbox" name="item" value="fruits" checked/> Fruits and Vegetables - Rs.100';
                        else
                            document.getElementById("fruits_div").innerHTML = '<input type="checkbox" name="item" value="fruits" /> Fruits and Vegetables - Rs.100';
                    </script>
                    <script>
                        if ('{checkBeverages}' == 1)
                            document.getElementById("tea_div").innerHTML = '<input type="checkbox" name="item" value="tea" checked/> Tea Coffe and Drinks - Rs.120';
                        else
                            document.getElementById("tea_div").innerHTML = '<input type="checkbox" name="item" value="tea" /> Tea Coffee and Drinks - Rs.120';
                    </script>
                    <script>
                        if ('{checkSweet}' == 1)
                            document.getElementById("sweet_div").innerHTML = '<input type="checkbox" name="item" value="sweet" checked/> Baking and Sweets - Rs.120';
                        else
                            document.getElementById("sweet_div").innerHTML = '<input type="checkbox" name="item" value="sweet" /> Baking and Sweets - Rs.120';
                    </script>
                    <script>
                        if ('{checkMeat}' == 1)
                            document.getElementById("meat_div").innerHTML = '<input type="checkbox" name="item" value="meat" checked/> Fish and Meat - Rs.120';
                        else
                            document.getElementById("meat_div").innerHTML = '<input type="checkbox" name="item" value="meat" /> Fish and Meat - Rs.120';
                    </script>
                    <script>
                        if ('{checkNuts}' == 1)
                            document.getElementById("nuts_div").innerHTML = '<input type="checkbox" name="item" value="nuts" checked/> Nuts and Dried Fruits - Rs.120';
                        else
                            document.getElementById("nuts_div").innerHTML = '<input type="checkbox" name="item" value="nuts" /> Nuts and Dried Fruits - Rs.120';
                    </script>
                    <script>
                        if ('{checkSpices}' == 1)
                            document.getElementById("spices_div").innerHTML = '<input type="checkbox" name="item" value="spices" checked/> Spices and Seasonings - Rs.120';
                        else
                            document.getElementById("spices_div").innerHTML = '<input type="checkbox" name="item" value="spices" /> Spices and Seasonings - Rs.120';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkMilk=checkMilk, checkFruits=checkFruits, checkBeverages=checkBeverages, checkSweet=checkSweet, checkMeat=checkMeat, checkNuts=checkNuts, checkSpices=checkSpices)

@app.route('/entertainment_final', methods=["GET", "POST"])
def ent_page():
    global checkRestaurant
    global checkMovies
    global checkTrip
    global checkParty
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">ENTERTAINMENT</p>
                    <form action="/entertainment1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="restaurant_div">{checkRestaurant}
                        </div>
                        <br />
                        <div id="movies_div">{checkMovies}
                        </div>
                        <br />
                        <div id="trip_div">{checkTrip}
                        </div>
                        <br />
                        <div id="party_div">{checkParty}
                        </div>
                    </form>
                    <script>
                        if ('{checkRestaurant}' == 1)
                            document.getElementById("restaurant_div").innerHTML = '<input type="checkbox" name="item" value="restaurant" checked/> Restaurant Rs.3000';
                        else
                            document.getElementById("restaurant_div").innerHTML = '<input type="checkbox" name="item" value="restaurant" /> Restaurant Rs.3000';
                    </script>
                    <script>
                        if ('{checkMovies}' == 1)
                            document.getElementById("movies_div").innerHTML = '<input type="checkbox" name="item" value="movies" checked/> Movies Rs.2000';
                        else
                            document.getElementById("movies_div").innerHTML = '<input type="checkbox" name="item" value="movies" /> Movies Rs.2000';
                    </script>
                    <script>
                        if ('{checkTrip}' == 1)
                            document.getElementById("trip_div").innerHTML = '<input type="checkbox" name="item" value="trip" checked/> Trip to Mahabaleshwar Rs.4000';
                        else
                            document.getElementById("trip_div").innerHTML = '<input type="checkbox" name="item" value="trip" /> Trip to Mahabaleshwar Rs.4000';
                    </script>
                    <script>
                        if ('{checkParty}' == 1)
                            document.getElementById("party_div").innerHTML = '<input type="checkbox" name="item" value="party" checked/> Weekend Party Rs.3500';
                        else
                            document.getElementById("party_div").innerHTML = '<input type="checkbox" name="item" value="party" /> Weekend Party Rs.3500';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkRestaurant=checkRestaurant, checkMovies=checkMovies, checkTrip=checkTrip, checkParty=checkParty)

@app.route('/transportation_final', methods=["GET", "POST"])
def tra_page():
    global checkTaxi
    global checkPass
    global checkFiat
    global checkAudi
    global checkScooty
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">TRANSPORTATION</p>
                    <form action="/transportation1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="taxi_div">{checkTaxi}
                        </div>
                        <br />
                        <div id="pass_div">{checkPass}
                        </div>
                        <br />
                        <div id="fiat_div">{checkFiat}
                        </div>
                        <br />
                        <div id="audi_div">{checkAudi}
                        </div>
                        <br />
                        <div id="scooty_div">{checkScooty}
                        </div>
                    </form>
                    <script>
                        if ('{checkTaxi}' == 1)
                            document.getElementById("taxi_div").innerHTML = '<input type="checkbox" name="item" value="taxi" checked/> Taxi (Rickshaw/Uber/Ola) Rs.1700';
                        else
                            document.getElementById("taxi_div").innerHTML = '<input type="checkbox" name="item" value="taxi" /> Taxi (Rickshaw/Uber/Ola) Rs.1700';
                    </script>
                    <script>
                        if ('{checkPass}' == 1)
                            document.getElementById("pass_div").innerHTML = '<input type="checkbox" name="item" value="pass" checked/> Monthly Pass (bus/train) Rs.1400';
                        else
                            document.getElementById("pass_div").innerHTML = '<input type="checkbox" name="item" value="pass" /> Pass (bus/train) Rs.1400';
                    </script>
                    <script>
                        if ('{checkFiat}' == 1)
                            document.getElementById("fiat_div").innerHTML = '<input type="checkbox" name="item" value="fiat" checked/> EMI (for economy car) Rs.20000';
                        else
                            document.getElementById("fiat_div").innerHTML = '<input type="checkbox" name="item" value="fiat" /> EMI (for economy car) Rs.20000';
                    </script>
                    <script>
                        if ('{checkAudi}' == 1)
                            document.getElementById("audi_div").innerHTML = '<input type="checkbox" name="item" value="audi" checked/> EMI (for luxury car) Rs.40000';
                        else
                            document.getElementById("audi_div").innerHTML = '<input type="checkbox" name="item" value="audi" /> EMI (for luxury car) Rs.40000';
                    </script>
                    <script>
                        if ('{checkScooty}' == 1)
                            document.getElementById("scooty_div").innerHTML = '<input type="checkbox" name="item" value="scooty" checked/> EMI (for two-wheeler) Rs.10000';
                        else
                            document.getElementById("scooty_div").innerHTML = '<input type="checkbox" name="item" value="scooty" /> EMI (for two-wheeler) Rs.10000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkTaxi=checkTaxi, checkPass=checkPass, checkFiat=checkFiat, checkAudi=checkAudi, checkScooty=checkScooty)

@app.route('/housing_final', methods=["GET", "POST"])
def hou_page():
    global checkRent
    global checkMortgage
    global checkTwo
    global checkThree
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">HOUSING</p>
                    <form action="/housing1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="rent_div">{checkRent}
                        </div>
                        <br />
                        <div id="mortgage_div">{checkMortgage}
                        </div>
                        <br />
                        <div id="two_div">{checkTwo}
                        </div>
                        <br />
                        <div id="three_div">{checkThree}
                        </div>
                    </form>
                    <script>
                        if ('{checkRent}' == 1)
                            document.getElementById("rent_div").innerHTML = '<input type="checkbox" name="item" value="rent" checked/> Rent (1BHK in Bavdhan) Rs.11000';
                        else
                            document.getElementById("rent_div").innerHTML = '<input type="checkbox" name="item" value="rent" /> Rent (1BHK in Bavdhan) Rs.11000';
                    </script>
                    <script>
                        if ('{checkMortgage}' == 1)
                            document.getElementById("mortgage_div").innerHTML = '<input type="checkbox" name="item" value="mortgage" checked/> EMI (1BHK in Aundh) Rs.20000';
                        else
                            document.getElementById("mortgage_div").innerHTML = '<input type="checkbox" name="item" value="mortgage" /> EMI (1BHK in Aundh) Rs.20000';
                    </script>
                    <script>
                        if ('{checkTwo}' == 1)
                            document.getElementById("two_div").innerHTML = '<input type="checkbox" name="item" value="two" checked/> EMI (2BHK in Kothrud) Rs.35000';
                        else
                            document.getElementById("two_div").innerHTML = '<input type="checkbox" name="item" value="two" /> EMI (2BHK in Kothrud) Rs.35000';
                    </script>
                    <script>
                        if ('{checkThree}' == 1)
                            document.getElementById("three_div").innerHTML = '<input type="checkbox" name="item" value="three" checked/> EMI (3BHK in Karvenagar) Rs.50000';
                        else
                            document.getElementById("three_div").innerHTML = '<input type="checkbox" name="item" value="three" /> EMI (3BHK in Karvenagar) Rs.50000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkRent=checkRent, checkMortgage=checkMortgage, checkTwo=checkTwo, checkThree=checkThree)

@app.route('/fitness_final', methods=["GET", "POST"])
def fit_page():
    global checkSports
    global checkGym
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">FITNESS</p>
                    <form action="/fitness1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="sports_div">{checkSports}
                        </div>
                        <br />
                        <div id="gym_div">{checkGym}
                        </div>
                    </form>
                    <script>
                        if ('{checkSports}' == 1)
                            document.getElementById("sports_div").innerHTML = '<input type="checkbox" name="item" value="sports" checked/> Sports Rs.700';
                        else
                            document.getElementById("sports_div").innerHTML = '<input type="checkbox" name="item" value="sports" /> Sports Rs.700';
                    </script>
                    <script>
                        if ('{checkGym}' == 1)
                            document.getElementById("gym_div").innerHTML = '<input type="checkbox" name="item" value="gym" checked/> Gym Rs.1400';
                        else
                            document.getElementById("gym_div").innerHTML = '<input type="checkbox" name="item" value="gym" /> Gym Rs.1400';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkSports=checkSports, checkGym=checkGym)

@app.route('/utilities_final', methods=["GET", "POST"])
def uti_page():
    global checkBasic
    global checkPhone
    global checkInternet
    global checkMaid
    return '''
        <html>
            <body bgcolor = "#228B22">
                <div style="color:white;">
                    <p style="font-size:20px;">UTILITIES</p>
                    <form action="/utilities1" method="post">
                        <input type="hidden" name="item" value="none" />
                        <div id="basic_div">{checkBasic}
                        </div>
                        <br />
                        <div id="phone_div">{checkPhone}
                        </div>
                        <br />
                        <div id="internet_div">{checkInternet}
                        </div>
                        <br />
                        <div id="maid_div">{checkMaid}
                        </div>
                    </form>
                    <script>
                        if ('{checkBasic}' == 1)
                            document.getElementById("basic_div").innerHTML = '<input type="checkbox" name="item" value="basic" checked/> Basic Rs.1200';
                        else
                            document.getElementById("basic_div").innerHTML = '<input type="checkbox" name="item" value="basic" /> Basic Rs.1200';
                    </script>
                    <script>
                        if ('{checkPhone}' == 1)
                            document.getElementById("phone_div").innerHTML = '<input type="checkbox" name="item" value="phone" checked/> Phone Rs.600';
                        else
                            document.getElementById("phone_div").innerHTML = '<input type="checkbox" name="item" value="phone" /> Phone Rs.600';
                    </script>
                    <script>
                        if ('{checkInternet}' == 1)
                            document.getElementById("internet_div").innerHTML = '<input type="checkbox" name="item" value="internet" checked/> Internet Rs.2500';
                        else
                            document.getElementById("internet_div").innerHTML = '<input type="checkbox" name="item" value="internet" /> Internet Rs.2500';
                    </script>
                    <script>
                        if ('{checkMaid}' == 1)
                            document.getElementById("maid_div").innerHTML = '<input type="checkbox" name="item" value="maid" checked/> Housemaid Rs.2000';
                        else
                            document.getElementById("maid_div").innerHTML = '<input type="checkbox" name="item" value="maid" /> Housemaid Rs.2000';
                    </script>
                </div>
            </body>
        </html>
    '''.format(checkBasic=checkBasic, checkPhone=checkPhone, checkInternet=checkInternet, checkMaid=checkMaid)

@app.route('/profile_final', methods=["GET", "POST"])
def pro_page():
    global profession
    global age
    global salary
    global gmi
    return '''
        <html>
            <img src="https://pixabay.com/get/54e0d7444c53a514f6da8c7dda6d49214b6ac3e45654784c77287dd494/african-2027619_1280.png" alt="Boy" height="125" width="150" style="float: left" />
            <p style="color:black; font-size:17px;">My profession is {profession}</p>
            <p style="color:black; font-size:17px;">Age: {age}</p>
            <p style="color:black; font-size:17px;">My salary is Rs. {salary}</p>
            <p style="color:black; font-size:17px;">My gross monthly income is Rs. {gmi}</p>
        </html>
    '''.format(profession=profession, age=age, salary=salary, gmi=gmi)

@app.route('/salary_final', methods=["GET", "POST"])
def sal_page():
    result = listed()
    federal = result[0];
    mt = result[1];
    nmi = result[2];
    result1 = left()
    return'''
        <html>
            <p style="color:black; text-align:center;">My total federal tax is Rs.{federal}</p>
            <p style="color:black; text-align:center;">My total monthly tax is Rs.{mt}</p>
            <p style="color:black; text-align:center;">My net monthly income is Rs.{nmi}</p>
            <p style="color:black; text-align:center;">My total savings for this month is Rs.{result1}</p>
        </html>
    '''.format(result1=result1, federal=federal, mt=mt, nmi=nmi)


#Start of code
if __name__ == '__main__':
	#main()
    app.run(debug=True)
