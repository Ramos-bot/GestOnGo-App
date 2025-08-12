const express = require('express');
const router = express.Router();

// Base de dados em memória (trocaremos por BD real depois)
let seq = 1;
const clientes = new Map(); // id -> { id, nome, email, telefone, localidade, ativo }

function toArray() {
    return Array.from(clientes.values());
}

// Create
router.post('/', (req, res) => {
    const { nome, email = '', telefone = '', localidade = '', ativo = true } = req.body || {};
    if (!nome || typeof nome !== 'string') return res.status(400).json({ error: 'Campo "nome" é obrigatório' });
    const id = seq++;
    const novo = { id, nome, email, telefone, localidade, ativo: Boolean(ativo) };
    clientes.set(id, novo);
    res.status(201).json(novo);
});

// Read all
router.get('/', (_req, res) => res.json(toArray()));

// Read one
router.get('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!clientes.has(id)) return res.status(404).json({ error: 'Cliente não encontrado' });
    res.json(clientes.get(id));
});

// Update
router.put('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!clientes.has(id)) return res.status(404).json({ error: 'Cliente não encontrado' });
    const current = clientes.get(id);
    const { nome, email, telefone, localidade, ativo } = req.body || {};
    const updated = {
        ...current,
        ...(nome !== undefined ? { nome } : {}),
        ...(email !== undefined ? { email } : {}),
        ...(telefone !== undefined ? { telefone } : {}),
        ...(localidade !== undefined ? { localidade } : {}),
        ...(ativo !== undefined ? { ativo: Boolean(ativo) } : {})
    };
    clientes.set(id, updated);
    res.json(updated);
});

// Delete
router.delete('/:id', (req, res) => {
    const id = Number(req.params.id);
    if (!clientes.has(id)) return res.status(404).json({ error: 'Cliente não encontrado' });
    clientes.delete(id);
    res.status(204).end();
});

module.exports = { router, _store: { clientes, reset: () => { clientes.clear(); seq = 1; } } };
