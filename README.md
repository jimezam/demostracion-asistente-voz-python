# Demostración de asistente de voz con Python

## Instalación

### Pasos previos

Instalar los siguientes requerimientos del sistema operativo

```
$ sudo apt install portaudio19-dev
```

### Instalar las librerías requeridas

Crear el ambiente virtual.

```
$ python -m venv venv
```

Activar el repositorio.

```
$ source venv/bin/activate
```

Instalar las librerías indicadas.

```
$ pip install -r requirements.txt
```

## Demostración

Para verificar el funcionamiento de la aplicación, utilizar la demostración llamada `test.py`.  La cual deberá mencionar verbalmente la palabra "`Marco`" y deberá reponderse la palabra "`Polo`" cuando se le indique.

Para ejecutar esta aplicación deberá utilizarse el siguiente comando.

```
$ python test.py
```

Recuérdese que para ejecutar estas aplicaciones, es necesario tener activo el ambiente virtual como se mostró en la sección anterior.

## Ejecutar la aplicación

Para ejecutar la aplicación es necesario utilizar el siguiente comando.

```
$ python main.py
```

## Para desarrolladores

Las funcionalidades de mencionar un mensaje verbalmente y de escuchar/reconocer un mensaje, han sido centralizadas en el archivo `assistant.py` y en las funciones `speak` y `listen` respectivamente.

## Librerías

Estas son las principales librerías utilizadas para la demostración.

  - SpeechRecognition
  - gTTS
  - playsound
  - PyAudio