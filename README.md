## Análise dos discursos do presidente Lula
Projeto final da disciplina de Machine Learning do Master em Jornalismo de Dados do Insper.

Neste trabalho, usamos a API da OpenAI para analisar os discursos do presidente Lula.

### Bibliotecas
- [openia](https://platform.openai.com/docs/libraries/python-library)
     > $ pip install openai
     
- [gspread](https://docs.gspread.org/en/v6.0.0/)
    > $ pip install gspread oauth2client
    
- [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [datetime](https://docs.python.org/3/library/datetime.html)

### Descrição
Na primeira parte, uilizamos as bibliotecas Requests e BeautifulSoup para fazer a raspagem dos discursos no [site do Planalto](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos-e-pronunciamentos).

Usamos a API da OpenAi para destacar a frase mais impactante do discurso, identificar o macrotema e gerar um resumo. 

Utilizando a API do Google Sheets, armazenamos os dados obtidos.  

