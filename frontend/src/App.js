import React, { useState } from 'react';
import DashboardWidgets from './components/DashboardWidgets';
import ClientesPage from './pages/ClientesPage';
import TarefasPage from './pages/TarefasPage';
import BackendStatus from './pages/BackendStatus';
import { useClientes } from './hooks/useClientes';
import { useTarefas } from './hooks/useTarefas';

export default function App() {
    const [page, setPage] = useState('dashboard');
    const { dados } = useClientes(); // para contar clientes no dashboard
    const { dados: tarefas } = useTarefas(); // para contar tarefas no dashboard

    return (
        <main style={{ padding: 24, maxWidth: 900, margin: '0 auto' }}>
            <header style={{ display: 'flex', gap: 12, alignItems: 'center', marginBottom: 16 }}>
                <h1 style={{ margin: 0 }}>GestOnGo</h1>
                <nav style={{ display: 'flex', gap: 8 }}>
                    <button onClick={() => setPage('dashboard')}>Dashboard</button>
                    <button onClick={() => setPage('clientes')}>Clientes</button>
                    <button onClick={() => setPage('tarefas')}>Tarefas</button>
                    <button onClick={() => setPage('status')}>🔌 Estado</button>
                </nav>
            </header>

            {page === 'dashboard' && (
                <>
                    <p className="small">build pipeline test ✅</p>
                    <DashboardWidgets
                        totalClientes={dados.length}
                        totalTarefas={tarefas.length}
                        pendentes={tarefas.filter(t => !t.feito).length}
                    />
                </>
            )}
            {page === 'clientes' && <ClientesPage />}
            {page === 'tarefas' && <TarefasPage />}
            {page === 'status' && <BackendStatus />}
        </main>
    );
}
