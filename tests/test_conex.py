# pip install pymysql
print("Resultados de PyMySQL:")
import pymysql,json
miConexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='nueva' )
cur = miConexion.cursor()
cur.execute( "SELECT nombre, apellidos FROM usuarios" )
rows=cur.fetchall()
for nombre, apellidos in rows :
    print(nombre, apellidos)
print(json.dumps(rows))
miConexion.close()
