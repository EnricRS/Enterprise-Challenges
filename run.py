#./run.sh

from flask import render_template, request, redirect, url_for


from flask import Flask
app = Flask(__name__)
activitats = []
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    
    if request.method == 'POST':
        dic_dades= {'nom': ""}

        
        dic_dades['nom'] = request.form['name']
        opcions = request.form.getlist('opcions')
        for opt in opcions:
            
            dic_dades[opt] = 1
        print(dic_dades)
        crear_csv(dic_dades)
        return redirect('/')
    import_txt()
    return render_template("signup_form.html", activitats = activitats)

import csv
def crear_csv(dic_dades):
    with open('dades_activitat.csv', mode='w') as csv_file:
        
        fieldnames = ["nom"]+activitats
        print(fieldnames, activitats)
        
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, dialect='excel')
        writer.writeheader()
        writer.writerow(dic_dades)

def import_txt():
    with open('fitxer_activitats.txt', 'r') as text_file:
        for row in text_file:
            #print(row.rstrip())
            activitats.append(row.rstrip())
            


