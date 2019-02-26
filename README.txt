Este es un proyecto de prueba sobre la automatización de Twitter en Python
usando la librería Tweepy. El Bot para el que se diseñaron las funciones trataba
de imitar el comportamiento de un fan del Real Madrid, como se ve reflejado en
el módulo dialogo y user_data.

El módulo funciones implementa diversas funciones que facilitan mucho el trabajo
con la librería Tweepy. Las acciones del bot deberían ser definidas en el 
módulo bot, quien debería controlar la lógica de este.
Entre las funciones se encuentran las de login, seguimiento de usuarios, 
tweeteo y retweeteo de tweets, entre otras.

El bot necesita de una serie de claves para poder entrar dentro de su cuenta de
Twitter. Estas deberían estar almacenadas en un archivo keys.py en la que se 
deberían inicializar las siguientes variables:
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_secret = ""
Todas ellas las proporciona Twitter.

El proyecto es uno piloto, y no tiene más voluntad que el aprender a utilizar
la librería Tweepy y comenzar a trabajar con la automatización en Twitter.


Fdo: Víctor Yrazusta