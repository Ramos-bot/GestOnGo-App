const express = require('express');
const router = express.Router();

let seq = 1;
const tarefas = new Map(); // id -> { id, clienteId, descricao, data, feito }

function toArray() {
    return Array.from(tarefas.values());
}

// Create
router.post('/', (req, res) => {
    const { clienteId, descricao, data, feito = false } = req.body || {};
    if (!clienteId || !descricao) return res.status(400).json({ error: 'clienteId e descricao são obrigatórios' });
    const id = seq++;
    const nova = { id, clienteId, descricao, data: data || null, feito: Boolean(feito) };
    tarefas.set(id, nova);
    res.status(201).json(nova);
});

// Read all
router.get('/', (_req, res) => res.json(toArray()));

// Read one
router.get('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!tarefas.has(id)) return res.status(404).json({ error: 'Tarefa não encontrada' });
    res.json(tarefas.get(id));
});

// Update
router.put('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!tarefas.has(id)) return res.status(404).json({ error: 'Tarefa não encontrada' });
    const atual = tarefas.get(id);
    const { clienteId, descricao, data, feito } = req.body || {};
    const atualizada = {
        ...atual,
        ...(clienteId !== undefined ? { clienteId } : {}),
        ...(descricao !== undefined ? { descricao } : {}),
        ...(data !== undefined ? { data } : {}),
        ...(feito !== undefined ? { feito: Boolean(feito) } : {})
    };
    tarefas.set(id, atualizada);
    res.json(atualizada);
});

// Delete
router.delete('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!tarefas.has(id)) return res.status(404).json({ error: 'Tarefa não encontrada' });
    tarefas.delete(id);
    res.status(204).end();
});

module.exports = { router, _store: { tarefas, reset: () => { tarefas.clear(); seq = 1; } } };
