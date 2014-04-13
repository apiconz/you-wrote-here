__author__ = 'Armando P.'

from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nombre = ndb.StringProperty()
    descripcion = ndb.StringProperty()
    correo_electronico = ndb.StringProperty()
    imagen_url = ndb.StringProperty()
    facebook_email = ndb.StringProperty()
    googleplus_id = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def usuario_key(cls, nombre_usuario):
        return ndb.Key('Usuario', nombre_usuario)

    @classmethod
    def consultar_usuario(cls, ancestor_key):
        return cls.query(ancestor=ancestor_key).order(-Usuario.nombre).fetch(5)
