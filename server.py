from lenhttp import Application, Endpoint

# Load handlers.
from handlers.launcher.serverinformation import info_get_handler

app = Application(
    port=8080,
    routes= [
        Endpoint("/Engine.svc/GetServerInformation", info_get_handler),
    ]
)

if __name__ == "__main__":
    app.start()