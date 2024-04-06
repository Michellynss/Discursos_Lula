import requests
from bs4 import BeautifulSoup
import openai
from datetime import date, datetime, time, timedelta
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Credenciais OpenIA
chave_api = ""
openai.api_key = chave_api

# Credenciais Google Sheets
arquivo_credenciais = ""
conta = ServiceAccountCredentials.from_json_keyfile_name(arquivo_credenciais)
api = gspread.authorize(conta)
planilha = api.open_by_key("")
sheet = planilha.worksheet("Discursos")

# Raspagem dos discusos
result = requests.get("https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/discursos-e-pronunciamentos")
soup = BeautifulSoup(result.text)
titles = soup.find_all("h2", class_="tileHeadline")
for title in titles[:3]:
    # Extrai o texto do título
    title_text = title.a.text.strip()
    # Extrai o link
    link = title.a["href"]

     # Requisição para acessar os três primeiros links
    link_response = requests.get(link)
    link_html = link_response.text
    link_soup = BeautifulSoup(link_html, "html.parser")
    date_tag = link_soup.find("span", class_="value")
    main_paragraphs = link_soup.find_all("p", attrs={'class': None})
    main_text = "\n".join(paragraph.get_text().strip() for paragraph in main_paragraphs)
    
#Integração com a OpenAI
    prompt = "Considere que você é um jornalista e está escrevendo uma matéria sobre este discurso do Presidente da República: na primeira linha, escreva o macrotema a que o discurso se refere (exemplos: saúde, educação, direitos sociais, economia). Na segunda linha, faça um resumo do discurso de até 1500 caracteres e indique que é o resumo. Na terceira linha, analise o conteúdo e selecione, sem realizar alteração no texto, o trecho de maior relevância para uma matéria jornalística com um limite de 280 caracteres. Este trecho precisa ter relação com a temática principal do discurso. Responda somente com o trecho, não acrescente palavra ou justificativa. Indique que esse é o trecho mais importante"
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
                    {"role": "user", "content": f"{main_text}: {prompt}"}])

# Enviando as respostas para o Google Sheets
    presposta = (response['choices'][0]['message']['content'])
    sheet.append_row([title_text, link, resposta, date_tag])

    print(response['choices'][0]['message']['content'])
