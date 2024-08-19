#Problema 01

import requests
#Creamos la funcion para obtener el precio de bitcoin en tiempo real según la página
def funcion_precio_bitcoin():
    try:
        salida = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        salida.raise_for_status()
        data = salida.json()
        precio_usd = data['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Error al conectar con la API:", e)
        return None

# La siguiente función nos hace la converción del bitcoin a dolares estadounidenses
def calcular_valor_bitcoins(bitcoins, precio_usd):
    return bitcoins * precio_usd

#La siguiente función realiza el llamado a la funcion "funcion_precio_bitcoin" creado
def main():
    try:
        n = float(input("Por favor, ingrese la cantidad bitcoins que posee o quiera convertir: "))
        precio_usd = funcion_precio_bitcoin()
        if precio_usd is not None:
            valor_total = calcular_valor_bitcoins(n, precio_usd)
            print(f"El valor de {n} Bitcoins en dólares americanos es: ${valor_total:,.4f}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()