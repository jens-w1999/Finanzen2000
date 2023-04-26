# <b>Authentificationsystem</b>
- [Authentificationsystem](#authentificationsystem)
  - [Developementumgebung](#developementumgebung)
    - [Virtual Environment](#virtual-environment)
    - [Webserver starten](#webserver-starten)


## Developementumgebung
### Virtual Environment
Da eine Virtuelle Entwicklungsumgebung Vorteile bietet wie z.B. dass man Bibliotheken nicht Lokal installieren muss und jeder den gleichen Developementstand hat muss diese gestartet werden. Hierfür einfach im Terminal in den Ordner [./authentification](./authentification/) navigieren und die Virtuelle Umgebung mit folgendem Befehl aktivieren

```cmd
venv\Scripts\activate.bat
```
oder alternativ
```cmd
venv\Scripts\activate.ps1
```

### Webserver starten
Um eine lokale Serverumgebung zu starten muss in den Ordner [./authentification/authsystem](./authentification/authsystem) navigiert werden und dort folgender Befehl ausgeführ werden
```cmd
python manage.py runserver
```