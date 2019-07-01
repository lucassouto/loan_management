# Loan Management API

## Rodando localmente

Assumindo que tenha docker e docker-compose instalados.


Subir API:

```shell
make up-local
```

Criar super usuário:

```bash
make createsuperuser
```

## Testes:

Rode o [Tox](https://tox.readthedocs.io/en/latest/) para os testes e checagem de código:

```bash
tox
```

Pode ser que seja preciso excluir arquivos pré compilados do Python antes dos testes e executar como `sudo`:

```bash
make clean
```

## Documentação da API
[Documentação](https://onidata-loan-management.herokuapp.com/api/v1/docs/)
