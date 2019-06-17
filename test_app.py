from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("home.html")

@app.route("/gene-search")
def geneSearch():
   return render_template("gene-search.html")

@app.route("/diagnosis-search")
def diagnosisSearch():
   return render_template("diagnosis-search.html")

@app.route("/reports")
def reports():
   return render_template("reports.html")

@app.route("/match-outcome")
def matchOutcome():
   return render_template("match-outcome.html")

@app.route("/reports/events")
def reportsEvents():
   return render_template("events.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/publications")
def publications():
   return render_template("publications.html")

@app.route("/statistics")
def statistics():
   return render_template("statistics.html")

@app.route("/contact-us")
def contactUs():
   return render_template("contact-us.html")

@app.route("/account")
def account():
   return render_template("account.html")

@app.route("/help/eula")
def eula():
   return render_template("eula.html")

@app.route("/help/faq")
def faq():
   return render_template("faq.html")

@app.route("/help/submission-help")
def submissionHelp():
   return render_template("submission-help.html")

@app.route("/help/features-table")
def featuresTable():
   return render_template("features-table.html")

@app.route("/help/matchy-api")
def matchyApi():
   return render_template("matchy-api.html")

@app.route("/help/mme-api")
def mmeApi():
   return render_template("mme-api.html")

@app.route("/help/external-data-sources")
def externalData():
   return render_template("external-data.html")





@app.route('/submission/result', methods=['GET', 'POST'])
def submissionResult():
	return render_template('submission-result.html', identifier=request.form['identifier'])

@app.route('/gene-search/result', methods=['GET', 'POST'])
def geneSearchResult():
	return render_template('gene-search-result.html', geneSymbol=request.form['gene-symbol'], symMatch=request.form['sym-match'], geneCoor=request.form['gene-coor'], coorMatch=request.form['coor-match'])

@app.route('/diagnosis-search/result', methods=['GET', 'POST'])
def diagnosisSearchResult():
	return render_template('diagnosis-search-result.html', mimNumber=request.form['mim-number'], disorderType=request.form['disorder-type'], inheritancePattern=request.form['inheritance-pattern'])



if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')

