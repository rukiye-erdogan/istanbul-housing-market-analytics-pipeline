import requests


def get_exchange_rates():

    try:
        url = "https://open.er-api.com/v6/latest/TRY"

        response = requests.get(url, timeout=10)
        data = response.json()

        print(data)
        
        usd_rate = data["rates"]["USD"]
        eur_rate = data["rates"]["EUR"]

        return {
            "USDTRY": round(1 / usd_rate, 2),
            "EURTRY": round(1 / eur_rate, 2)
        }

    except Exception as e:

        print(f"FX API error: {e}")

        return {
            "USDTRY": 39.0,
            "EURTRY": 44.0
        }