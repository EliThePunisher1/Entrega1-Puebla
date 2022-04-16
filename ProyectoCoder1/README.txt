ProyectoCoder1 es la carpeta principal del proyecto. Esta tiene sus propios urls y views.
AppCoder1 es la aplicacion del proyecto que se encarga de la parte estetica. Dentro esta templates que tiene cargadas las plantillas 
html que son las que se van a mostrar en la pagina.


1_ mi problema es que no puedo hacer mi formulario de busqueda, me tira el error 
"" AttributeError at /buscar/
'WSGIRequest' object has no attribute 'get'""

la verdad es que trate de seguir al pie de la letra las clases, se me dificulto cambiarle los nombres y tratar de hacer lo mismo pero creo 
que voy bien.

2_mi otro problema es que la primary key de mis modelos no se esta generando por si sola. Entonces cada vez que alguien quiere llenar el formulario
desplaza los lugares de mi orden en +1 debido a que tomar al primer valor como el id. Lo que hize para salvar este error y no tocar los models
fue añadir un valor llamado "identificacion" que es un numero que el usuario elige y nada eso me lo soluciono.

