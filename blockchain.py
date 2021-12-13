# Блокчейн

from . import data_to_hash

blockchain = [
  { # genesis (первая запись для предыдущего хеша)
    "from": "Bob",    # кто отправил
    "to": "Sam",      # кому отправил
    "amount": 0.0     # сколько отправил
  }
]


# функция добавления записи (блока) в блокчейн
def addNewBlock(account_from, account_to, amount):
  prev_block = blockchain[-1] # последний блок в блокчейне
  prev_hash = data_to_hash(prev_block)

  block = {
    "from": account_from,
    "to": account_to,
    "amount": amount,
    "prev_hash": prev_hash
  }
  blockchain.append(block)

# @deeplogger
