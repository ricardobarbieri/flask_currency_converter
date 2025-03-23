from flask import Flask, render_template, request
import requests
import os
from http import HTTPStatus

app = Flask(__name__)

# Configuração da API
API_KEY = os.getenv("API_KEY", "*********************************")  # Chave padrão se não houver variável de ambiente
API_URL = "https://api.currencyapi.com/v3/latest"
TIMEOUT = 10  # Tempo limite para requisições em segundos

# Função para obter lista de moedas disponíveis
def get_available_currencies():
    try:
        params = {"apikey": API_KEY}
        response = requests.get(f"{API_URL}", params=params, timeout=TIMEOUT)
        response.raise_for_status()  # Levanta exceção para erros HTTP
        data = response.json()
        return sorted(data["data"].keys())  # Retorna lista ordenada de códigos de moedas
    except requests.RequestException as e:
        print(f"Erro ao obter moedas: {e}")
        return ["USD", "EUR", "BRL", "GBP", "JPY", "AUD"]  # Lista padrão em caso de falha

# Lista inicial de moedas (será atualizada pela API)
MOEDAS = get_available_currencies()

@app.route("/", methods=["GET", "POST"])
def conversor():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            # Obtém os dados do formulário
            valor = float(request.form["valor"])
            moeda_origem = request.form["moeda_origem"]
            moeda_destino = request.form["moeda_destino"]

            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")

            # Requisição à API
            params = {
                "apikey": API_KEY,
                "base_currency": moeda_origem
            }
            response = requests.get(API_URL, params=params, timeout=TIMEOUT)
            response.raise_for_status()  # Levanta exceção para erros HTTP

            dados = response.json()
            taxas = dados.get("data", {})

            if moeda_destino not in taxas:
                raise KeyError(f"Moeda de destino '{moeda_destino}' não disponível.")

            taxa = taxas[moeda_destino]["value"]
            resultado_valor = valor * taxa
            resultado = f"{resultado_valor:.2f} {moeda_destino}"

        except ValueError as ve:
            erro = str(ve) if "negativo" in str(ve) else "Por favor, insira um valor numérico válido."
        except KeyError as ke:
            erro = str(ke)
        except requests.RequestException as re:
            erro = f"Erro na API: {re}. Tente novamente mais tarde."
        except Exception as e:
            erro = f"Erro inesperado: {e}. Contate o suporte."

    return render_template(
        "index.html",
        moedas=MOEDAS,
        resultado=resultado,
        erro=erro
    )

if __name__ == "__main__":
    # Modo debug apenas para desenvolvimento
    app.run(debug=True, host="0.0.0.0", port=5000)