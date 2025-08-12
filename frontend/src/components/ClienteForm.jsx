import React, { useState } from 'react';

export default function ClienteForm({ onSubmit }) {
  const [form, setForm] = useState({ nome: '', email: '', telefone: '', localidade: '' });

  const handle = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const submit = async (e) => {
    e.preventDefault();
    if (!form.nome.trim()) return;
    await onSubmit(form);
    setForm({ nome: '', email: '', telefone: '', localidade: '' });
  };

  return (
    <form onSubmit={submit} style={{ display: 'grid', gap: 8, marginBottom: 16 }}>
      <input name="nome" placeholder="Nome *" value={form.nome} onChange={handle} required />
      <input name="email" placeholder="Email" value={form.email} onChange={handle} />
      <input name="telefone" placeholder="Telefone" value={form.telefone} onChange={handle} />
      <input name="localidade" placeholder="Localidade" value={form.localidade} onChange={handle} />
      <button type="submit">Adicionar cliente</button>
    </form>
  );
}
