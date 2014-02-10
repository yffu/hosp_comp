'''
Created on Dec 28, 2013

@author: Yuan-Fang
'''
import web, MySQLdb
from web import form

render=web.template.render("templates/", base="layout")
db=web.database(dbn="mysql", user="yffu", pw="1989Oct.2319", db="hc")

urls=(
      "/search", "search",
      "/results", "results"
      )

class search:
    def GET(self):
        i=web.input(table_name=None)
        tname=i.table_name
        if tname==None:
            tname="hospital"
        return render.search()

class results:
    def POST(self):
        i=web.input(zipcode=None)
        z_code=i.zipcode
        print z_code
        if z_code==None:
            return render.error("no zip code entered")
        else:
            return render.results(z_code)
    
if __name__ =="__main__":
    app=web.application(urls, globals())
    app.run()