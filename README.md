# Semantic Memory Engine

Projeto pequeno para demonstração de um motor de memória semântica.

Requisitos (virtualenv recomendado):

```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Executar a API (FastAPI):

```bash
uvicorn main:app --reload
```

Executar CLI:

```bash
python run.py
```

Testes:

```bash
pip install -r requirements.txt
pytest --maxfail=1 -q
pytest --cov=app --cov-report=term-missing
```

Os testes usam `pytest` e `pytest-cov`.