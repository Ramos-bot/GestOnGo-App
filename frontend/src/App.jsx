import { useState, useEffect } from 'react';
import axios from 'axios';
import LoginForm from './components/LoginForm';
import ClienteManager from './components/ClienteManager';
import ServicoManager from './components/ServicoManager';

/**
 * Componente principal da aplicação GestOnGo - gestão de serviços
 */
function App() {
    const [token, setToken] = useState('');
    const [utilizador, setUtilizador] = useState(null);
    const [clientes, setClientes] = useState([]);
    const [servicos, setServicos] = useState([]);
    const [carregandoLogin, setCarregandoLogin] = useState(false);
    const [abaSelecionada, setAbaSelecionada] = useState('dashboard');

    // Configuração base do axios usando variáveis de ambiente
    const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
    const api = axios.create({
        baseURL: API_BASE_URL,
        timeout: 10000,
    });

    // Interceptor para adicionar token automaticamente
    api.interceptors.request.use((config) => {
        if (token) {
            config.headers.Authorization = `Bearer ${token}`;
        }
        return config;
    });

    /**
     * Efectua login com email e senha
     */
    async function fazerLogin(email, senha) {
        setCarregandoLogin(true);
        try {
            const dados = new URLSearchParams();
            dados.append('username', email);
            dados.append('password', senha);

            const resposta = await axios.post('http://localhost:8000/utilizadores/login', dados);
            const accessToken = resposta.data.access_token;

            setToken(accessToken);
            setUtilizador({ email });

            // Carregar dados iniciais
            await Promise.all([
                carregarClientes(accessToken),
                carregarServicos(accessToken)
            ]);

        } catch (error) {
            console.error('Erro ao iniciar sessão', error);
            throw new Error('Credenciais inválidas');
        } finally {
            setCarregandoLogin(false);
        }
    }

    /**
     * Efectua logout
     */
    function fazerLogout() {
        setToken('');
        setUtilizador(null);
        setClientes([]);
        setServicos([]);
        setAbaSelecionada('dashboard');
    }

    /**
     * Carrega lista de clientes
     */
    async function carregarClientes(authToken = token) {
        try {
            const resposta = await api.get('/clientes', {
                headers: authToken ? { Authorization: `Bearer ${authToken}` } : {}
            });
            setClientes(resposta.data);
        } catch (error) {
            console.error('Erro ao carregar clientes', error);
        }
    }

    /**
     * Carrega lista de serviços
     */
    async function carregarServicos(authToken = token) {
        try {
            const resposta = await api.get('/servicos', {
                headers: authToken ? { Authorization: `Bearer ${authToken}` } : {}
            });
            setServicos(resposta.data);
        } catch (error) {
            console.error('Erro ao carregar serviços', error);
        }
    }

    // Efeito para carregar dados quando o token muda
    useEffect(() => {
        if (token) {
            carregarClientes();
            carregarServicos();
        }
    }, [token]);

    // Se não estiver logado, mostrar formulário de login
    if (!token) {
        return (
            <div style={{
                minHeight: '100vh',
                backgroundColor: '#f0f8f0',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '2rem'
            }}>
                <div style={{ width: '100%', maxWidth: '500px' }}>
                    <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
                        <h1 style={{ color: '#2c5530', fontSize: '3rem', margin: '0 0 0.5rem 0' }}>
                            🌿 GestOnGo
                        </h1>
                        <p style={{ color: '#666', fontSize: '1.2rem', margin: '0' }}>
                            Sistema de Gestão de Serviços de Campo
                        </p>
                        <p style={{ color: '#888', fontSize: '1rem' }}>
                            Jardinagem • Manutenção de Piscinas
                        </p>
                    </div>
                    <LoginForm onLogin={fazerLogin} isLoading={carregandoLogin} />
                </div>
            </div>
        );
    }

    // Interface principal após login
    return (
        <div style={{
            minHeight: '100vh',
            backgroundColor: '#f0f8f0',
            fontFamily: 'Arial, sans-serif'
        }}>
            {/* Header */}
            <header style={{
                backgroundColor: '#2c5530',
                color: 'white',
                padding: '1rem 2rem',
                boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
            }}>
                <div style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    maxWidth: '1200px',
                    margin: '0 auto'
                }}>
                    <div>
                        <h1 style={{ margin: '0', fontSize: '1.8rem' }}>
                            🌿 GestOnGo
                        </h1>
                        <p style={{ margin: '0.25rem 0 0 0', fontSize: '0.9rem', opacity: 0.8 }}>
                            Bem-vindo, {utilizador?.email}
                        </p>
                    </div>
                    <button
                        onClick={fazerLogout}
                        style={{
                            backgroundColor: 'transparent',
                            color: 'white',
                            border: '1px solid rgba(255,255,255,0.3)',
                            padding: '0.5rem 1rem',
                            borderRadius: '4px',
                            cursor: 'pointer',
                            fontSize: '14px'
                        }}
                    >
                        🚪 Sair
                    </button>
                </div>
            </header>

            {/* Navigation */}
            <nav style={{
                backgroundColor: 'white',
                padding: '0 2rem',
                borderBottom: '1px solid #ddd'
            }}>
                <div style={{
                    maxWidth: '1200px',
                    margin: '0 auto',
                    display: 'flex',
                    gap: '2rem'
                }}>
                    {[
                        { id: 'dashboard', nome: '📊 Dashboard', icone: '📊' },
                        { id: 'clientes', nome: '👥 Clientes', icone: '👥' },
                        { id: 'servicos', nome: '🛠️ Serviços', icone: '🛠️' }
                    ].map(aba => (
                        <button
                            key={aba.id}
                            onClick={() => setAbaSelecionada(aba.id)}
                            style={{
                                backgroundColor: 'transparent',
                                border: 'none',
                                padding: '1rem 0',
                                fontSize: '16px',
                                cursor: 'pointer',
                                borderBottom: abaSelecionada === aba.id ? '3px solid #2c5530' : '3px solid transparent',
                                color: abaSelecionada === aba.id ? '#2c5530' : '#666',
                                fontWeight: abaSelecionada === aba.id ? 'bold' : 'normal'
                            }}
                        >
                            {aba.nome}
                        </button>
                    ))}
                </div>
            </nav>

            {/* Main Content */}
            <main style={{
                maxWidth: '1200px',
                margin: '0 auto',
                padding: '2rem'
            }}>
                {abaSelecionada === 'dashboard' && (
                    <div>
                        <h2 style={{ color: '#2c5530', marginBottom: '2rem' }}>
                            📊 Dashboard - Visão Geral
                        </h2>

                        <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))',
                            gap: '1rem',
                            marginBottom: '2rem'
                        }}>
                            {/* Cards de estatísticas */}
                            <div style={{
                                backgroundColor: 'white',
                                padding: '1.5rem',
                                borderRadius: '8px',
                                boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
                                textAlign: 'center'
                            }}>
                                <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>👥</div>
                                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c5530' }}>
                                    {clientes.length}
                                </div>
                                <div style={{ color: '#666' }}>Clientes Registados</div>
                            </div>

                            <div style={{
                                backgroundColor: 'white',
                                padding: '1.5rem',
                                borderRadius: '8px',
                                boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
                                textAlign: 'center'
                            }}>
                                <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🛠️</div>
                                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c5530' }}>
                                    {servicos.length}
                                </div>
                                <div style={{ color: '#666' }}>Serviços Agendados</div>
                            </div>

                            <div style={{
                                backgroundColor: 'white',
                                padding: '1.5rem',
                                borderRadius: '8px',
                                boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
                                textAlign: 'center'
                            }}>
                                <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🌱</div>
                                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c5530' }}>
                                    {servicos.filter(s => s.tipo === 'jardinagem').length}
                                </div>
                                <div style={{ color: '#666' }}>Serviços Jardinagem</div>
                            </div>

                            <div style={{
                                backgroundColor: 'white',
                                padding: '1.5rem',
                                borderRadius: '8px',
                                boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
                                textAlign: 'center'
                            }}>
                                <div style={{ fontSize: '2rem', marginBottom: '0.5rem' }}>🏊</div>
                                <div style={{ fontSize: '2rem', fontWeight: 'bold', color: '#2c5530' }}>
                                    {servicos.filter(s => s.tipo === 'piscina').length}
                                </div>
                                <div style={{ color: '#666' }}>Serviços Piscina</div>
                            </div>
                        </div>

                        {/* Resumo de actividade recente */}
                        <div style={{
                            backgroundColor: 'white',
                            padding: '1.5rem',
                            borderRadius: '8px',
                            boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
                        }}>
                            <h3 style={{ color: '#2c5530', marginTop: 0 }}>📅 Próximos Serviços</h3>
                            {servicos
                                .filter(s => new Date(s.data_servico) >= new Date())
                                .sort((a, b) => new Date(a.data_servico) - new Date(b.data_servico))
                                .slice(0, 5)
                                .map(servico => {
                                    const cliente = clientes.find(c => c.id === servico.cliente_id);
                                    return (
                                        <div key={servico.id} style={{
                                            display: 'flex',
                                            justifyContent: 'space-between',
                                            alignItems: 'center',
                                            padding: '0.75rem 0',
                                            borderBottom: '1px solid #eee'
                                        }}>
                                            <div>
                                                <span style={{ marginRight: '0.5rem' }}>
                                                    {servico.tipo === 'jardinagem' ? '🌱' : '🏊'}
                                                </span>
                                                <strong>{cliente?.nome || 'Cliente'}</strong>
                                                <span style={{ color: '#666', marginLeft: '0.5rem' }}>
                                                    - {servico.tipo}
                                                </span>
                                            </div>
                                            <div style={{ color: '#666', fontSize: '14px' }}>
                                                {new Date(servico.data_servico).toLocaleDateString('pt-PT')}
                                            </div>
                                        </div>
                                    );
                                })
                            }
                            {servicos.filter(s => new Date(s.data_servico) >= new Date()).length === 0 && (
                                <p style={{ color: '#666', textAlign: 'center', margin: '1rem 0' }}>
                                    Nenhum serviço agendado para o futuro.
                                </p>
                            )}
                        </div>
                    </div>
                )}

                {abaSelecionada === 'clientes' && (
                    <ClienteManager
                        token={token}
                        clientes={clientes}
                        onClientesCriado={() => { }}
                        onClientesActualizados={carregarClientes}
                    />
                )}

                {abaSelecionada === 'servicos' && (
                    <ServicoManager
                        token={token}
                        servicos={servicos}
                        clientes={clientes}
                        onServicosCriado={() => { }}
                        onServicosActualizados={carregarServicos}
                    />
                )}
            </main>

            {/* Footer */}
            <footer style={{
                backgroundColor: '#2c5530',
                color: 'white',
                padding: '1rem 2rem',
                textAlign: 'center',
                marginTop: '2rem'
            }}>
                <p style={{ margin: '0', fontSize: '14px' }}>
                    GestOnGo v0.1.0 - Sistema de Gestão de Serviços de Campo 🇵🇹
                </p>
            </footer>
        </div>
    );
}

export default App;