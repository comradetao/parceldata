from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
import xmltodict
import json
app = Flask(__name__, static_url_path='/static')

def xmlUrlFromParcel(parcelNumber):
    #Get the XML data based on the parcel's ID
    url = "http://neocando.case.edu/cando/housingReport/lbxml.jsp?parcel=" + parcelNumber
    return url

def parcelToDictionary(parcelNumber):
    #Get XML data based on the parcel's ID
    url = xmlUrlFromParcel(parcelNumber)

    #DEBUG - Print the URL of the XML data followed by a blank line to make sure it is correct.
    #print(url)
    #print("\n")

    #Get a web response from the URL of the XML Data
    response = requests.get(url)

    #DEBUG - Print the content of the response so it can be checked
    #against the XML file data from a direct download.
    #print(response.content)
    #print("\n")

    #Parse the XML data into a dictionary or directly to JSON.
    #The leading empty space is stripped because it intereferes with the parse.

    document = xmltodict.parse(response.content.lstrip())
    return document


@app.route('/json/<string:parcel>', methods=['GET'])
def parcelJson(parcel):
    #Return the JSON-formatted document data.
    return jsonify(parcelToDictionary(parcel))

@app.route('/page/<string:parcel>', methods=['GET'])
def parcelPage(parcel):

    #Get the parcel XML data as a python list of dictionaries
    parcelData = parcelToDictionary(parcel)
    # Get the URL for the JSON data.
    url = "/json/" + parcel
    return render_template("parcel.html", jsonDataUrl=url, parcelData=parcelData)

@app.route('/', methods={'GET'})
@app.route('/howto/', methods={'GET'})
def howto():
    return render_template("howto.html")

@app.route('/search', methods=['POST'])
def search():
    parcelId = request.form['searchText']
    print(parcelId)
    return redirect(url_for("parcelPage", parcel=parcelId))

if __name__ == '__main__':
   app.run(debug=True)
