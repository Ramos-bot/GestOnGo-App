import { useState, useEffect } from 'react';

/**
 * Componente para gestão de serviços
 */
function ServicoManager({ token, servicos, clientes, onServicosCriado, onServicosActualizados }) {
    const [mostrarFormulario, setMostrarFormulario] = useState(false);
    const [novoServico, setNovoServico] = useState({
        tipo: 'jardinagem',
        data_servico: '',
        duracao_horas: 2,
        cliente_id: '',
        descricao: ''
    });
    const [carregando, setCarregando] = useState(false);
    const [erro, setErro] = useState('');

    // Set default date to tomorrow
    useEffect(() => {
        const amanha = new Date();
        amanha.setDate(amanha.getDate() + 1);
        const dataFormatada = amanha.toISOString().split('T')[0];
        setNovoServico(prev => ({ ...prev, data_servico: dataFormatada }));
    }, []);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setCarregando(true);
        setErro('');

        try {
            const response = await fetch('http://localhost:8000/servicos/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    ...novoServico,
                    cliente_id: parseInt(novoServico.cliente_id)
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao criar serviço');
            }

            const servicoCriado = await response.json();

            // Reset form
            const amanha = new Date();
            amanha.setDate(amanha.getDate() + 1);
            const dataFormatada = amanha.toISOString().split('T')[0];

            setNovoServico({
                tipo: 'jardinagem',
                data_servico: dataFormatada,
                duracao_horas: 2,
                cliente_id: '',
                descricao: ''
            });
            setMostrarFormulario(false);

            // Callbacks to parent
            if (onServicosCriado) {
                onServicosCriado(servicoCriado);
            }
            if (onServicosActualizados) {
                onServicosActualizados();
            }

        } catch (error) {
            setErro(error.message);
        } finally {
            setCarregando(false);
        }
    };

    const formatarData = (dataString) => {
        const data = new Date(dataString + 'T00:00:00');
        return data.toLocaleDateString('pt-PT', {
            weekday: 'long',
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    };

    const obterNomeCliente = (clienteId) => {
        const cliente = clientes.find(c => c.id === clienteId);
        return cliente ? cliente.nome : `Cliente ID: ${clienteId}`;
    };

    const obterIconeTipo = (tipo) => {
        return tipo === 'jardinagem' ? '🌱' : '🏊';
    };

    const obterCorStatus = (status) => {
        const cores = {
            'agendado': '#ffc107',
            'em_progresso': '#17a2b8',
            'concluido': '#28a745',
            'cancelado': '#dc3545'
        };
        return cores[status] || '#6c757d';
    };

    const obterTextoStatus = (status) => {
        const textos = {
            'agendado': 'Agendado',
            'em_progresso': 'Em Progresso',
            'concluido': 'Concluído',
            'cancelado': 'Cancelado'
        };
        return textos[status] || status;
    };

    return (
        <div>
            <div style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                marginBottom: '1rem'
            }}>
                <h3 style={{ color: '#2c5530', margin: 0 }}>
                    🛠️ Serviços ({servicos.length})
                </h3>
                <button
                    onClick={() => setMostrarFormulario(!mostrarFormulario)}
                    disabled={clientes.length === 0}
                    style={{
                        backgroundColor: clientes.length === 0 ? '#6c757d' : '#FF9800',
                        color: 'white',
                        border: 'none',
                        padding: '0.5rem 1rem',
                        borderRadius: '4px',
                        cursor: clientes.length === 0 ? 'not-allowed' : 'pointer',
                        fontSize: '14px'
                    }}
                    title={clientes.length === 0 ? 'Crie primeiro um cliente' : ''}
                >
                    {mostrarFormulario ? '❌ Cancelar' : '➕ Novo Serviço'}
                </button>
            </div>

            {clientes.length === 0 && (
                <div style={{
                    backgroundColor: '#fff3cd',
                    color: '#856404',
                    padding: '1rem',
                    borderRadius: '4px',
                    marginBottom: '1rem',
                    border: '1px solid #ffeaa7'
                }}>
                    ⚠️ Para criar um serviço, primeiro crie pelo menos um cliente.
                </div>
            )}

            {mostrarFormulario && (
                <div style={{
                    backgroundColor: '#f8f9fa',
                    padding: '1rem',
                    borderRadius: '8px',
                    marginBottom: '1rem',
                    border: '1px solid #dee2e6'
                }}>
                    <h4 style={{ color: '#2c5530', marginTop: 0 }}>✨ Novo Serviço</h4>

                    <form onSubmit={handleSubmit}>
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
                            <div>
                                <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                    Tipo de Serviço *
                                </label>
                                <select
                                    value={novoServico.tipo}
                                    onChange={(e) => setNovoServico({ ...novoServico, tipo: e.target.value })}
                                    style={{
                                        width: '100%',
                                        padding: '0.5rem',
                                        border: '1px solid #ccc',
                                        borderRadius: '4px'
                                    }}
                                    required
                                >
                                    <option value="jardinagem">🌱 Jardinagem</option>
                                    <option value="piscina">🏊 Manutenção de Piscina</option>
                                </select>
                            </div>
                            <div>
                                <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                    Cliente *
                                </label>
                                <select
                                    value={novoServico.cliente_id}
                                    onChange={(e) => setNovoServico({ ...novoServico, cliente_id: e.target.value })}
                                    style={{
                                        width: '100%',
                                        padding: '0.5rem',
                                        border: '1px solid #ccc',
                                        borderRadius: '4px'
                                    }}
                                    required
                                >
                                    <option value="">Seleccione um cliente</option>
                                    {clientes.map(cliente => (
                                        <option key={cliente.id} value={cliente.id}>
                                            {cliente.nome}
                                        </option>
                                    ))}
                                </select>
                            </div>
                        </div>

                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
                            <div>
                                <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                    Data do Serviço *
                                </label>
                                <input
                                    type="date"
                                    value={novoServico.data_servico}
                                    onChange={(e) => setNovoServico({ ...novoServico, data_servico: e.target.value })}
                                    min={new Date().toISOString().split('T')[0]}
                                    style={{
                                        width: '100%',
                                        padding: '0.5rem',
                                        border: '1px solid #ccc',
                                        borderRadius: '4px'
                                    }}
                                    required
                                />
                            </div>
                            <div>
                                <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                    Duração (horas) *
                                </label>
                                <input
                                    type="number"
                                    value={novoServico.duracao_horas}
                                    onChange={(e) => setNovoServico({ ...novoServico, duracao_horas: parseInt(e.target.value) })}
                                    min="1"
                                    max="12"
                                    style={{
                                        width: '100%',
                                        padding: '0.5rem',
                                        border: '1px solid #ccc',
                                        borderRadius: '4px'
                                    }}
                                    required
                                />
                            </div>
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                Descrição
                            </label>
                            <textarea
                                value={novoServico.descricao}
                                onChange={(e) => setNovoServico({ ...novoServico, descricao: e.target.value })}
                                rows="3"
                                placeholder="Descreva os trabalhos a realizar..."
                                style={{
                                    width: '100%',
                                    padding: '0.5rem',
                                    border: '1px solid #ccc',
                                    borderRadius: '4px',
                                    resize: 'vertical'
                                }}
                            />
                        </div>

                        {erro && (
                            <div style={{
                                backgroundColor: '#f8d7da',
                                color: '#721c24',
                                padding: '0.5rem',
                                borderRadius: '4px',
                                marginBottom: '1rem',
                                fontSize: '14px'
                            }}>
                                ❌ {erro}
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={carregando}
                            style={{
                                backgroundColor: carregando ? '#6c757d' : '#FF9800',
                                color: 'white',
                                border: 'none',
                                padding: '0.5rem 1rem',
                                borderRadius: '4px',
                                cursor: carregando ? 'not-allowed' : 'pointer'
                            }}
                        >
                            {carregando ? '⏳ A criar...' : '💾 Agendar Serviço'}
                        </button>
                    </form>
                </div>
            )}

            <div style={{
                backgroundColor: 'white',
                borderRadius: '8px',
                boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
                overflow: 'hidden'
            }}>
                {servicos.length === 0 ? (
                    <div style={{ padding: '2rem', textAlign: 'center', color: '#666' }}>
                        📅 Nenhum serviço agendado. Crie o primeiro serviço!
                    </div>
                ) : (
                    <div style={{ maxHeight: '400px', overflow: 'auto' }}>
                        {servicos.map((servico, index) => (
                            <div
                                key={servico.id}
                                style={{
                                    padding: '1rem',
                                    borderBottom: index < servicos.length - 1 ? '1px solid #eee' : 'none',
                                    backgroundColor: index % 2 === 0 ? '#f8f9fa' : 'white'
                                }}
                            >
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <div style={{ flex: 1 }}>
                                        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '0.5rem' }}>
                                            <h4 style={{ margin: '0 0.5rem 0 0', color: '#2c5530' }}>
                                                {obterIconeTipo(servico.tipo)} {servico.tipo.charAt(0).toUpperCase() + servico.tipo.slice(1)}
                                            </h4>
                                            <span style={{
                                                backgroundColor: obterCorStatus(servico.status),
                                                color: 'white',
                                                padding: '0.25rem 0.5rem',
                                                borderRadius: '12px',
                                                fontSize: '12px',
                                                fontWeight: 'bold'
                                            }}>
                                                {obterTextoStatus(servico.status)}
                                            </span>
                                        </div>
                                        <div style={{ fontSize: '14px', color: '#666', marginBottom: '0.25rem' }}>
                                            👤 {obterNomeCliente(servico.cliente_id)}
                                        </div>
                                        <div style={{ fontSize: '14px', color: '#666', marginBottom: '0.25rem' }}>
                                            📅 {formatarData(servico.data_servico)}
                                        </div>
                                        <div style={{ fontSize: '14px', color: '#666', marginBottom: '0.25rem' }}>
                                            ⏱️ {servico.duracao_horas} hora{servico.duracao_horas > 1 ? 's' : ''}
                                        </div>
                                        {servico.descricao && (
                                            <div style={{ fontSize: '14px', color: '#666', fontStyle: 'italic', marginTop: '0.5rem' }}>
                                                📝 {servico.descricao}
                                            </div>
                                        )}
                                    </div>
                                    <div style={{ fontSize: '12px', color: '#999', textAlign: 'right' }}>
                                        ID: {servico.id}
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
}

export default ServicoManager;
