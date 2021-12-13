# Поиск коллизий в хеше

# Коллизии - когда у разных данных один хеш
# - Если длина хеша меньше длина данных, то невозможно
#   создать хеш функцию которая не дает коллизий


from blockchain import blockchain
from hash import data_to_hash

block = 5
ammount = blockchain[block]['ammount']

# нужно сделать такойже хеш
expected_hash = blockchain[block+1]['prev_hash']


def simple_change_amount(blockchain, block, ammount):
  # простой поиск первой колизии
  x_hash = ""

  while x_hash != expected_hash:
    # до тех пор пока хеши не совпадают увеличиваем
    # кол-во денег в транзакции
    ammount += 1
    blockchain[block]['ammount'] = ammount

    # создание хеша с новыми значениями
    x_hash = data_to_hash(blockchain[block])
  
  return blockchain


def search_range_amount(min, max):
  # поиск совподений хеша в деапазоне значений суммы транзакции
  range_ammount = []
  for ammount in range(min, max):
    blockchain[block]['ammount'] = ammount
    
    # создание хеша с новыми значениями
    x_hash = data_to_hash(blockchain[block])

    # если хеш совпадает, то добавляем его в список совпадений
    if x_hash == expected_hash:
      range_ammount.append({
        "hash": x_hash,
        "ammount": ammount
      })
  return range_ammount
