from flask import Flask, render_template, request
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os
import json

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds_json = os.getenv("GOOGLE_CREDENTIALS")
creds_dict = json.loads(creds_json)

credentials = Credentials.from_service_account_info(
    creds_dict,
    scopes=SCOPES
)

gc = gspread.authorize(credentials)
spreadsheet = gc.open("Escala da Recepção")

app = Flask(__name__)

meses_pt = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
    7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
}

class Pesquisas_escala():
    def __init__(self, planilha):      
        try:
            self.planilha = spreadsheet.worksheet(planilha)
        except gspread.exceptions.WorksheetNotFound:
            raise ValueError(f"Planilha '{planilha}' não encontrada. Verifique o nome.")

    def get_escala(self):
        return self.planilha.get_all_records()

    def separar_por_mes(self, escala):
        fevereiro =[]
        marco = []
        abril = []
        maio = []
        junho = []
        julho = []
        agosto = []
        setembro = []
        outubro = []
        novembro = []
        dezembro = []

        for row in escala:
            try:
                mes = datetime.strptime(row['Data'], '%d/%m').month
                if mes in [2]:
                    fevereiro.append(row)
                elif mes in [3]:
                    marco.append(row)
                elif mes in [4]:
                    abril.append(row)
                elif mes in [5]:
                    maio.append(row)
                elif mes in [6]:
                    junho.append(row)
                elif mes in [7]:
                    julho.append(row)
                elif mes in [8]:
                    agosto.append(row)
                elif mes in [9]:
                    setembro.append(row)
                elif mes in [10]:
                    outubro.append(row)
                elif mes in [11]:
                    novembro.append(row)
                elif mes in [12]:
                    dezembro.append(row)
            except ValueError:
                continue

        return fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro



@app.route("/")
def escala():
    pesquisa = Pesquisas_escala("Escala")
    
    resultado = pesquisa.get_escala()

    fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro = pesquisa.separar_por_mes(resultado)

    return render_template(
        "escala.html",
        fevereiro=fevereiro,
        marco=marco,
        abril=abril,
        maio=maio,
        junho=junho,
        julho=julho,
        agosto=agosto,
        setembro=setembro,
        outubro=outubro,
        novembro=novembro,
        dezembro=dezembro,
        year=datetime.now().year,
    )

if __name__ == "__main__":
    app.run(debug=True)


