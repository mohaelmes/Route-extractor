# Route-extractor

Route-Extractor es una aplicación web diseñada para extraer enlaces de una página web dada, mostrarlos al usuario y almacenar los enlaces en una base de datos MongoDB. Esta herramienta es útil para analizar la estructura de una página web, recopilar enlaces para crawling, o simplemente para explorar los enlaces disponibles en una página de manera organizada.

**Funcionamiento del Proyecto**
El proyecto se compone de varias partes integradas:

1. **Servidor Web Flask:** Una aplicación Flask que maneja las solicitudes del usuario y la interfaz web.
2. **Extracción de Rutas:** Utiliza la biblioteca requests para obtener el contenido HTML de una página web y BeautifulSoup para analizar y extraer los enlaces.
3. **Base de Datos MongoDB:** Almacena los enlaces extraídos junto con la dirección IP del solicitante y la fecha de inserción.
4. **Frontend HTML:** Proporciona una interfaz web para que los usuarios puedan ingresar una URL y ver los enlaces extraídos.

# Detalles del Funcionamiento
*1. Servidor Web Flask*
- El servidor web está configurado en el archivo app.py.
- Define una ruta principal (/) que maneja las solicitudes GET y POST.
- Cuando el usuario envía una URL a través del formulario HTML, el servidor Flask procesa esta solicitud y llama a la función de extracción de rutas.
  
*2. Extracción de Rutas*
La función extraer_rutas(url) se encarga de:
- Realizar una solicitud HTTP a la URL proporcionada utilizando requests.get(url).
- Verificar que la solicitud sea exitosa (código de estado 200).
- Analizar el contenido HTML con BeautifulSoup y encontrar todas las etiquetas <a>.
- Extraer los enlaces (href) de cada etiqueta <a> y filtrar los enlaces que comienzan con http o https.
  
*3. Base de Datos MongoDB*
- La interacción con MongoDB se maneja en el módulo mongo/mongo.py.
- Se conecta a una base de datos MongoDB Atlas utilizando un URI.
- Las funciones principales incluyen:

   - insert(route, ip): Inserta un documento en la colección con la ruta, la dirección IP del solicitante y la fecha actual.
  
   - ping(): Verifica la conexión a la base de datos.
  
   - delete(): Elimina todos los documentos de la colección (utilizado para limpieza).
  
*4. Frontend HTML*
- El archivo templates/index.html define la interfaz de usuario.
- Un formulario permite al usuario ingresar una URL.
- Después de enviar el formulario, los enlaces extraídos se muestran en una lista debajo del formulario.
- Utiliza la plantilla de Flask para renderizar los resultados dinámicamente.
  
*5. Docker*
  
- **Dockerfile:** Define la configuración para construir una imagen Docker de la aplicación Flask.
- **docker-compose.yml:** Configura los servicios para Docker Compose, incluyendo el servicio web (Flask) y la base de datos MongoDB.
# Flujo de Trabajo
- **Usuario Accede a la Aplicación:** El usuario abre la aplicación web en su navegador.
- **Usuario Envía una URL:** El usuario ingresa una URL en el formulario y envía la solicitud.
- **Extracción de Enlaces:** El servidor Flask recibe la URL, llama a extraer_rutas(url), y obtiene los enlaces de la página web.
- **Almacenamiento en MongoDB:** Los enlaces extraídos se almacenan en MongoDB junto con la dirección IP del usuario y la fecha.
- **Mostrar Resultados:** Los enlaces se muestran en la interfaz web para que el usuario pueda verlos y acceder a ellos.
