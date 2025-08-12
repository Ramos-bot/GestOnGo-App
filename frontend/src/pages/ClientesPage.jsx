import React from 'react';
import { useClientes } from '../hooks/useClientes';
import ClienteForm from '../components/ClienteForm';
import ClientesList from '../components/ClientesList';

export default function ClientesPage() {
    const { dados, loading, erro, criar, remover } = useClientes();

    return (
        <section>
            <h2>Clientes</h2>
            {erro && <p style={{ color: 'crimson' }}>{erro}</p>}
            <ClienteForm onSubmit={criar} />
            {loading ? <p>A carregar…</p> : <ClientesList items={dados} onDelete={remover} />}
        </section>
    );
}
