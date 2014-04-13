__author__ = 'Armando'
import webapp2
import json
import datetime

from entities.Usuario import Usuario
from time import mktime


class ObtenerUsuario(webapp2.RequestHandler):
    def get(self):
        in_nombre = self.request.get('nombre')
        print 'in_nombre=%r' % in_nombre
        usuarios = Usuario.consultar_usuario(Usuario.usuario_key(in_nombre))

        for u in usuarios:
            if u.nombre:
                self.response.headers['Content-Type'] = 'application/json'
                obj = {
                    'nombre': u.nombre,
                    'correo_electronico': u.correo_electronico,
                    'fecha': u.date
                }
                self.response.out.write(json.dumps(obj, cls=MyEncoder))




class RegistrarUsuario(webapp2.RequestHandler):
    def get(self):
        in_nombre = self.request.get('nombre')
        in_correo_electronico = self.request.get('correo_electronico')
        print 'in_nombre=%r,in_correo_electronico=%r' % (in_nombre, in_correo_electronico)


        usuario = Usuario(parent=Usuario.usuario_key(in_nombre))
        usuario.nombre = in_nombre
        usuario.correo_electronico = in_correo_electronico
        if usuario.put():
            respuesta = {'exito': 1}
        else:
            respuesta = {'exito': 0}

        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(respuesta, cls=MyEncoder))


class MyEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, datetime.datetime):
            return int(mktime(o.timetuple()))

        return json.JSONEncoder.default(self, o)

app = webapp2.WSGIApplication([
  ('/registrar', RegistrarUsuario),
  ('/obtener', ObtenerUsuario)
],debug=True)