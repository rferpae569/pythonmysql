# pip install pymysql
import pymysql,json

class usuarios:
 def datos(self):
   miConexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='nueva' )
   cur = miConexion.cursor()
   cur.execute( "SELECT nombre, apellidos FROM usuarios" )
   rows=cur.fetchall()
   miConexion.close()
   return json.dumps(rows)

 def insertar(self,nom,ape):
   miConexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='nueva' )
   cur = miConexion.cursor()
   sql = "INSERT INTO usuarios (nombre, apellidos) VALUES (%s, %s)"
   val = (nom, ape)
   cur.execute(sql,val)
   miConexion.commit()
   miConexion.close()
   return json.dumps([nom,ape])

if __name__=="__main__":
   a=usuarios()
   #print(a.insertar(input('Nombre: '),input('Apellidos: ')))
   print(a.datos())
   

