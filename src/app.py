import os
import pandas as pd
import streamlit as st

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'bugsDataset.csv')

st.set_page_config(page_title="Portal de Bugs", page_icon="🐛")

st.title("🐛 Portal de Report de Bugs")
st.write("Ajude a mapear falhas no sistema. Os seus relatos alimentam e treinam a IA de triagem de QA.")

# formulário
with st.form("bug_form", clear_on_submit=True):
    titulo = st.text_input("Título do Bug", placeholder="Ex: Alteração de Senha")
    descricao = st.text_area("O que aconteceu?", placeholder="Descreva o passo a passo até o erro ocorrer... \nEx: Não consigo alterar minha senha, pois precisa da permissão do oraganizador da equipe")
    modulo = st.selectbox("Em qual módulo ocorreu?", ["Autenticação", "Checkout", "UI/UX", "Segurança", "Infraestrutura", "Performance", "Outro"])
    severidade = st.selectbox("Severidade percebida", ["Pendente de Análise", "Baixo", "Alta", "Crítico", "Segurança"])
    
    submit_button = st.form_submit_button("Enviar Relatório")
    
    if submit_button:
        if titulo.strip() == "" or descricao.strip() == "":
            st.error("ATENÇÃO! O título e a descrição são obrigatórios.")
        else:
            # cálculo do próximo ID
            df = pd.read_csv(DATA_PATH)
            novo_id = df['id'].max() + 1 if not df.empty else 1
            
            # cria a nova linha
            novo_bug = pd.DataFrame([{
                "id": novo_id,
                "titulo": titulo,
                "descricao": descricao,
                "modulo": modulo,
                "severidade": severidade
            }])
            
            # append
            novo_bug.to_csv(DATA_PATH, mode='a', header=False, index=False)
            
            st.success("Bug registado com sucesso! Obrigado pelo seu contributo para melhorar o sistema.")
st.write("Sua ajuda é uma grande contribuição para aprimorar a IA e enriquecer o Dataset deste projeto, com isso, você faz parte dele!")