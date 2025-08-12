const request = require('supertest');
const app = require('../server');
const { _store } = require('../routes/clientes');

beforeEach(() => _store.reset());

describe('Clientes CRUD', () => {
  test('POST /api/clientes cria cliente', async () => {
    const res = await request(app).post('/api/clientes').send({ nome: 'Dona Adelaide', telefone: '912345678' });
    expect(res.status).toBe(201);
    expect(res.body).toMatchObject({ id: 1, nome: 'Dona Adelaide', telefone: '912345678', ativo: true });
  });

  test('GET /api/clientes lista clientes', async () => {
    await request(app).post('/api/clientes').send({ nome: 'A' });
    await request(app).post('/api/clientes').send({ nome: 'B' });
    const res = await request(app).get('/api/clientes');
    expect(res.status).toBe(200);
    expect(res.body.length).toBe(2);
  });

  test('PUT /api/clientes/:id atualiza cliente', async () => {
    await request(app).post('/api/clientes').send({ nome: 'X' });
    const res = await request(app).put('/api/clientes/1').send({ nome: 'Y', ativo: false });
    expect(res.status).toBe(200);
    expect(res.body).toMatchObject({ id: 1, nome: 'Y', ativo: false });
  });

  test('DELETE /api/clientes/:id remove cliente', async () => {
    await request(app).post('/api/clientes').send({ nome: 'X' });
    const res = await request(app).delete('/api/clientes/1');
    expect(res.status).toBe(204);
    const list = await request(app).get('/api/clientes');
    expect(list.body.length).toBe(0);
  });
});
