# простой пример создание хеша данных с помощью sha256
# и усложением создания хеша с помощью алгоритма консенсуса
# Proof Of Work

import hashlib
import json
from proof_of_work import mine_proof_of_work

account = {
  "name": "Bob",
  "balance": 31845,
  "created": "12-03-2000"
}


def data_to_hash(data):
  # майним (ищем) proof-значение, для получения хеша с
  # доказательством работы
  proof = mine_proof_of_work(data)

  # добавляем proof-значение 
  data['proof'] = proof

  # преобразование в строку
  str_data = json.dumps(data, sort_keys=True)

  # преобразование строки в бинарные данные
  binary_data = str_data.encode()

  # создание хеша данных
  data_hash = hashlib.sha256(binary_data).hexdigest()
  return data_hash 

# на вход любые данные например account
account_hash = data_to_hash(account)


# @deeplogger
