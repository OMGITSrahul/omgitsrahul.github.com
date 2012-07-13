#!/usr/bin/python3.2

html = open("index.html", "r")
htmllines = html.read()

newhtml = htmllines.replace("""                <h1><a href=".">{Fleeting thoughts of the pointless variety} </a></h1>""", """                <h1><a href="./index.html">{Fleeting thoughts of the pointless variety} </a></h1>""")


newhtml = newhtml.replace("""<p>In <a href="./category/Home.html">Home</a>. </p>""", "")


newhtml = newhtml.replace("""<p>tags: <a href="./tag/first!.html">first!</a></p>""", "")

html.close()

html = open("index.new", "w")
print(newhtml, file=html)
html.close()
