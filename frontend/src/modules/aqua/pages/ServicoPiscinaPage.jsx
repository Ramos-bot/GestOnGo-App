/**
 * Página de Serviços de Piscinas - Módulo Aqua
 * Gestão completa de serviços de piscinas
 */

import React, { useState, useEffect } from 'react';
import { apiClient } from '../../../app/api';

const ServicoPiscinaPage = () => {
    const [servicos, setServicos] = useState([]);
    const [clientes, setClientes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState('');
    const [showForm, setShowForm] = useState(false);

    const tiposServico = [
        'Limpeza de Piscina',
        'Tratamento Químico',
        'Manutenção de Equipamentos',
        'Análise de pH',
        'Troca de Filtros',
        'Reparação de Bomba',
        'Limpeza de Azulejos',
        'Manutenção Geral'
    ];

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        try {
            setLoading(true);
            const [servicosData, clientesData] = await Promise.all([
                apiClient.getServicosPiscina(),
                apiClient.getClientes()
            ]);
            setServicos(servicosData);
            setClientes(clientesData);
        } catch (err) {
            setError('Erro ao carregar dados');
        } finally {
            setLoading(false);
        }
    };

    if (loading) {
        return (
            <div className="page-container">
                <div className="loading">🏊 A carregar serviços de piscinas...</div>
            </div>
        );
    }

    return (
        <div className="page-container">
            <div className="page-header">
                <h1>🏊 Serviços de Piscinas</h1>
                <button
                    onClick={() => setShowForm(true)}
                    className="btn btn-primary"
                >
                    + Novo Serviço
                </button>
            </div>

            {error && (
                <div className="error-message">
                    {error}
                </div>
            )}

            <div className="servicos-grid">
                {servicos.length === 0 ? (
                    <div className="empty-state">
                        <p>🏊 Nenhum serviço de piscina encontrado</p>
                        <button onClick={() => setShowForm(true)} className="btn btn-primary">
                            Criar primeiro serviço
                        </button>
                    </div>
                ) : (
                    <div className="coming-soon">
                        <h2>🚧 Em Desenvolvimento</h2>
                        <p>Módulo Aqua será completado na próxima fase</p>
                        <div className="features-list">
                            <h3>Funcionalidades Previstas:</h3>
                            <ul>
                                <li>🧪 Análise química da água</li>
                                <li>📊 Relatórios de qualidade</li>
                                <li>🔧 Gestão de equipamentos</li>
                                <li>📅 Agendamento de manutenções</li>
                                <li>💧 Controlo de pH e cloro</li>
                            </ul>
                        </div>
                    </div>
                )}
            </div>

            <style jsx>{`
        .page-container {
          padding: 2rem;
          max-width: 1200px;
          margin: 0 auto;
        }

        .page-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 2rem;
        }

        .page-header h1 {
          margin: 0;
          color: #17a2b8;
        }

        .loading {
          text-align: center;
          padding: 4rem;
          color: #666;
          font-size: 1.1rem;
        }

        .error-message {
          background: #fee;
          color: #c33;
          padding: 1rem;
          border-radius: 6px;
          margin-bottom: 1rem;
          border: 1px solid #fcc;
        }

        .btn {
          padding: 0.5rem 1rem;
          border: none;
          border-radius: 6px;
          cursor: pointer;
          font-size: 0.9rem;
          transition: all 0.2s ease;
        }

        .btn-primary {
          background: #17a2b8;
          color: white;
        }

        .btn-primary:hover {
          background: #138496;
        }

        .empty-state {
          text-align: center;
          padding: 4rem;
          grid-column: 1 / -1;
        }

        .coming-soon {
          text-align: center;
          padding: 4rem;
          background: white;
          border-radius: 12px;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          border-left: 4px solid #17a2b8;
        }

        .coming-soon h2 {
          color: #17a2b8;
          margin-bottom: 1rem;
        }

        .features-list {
          margin-top: 2rem;
          text-align: left;
          max-width: 500px;
          margin-left: auto;
          margin-right: auto;
        }

        .features-list h3 {
          color: #333;
          margin-bottom: 1rem;
        }

        .features-list ul {
          list-style: none;
          padding: 0;
        }

        .features-list li {
          padding: 0.5rem 0;
          border-bottom: 1px solid #e1e5e9;
        }

        .features-list li:last-child {
          border-bottom: none;
        }
      `}</style>
        </div>
    );
};

export default ServicoPiscinaPage;
