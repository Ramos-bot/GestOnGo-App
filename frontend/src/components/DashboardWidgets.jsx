import React from 'react';

export default function DashboardWidgets({ totalClientes, totalTarefas, pendentes }) {
    const card = {
        padding: 16,
        borderRadius: 12,
        background: '#fff',
        boxShadow: '0 2px 12px rgba(0,0,0,0.06)',
        display: 'grid',
        gap: 4
    };
    return (
        <div style={{ display: 'grid', gap: 16 }}>
            <div style={card}>
                <div className="small" style={{ color: '#666' }}>Clientes</div>
                <div style={{ fontSize: 28, fontWeight: 700 }}>{totalClientes}</div>
            </div>
            <div style={card}>
                <div className="small" style={{ color: '#666' }}>Tarefas</div>
                <div style={{ fontSize: 20, fontWeight: 700 }}>
                    {pendentes} pendentes / {totalTarefas} total
                </div>
            </div>
        </div>
    );
}
