# 각 디렉터리 구성을 위해 사용된 스크립트

## api

```bash
poetry add fastapi orjson aiohttp pydantic pydantic-settings motor uvicorn async-lru
poetry add isort black --group dev
poetry run uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers ${WORKERS}
```

## web

```bash
nvm use v20
npm create svelte@latest web
cd web
npm i -D autoprefixer postcss tailwindcss
npm run dev -- --port 5173 --host
```
