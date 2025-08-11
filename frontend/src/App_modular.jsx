/**
 * GestOnGo - Aplicação principal com arquitectura modular
 * Sistema de gestão de serviços de campo com módulos Verde e Aqua
 */

import React, { useState } from 'react';
import LoginForm from './components/LoginForm';
import ClienteManager from './components/ClienteManager';

// Importar módulos (podem ser comentados para desativar)
import ServicoJardimManager from './modules/verde/ServicoJardimManager';
import ServicoPiscinaManager from './modules/aqua/ServicoPiscinaManager';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

function App() {
    const [token, setToken] = useState(localStorage.getItem('token'));
    const [activeTab, setActiveTab] = useState('clientes');
    const [systemInfo, setSystemInfo] = useState(null);

    const handleLogin = (newToken) => {
        localStorage.setItem('token', newToken);
        setToken(newToken);

        // Carregar informações do sistema
        fetch(`${API_URL}/`)
            .then(res => res.json())
            .then(data => setSystemInfo(data))
            .catch(err => console.error('Erro ao carregar info do sistema:', err));
    };

    const handleLogout = () => {
        localStorage.removeItem('token');
        setToken(null);
        setSystemInfo(null);
        setActiveTab('clientes');
    };

    // Verificar quais módulos estão disponíveis
    const modulosDisponiveis = {
        verde: true,  // Módulo Verde (Jardinagem) - comentar esta linha para desativar
        aqua: true,   // Módulo Aqua (Piscinas) - comentar esta linha para desativar
    };

    if (!token) {
        return (
            <div style={{
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                minHeight: '100vh',
                backgroundColor: '#f5f5f5'
            }}>
                <div style={{
                    backgroundColor: 'white',
                    padding: '2rem',
                    borderRadius: '8px',
                    boxShadow: '0 2px 10px rgba(0,0,0,0.1)'
                }}>
                    <h1 style={{ textAlign: 'center', color: '#333', marginBottom: '2rem' }}>
                        🌿 GestOnGo 🏊
                    </h1>
                    <p style={{ textAlign: 'center', color: '#666', marginBottom: '2rem' }}>
                        Sistema Modular de Gestão de Serviços de Campo
                    </p>
                    <LoginForm onLogin={handleLogin} />
                </div>
            </div>
        );
    }

    return (
        <div style={{ minHeight: '100vh', backgroundColor: '#f5f5f5' }}>
            {/* Header */}
            <header style={{
                backgroundColor: '#2c3e50',
                color: 'white',
                padding: '1rem 2rem',
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center'
            }}>
                <div>
                    <h1 style={{ margin: 0 }}>GestOnGo v{systemInfo?.versao || '2.0'}</h1>
                    <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.9rem', opacity: 0.8 }}>
                        {systemInfo?.descricao || 'Sistema Modular de Gestão de Serviços'}
                    </p>
                </div>
                <button
                    onClick={handleLogout}
                    style={{
                        padding: '0.5rem 1rem',
                        backgroundColor: '#e74c3c',
                        color: 'white',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer'
                    }}
                >
                    Sair
                </button>
            </header>

            {/* Navigation */}
            <nav style={{
                backgroundColor: '#34495e',
                padding: '0 2rem',
                display: 'flex',
                gap: '1rem'
            }}>
                <button
                    onClick={() => setActiveTab('clientes')}
                    style={{
                        padding: '1rem',
                        backgroundColor: activeTab === 'clientes' ? '#3498db' : 'transparent',
                        color: 'white',
                        border: 'none',
                        cursor: 'pointer'
                    }}
                >
                    👥 Clientes
                </button>

                {modulosDisponiveis.verde && (
                    <button
                        onClick={() => setActiveTab('jardim')}
                        style={{
                            padding: '1rem',
                            backgroundColor: activeTab === 'jardim' ? '#27ae60' : 'transparent',
                            color: 'white',
                            border: 'none',
                            cursor: 'pointer'
                        }}
                    >
                        🌿 Módulo Verde
                    </button>
                )}

                {modulosDisponiveis.aqua && (
                    <button
                        onClick={() => setActiveTab('piscina')}
                        style={{
                            padding: '1rem',
                            backgroundColor: activeTab === 'piscina' ? '#3498db' : 'transparent',
                            color: 'white',
                            border: 'none',
                            cursor: 'pointer'
                        }}
                    >
                        🏊 Módulo Aqua
                    </button>
                )}
            </nav>

            {/* Content */}
            <main style={{ padding: '2rem' }}>
                {/* Informações do sistema */}
                {systemInfo && (
                    <div style={{
                        marginBottom: '2rem',
                        padding: '1rem',
                        backgroundColor: '#e8f5e8',
                        borderRadius: '8px',
                        border: '1px solid #27ae60'
                    }}>
                        <h3 style={{ margin: '0 0 0.5rem 0', color: '#27ae60' }}>
                            Sistema Activo
                        </h3>
                        <p style={{ margin: 0 }}>
                            <strong>Módulos disponíveis:</strong> {systemInfo.modulos_activos?.join(', ')}
                        </p>
                    </div>
                )}

                {/* Renderizar componente ativo */}
                {activeTab === 'clientes' && <ClienteManager token={token} />}
                {activeTab === 'jardim' && modulosDisponiveis.verde && <ServicoJardimManager token={token} />}
                {activeTab === 'piscina' && modulosDisponiveis.aqua && <ServicoPiscinaManager token={token} />}
            </main>

            {/* Footer */}
            <footer style={{
                backgroundColor: '#2c3e50',
                color: 'white',
                padding: '1rem 2rem',
                textAlign: 'center',
                marginTop: '2rem'
            }}>
                <p style={{ margin: 0, fontSize: '0.9rem' }}>
                    GestOnGo - Sistema Modular de Gestão de Serviços de Campo
                </p>
                <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.8rem', opacity: 0.7 }}>
                    Arquitectura modular: Base + {modulosDisponiveis.verde ? 'Verde ' : ''}{modulosDisponiveis.aqua ? 'Aqua' : ''}
                </p>
            </footer>
        </div>
    );
}

export default App;
