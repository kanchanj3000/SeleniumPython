import requests

str_name = requests.get("http://www.pythonforbeginners.com/requests/using-requests-in-python")
k = str_name.content
print k