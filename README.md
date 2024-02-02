# Aplicación de Descarga de Imágenes de KoboToolbox

Esta aplicación Python permite descargar automáticamente imágenes almacenadas en KoboToolbox, organizándolas en carpetas locales basadas en el tipo de insecto detallado. Utiliza la API de KoboToolbox y requiere autenticación mediante token para acceder a las imágenes.

## Requisitos

- Python 3.6 o superior.
- Bibliotecas de Python: `requests`, `pandas`, y `python-dotenv`.
- Token de acceso de KoboToolbox.

## Configuración

## Instalación de Dependencias

Primero, instala las dependencias necesarias usando `pip`. Abre tu terminal y ejecuta:

```bash
pip install requests pandas python-dotenv
```

### Configuración del Token de KoboToolbox

Crea un archivo .env en el directorio raíz de tu proyecto.

Agrega la siguiente línea al archivo .env, reemplazando tu_token_aquí con tu token de acceso de KoboToolbox:

```
TOKEN_KOBO=tu_token_aquí
```

### Uso

Asegúrate de tener un archivo CSV con las columnas Tipo_Insecto, Tipo insecto detalle, y Url foto, que contenga los datos necesarios para la descarga.

Modifica la variable file_path en el script para que apunte a la ubicación de tu archivo CSV.

Ejecuta el script con Python:

```bash
python app.py
```

El script descargará las imágenes en la carpeta especificada en la variable base_folder, creando subcarpetas según el Tipo insecto detalle.

### Estructura del Proyecto

El proyecto incluye los siguientes archivos y carpetas:

app.py: Script principal de la aplicación.
.env: Archivo para almacenar el token de acceso de KoboToolbox.
archivos_descargar.csv: Archivo CSV de ejemplo con las URLs de las imágenes a descargar.

```

└── 📁src
└── .DS_Store
└── .env
└── .envEXAMPLE
└── .gitignore
└── app.py
└── archivos_descargar.csv
└── 📁descargas
└── .DS_Store
└── requirements.txt

```

##Contribuir
Si deseas contribuir a este proyecto, por favor haz fork del repositorio y envía tus pull requests.

##Licencia
Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

```

```
