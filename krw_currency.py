import requests
api_key = ' '

def get_my_exchange_rates(api_key):
    # We use KRW as the base to get all rates relative to the Won
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/KRW"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("result") == "success":
            rates = data["conversion_rates"]
            
            # The API gives: 1 KRW = X Currency. 
            # We want: 1 Currency = X KRW (Inversion)
            usd_krw = 1 / rates["USD"]
            eur_krw = 1 / rates["EUR"]
            jpy_krw = (1 / rates["JPY"]) * 100 # Standard quote is for 100 Yen
            
            print(f"--- Updated Rates ({data['time_last_update_utc'][:16]}) ---")
            print(f"USD💵 to KRW: {usd_krw:,.2f} 원")
            print(f"EUR💷 to KRW: {eur_krw:,.2f} 원")
            print(f"JPY💴 to KRW: {jpy_krw:,.2f} 원 (per 100¥)")
        else:
            print("API Error:", data.get("error-type", "Unknown error"))
            
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    # Your provided API Key
    MY_API_KEY =""
    get_my_exchange_rates(MY_API_KEY)