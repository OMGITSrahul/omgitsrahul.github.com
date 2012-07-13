def pageslist():
    import os
    import re
    listall = os.listdir('.')
    list_html = []
    
    #Find html file in the curr dir
    html = re.compile(r"[^.]+\.html")
    list_file = [item for item in listall if (html.match(item) and item!="tags.html")]
    
    #Find html files in 2012 dir
    directory = re.compile(r"(\.*)([^\.]*)(\.+)")
    list_dir = [item for item in listall if not directory.match(item)]
    list_dir = [item for item in list_dir if item!="feeds" and item!="source" and item!="static" and item!="theme" and item!="README"]
    
    return list_dir


print(pageslist())