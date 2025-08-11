import { useState } from 'react';

/**
 * Componente para formulário de login
 */
function LoginForm({ onLogin, isLoading }) {
    const [credenciais, setCredenciais] = useState({
        email: 'admin@gestongo.pt',
        senha: 'gestongo2025'
    });
    const [erro, setErro] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErro('');

        try {
            await onLogin(credenciais.email, credenciais.senha);
        } catch (error) {
            setErro('Credenciais inválidas. Verifique o email e senha.');
        }
    };

    return (
        <div style={{
            backgroundColor: 'white',
            padding: '2rem',
            borderRadius: '8px',
            boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
            maxWidth: '400px',
            margin: '0 auto'
        }}>
            <h2 style={{ color: '#2c5530', textAlign: 'center', marginBottom: '1.5rem' }}>
                🔐 Iniciar Sessão
            </h2>

            <form onSubmit={handleSubmit}>
                <div style={{ marginBottom: '1rem' }}>
                    <label style={{ display: 'block', marginBottom: '0.5rem', color: '#333' }}>
                        📧 Email:
                    </label>
                    <input
                        type="email"
                        value={credenciais.email}
                        onChange={(e) => setCredenciais({ ...credenciais, email: e.target.value })}
                        style={{
                            width: '100%',
                            padding: '0.75rem',
                            border: '1px solid #ddd',
                            borderRadius: '4px',
                            fontSize: '16px'
                        }}
                        required
                    />
                </div>

                <div style={{ marginBottom: '1.5rem' }}>
                    <label style={{ display: 'block', marginBottom: '0.5rem', color: '#333' }}>
                        🔒 Senha:
                    </label>
                    <input
                        type="password"
                        value={credenciais.senha}
                        onChange={(e) => setCredenciais({ ...credenciais, senha: e.target.value })}
                        style={{
                            width: '100%',
                            padding: '0.75rem',
                            border: '1px solid #ddd',
                            borderRadius: '4px',
                            fontSize: '16px'
                        }}
                        required
                    />
                </div>

                {erro && (
                    <div style={{
                        backgroundColor: '#f8d7da',
                        color: '#721c24',
                        padding: '0.75rem',
                        borderRadius: '4px',
                        marginBottom: '1rem'
                    }}>
                        ❌ {erro}
                    </div>
                )}

                <button
                    type="submit"
                    disabled={isLoading}
                    style={{
                        width: '100%',
                        backgroundColor: isLoading ? '#6c757d' : '#4CAF50',
                        color: 'white',
                        padding: '0.75rem',
                        border: 'none',
                        borderRadius: '4px',
                        fontSize: '16px',
                        cursor: isLoading ? 'not-allowed' : 'pointer'
                    }}
                >
                    {isLoading ? '⏳ A entrar...' : '🚀 Entrar'}
                </button>
            </form>
        </div>
    );
}

export default LoginForm;
