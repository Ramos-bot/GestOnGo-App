/**
 * Router simples para GestOnGo sem dependências externas
 * Navegação baseada em estado para aplicação SPA
 */

import React, { createContext, useContext, useState, ReactNode } from 'react';

// Tipos para as rotas
export type Route = {
  path: string;
  component: React.ComponentType<any>;
  protected?: boolean;
  title?: string;
};

// Contexto do router
interface RouterContextType {
  currentPath: string;
  navigate: (path: string) => void;
  goBack: () => void;
}

const RouterContext = createContext<RouterContextType | null>(null);

// Hook para usar o router
export const useRouter = () => {
  const context = useContext(RouterContext);
  if (!context) {
    throw new Error('useRouter deve ser usado dentro de um RouterProvider');
  }
  return context;
};

// Componente Router Provider
interface RouterProviderProps {
  children: ReactNode;
  initialPath?: string;
}

export const RouterProvider: React.FC<RouterProviderProps> = ({
  children,
  initialPath = '/login'
}) => {
  const [currentPath, setCurrentPath] = useState(initialPath);
  const [history, setHistory] = useState<string[]>([initialPath]);

  const navigate = (path: string) => {
    if (path !== currentPath) {
      setCurrentPath(path);
      setHistory(prev => [...prev, path]);

      // Actualizar URL do browser (opcional)
      window.history.pushState({}, '', path);
    }
  };

  const goBack = () => {
    if (history.length > 1) {
      const newHistory = history.slice(0, -1);
      const previousPath = newHistory[newHistory.length - 1];
      setHistory(newHistory);
      setCurrentPath(previousPath);

      // Actualizar URL do browser (opcional)
      window.history.pushState({}, '', previousPath);
    }
  };

  // Escutar mudanças do browser (botão voltar)
  React.useEffect(() => {
    const handlePopState = () => {
      const path = window.location.pathname;
      setCurrentPath(path);
    };

    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, []);

  const value: RouterContextType = {
    currentPath,
    navigate,
    goBack,
  };

  return (
    <RouterContext.Provider value={value}>
      {children}
    </RouterContext.Provider>
  );
};

// Componente Route Matcher
interface RouteMatcherProps {
  routes: Route[];
  fallback?: React.ComponentType;
}

export const RouteMatcher: React.FC<RouteMatcherProps> = ({
  routes,
  fallback: Fallback
}) => {
  const { currentPath } = useRouter();

  // Encontrar rota correspondente
  const matchedRoute = routes.find(route => {
    // Suporte para rotas exactas e com parâmetros simples
    if (route.path === currentPath) return true;

    // Suporte para rotas com parâmetros (ex: /clientes/:id)
    const routeParts = route.path.split('/');
    const pathParts = currentPath.split('/');

    if (routeParts.length !== pathParts.length) return false;

    return routeParts.every((part, index) => {
      return part.startsWith(':') || part === pathParts[index];
    });
  });

  if (matchedRoute) {
    const Component = matchedRoute.component;
    return <Component />;
  }

  // Rota não encontrada
  if (Fallback) {
    return <Fallback />;
  }

  return (
    <div style={{ padding: '2rem', textAlign: 'center' }}>
      <h2>Página não encontrada</h2>
      <p>O caminho "{currentPath}" não existe.</p>
    </div>
  );
};

// Componente Link para navegação
interface LinkProps {
  to: string;
  children: ReactNode;
  className?: string;
  style?: React.CSSProperties;
  onClick?: () => void;
}

export const Link: React.FC<LinkProps> = ({
  to,
  children,
  className,
  style,
  onClick
}) => {
  const { navigate, currentPath } = useRouter();

  const handleClick = (e: React.MouseEvent) => {
    e.preventDefault();
    onClick?.();
    navigate(to);
  };

  const isActive = currentPath === to;

  return (
    <a
      href={to}
      onClick={handleClick}
      className={className}
      style={{
        textDecoration: 'none',
        color: isActive ? '#007bff' : 'inherit',
        fontWeight: isActive ? 'bold' : 'normal',
        ...style,
      }}
    >
      {children}
    </a>
  );
};

// Componente para rotas protegidas
interface ProtectedRouteProps {
  children: ReactNode;
  isAuthenticated: boolean;
  fallback?: ReactNode;
}

export const ProtectedRoute: React.FC<ProtectedRouteProps> = ({
  children,
  isAuthenticated,
  fallback
}) => {
  const { navigate } = useRouter();

  React.useEffect(() => {
    if (!isAuthenticated) {
      navigate('/login');
    }
  }, [isAuthenticated, navigate]);

  if (!isAuthenticated) {
    return fallback ? <>{fallback}</> : null;
  }

  return <>{children}</>;
};

// Utilitários para extrair parâmetros da rota
export const useParams = () => {
  const { currentPath } = useRouter();

  // Esta é uma implementação simples
  // Em aplicações mais complexas, use react-router-dom
  return {};
};

export default RouterProvider;
