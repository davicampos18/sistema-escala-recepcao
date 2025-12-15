# 📅 Sistema de Gestão de Escalas - Recepção

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)

> Sistema web desenvolvido para automatizar a visualização de escalas de voluntários da recepção na Assembleia de Deus em Rodovia A, integrando Python (Flask) diretamente com Google Sheets API para gestão de dados em tempo real.

## 💡 O Problema e a Solução

**O Problema:** A gestão de escalas de recepção era feita manualmente e o compartilhamento de arquivos estáticos (PDF/Imagens) dificultava atualizações rápidas quando havia trocas de turno.

**A Solução:** Desenvolvi uma aplicação web onde o administrador apenas edita uma **Planilha Google** simples. O sistema consome esses dados via API e gera uma interface web responsiva e amigável para os voluntários da recepção.
- **CMS Headless:** A planilha do Google funciona como um painel administrativo.
- **Updates em Tempo Real:** Alterou na planilha, atualizou no site.

## 🛠️ Tecnologias Utilizadas

* **Back-end:** Python 3, Flask (Framework Web).
* **Database/Integração:** Google Sheets API (via biblioteca `gspread`).
* **Front-end:** HTML5, CSS3, Bootstrap 5 (Responsivo).
* **Segurança:** Gerenciamento de credenciais via Variáveis de Ambiente (OAuth2).
* **Deploy:** Vercel (Serverless Functions) / Fly.io.

## ⚙️ Funcionalidades Técnicas

1.  **Filtragem de Dados:** O Back-end processa os dados brutos da planilha e os organiza logicamente por trimestres e meses antes de enviar ao Front-end.
2.  **Tratamento de Erros:** O sistema lida com formatações de data e células vazias para evitar quebras na renderização.
3.  **Arquitetura Serverless:** Configurado para rodar em arquitetura serverless utilizando `vercel.json` para roteamento de requisições Python.

## 🚀 Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone (https://github.com/davicampos18/sistema-escala-recepcao.git)
   ````

2. Instale as dependências:
   ````bash
   pip install -r requirements.txt
   ````
3. Configuração da API do Google:
   - Crie um projeto no Google Cloud Console.
   - Ative a API do Google Sheets e Google Drive.
   - Baixe as credenciais (credentials.json) e configure no .env ou nas variáveis de ambiente.

4. Execute a aplicação:
   ````bash
   flask run
   ````

📄 Estrutura do Projeto
````bash
/api
 └── index.py       # Lógica do Backend e Rotas Flask
/templates
 └── escala.html    # Front-end com Jinja2 e Bootstrap
requirements.txt    # Dependências do Python
vercel.json         # Configuração de Deploy
````


## 🖼️ Preview do Projeto

<img src="https://github.com/user-attachments/assets/f55b82ff-13cc-44f5-a8e9-4b42a6856899" alt="Preview da Escala" width="100%">
