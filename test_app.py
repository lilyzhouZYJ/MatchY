<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

import json
#import elasticsearch and connect to clutter
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '172.23.117.23', 'port': 9200}])

@app.route('/', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['email'] != 'admin' or request.form['pswd'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect('/home')
	return render_template('login.html', error=error)
=======
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")
>>>>>>> 62f8a435b7cefe3a15277dea784a9323c28c2531

@app.route("/home")
def home():
   return render_template("home.html")

<<<<<<< HEAD

@app.route("/home")
def test():
   query = request.GET.get('query') or ""
   res = es.search(index="patients", body={
		"query":{
		    "match":{
		        "phenotype":query
                    }
                }
	}, size=10)
   phnDic = {}
   for result in res['hits']['hits']:
       for p in result['_source']['phenotype']:
            phnDic["phenotype"] = p
   phenotypes = json.dumps(phnDic)
   return phenotypes


=======
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
>>>>>>> 62f8a435b7cefe3a15277dea784a9323c28c2531

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

<<<<<<< HEAD
@app.route("/my_submissions")
def mySubmissions():
   return render_template("my-submissions.html")




#create dictionary with HGNC names as keys and ENSG names as values
genes = open("mart_export_ens_hgnc_1to1only.txt","r").readlines()
geneDic = {}
for line in genes:
	line = line.replace("\n","")
	text = line.split("\t")
	geneDic[text[0]] = text[1]

@app.route('/search-result', methods=['GET', 'POST'])
def searchResult():
	geneHGNC = request.form['gene']
	geneENSG = geneDic[geneHGNC]
	inheritancePattern=request.form['inheritance-pattern']
	variantType=request.form['variant-type']
	chr=request.form['chr']
	position=request.form['position']
	ref=request.form['ref']
	alt=request.form['alt']
	phenotype=request.form['phenotype']

        res = es.search(index="patients", body={
		"query":{
		    "match":{
		        "gene":geneENSG
                    }
                }
	}, size=100)
	
	return render_template('search-result.html', gene=geneHGNC, inheritancePattern=inheritancePattern, variantType=variantType, chr=chr, position=position, alt=alt, ref=ref, phenotype=phenotype,res=res)
=======




@app.route('/submission/result', methods=['GET', 'POST'])
def submissionResult():
	return render_template('submission-result.html', identifier=request.form['identifier'])

@app.route('/gene-search/result', methods=['GET', 'POST'])
def geneSearchResult():
	return render_template('gene-search-result.html', geneSymbol=request.form['gene-symbol'], symMatch=request.form['sym-match'], geneCoor=request.form['gene-coor'], coorMatch=request.form['coor-match'])

@app.route('/diagnosis-search/result', methods=['GET', 'POST'])
def diagnosisSearchResult():
	return render_template('diagnosis-search-result.html', mimNumber=request.form['mim-number'], disorderType=request.form['disorder-type'], inheritancePattern=request.form['inheritance-pattern'])


>>>>>>> 62f8a435b7cefe3a15277dea784a9323c28c2531

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')

