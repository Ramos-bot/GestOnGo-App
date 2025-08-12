import { useEffect, useState, useCallback } from 'react';
import { apiGet, apiJson } from '../api';

export function useTarefas() {
    const [dados, setDados] = useState([]);
    const [loading, setLoading] = useState(true);
    const [erro, setErro] = useState(null);

    const carregar = useCallback(async () => {
        try {
            setLoading(true);
            setErro(null);
            const list = await apiGet('/api/tarefas');
            setDados(list);
        } catch (e) {
            setErro(e.message);
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => { carregar(); }, [carregar]);

    const criar = async (payload) => { await apiJson('POST', '/api/tarefas', payload); await carregar(); };
    const atualizar = async (id, payload) => { await apiJson('PUT', `/api/tarefas/${id}`, payload); await carregar(); };
    const remover = async (id) => { await apiJson('DELETE', `/api/tarefas/${id}`); await carregar(); };

    return { dados, loading, erro, criar, atualizar, remover, reload: carregar };
}
