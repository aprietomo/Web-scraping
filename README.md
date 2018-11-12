# Web-scraping
Práctica 1 de la asignatura de “Tipologia i cicle de vida de les dades” de la UOC.

# Descripción
Esta práctica consiste en la generación de un dataset con el listado de diferentes productos de una categoría que posee la tienda Mediamarkt durante un día en concreto. Las variables que contiene este listado son el nombre del producto, el precio y la fecha de obtención del dato.

# Miembros del equipo
Esta práctica ha sido realizada de manera individual por Aitor Prieto Moreno


# Ejecución del script
Para ejecutar el script se debe ejecutar el siguiente comando:


              python MediamarktScraper.py <Nombre de la categoría> <url de la categoría>
  
El nombre de la categoría hace referencia a una categoría de productos de la cual se obtendrá información (ej : televisiones). Este nombre también formara parte del nombre del fichero de salida resultante.

Para obtener las urls se puede hacer uso del sitemap publicado por Mediamarkt:


            https://www.mediamarkt.es/sitemap/sitemap-productlist.xml
