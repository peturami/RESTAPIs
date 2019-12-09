from app import app
from db import db

db.init_app(app)

# decorater that is executed first
# nahrazuje puvodni create scripty
# vytvoři db a všechny tabulky - musi byt importovany zde jinak je neuvidi
@app.before_first_request
def create_tables():
    db.create_all()
