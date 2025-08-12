const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/health', (_req, res) => res.json({ ok: true }));

// Clientes
const { router: clientesRouter } = require('./routes/clientes');
app.use('/api/clientes', clientesRouter);

// Exporta app para testes e arranque condicional
module.exports = app;

if (require.main === module) {
    const PORT = process.env.PORT || 8000;
    app.listen(PORT, () => console.log(`API on :${PORT}`));
}