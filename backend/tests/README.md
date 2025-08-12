# Tests para o Backend GestOnGo

Este diretório contém os testes automatizados para o backend FastAPI.

## Estrutura:
- `test_api.py` - Testes da API principal
- `test_modules.py` - Testes dos módulos (aqua, verde, phyto)
- `conftest.py` - Configurações e fixtures do pytest

## Executar testes:
```bash
# Todos os testes
pytest

# Com verbosidade
pytest -v

# Com coverage
pytest --cov=.

# Testes específicos
pytest tests/test_api.py
```
