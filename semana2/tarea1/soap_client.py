from zeep import Client

client = Client('http://localhost:8000')
result = client.service.SumaDosNumeros(num1= 2, num2 = 4)
print(result)

result = client.service.CadenaPalindromo(cadena = "radar")
print(result)