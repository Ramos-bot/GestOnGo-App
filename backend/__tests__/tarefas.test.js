const request = require('supertest');
const app = require('../server');
const { _store } = require('../routes/tarefas');

beforeEach(() => _store.reset());

describe('Tarefas CRUD', () => {
    test('POST /api/tarefas cria tarefa', async () => {
        const res = await request(app).post('/api/tarefas').send({ clienteId: 1, descricao: 'Cortar relva' });
        expect(res.status).toBe(201);
        expect(res.body).toMatchObject({ id: 1, clienteId: 1, descricao: 'Cortar relva', feito: false });
    });

    test('GET /api/tarefas lista tarefas', async () => {
        await request(app).post('/api/tarefas').send({ clienteId: 1, descricao: 'A' });
        await request(app).post('/api/tarefas').send({ clienteId: 2, descricao: 'B' });
        const res = await request(app).get('/api/tarefas');
        expect(res.status).toBe(200);
        expect(res.body.length).toBe(2);
    });

    test('PUT /api/tarefas/:id atualiza tarefa', async () => {
        await request(app).post('/api/tarefas').send({ clienteId: 1, descricao: 'A' });
        const res = await request(app).put('/api/tarefas/1').send({ feito: true });
        expect(res.status).toBe(200);
        expect(res.body.feito).toBe(true);
    });

    test('DELETE /api/tarefas/:id remove tarefa', async () => {
        await request(app).post('/api/tarefas').send({ clienteId: 1, descricao: 'A' });
        const res = await request(app).delete('/api/tarefas/1');
        expect(res.status).toBe(204);
        const list = await request(app).get('/api/tarefas');
        expect(list.body.length).toBe(0);
    });
});
