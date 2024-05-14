# PLAYGROUND

템플릿 프로젝트입니다.

## 실행정보

```bash
make build
make up
make down
```

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
