/**
 * Página de Serviços de Jardinagem - Módulo Verde
 * Gestão completa de serviços de jardinagem
 */

import React, { useState, useEffect } from 'react';
import { apiClient } from '../../app/api';

const ServicosJardimPage = () => {
  const [servicos, setServicos] = useState([]);
  const [clientes, setClientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [editingServico, setEditingServico] = useState(null);
  const [formData, setFormData] = useState({
    cliente_id: '',
    tipo_servico: '',
    descricao: '',
    data_agendada: '',
    preco: '',
    status: 'pendente'
  });

  const tiposServico = [
    'Corte de Relva',
    'Poda de Árvores',
    'Plantação',
    'Limpeza de Jardim',
    'Fertilização',
    'Irrigação',
    'Paisagismo',
    'Manutenção Geral'
  ];

  const statusOptions = [
    { value: 'pendente', label: '⏳ Pendente', color: '#ffc107' },
    { value: 'em_andamento', label: '🔄 Em Andamento', color: '#17a2b8' },
    { value: 'concluido', label: '✅ Concluído', color: '#28a745' },
    { value: 'cancelado', label: '❌ Cancelado', color: '#dc3545' }
  ];

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [servicosData, clientesData] = await Promise.all([
        apiClient.getServicosJardim(),
        apiClient.getClientes()
      ]);
      setServicos(servicosData);
      setClientes(clientesData);
    } catch (err) {
      setError('Erro ao carregar dados');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const servicoData = {
        ...formData,
        preco: parseFloat(formData.preco),
        cliente_id: parseInt(formData.cliente_id)
      };

      if (editingServico) {
        await apiClient.updateServicoJardim(editingServico.id, servicoData);
      } else {
        await apiClient.createServicoJardim(servicoData);
      }

      await loadData();
      resetForm();
    } catch (err) {
      setError(err.message || 'Erro ao salvar serviço');
    }
  };

  const handleEdit = (servico) => {
    setEditingServico(servico);
    setFormData({
      cliente_id: servico.cliente_id.toString(),
      tipo_servico: servico.tipo_servico,
      descricao: servico.descricao,
      data_agendada: servico.data_agendada,
      preco: servico.preco.toString(),
      status: servico.status
    });
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!confirm('Tem certeza que deseja excluir este serviço?')) return;

    try {
      await apiClient.deleteServicoJardim(id);
      await loadData();
    } catch (err) {
      setError('Erro ao excluir serviço');
    }
  };

  const resetForm = () => {
    setFormData({
      cliente_id: '',
      tipo_servico: '',
      descricao: '',
      data_agendada: '',
      preco: '',
      status: 'pendente'
    });
    setEditingServico(null);
    setShowForm(false);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const getStatusBadge = (status) => {
    const statusInfo = statusOptions.find(s => s.value === status);
    return statusInfo ? statusInfo : { label: status, color: '#6c757d' };
  };

  const getClienteNome = (clienteId) => {
    const cliente = clientes.find(c => c.id === clienteId);
    return cliente ? cliente.nome : 'Cliente não encontrado';
  };

  if (loading) {
    return (
      <div className="page-container">
        <div className="loading">🌿 A carregar serviços de jardinagem...</div>
      </div>
    );
  }

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>🌿 Serviços de Jardinagem</h1>
        <button
          onClick={() => setShowForm(true)}
          className="btn btn-primary"
        >
          + Novo Serviço
        </button>
      </div>

      {error && (
        <div className="error-message">
          {error}
        </div>
      )}

      {showForm && (
        <div className="modal-overlay">
          <div className="modal">
            <div className="modal-header">
              <h2>{editingServico ? 'Editar Serviço' : 'Novo Serviço de Jardinagem'}</h2>
              <button onClick={resetForm} className="close-btn">&times;</button>
            </div>

            <form onSubmit={handleSubmit} className="form">
              <div className="form-group">
                <label htmlFor="cliente_id">Cliente:</label>
                <select
                  id="cliente_id"
                  name="cliente_id"
                  value={formData.cliente_id}
                  onChange={handleChange}
                  required
                >
                  <option value="">Selecione um cliente</option>
                  {clientes.map(cliente => (
                    <option key={cliente.id} value={cliente.id}>
                      {cliente.nome}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="tipo_servico">Tipo de Serviço:</label>
                <select
                  id="tipo_servico"
                  name="tipo_servico"
                  value={formData.tipo_servico}
                  onChange={handleChange}
                  required
                >
                  <option value="">Selecione o tipo</option>
                  {tiposServico.map(tipo => (
                    <option key={tipo} value={tipo}>
                      {tipo}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-group">
                <label htmlFor="descricao">Descrição:</label>
                <textarea
                  id="descricao"
                  name="descricao"
                  value={formData.descricao}
                  onChange={handleChange}
                  rows="3"
                  placeholder="Descreva o serviço a ser realizado..."
                  required
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label htmlFor="data_agendada">Data Agendada:</label>
                  <input
                    type="date"
                    id="data_agendada"
                    name="data_agendada"
                    value={formData.data_agendada}
                    onChange={handleChange}
                    required
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="preco">Preço (€):</label>
                  <input
                    type="number"
                    id="preco"
                    name="preco"
                    value={formData.preco}
                    onChange={handleChange}
                    step="0.01"
                    min="0"
                    placeholder="0.00"
                    required
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="status">Status:</label>
                <select
                  id="status"
                  name="status"
                  value={formData.status}
                  onChange={handleChange}
                >
                  {statusOptions.map(status => (
                    <option key={status.value} value={status.value}>
                      {status.label}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-actions">
                <button type="button" onClick={resetForm} className="btn btn-secondary">
                  Cancelar
                </button>
                <button type="submit" className="btn btn-primary">
                  {editingServico ? 'Atualizar' : 'Criar'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      <div className="servicos-grid">
        {servicos.length === 0 ? (
          <div className="empty-state">
            <p>🌱 Nenhum serviço de jardinagem encontrado</p>
            <button onClick={() => setShowForm(true)} className="btn btn-primary">
              Criar primeiro serviço
            </button>
          </div>
        ) : (
          servicos.map(servico => {
            const statusInfo = getStatusBadge(servico.status);
            return (
              <div key={servico.id} className="servico-card">
                <div className="servico-header">
                  <h3>{servico.tipo_servico}</h3>
                  <span
                    className="status-badge"
                    style={{ backgroundColor: statusInfo.color }}
                  >
                    {statusInfo.label}
                  </span>
                </div>

                <div className="servico-info">
                  <p className="cliente">👤 {getClienteNome(servico.cliente_id)}</p>
                  <p className="descricao">{servico.descricao}</p>
                  <p className="data">📅 {new Date(servico.data_agendada).toLocaleDateString('pt-PT')}</p>
                  <p className="preco">💰 €{servico.preco.toFixed(2)}</p>
                </div>

                <div className="servico-actions">
                  <button onClick={() => handleEdit(servico)} className="btn btn-edit">
                    ✏️ Editar
                  </button>
                  <button onClick={() => handleDelete(servico.id)} className="btn btn-delete">
                    🗑️ Excluir
                  </button>
                </div>
              </div>
            );
          })
        )}
      </div>

      <style jsx>{`
        .page-container {
          padding: 2rem;
          max-width: 1200px;
          margin: 0 auto;
        }

        .page-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 2rem;
        }

        .page-header h1 {
          margin: 0;
          color: #28a745;
        }

        .loading {
          text-align: center;
          padding: 4rem;
          color: #666;
          font-size: 1.1rem;
        }

        .error-message {
          background: #fee;
          color: #c33;
          padding: 1rem;
          border-radius: 6px;
          margin-bottom: 1rem;
          border: 1px solid #fcc;
        }

        .btn {
          padding: 0.5rem 1rem;
          border: none;
          border-radius: 6px;
          cursor: pointer;
          font-size: 0.9rem;
          transition: all 0.2s ease;
        }

        .btn-primary {
          background: #28a745;
          color: white;
        }

        .btn-primary:hover {
          background: #218838;
        }

        .btn-secondary {
          background: #6c757d;
          color: white;
        }

        .btn-edit {
          background: #17a2b8;
          color: white;
          margin-right: 0.5rem;
        }

        .btn-delete {
          background: #dc3545;
          color: white;
        }

        .modal-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0, 0, 0, 0.5);
          display: flex;
          justify-content: center;
          align-items: center;
          z-index: 1000;
        }

        .modal {
          background: white;
          padding: 2rem;
          border-radius: 12px;
          width: 90%;
          max-width: 600px;
          max-height: 90vh;
          overflow-y: auto;
        }

        .modal-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 1.5rem;
        }

        .close-btn {
          background: none;
          border: none;
          font-size: 1.5rem;
          cursor: pointer;
          color: #666;
        }

        .form-group {
          margin-bottom: 1rem;
        }

        .form-row {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 1rem;
        }

        .form-group label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 500;
          color: #333;
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
          width: 100%;
          padding: 0.75rem;
          border: 2px solid #e1e5e9;
          border-radius: 6px;
          font-size: 1rem;
        }

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
          outline: none;
          border-color: #28a745;
        }

        .form-actions {
          display: flex;
          gap: 1rem;
          justify-content: flex-end;
          margin-top: 1.5rem;
        }

        .servicos-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
          gap: 1.5rem;
        }

        .servico-card {
          background: white;
          padding: 1.5rem;
          border-radius: 12px;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          border: 1px solid #e1e5e9;
          border-left: 4px solid #28a745;
        }

        .servico-header {
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          margin-bottom: 1rem;
        }

        .servico-header h3 {
          margin: 0;
          color: #333;
          font-size: 1.1rem;
        }

        .status-badge {
          color: white;
          padding: 0.25rem 0.5rem;
          border-radius: 12px;
          font-size: 0.8rem;
          font-weight: 500;
        }

        .servico-info p {
          margin: 0.5rem 0;
          color: #666;
          font-size: 0.9rem;
        }

        .cliente {
          font-weight: 500;
          color: #333 !important;
        }

        .preco {
          font-weight: 600;
          color: #28a745 !important;
          font-size: 1rem !important;
        }

        .servico-actions {
          margin-top: 1rem;
          padding-top: 1rem;
          border-top: 1px solid #e1e5e9;
        }

        .empty-state {
          text-align: center;
          padding: 4rem;
          grid-column: 1 / -1;
        }

        .empty-state p {
          color: #666;
          margin-bottom: 1rem;
          font-size: 1.1rem;
        }
      `}</style>
    </div>
  );
};

export default ServicosJardimPage;
