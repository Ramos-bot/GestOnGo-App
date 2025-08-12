# GestOnGo Frontend (CRA)

## Scripts
- `npm start` — dev server em `http://localhost:3000`
- `npm test` — Jest (usa `--watchAll=false` no CI)
- `npm run build` — build de produção em `build/`
- `npm run lint` — ESLint

## Estrutura
```
frontend/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── index.js
│   ├── index.css
│   ├── App.test.js
│   └── setupTests.js
```

## Notas
- Projeto criado para `react-scripts@5`. Node 20+.
- Para deploy no Firebase, `firebase.json` aponta para `build/`.
