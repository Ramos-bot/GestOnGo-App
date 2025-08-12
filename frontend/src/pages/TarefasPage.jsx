import React, { useState } from 'react';
import { useTarefas } from '../hooks/useTarefas';
import dayjs from 'dayjs';

export default function TarefasPage() {
    const { dados, loading, erro, criar, atualizar, remover } = useTarefas();
    const [form, setForm] = useState({ clienteId: '', descricao: '', data: '' });
    const [filtro, setFiltro] = useState('todas');

    const handle = (e) => setForm({ ...form, [e.target.name]: e.target.value });

    const submit = async (e) => {
        e.preventDefault();
        if (!form.clienteId || !form.descricao.trim()) return;
        await criar({ ...form, clienteId: Number(form.clienteId) });
        setForm({ clienteId: '', descricao: '', data: '' });
    };

    // Função para aplicar o filtro
    const filtrarTarefas = () => {
        const hojeISO = dayjs().format('YYYY-MM-DD');
        const inicioSemana = dayjs().startOf('week');
        const fimSemana = dayjs().endOf('week');
        switch (filtro) {
            case 'pendentes':
                return dados.filter(t => !t.feito);
            case 'concluidas':
                return dados.filter(t => t.feito);
            case 'hoje':
                return dados.filter(t => t.data === hojeISO);
            case 'semana':
                return dados.filter(t => t.data && dayjs(t.data).isBetween(inicioSemana, fimSemana, 'day', '[]'));
            default:
                return dados;
        }
    };

    const tarefasFiltradas = filtrarTarefas();

    return (
        <section>
            <h2>Tarefas</h2>
            {erro && <p style={{ color: 'crimson' }}>{erro}</p>}

            {/* Botões de filtro */}
            <div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
                <button onClick={() => setFiltro('todas')} disabled={filtro === 'todas'}>Todas</button>
                <button onClick={() => setFiltro('pendentes')} disabled={filtro === 'pendentes'}>Pendentes</button>
                <button onClick={() => setFiltro('concluidas')} disabled={filtro === 'concluidas'}>Concluídas</button>
                <button onClick={() => setFiltro('hoje')} disabled={filtro === 'hoje'}>Hoje</button>
                <button onClick={() => setFiltro('semana')} disabled={filtro === 'semana'}>Semana</button>
            </div>

            <form onSubmit={submit} style={{ display: 'grid', gap: 8, marginBottom: 16 }}>
                <input name="clienteId" placeholder="ID Cliente" value={form.clienteId} onChange={handle} />
                <input name="descricao" placeholder="Descrição" value={form.descricao} onChange={handle} />
                <input type="date" name="data" value={form.data} onChange={handle} />
                <button type="submit">Adicionar tarefa</button>
            </form>

            {loading ? (
                <p>A carregar…</p>
            ) : (
                <table style={{ width: '100%', borderCollapse: 'collapse' }}>
                    <thead>
                        <tr><th>Cliente</th><th>Descrição</th><th>Data</th><th>Feito</th><th></th></tr>
                    </thead>
                    <tbody>
                        {tarefasFiltradas.map(t => {
                            const hojeISO = dayjs().format('YYYY-MM-DD');
                            const isHoje = t.data === hojeISO;
                            const estiloLinha = t.feito
                                ? { backgroundColor: '#e6ffed' } // verde-claro
                                : isHoje
                                    ? { backgroundColor: '#fff9e6' } // amarelo-claro
                                    : {};
                            return (
                                <tr key={t.id} style={{ borderTop: '1px solid #eee', ...estiloLinha }}>
                                    <td>{t.clienteId}</td>
                                    <td>
                                        {t.feito ? '✅' : isHoje ? '📅' : '•'} {t.descricao}
                                    </td>
                                    <td>{t.data || '-'}</td>
                                    <td>
                                        <input
                                            type="checkbox"
                                            checked={t.feito}
                                            onChange={() => atualizar(t.id, { feito: !t.feito })}
                                        />
                                    </td>
                                    <td align="right"><button onClick={() => remover(t.id)}>Remover</button></td>
                                </tr>
                            );
                        })}
                    </tbody>
                </table>
            )}
        </section>
    );
}
