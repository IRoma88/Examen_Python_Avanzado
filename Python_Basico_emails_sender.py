# -*- coding: utf-8 -*-

#Proyecto final 2 Python avanzado

En este proyecto vamos a automatizar la generación de emails. Para ello os entregaremos una lista de correos ficticia de diferentes proveedores de emails (En lugar de utilizar gmail, yahoo y outlook usaremos vmail,gagoo y youtlook, para evitar que sean reales).

# Crear el diccionario proveedor_usuarios

Para empezar crearemos la clase y el primer método llamado proveedor_usuarios el cual recibirá una lista de correos como parámetro y devolverá el diccionario donde las claves serán los diferentes proveedores de correos y los valores la lista de nombres de usuario que utilizan dicho proveedor.

Por ejemplo, en la dirreción de correo 'jimenez@gagoo.es' el nombre de usuario es 'jimenez' y su proveedor 'gagoo.es'.
"""

Lista_emails=['garcia@vmail.es','sanchez@gagoo.es','pedro@youtlook.es','carlos@vmail.es','german@gagoo.es','pablo@youtlook.es','fernandez@vmail.es','jimenez@gagoo.es','edu.perez@youtlook.es','rubia.17@vmail.es','1995sanz@gagoo.es','donaire@youtlook.es','pascual@vmail.es','pantoja14@vmail.es','romero@gagoo.es']

class Email:

  def proveedor_usuarios(self,lista_emails):
    self.lista_emails=lista_emails
    proveedores=[]
    dict_emails={}
    for i in self.lista_emails:
      i=i.split('@')
      if i[1] not in proveedores:
        proveedores.append(i[1])
    for x in proveedores:
      dict_emails[x]=[user[:user.index('@')] for user in self.lista_emails if x in user]

    return dict_emails

Email().proveedor_usuarios(Lista_emails)

lista_check=['a1@hola.com','a2@adios.es','b1@hola.com']
Email().proveedor_usuarios(lista_check)

lista_check=['a1@hola.com','a2@adios.es','b1@hola.com']
def check():
  if Email().proveedor_usuarios(Lista_emails)=={'gagoo.es': ['sanchez', 'german', 'jimenez', '1995sanz', 'romero'], 'vmail.es': ['garcia', 'carlos', 'fernandez', 'rubia.17', 'pascual', 'pantoja14'], 'youtlook.es': ['pedro', 'pablo', 'edu.perez', 'donaire']} and Email().proveedor_usuarios(lista_check)=={'adios.es': ['a2'], 'hola.com': ['a1', 'b1']}:
    return 'Correcto'
  else:
    return 'Incorrecto'

check()

"""## Método mensaje

Añade el método mensaje a la clase anterior.

Este método mensaje recibirá como parámetro el texto genérico que contendrá el mensaje y creará un txt con dicho texto. Debes marcar de alguna forma las partes del texto personalizables.

"""

import re
class Email:

  def __init__(self):
        self.lista_emails = []

  def proveedor_usuarios(self,lista_emails):
    self.lista_emails=lista_emails
    proveedores=[]
    dict_emails={}
    for i in self.lista_emails:
      i=i.split('@')
      if i[1] not in proveedores:
        proveedores.append(i[1])
    for x in proveedores:
      dict_emails[x]=[user[:user.index('@')] for user in self.lista_emails if x in user]

    return dict_emails

  def mensaje(self,texto):
    self.texto=texto
    file = open("mensaje_generico.txt", "w")
    file.write(texto)

    try:
      open('mensaje_generico.txt','r')
    except:
      return 'Fallo al crear el mensaje genérico'
    else:
      print(f'Mensaje genérico creado con éxito')
      file = open("mensaje_generico.txt", "r")
      return file.read()


Email().mensaje('Buenos dias {nombre},\nGracias por elegir {proveedor} como tu proveedor de mensajes.\nUn cordial saludo')

texto_check2='Comprobando el método mensaje de la clase Email para {nombre} y {proveedor}'
def check2():
  if Email().mensaje(texto_check2)=='Comprobando el método mensaje de la clase Email para {nombre} y {proveedor}':
    return 'Correcto'
  else:
    return 'Incorrecto'

check2()

"""##Método preparar_envio

Añade el método preparar_envio el cual debe recibir como parámetros:

* El diccionario con los correos separados por proveedor.

* El proveedor de correos a cuyos usuarios queremos enviarles el correo.

* El mensaje genérico a personalizar.

Y debe crear tantos emails personalizados en txt y devolver la cadena de texto: 'Se han creado x correos personalizados para ususarios que usan y'.

Donde "x" sea el número de correos creados e "y" el nombre del proveedor de correo.
"""

import re
class Email:
  def proveedor_usuarios(self,lista_emails):
    self.lista_emails=lista_emails
    proveedores=[]
    dict_emails={}
    for i in self.lista_emails:
      i=i.split('@')
      if i[1] not in proveedores:
        proveedores.append(i[1])
    for x in proveedores:
      dict_emails[x]=[user[:user.index('@')] for user in self.lista_emails if x in user]

    return dict_emails

  def mensaje(self,texto):
    self.texto=texto
    file = open("mensaje_generico.txt", "w")
    file.write(texto)

    try:
      open('mensaje_generico.txt','r')
    except:
      return 'Fallo al crear el mensaje genérico'
    else:
      print(f'Mensaje genérico creado con éxito')
      file = open("mensaje_generico.txt", "r")
      return file.read()

  def preparar_envio(self,dic,proveedor,texto_generico):
    self.dic=dic
    self.proveedor=proveedor
    self.generico=texto_generico

    nombres=self.dic[self.proveedor]
    mails_listos=0
    for nombre in nombres:
      mensaje_personalizado=re.sub(r'{nombre}',nombre,self.generico)
      mensaje_personalizado=re.sub(r'{proveedor}',self.proveedor,mensaje_personalizado)
      file= open(nombre+'@'+proveedor+'.txt','w')
      file.write(mensaje_personalizado)
      file.close()
      mails_listos+=1
    return f'Se han creado {mails_listos} emails personalizados de cuentas de {self.proveedor}'


dict_emails=Email().proveedor_usuarios(Lista_emails)
generico=Email().mensaje('Buenos dias {nombre},\nGracias por elegir {proveedor} como tu proveedor de mensajes.\nUn cordial saludo')
Email().preparar_envio(dict_emails,'youtlook.es',generico)

# Opción Clean Code
import re

class Email:
    def __init__(self):
        self.lista_emails = []

    def proveedor_usuarios(self, lista_emails):
        self.lista_emails = lista_emails
        proveedores = set(i.split('@')[1] for i in self.lista_emails)
        dict_emails = {prov: [user.split('@')[0] for user in self.lista_emails if prov in user] for prov in proveedores}
        return dict_emails

    def mensaje(self, texto):
        try:
            with open("mensaje_generico.txt", "w") as file:
                file.write(texto)
            with open('mensaje_generico.txt', 'r') as file_read:
                return file_read.read()
        except IOError:
            return 'Fallo al crear el mensaje genérico'
        else:
            print('Mensaje genérico creado con éxito')

    def preparar_envio(self, dic, proveedor, texto_generico):
        self.dic = dic
        self.proveedor = proveedor
        self.generico = texto_generico
        nombres = self.dic[self.proveedor]
        mails_listos = 0
        for nombre in nombres:
            mensaje_personalizado = re.sub(r'{nombre}', nombre, self.generico)
            mensaje_personalizado = re.sub(r'{proveedor}', self.proveedor, mensaje_personalizado)
            filename = f"{nombre}@{proveedor}.txt"
            with open(filename, 'w') as file:
                file.write(mensaje_personalizado)
            mails_listos += 1
        return f'Se han creado {mails_listos} emails personalizados de cuentas de {self.proveedor}'

Lista_emails=['garcia@vmail.es','sanchez@gagoo.es','pedro@youtlook.es','carlos@vmail.es','german@gagoo.es','pablo@youtlook.es','fernandez@vmail.es','jimenez@gagoo.es','edu.perez@youtlook.es','rubia.17@vmail.es','1995sanz@gagoo.es','donaire@youtlook.es','pascual@vmail.es','pantoja14@vmail.es','romero@gagoo.es']
dict_emails=Email().proveedor_usuarios(Lista_emails)
generico=Email().mensaje('Buenos dias {nombre},\nGracias por elegir {proveedor} como tu proveedor de mensajes.\nUn cordial saludo')
Email().preparar_envio(dict_emails,'youtlook.es',generico)

def check3():
  if Email().preparar_envio(Email().proveedor_usuarios(lista_check),'hola.com',Email().mensaje('Comprobando el método mensaje de la clase Email para {nombre} y {proveedor}'))=='Se han creado 2 emails personalizados de cuentas de hola.com':
    fileA=open('pedro@youtlook.es.txt','r')
    text_check3A=fileA.read()
    fileA.close()
    fileB=open('donaire@youtlook.es.txt','r')
    text_check3B=fileB.read()
    fileB.close()
    if text_check3A!=text_check3B:
      return 'Correcto'
    else:
      return 'Incorrecto. Comprueba el contenido de los txt.'
  else:
    return 'Incorrecto'

check3()


hashlib.sha256((str(text_token1)).encode()).hexdigest()

hashlib.sha256((str(text_token2)).encode()).hexdigest()
