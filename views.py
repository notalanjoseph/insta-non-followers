#file for the roots

from flask import Blueprint, render_template
from flask import request

myviews = Blueprint(__name__, "views")


@myviews.route("/", methods=['GET','POST'])
def getData():
    if request.method == 'POST':
        #run code and display output
        return render_template("index.html", ans = "hello ther")
    else:
        return render_template("index.html")