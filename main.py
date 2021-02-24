import os
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
import tabula
import pandas as  pd
import sweetviz as sv
from sklearn.preprocessing import StandardScaler
import numpy as np
app = Flask(__name__)

# df = pd.read_csv('bank.csv')
pdf_name=""
temp=os.listdir()
for i in temp:
    if ".pdf" in i:
        pdf_name=i

if pdf_name!= None:
    if pdf_name in os.listdir():
        df = tabula.read_pdf(pdf_name, pages='all')
        tabula.convert_into(pdf_name, "output.csv", output_format="csv", pages='all')
        print(df)
    else:
        df = pd.read_csv('output.csv')
        bank_report = sv.analyze(df)
        # bank_report.show_html('bank.html')
        df1 = sv.compare(df[5000:], df[:5000])
        # df1.show_html('Compare.html')


@app.route('/')
def home():
    return render_template('Compare.html')
@app.route('/bank')
def bank():
    return render_template('bank.html')


if __name__ == "__main__":
    app.run(debug=True)
