# Operator precedence parser
Easy operator precedence parser written by python.

## Sample
```commandline
paraches$ python main.py
exp > 1+2+3;
push ('constant', '1', 'int')
push ('constant', '2', 'int')
arithmetic ('add',)
push ('constant', '3', 'int')
arithmetic ('add',)

exp > 1+2*3;
push ('constant', '1', 'int')
push ('constant', '2', 'int')
push ('constant', '3', 'int')
arithmetic ('call Math.multiply 2',)
arithmetic ('add',)

exp > (1+2)*3;
push ('constant', '1', 'int')
push ('constant', '2', 'int')
arithmetic ('add',)
push ('constant', '3', 'int')
arithmetic ('call Math.multiply 2',)
```
## Environment
- python 3.8
- iMac 2019
- macOS 10.15.7

## Note
https://zenn.dev/paraches/articles/prioritized_expression