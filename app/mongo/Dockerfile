# Usa una imagen base de MongoDB
FROM mongo

# Copia el script de inicialización de la base de datos
COPY mongo.py /docker-entrypoint-initdb.d/

# Expone el puerto de MongoDB (por defecto 27017)
EXPOSE 27017


