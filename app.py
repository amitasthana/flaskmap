from flask import Flask, render_template
import csv
from pprint import pprint
from flask import jsonify
import random

app = Flask(__name__)

@app.route('/vinden')
def index():
	return render_template('map.html')


@app.route('/')
def readcsv():

	result = {}
	resultarray = [ ]	
	with open('files/sales.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in csvreader:
			makedict = { }
			if row[6] in result:
				
				result[row[6]].append( float(row[1][1:]))

				amount = sum(result[row[6]])
				#makedict['id'] = makedict['values'].append(float( row[1][1:]))
			else:
				if row[1] != 'Order Amount':
					result[row[6]] = [ float( row[1][1:] )]					
					#makedict['id'] = makedict['values'].append(float( row[1][1:]))				
	

	dictlist = []	

	objet = { }

	for key, value in result.items():
		temp = [key, sum(  value) ]		
		r = lambda: random.randint(0,255)
		color = '#%02X%02X%02X' % (r(),r(),r())
		temp_dict = { "color":color, "totalamount":sum ( value) }
		objet[key] = temp_dict

	return render_template('map.html', result=objet)

	


if __name__ == '__main__':
	app.run()