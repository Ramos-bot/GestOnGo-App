import React from 'react';

export default function ClientesList({ items, onDelete }) {
    if (!items.length) return <p className="small">Sem clientes ainda.</p>;
    return (
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
            <thead>
                <tr><th align="left">Nome</th><th align="left">Telefone</th><th align="left">Localidade</th><th></th></tr>
            </thead>
            <tbody>
                {items.map(c => (
                    <tr key={c.id} style={{ borderTop: '1px solid #eee' }}>
                        <td>{c.nome}</td>
                        <td>{c.telefone || '-'}</td>
                        <td>{c.localidade || '-'}</td>
                        <td align="right"><button onClick={() => onDelete(c.id)}>Remover</button></td>
                    </tr>
                ))}
            </tbody>
        </table>
    );
}
