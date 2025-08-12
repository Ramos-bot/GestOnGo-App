import { useEffect, useState, useCallback } from 'react';
import { apiGet, apiJson } from '../api';

export function useClientes() {
    const [dados, setDados] = useState([]);
    const [loading, setLoading] = useState(true);
    const [erro, setErro] = useState(null);

    const carregar = useCallback(async () => {
        try {
            setLoading(true);
            setErro(null);
            const list = await apiGet('/api/clientes');
            setDados(list);
        } catch (e) {
            setErro(e.message);
        } finally {
            setLoading(false);
        }
    }, []);

    useEffect(() => { carregar(); }, [carregar]);

    const criar = async (payload) => { await apiJson('POST', '/api/clientes', payload); await carregar(); };
    const atualizar = async (id, payload) => { await apiJson('PUT', `/api/clientes/${id}`, payload); await carregar(); };
    const remover = async (id) => { await apiJson('DELETE', `/api/clientes/${id}`); await carregar(); };

    return { dados, loading, erro, criar, atualizar, remover, reload: carregar };
}
