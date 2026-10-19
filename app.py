import os
import streamlit as st

st.set_page_config(page_title="Assistente da Secretaria")

st.title("Assistente da Secretaria Acadêmica")

pergunta = st.text_input("Digite sua pergunta:")

if pergunta:

    pergunta = pergunta.lower()

    resposta = None

    arquivos = {
        "matricula": "documentos/matricula.txt",
        "transferencia": "documentos/transferencia.txt",
        "cancelamento": "documentos/cancelamento.txt",
        "atendimento": "documentos/atendimento.txt"
    }

    if "matrícula" in pergunta or "matricula" in pergunta:
        arquivo = arquivos["matricula"]

    elif "transferência" in pergunta or "transferencia" in pergunta:
        arquivo = arquivos["transferencia"]

    elif "cancelamento" in pergunta:
        arquivo = arquivos["cancelamento"]

    elif "atendimento" in pergunta or "horário" in pergunta or "horario" in pergunta:
        arquivo = arquivos["atendimento"]

    else:
        arquivo = None

    if arquivo:
        with open(arquivo, "r", encoding="utf-8") as f:
            resposta = f.read()

        st.success(resposta)

        st.info(
            "Resposta obtida a partir da base de conhecimento da secretaria acadêmica."
        )

    else:
        st.warning(
            "Não encontrei essa informação na base de conhecimento."
        )