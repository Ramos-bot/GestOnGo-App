import React, { useState } from 'react';
import DashboardWidgets from './components/DashboardWidgets';
import ClientesPage from './pages/ClientesPage';
import { useClientes } from './hooks/useClientes';

export default function App() {
  const [page, setPage] = useState('dashboard');
  const { dados } = useClientes(); // para contar clientes no dashboard

  return (
    <main style={{ padding: 24, maxWidth: 900, margin: '0 auto' }}>
      <header style={{ display: 'flex', gap: 12, alignItems: 'center', marginBottom: 16 }}>
        <h1 style={{ margin: 0 }}>GestOnGo</h1>
        <nav style={{ display: 'flex', gap: 8 }}>
          <button onClick={() => setPage('dashboard')}>Dashboard</button>
          <button onClick={() => setPage('clientes')}>Clientes</button>
        </nav>
      </header>

      {page === 'dashboard' && (
        <>
          <p className="small">build pipeline test ✅</p>
          <DashboardWidgets totalClientes={dados.length} />
        </>
      )}
      {page === 'clientes' && <ClientesPage />}
    </main>
  );
}
