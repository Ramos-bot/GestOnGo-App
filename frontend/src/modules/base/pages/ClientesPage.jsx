/**
 * Página de Gestão de Clientes - Módulo Base
 * CRUD completo de clientes com validação
 */

import React, { useState, useEffect } from 'react';
import { apiClient } from '../../app/api';

const ClientesPage = () => {
  const [clientes, setClientes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [editingCliente, setEditingCliente] = useState(null);
  const [formData, setFormData] = useState({
    nome: '',
    email: '',
    telefone: '',
    endereco: ''
  });

  // Carregar clientes
  useEffect(() => {
    loadClientes();
  }, []);

  const loadClientes = async () => {
    try {
      setLoading(true);
      const data = await apiClient.getClientes();
      setClientes(data);
    } catch (err) {
      setError('Erro ao carregar clientes');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      if (editingCliente) {
        await apiClient.updateCliente(editingCliente.id, formData);
      } else {
        await apiClient.createCliente(formData);
      }

      await loadClientes();
      resetForm();
    } catch (err) {
      setError(err.message || 'Erro ao salvar cliente');
    }
  };

  const handleEdit = (cliente) => {
    setEditingCliente(cliente);
    setFormData({
      nome: cliente.nome,
      email: cliente.email,
      telefone: cliente.telefone,
      endereco: cliente.endereco
    });
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    if (!confirm('Tem certeza que deseja excluir este cliente?')) return;

    try {
      await apiClient.deleteCliente(id);
      await loadClientes();
    } catch (err) {
      setError('Erro ao excluir cliente');
    }
  };

  const resetForm = () => {
    setFormData({ nome: '', email: '', telefone: '', endereco: '' });
    setEditingCliente(null);
    setShowForm(false);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  if (loading) {
    return (
      <div className="page-container">
        <div className="loading">A carregar clientes...</div>
      </div>
    );
  }

  return (
    <div className="page-container">
      <div className="page-header">
        <h1>👥 Gestão de Clientes</h1>
        <button
          onClick={() => setShowForm(true)}
          className="btn btn-primary"
        >
          + Novo Cliente
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
              <h2>{editingCliente ? 'Editar Cliente' : 'Novo Cliente'}</h2>
              <button onClick={resetForm} className="close-btn">&times;</button>
            </div>

            <form onSubmit={handleSubmit} className="form">
              <div className="form-group">
                <label htmlFor="nome">Nome:</label>
                <input
                  type="text"
                  id="nome"
                  name="nome"
                  value={formData.nome}
                  onChange={handleChange}
                  required
                  placeholder="Nome do cliente"
                />
              </div>

              <div className="form-group">
                <label htmlFor="email">Email:</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  required
                  placeholder="cliente@email.com"
                />
              </div>

              <div className="form-group">
                <label htmlFor="telefone">Telefone:</label>
                <input
                  type="tel"
                  id="telefone"
                  name="telefone"
                  value={formData.telefone}
                  onChange={handleChange}
                  placeholder="+351 123 456 789"
                />
              </div>

              <div className="form-group">
                <label htmlFor="endereco">Endereço:</label>
                <textarea
                  id="endereco"
                  name="endereco"
                  value={formData.endereco}
                  onChange={handleChange}
                  rows="3"
                  placeholder="Endereço completo"
                />
              </div>

              <div className="form-actions">
                <button type="button" onClick={resetForm} className="btn btn-secondary">
                  Cancelar
                </button>
                <button type="submit" className="btn btn-primary">
                  {editingCliente ? 'Atualizar' : 'Criar'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      <div className="clientes-grid">
        {clientes.length === 0 ? (
          <div className="empty-state">
            <p>Nenhum cliente encontrado</p>
            <button onClick={() => setShowForm(true)} className="btn btn-primary">
              Criar primeiro cliente
            </button>
          </div>
        ) : (
          clientes.map(cliente => (
            <div key={cliente.id} className="cliente-card">
              <div className="cliente-info">
                <h3>{cliente.nome}</h3>
                <p className="email">{cliente.email}</p>
                {cliente.telefone && <p className="telefone">📞 {cliente.telefone}</p>}
                {cliente.endereco && <p className="endereco">📍 {cliente.endereco}</p>}
              </div>
              <div className="cliente-actions">
                <button onClick={() => handleEdit(cliente)} className="btn btn-edit">
                  ✏️ Editar
                </button>
                <button onClick={() => handleDelete(cliente.id)} className="btn btn-delete">
                  🗑️ Excluir
                </button>
              </div>
            </div>
          ))
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
          color: #333;
        }

        .loading {
          text-align: center;
          padding: 4rem;
          color: #666;
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
          background: #007bff;
          color: white;
        }

        .btn-primary:hover {
          background: #0056b3;
        }

        .btn-secondary {
          background: #6c757d;
          color: white;
        }

        .btn-edit {
          background: #28a745;
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
          max-width: 500px;
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

        .form-group label {
          display: block;
          margin-bottom: 0.5rem;
          font-weight: 500;
          color: #333;
        }

        .form-group input,
        .form-group textarea {
          width: 100%;
          padding: 0.75rem;
          border: 2px solid #e1e5e9;
          border-radius: 6px;
          font-size: 1rem;
        }

        .form-group input:focus,
        .form-group textarea:focus {
          outline: none;
          border-color: #007bff;
        }

        .form-actions {
          display: flex;
          gap: 1rem;
          justify-content: flex-end;
          margin-top: 1.5rem;
        }

        .clientes-grid {
          display: grid;
          grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
          gap: 1.5rem;
        }

        .cliente-card {
          background: white;
          padding: 1.5rem;
          border-radius: 12px;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
          border: 1px solid #e1e5e9;
        }

        .cliente-info h3 {
          margin: 0 0 0.5rem 0;
          color: #333;
        }

        .cliente-info p {
          margin: 0.25rem 0;
          color: #666;
          font-size: 0.9rem;
        }

        .email {
          color: #007bff !important;
        }

        .cliente-actions {
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
        }
      `}</style>
    </div>
  );
};

export default ClientesPage;
