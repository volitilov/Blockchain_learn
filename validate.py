# Валидация (проверка) целостности блокчейна

def validate_blockchain(blockchain, data_to_hash):
  # blockchain: блокчейн (реестр) данных
  # data_to_hash: функция хеширования данных

  prev_block = None

  for block in blockchain:
    if prev_block:
      # сверка хешей начиная со второго блока
      
      # считаем хеш предыдущего блока
      actual_prev_hash = data_to_hash(prev_block)

      # получаем записанный хеш в блоке
      recorded_prev_hash = block['prev_hash']

      if recorded_prev_hash != actual_prev_hash:
        print(f"Blockchain is invalid, expected - {recorded_prev_hash}, actual - {actual_prev_hash}")
      else:
        print(f"Valid hash: {actual_prev_hash}")
