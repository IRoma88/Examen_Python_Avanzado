# 📧 Proyecto Final 2 – Python Avanzado: Automatización de Correos

Este proyecto es una práctica avanzada de Python centrada en la **automatización de correos electrónicos personalizados**. Utiliza manipulación de texto, archivos `.txt` y programación orientada a objetos para simular el envío de correos.

## 📌 Objetivo

Crear una clase `Email` capaz de:

1. Agrupar usuarios por proveedor de email.
2. Generar un mensaje genérico parametrizable.
3. Crear mensajes personalizados y guardarlos como archivos `.txt`.

## 🧩 Estructura del Proyecto

- `Email` es una clase que contiene los siguientes métodos:

### ✅ `proveedor_usuarios(lista_emails)`

- Recibe una lista de emails.
- Devuelve un diccionario donde:
  - Las **claves** son los **proveedores de correo** (`vmail.es`, `gagoo.es`, `youtlook.es`).
  - Los **valores** son listas con los **nombres de usuario** correspondientes.

### ✅ `mensaje(texto)`

- Crea un archivo `mensaje_generico.txt` con el contenido del texto.
- Debe contener variables marcadas como `{nombre}` y `{proveedor}` para personalización.
- Devuelve el contenido del archivo generado.

### ✅ `preparar_envio(diccionario, proveedor, texto)`

- Recibe:
  - Un diccionario de usuarios por proveedor.
  - Un proveedor específico.
  - Un texto genérico con variables.
- Crea un archivo `.txt` personalizado para cada usuario del proveedor.
- Devuelve un mensaje indicando cuántos correos se han generado.

## 📂 Ejemplo de uso

```python
emails = ['usuario@vmail.es', 'otro@gagoo.es']
emailer = Email()
dicc = emailer.proveedor_usuarios(emails)
msg = emailer.mensaje("Hola {nombre}, gracias por usar {proveedor}")
print(emailer.preparar_envio(dicc, 'vmail.es', msg))
````

## ✅ Verificación
El proyecto incluye funciones check() para verificar automáticamente la correcta implementación de cada parte del ejercicio.

## 💻 Requisitos
Python 3.x

No se requieren librerías externas

## ⚙️ Entorno de desarrollo
Compatible con Google Colab (recomendado)

También funcional en entornos locales con Windows 11

## 📄 Licencia
Este proyecto es solo para fines educativos y de práctica personal.
