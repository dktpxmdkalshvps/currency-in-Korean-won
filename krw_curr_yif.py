import yfinance as yf

def get_exchange_rates_yf():
    # Symbols mapping
    symbols = {
        "USD/KRW": "USDKRW=X",
        "EUR/KRW": "EURKRW=X",
        "JPY/KRW": "JPYKRW=X"
    }
    
    print(f"{'Currency':<12} | {'Rate (KRW)':<10}")
    print("-" * 30)

    for name, ticker_symbol in symbols.items():
        try:
            ticker = yf.Ticker(ticker_symbol)
            # Fetching the last price directly
            current_rate = ticker.fast_info['last_price']
            
            # Handling NaN or errors
            if current_rate is None or str(current_rate) == 'nan':
                hist = ticker.history(period="1d")
                current_rate = hist['Close'].iloc[-1]

            # Display Logic
            if "JPY" in name:
                # Multiply by 100 and label as 100¥
                print(f"{'JPY (100¥)':<12} | {current_rate * 100:,.2f}")
            else:
                print(f"{name:<12} | {current_rate:,.2f}")
                
        except Exception:
            print(f"{name:<12} | Error fetching data")

if __name__ == "__main__":
    get_exchange_rates_yf()