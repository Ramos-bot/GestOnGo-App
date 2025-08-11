import { useState } from 'react';

/**
 * Componente para gestão de clientes
 */
function ClienteManager({ token, clientes, onClientesCriado, onClientesActualizados }) {
    const [mostrarFormulario, setMostrarFormulario] = useState(false);
    const [novoCliente, setNovoCliente] = useState({
        nome: '',
        telefone: '',
        endereco: '',
        observacoes: ''
    });
    const [carregando, setCarregando] = useState(false);
    const [erro, setErro] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setCarregando(true);
        setErro('');

        try {
            const response = await fetch('http://localhost:8000/clientes/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify(novoCliente)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Erro ao criar cliente');
            }

            const clienteCriado = await response.json();

            // Reset form
            setNovoCliente({ nome: '', telefone: '', endereco: '', observacoes: '' });
            setMostrarFormulario(false);

            // Callback to parent
            if (onClientesCriado) {
                onClientesCriado(clienteCriado);
            }

            // Refresh list
            if (onClientesActualizados) {
                onClientesActualizados();
            }

        } catch (error) {
            setErro(error.message);
        } finally {
            setCarregando(false);
        }
    };

    const formatarTelefone = (telefone) => {
        if (!telefone) return 'N/A';
        // Format Portuguese phone numbers
        if (telefone.startsWith('351')) {
            return `+${telefone}`;
        }
        if (telefone.length === 9) {
            return `+351 ${telefone}`;
        }
        return telefone;
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
                    👥 Clientes ({clientes.length})
                </h3>
                <button
                    onClick={() => setMostrarFormulario(!mostrarFormulario)}
                    style={{
                        backgroundColor: '#2196F3',
                        color: 'white',
                        border: 'none',
                        padding: '0.5rem 1rem',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        fontSize: '14px'
                    }}
                >
                    {mostrarFormulario ? '❌ Cancelar' : '➕ Novo Cliente'}
                </button>
            </div>

            {mostrarFormulario && (
                <div style={{
                    backgroundColor: '#f8f9fa',
                    padding: '1rem',
                    borderRadius: '8px',
                    marginBottom: '1rem',
                    border: '1px solid #dee2e6'
                }}>
                    <h4 style={{ color: '#2c5530', marginTop: 0 }}>✨ Novo Cliente</h4>

                    <form onSubmit={handleSubmit}>
                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem', marginBottom: '1rem' }}>
                            <div>
                                <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                    Nome *
                                </label>
                                <input
                                    type="text"
                                    value={novoCliente.nome}
                                    onChange={(e) => setNovoCliente({ ...novoCliente, nome: e.target.value })}
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
                                    Telefone
                                </label>
                                <input
                                    type="tel"
                                    value={novoCliente.telefone}
                                    onChange={(e) => setNovoCliente({ ...novoCliente, telefone: e.target.value })}
                                    placeholder="912345678 ou +351912345678"
                                    style={{
                                        width: '100%',
                                        padding: '0.5rem',
                                        border: '1px solid #ccc',
                                        borderRadius: '4px'
                                    }}
                                />
                            </div>
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                Endereço
                            </label>
                            <input
                                type="text"
                                value={novoCliente.endereco}
                                onChange={(e) => setNovoCliente({ ...novoCliente, endereco: e.target.value })}
                                style={{
                                    width: '100%',
                                    padding: '0.5rem',
                                    border: '1px solid #ccc',
                                    borderRadius: '4px'
                                }}
                            />
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.25rem', fontSize: '14px', fontWeight: 'bold' }}>
                                Observações
                            </label>
                            <textarea
                                value={novoCliente.observacoes}
                                onChange={(e) => setNovoCliente({ ...novoCliente, observacoes: e.target.value })}
                                rows="3"
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
                                backgroundColor: carregando ? '#6c757d' : '#28a745',
                                color: 'white',
                                border: 'none',
                                padding: '0.5rem 1rem',
                                borderRadius: '4px',
                                cursor: carregando ? 'not-allowed' : 'pointer'
                            }}
                        >
                            {carregando ? '⏳ A criar...' : '💾 Criar Cliente'}
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
                {clientes.length === 0 ? (
                    <div style={{ padding: '2rem', textAlign: 'center', color: '#666' }}>
                        📝 Nenhum cliente encontrado. Crie o primeiro cliente!
                    </div>
                ) : (
                    <div style={{ maxHeight: '400px', overflow: 'auto' }}>
                        {clientes.map((cliente, index) => (
                            <div
                                key={cliente.id}
                                style={{
                                    padding: '1rem',
                                    borderBottom: index < clientes.length - 1 ? '1px solid #eee' : 'none',
                                    backgroundColor: index % 2 === 0 ? '#f8f9fa' : 'white'
                                }}
                            >
                                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                                    <div style={{ flex: 1 }}>
                                        <h4 style={{ margin: '0 0 0.5rem 0', color: '#2c5530' }}>
                                            👤 {cliente.nome}
                                        </h4>
                                        <div style={{ fontSize: '14px', color: '#666' }}>
                                            📞 {formatarTelefone(cliente.telefone)}
                                        </div>
                                        {cliente.endereco && (
                                            <div style={{ fontSize: '14px', color: '#666', marginTop: '0.25rem' }}>
                                                📍 {cliente.endereco}
                                            </div>
                                        )}
                                        {cliente.observacoes && (
                                            <div style={{ fontSize: '14px', color: '#666', marginTop: '0.25rem', fontStyle: 'italic' }}>
                                                💭 {cliente.observacoes}
                                            </div>
                                        )}
                                    </div>
                                    <div style={{ fontSize: '12px', color: '#999' }}>
                                        ID: {cliente.id}
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

export default ClienteManager;
