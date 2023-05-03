# <b>Authentificationsystem</b>
- [Authentificationsystem](#authentificationsystem)
  - [Developementumgebung](#developementumgebung)
    - [Virtual Environment](#virtual-environment)
      - [**Benötigte Pakete**](#benötigte-pakete)
    - [Webserver starten](#webserver-starten)


## Developementumgebung
### Virtual Environment
Da eine Virtuelle Entwicklungsumgebung Vorteile bietet wie z.B. dass man Bibliotheken nicht Lokal installieren muss. Hierfür einfach im Terminal in den Ordner [./authentification](./authentification/) navigieren und die Virtuelle Umgebung erzeugen mit:
```ps
py -m venv venv
```
und mit einem der beiden folgenden Befehle aktivieren. **Der unterschied ist lediglich, dass die .bat mit der Kommandozeile und die .ps1 mit der Powershell ausgeführt werden kann.**

```cmd
venv\Scripts\activate.bat
venv\Scripts\activate.ps1
```
<body>
<b style="color:red;">Was tun bei Fehlermeldung</b>
<p>Falls eine Sicherheitsfehlermeldung kommt, liegt das daran, dass Standartmäßig die Ausführung von Skripten unter Windows aus Sicherheitsgründen deaktiviert ist. Diese muss verändert werden um die virtuelle Umgebung zu Starten. Folgender Befehl erlaubt die Ausführung von lokal erzeugten .ps1 oder .bat und verlangt bei heruntergeladenen Skripten, dass diese von einer Vertrauenswürdigen Quelle Signiert wurden.<p>
</body>

```ps
Set-ExecutionPolicy RemoteSigned
```

#### **Benötigte Pakete**
Da wir einige Packete benötigen, müssen wir diese nun in der virtuellen Umgebung installieren. Hierfür folgende Pakete installieren:
```ps
pip install django
pip install django_crispy_forms
```

**Prüfen ob es funktioniert hat**
Um zu überprüfen, ob die Umgebung nun bereit ist, kann der befehl `django-admin` eingegeben werden und falls dann alle vorhandenen Kommandos gelistet werden und keine Fehlermeldung kommt, läuft alles. 

### Webserver starten
Um eine lokale Serverumgebung zu starten muss in den Ordner [./authentification/authsystem](./authentification/authsystem) navigiert werden und dort folgender Befehl ausgeführ werden
```cmd
python manage.py runserver
```