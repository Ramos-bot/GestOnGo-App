/**
 * API Client configurado para GestOnGo
 * Axios com baseURL e interceptors para autenticação JWT
 */

import axios from 'axios';

// Configuração base da API
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Criar instância axios configurada
export const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para adicionar token JWT automaticamente
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para lidar com respostas e erros
api.interceptors.response.use(
  (response) => response,
  (error) => {
    // Se receber 401, remover token e redirecionar para login
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }

    // Formatar mensagens de erro em PT-PT
    if (error.response?.data?.detail) {
      error.message = error.response.data.detail;
    }

    return Promise.reject(error);
  }
);

// Funções auxiliares para chamadas comuns
export const apiClient = {
  // Utilizadores
  async login(email: string, password: string) {
    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);

    const response = await api.post('/utilizadores/login', formData);
    return response.data;
  },

  async getCurrentUser() {
    const response = await api.get('/utilizadores/me');
    return response.data;
  },

  // Clientes
  async getClientes(offset = 0, limit = 50) {
    const response = await api.get(`/clientes?offset=${offset}&limit=${limit}`);
    return response.data;
  },

  async createCliente(cliente: any) {
    const response = await api.post('/clientes/', cliente);
    return response.data;
  },

  async updateCliente(id: number, cliente: any) {
    const response = await api.put(`/clientes/${id}`, cliente);
    return response.data;
  },

  async deleteCliente(id: number) {
    await api.delete(`/clientes/${id}`);
  },

  // Serviços de Jardinagem (Módulo Verde)
  async getServicosJardim(offset = 0, limit = 50, cliente_id?: number) {
    let url = `/servicos-jardim?offset=${offset}&limit=${limit}`;
    if (cliente_id) url += `&cliente_id=${cliente_id}`;

    const response = await api.get(url);
    return response.data;
  },

  async createServicoJardim(servico: any) {
    const response = await api.post('/servicos-jardim/', servico);
    return response.data;
  },

  async updateServicoJardim(id: number, servico: any) {
    const response = await api.put(`/servicos-jardim/${id}`, servico);
    return response.data;
  },

  async deleteServicoJardim(id: number) {
    await api.delete(`/servicos-jardim/${id}`);
  },

  // Serviços de Piscina (Módulo Aqua)
  async getServicosPiscina(offset = 0, limit = 50, cliente_id?: number) {
    let url = `/servicos-piscina?offset=${offset}&limit=${limit}`;
    if (cliente_id) url += `&cliente_id=${cliente_id}`;

    const response = await api.get(url);
    return response.data;
  },

  async createServicoPiscina(servico: any) {
    const response = await api.post('/servicos-piscina/', servico);
    return response.data;
  },

  async updateServicoPiscina(id: number, servico: any) {
    const response = await api.put(`/servicos-piscina/${id}`, servico);
    return response.data;
  },

  async deleteServicoPiscina(id: number) {
    await api.delete(`/servicos-piscina/${id}`);
  },

  // Sistema
  async getSystemInfo() {
    const response = await api.get('/');
    return response.data;
  },

  async getHealthCheck() {
    const response = await api.get('/health');
    return response.data;
  },
};

export default api;
