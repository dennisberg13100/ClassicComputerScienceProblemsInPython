
#!/usr/bin/python3
from typing import Generator 

def fib(n:int) -> Generator[int, None, None]:
  yield 0
  if n > 0: yield 1
  last: int = 0
  next: int = 1
  for _ in range(1, n):
    # last = next e next = last + next 
    last, next = next, last + next
    yield next

if __name__ == "__main__": 
  # executa o codigo apenas se o programa for rodado diratamente
  # Não irá rodar caso este módulo seja importado 
  for i in (fib(50)):
    print(i)
  