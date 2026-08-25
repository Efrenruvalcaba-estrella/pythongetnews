basicamente construi un programa en python que hace 4 cosas principales.
primero se conecta a internet para entrar a la pagina web de la cespe y descargar 
todo el texto de las noticias de forma automatica usando la libreria 
requests y bs4. 
tome esta decision porque intente al principio con otras librerias 
como mysqlclient pero me daban muchos errores, asi que me di cuenta
de que requests es la forma mas directa, limpia y facil de traer texto 
de internet sin enredarme.
despues limpie el texto aplicandole replace para quitarle las comas
y los puntos, y luego use split para cortarlo todo y convertirlo en una 
lista gigante de palabras sueltas. tome esta decision porque si una palabra
viene escrita con coma como 10, python no reconoce que es un numero,
asi que al quitarle la puntuacion logre que la palabra quede puramente 
como 10 y me permita usar isdigit sin que falle.
para buscar los dias y evaluar sus numeros recorri la lista palabra
por palabra usando un contador i que va desde 0 hasta la ultima palabra 
del texto. asi cuando encuentra un dia como lunes puedo asomarme a la casilla
siguiente haciendo i mas 1 para ver que palabra o numero le sigue.
tome esta decision porque al principio pense en usar un for sencillo,
pero si solo veia la palabra actual no tenia forma facil de saber que 
numero tenia a la derecha. luego use isdigit para verificar que fuera 
un numero, lo converti a entero con int y le puse la condicion de que 
estuviera entre 1 y 31 para descartar numeros grandes como codigos 
postales o folios y guardar unicamente digitos de dias validos del mes.
finalmente guarde todo en diccionarios. para los dias use setdefault 
porque si solo asignaba el numero directamente cada que aparecia un 
lunes nuevo se borraba el anterior, mientras que con setdefault python 
crea una lista automatica para cada dia y me permite ir agregando todos 
los numeros que encuentre sin sobrescribir nada. para las calles,
colonias y avenidas cree una lista con las palabras clave como calle, 
colonia o avenida, y cuando el ciclo encuentra una de estas palabras
toma la palabra siguiente y la guarda en la categoria correspondiente de
nuestro diccionario de ubicaciones. es la forma mas sencilla que se me 
ocurrio sin meterme en expresiones regulares avanzadas.
