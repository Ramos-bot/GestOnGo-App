const API_BASE = process.env.REACT_APP_API_BASE || '';

export async function apiGet(path) {
  const res = await fetch(`${API_BASE}${path}`);
  if (!res.ok) throw new Error(`GET ${path} falhou: ${res.status}`);
  return res.json();
}

export async function apiJson(method, path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body || {})
  });
  if (!res.ok) {
    const msg = await res.text().catch(() => '');
    throw new Error(`${method} ${path} falhou: ${res.status} ${msg}`);
  }
  return res.status === 204 ? null : res.json();
}
