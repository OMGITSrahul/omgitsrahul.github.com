#!/usr/bin/python3.2

def pageslist():
    import os
    import re
    listall = os.listdir('.')
    list_html = []
    
    ###Find html file in the curr dir
    html = re.compile(r"[^.]+\.html")
    list_file = [item for item in listall if (html.match(item) and item!="tags.html")]
    list_html += list_file
    ###Find html files in 2012 dir
    directory = re.compile(r"(\.*)([^\.]*)(\.+)")
    list_dir = [item for item in listall if not directory.match(item)]
    list_dir = [item for item in list_dir if item!="feeds" and item!="source" and item!="static" and item!="theme" and item!="README"]
    flat_dir = [item for item in list_dir if not item.isnumeric()]
    comp_dir = [item for item in list_dir if item not in flat_dir]
    #sort out flat dirs first
    for dir in flat_dir:
        for file in os.listdir('./'+dir):
            list_html.append("./"+dir+"/"+file)
    #now the double layered dir
    for dirs in comp_dir:
        for dir in os.listdir('./'+dirs):
            for file in os.listdir('./'+dirs+'/'+dir):
                list_html.append('./'+dirs+'/'+dir+'/'+file)
    
    
    return list_html

def fix(filepath):
    infile = open(filepath)
    data = infile.read()
    infile.close()
    numslash = filepath.count("/")
    if numslash == 0:
        dots = "."
    elif numslash == 2:
        dots = ".."
    else:
        dots = "../.."
    
    data = data.replace("""                <h1><a href=".">{Fleeting thoughts of the pointless variety} </a></h1>""", """                <h1><a href=\""""+dots+"""/index.html">{Fleeting thoughts of the pointless variety} </a></h1>""")
    data = data.replace("""                <h1><a href="../.">{Fleeting thoughts of the pointless variety} </a></h1>""", """                <h1><a href=\""""+dots+"""/index.html">{Fleeting thoughts of the pointless variety} </a></h1>""")
    data = data.replace("""                <h1><a href="../../.">{Fleeting thoughts of the pointless variety} </a></h1>""", """                <h1><a href=\""""+dots+"""/index.html">{Fleeting thoughts of the pointless variety} </a></h1>""")
    
    data = data.replace("""<p>In <a href="./category/Home.html">Home</a>. </p>""", "")
    data = data.replace("""<p>In <a href=".././category/Home.html">Home</a>. </p>""", "")
    data = data.replace("""<p>In <a href="../.././category/Home.html">Home</a>. </p>""", "")
    
    data = data.replace("""<p class="paginator">
    
    Page 1 / 1
    
</p>""", "")

    
    
    
    outfile = open(filepath, "w")
    print(data, file=outfile)
    outfile.close()
    

print(pageslist())

for filepath in pageslist():
    fix(filepath)