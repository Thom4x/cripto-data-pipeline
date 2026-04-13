from src.extract import fetch_crypto_data
import os

def run_pipeline(coin_id="bitcoin"):
    print(f"--- Iniciando Pipeline para: {coin_id.upper()} ---")
    
    # 1. EXTRACCIÓN
    raw_data = fetch_crypto_data(coin_id)
    if not raw_data:
        print("Error en la extracción.")
        return
    
    print("Extracción completada...")

if __name__ == "__main__":
    run_pipeline("bitcoin")