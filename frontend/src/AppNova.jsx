/**
 * Aplicação principal GestOnGo - Versão Modular Nova
 * Sistema com autenticação e páginas modulares
 */

import React, { useState, useEffect } from 'react';
import { useAuth } from './app/auth';
import LoginPage from './modules/base/pages/LoginPage';
import ClientesPage from './modules/base/pages/ClientesPage';
import ServicosJardimPage from './modules/verde/pages/ServicosJardimPage';
import ServicoPiscinaPage from './modules/aqua/pages/ServicoPiscinaPage';

// Configuração dos módulos disponíveis
const MODULES = {
    base: {
        name: 'Base',
        color: '#007bff',
        icon: '🏠',
        pages: [
            { key: 'clientes', name: 'Clientes', component: ClientesPage }
        ]
    },
    verde: {
        name: 'Jardinagem',
        color: '#28a745',
        icon: '🌿',
        pages: [
            { key: 'servicos-jardim', name: 'Serviços Jardim', component: ServicosJardimPage }
        ]
    },
    aqua: {
        name: 'Piscinas',
        color: '#17a2b8',
        icon: '🏊',
        pages: [
            { key: 'servicos-piscina', name: 'Serviços Piscina', component: ServicoPiscinaPage }
        ]
    }
};

// Módulos ativos (simulando configuração)
const ACTIVE_MODULES = ['base', 'verde', 'aqua'];

function AppModularNova() {
    const { isAuthenticated, user, logout } = useAuth();
    const [currentPage, setCurrentPage] = useState('clientes');
    const [currentModule, setCurrentModule] = useState('base');

    // Encontrar a página atual
    const getCurrentPageComponent = () => {
        const module = MODULES[currentModule];
        if (!module) return () => <div>Módulo não encontrado</div>;

        const page = module.pages.find(p => p.key === currentPage);
        if (!page) return () => <div>Página não encontrada</div>;

        return page.component;
    };

    const CurrentPageComponent = getCurrentPageComponent();

    // Se não estiver autenticado, mostrar página de login
    if (!isAuthenticated) {
        return <LoginPage onLogin={() => window.location.reload()} />;
    }

    return (
        <div className="app">
            {/* Header */}
            <header className="app-header">
                <div className="header-content">
                    <h1>🌿🏊 GestOnGo</h1>
                    <div className="user-info">
                        <span>Olá, {user?.nome || 'Utilizador'}</span>
                        <button onClick={logout} className="logout-btn">
                            🚪 Sair
                        </button>
                    </div>
                </div>
            </header>

            <div className="app-body">
                {/* Sidebar */}
                <aside className="sidebar">
                    <nav className="nav">
                        {ACTIVE_MODULES.map(moduleKey => {
                            const module = MODULES[moduleKey];
                            if (!module) return null;

                            return (
                                <div key={moduleKey} className="nav-module">
                                    <div
                                        className={`module-header ${currentModule === moduleKey ? 'active' : ''}`}
                                        style={{ borderLeftColor: module.color }}
                                        onClick={() => setCurrentModule(moduleKey)}
                                    >
                                        <span className="module-icon">{module.icon}</span>
                                        <span className="module-name">{module.name}</span>
                                    </div>

                                    {currentModule === moduleKey && (
                                        <div className="module-pages">
                                            {module.pages.map(page => (
                                                <button
                                                    key={page.key}
                                                    className={`page-btn ${currentPage === page.key ? 'active' : ''}`}
                                                    onClick={() => {
                                                        setCurrentModule(moduleKey);
                                                        setCurrentPage(page.key);
                                                    }}
                                                >
                                                    {page.name}
                                                </button>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            );
                        })}
                    </nav>
                </aside>

                {/* Main Content */}
                <main className="main-content">
                    <CurrentPageComponent />
                </main>
            </div>

            <style jsx>{`
        .app {
          min-height: 100vh;
          display: flex;
          flex-direction: column;
          font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }

        .app-header {
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          color: white;
          padding: 1rem 0;
          box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .header-content {
          max-width: 1200px;
          margin: 0 auto;
          padding: 0 2rem;
          display: flex;
          justify-content: space-between;
          align-items: center;
        }

        .header-content h1 {
          margin: 0;
          font-size: 1.5rem;
        }

        .user-info {
          display: flex;
          align-items: center;
          gap: 1rem;
        }

        .logout-btn {
          background: rgba(255, 255, 255, 0.2);
          border: 1px solid rgba(255, 255, 255, 0.3);
          color: white;
          padding: 0.5rem 1rem;
          border-radius: 6px;
          cursor: pointer;
          transition: background-color 0.2s ease;
        }

        .logout-btn:hover {
          background: rgba(255, 255, 255, 0.3);
        }

        .app-body {
          display: flex;
          flex: 1;
          min-height: 0;
        }

        .sidebar {
          width: 280px;
          background: #f8f9fa;
          border-right: 1px solid #e1e5e9;
          overflow-y: auto;
        }

        .nav {
          padding: 1rem 0;
        }

        .nav-module {
          margin-bottom: 0.5rem;
        }

        .module-header {
          padding: 0.75rem 1rem;
          border-left: 4px solid transparent;
          cursor: pointer;
          transition: all 0.2s ease;
          display: flex;
          align-items: center;
          gap: 0.5rem;
          font-weight: 500;
        }

        .module-header:hover {
          background: #e9ecef;
        }

        .module-header.active {
          background: #e3f2fd;
          border-left-color: #2196f3;
        }

        .module-icon {
          font-size: 1.2rem;
        }

        .module-pages {
          background: #fff;
          border-top: 1px solid #e1e5e9;
        }

        .page-btn {
          width: 100%;
          padding: 0.75rem 2rem;
          border: none;
          background: none;
          text-align: left;
          cursor: pointer;
          transition: background-color 0.2s ease;
          border-bottom: 1px solid #f1f3f4;
        }

        .page-btn:hover {
          background: #f8f9fa;
        }

        .page-btn.active {
          background: #e8f5e8;
          color: #2e7d32;
          font-weight: 500;
        }

        .main-content {
          flex: 1;
          overflow-y: auto;
          background: #f5f5f5;
        }

        @media (max-width: 768px) {
          .app-body {
            flex-direction: column;
          }

          .sidebar {
            width: 100%;
            max-height: 200px;
          }

          .header-content {
            padding: 0 1rem;
          }

          .header-content h1 {
            font-size: 1.2rem;
          }
        }
      `}</style>
        </div>
    );
}

export default AppModularNova;
