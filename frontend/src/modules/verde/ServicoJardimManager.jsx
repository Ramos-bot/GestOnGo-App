/**
 * Componentes do Módulo Verde - Jardinagem
 * Gestão de serviços de jardinagem e manutenção de espaços verdes
 */

import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const ServicoJardimManager = ({ token }) => {
    const [servicos, setServicos] = useState([]);
    const [clientes, setClientes] = useState([]);
    const [novoServico, setNovoServico] = useState({
        data_servico: '',
        duracao_horas: 1,
        descricao: '',
        cliente_id: ''
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const headers = {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };

    // Carregar clientes e serviços ao inicializar
    useEffect(() => {
        if (token) {
            carregarClientes();
            carregarServicos();
        }
    }, [token]);

    const carregarClientes = async () => {
        try {
            const response = await axios.get(`${API_URL}/clientes`, { headers });
            setClientes(response.data);
        } catch (err) {
            setError('Erro ao carregar clientes');
        }
    };

    const carregarServicos = async () => {
        try {
            setLoading(true);
            const response = await axios.get(`${API_URL}/servicos-jardim`, { headers });
            setServicos(response.data);
        } catch (err) {
            setError('Erro ao carregar serviços de jardinagem');
        } finally {
            setLoading(false);
        }
    };

    const criarServico = async (e) => {
        e.preventDefault();
        try {
            setLoading(true);

            const servicoData = {
                ...novoServico,
                tipo: 'jardinagem',
                cliente_id: parseInt(novoServico.cliente_id)
            };

            await axios.post(`${API_URL}/servicos-jardim/`, servicoData, { headers });

            // Limpar formulário
            setNovoServico({
                data_servico: '',
                duracao_horas: 1,
                descricao: '',
                cliente_id: ''
            });

            // Recarregar lista
            carregarServicos();
            setError('');
        } catch (err) {
            setError(err.response?.data?.detail || 'Erro ao criar serviço');
        } finally {
            setLoading(false);
        }
    };

    const eliminarServico = async (id) => {
        if (!confirm('Tem certeza que deseja eliminar este serviço?')) return;

        try {
            await axios.delete(`${API_URL}/servicos-jardim/${id}`, { headers });
            carregarServicos();
        } catch (err) {
            setError('Erro ao eliminar serviço');
        }
    };

    return (
        <div className="servico-jardim-manager">
            <h2>🌿 Módulo Verde - Jardinagem</h2>

            {error && (
                <div className="error-message" style={{ color: 'red', marginBottom: '1rem' }}>
                    {error}
                </div>
            )}

            {/* Formulário de criação */}
            <form onSubmit={criarServico} style={{ marginBottom: '2rem', padding: '1rem', border: '1px solid #ddd', borderRadius: '8px' }}>
                <h3>Novo Serviço de Jardinagem</h3>

                <div style={{ marginBottom: '1rem' }}>
                    <label>Cliente:</label>
                    <select
                        value={novoServico.cliente_id}
                        onChange={(e) => setNovoServico({ ...novoServico, cliente_id: e.target.value })}
                        required
                        style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
                    >
                        <option value="">Seleccionar cliente...</option>
                        {clientes.map(cliente => (
                            <option key={cliente.id} value={cliente.id}>
                                {cliente.nome}
                            </option>
                        ))}
                    </select>
                </div>

                <div style={{ marginBottom: '1rem' }}>
                    <label>Data do Serviço:</label>
                    <input
                        type="date"
                        value={novoServico.data_servico}
                        onChange={(e) => setNovoServico({ ...novoServico, data_servico: e.target.value })}
                        required
                        style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
                    />
                </div>

                <div style={{ marginBottom: '1rem' }}>
                    <label>Duração (horas):</label>
                    <input
                        type="number"
                        min="1"
                        max="24"
                        value={novoServico.duracao_horas}
                        onChange={(e) => setNovoServico({ ...novoServico, duracao_horas: parseInt(e.target.value) })}
                        required
                        style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
                    />
                </div>

                <div style={{ marginBottom: '1rem' }}>
                    <label>Descrição:</label>
                    <textarea
                        value={novoServico.descricao}
                        onChange={(e) => setNovoServico({ ...novoServico, descricao: e.target.value })}
                        placeholder="Corte de relva, poda de arbustos..."
                        rows="3"
                        style={{ width: '100%', padding: '0.5rem', marginTop: '0.25rem' }}
                    />
                </div>

                <button type="submit" disabled={loading} style={{ padding: '0.5rem 1rem', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '4px' }}>
                    {loading ? 'A criar...' : 'Criar Serviço de Jardinagem'}
                </button>
            </form>

            {/* Lista de serviços */}
            <div>
                <h3>Serviços de Jardinagem</h3>
                {loading ? (
                    <p>A carregar...</p>
                ) : servicos.length === 0 ? (
                    <p>Nenhum serviço de jardinagem registado.</p>
                ) : (
                    <div style={{ display: 'grid', gap: '1rem' }}>
                        {servicos.map(servico => (
                            <div key={servico.id} style={{ padding: '1rem', border: '1px solid #ddd', borderRadius: '8px', backgroundColor: '#f9f9f9' }}>
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <div>
                                        <h4 style={{ margin: '0 0 0.5rem 0', color: '#4CAF50' }}>
                                            🌿 Jardinagem - {new Date(servico.data_servico).toLocaleDateString('pt-PT')}
                                        </h4>
                                        <p><strong>Cliente:</strong> {clientes.find(c => c.id === servico.cliente_id)?.nome || `ID: ${servico.cliente_id}`}</p>
                                        <p><strong>Duração:</strong> {servico.duracao_horas} hora(s)</p>
                                        {servico.descricao && <p><strong>Descrição:</strong> {servico.descricao}</p>}
                                    </div>
                                    <button
                                        onClick={() => eliminarServico(servico.id)}
                                        style={{ padding: '0.25rem 0.5rem', backgroundColor: '#f44336', color: 'white', border: 'none', borderRadius: '4px' }}
                                    >
                                        Eliminar
                                    </button>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default ServicoJardimManager;
