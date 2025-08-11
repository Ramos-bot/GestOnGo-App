/**
 * Gestão de autenticação para GestOnGo
 * Estado simples com token JWT e localStorage
 */

import { apiClient } from './api';

// Tipo para dados do utilizador
export interface User {
  id: number;
  nome: string;
  email: string;
  is_active: boolean;
}

// Tipo para resposta de login
export interface LoginResponse {
  access_token: string;
  token_type: string;
}

// Estado de autenticação
export class AuthService {
  private static instance: AuthService;
  private token: string | null = null;
  private user: User | null = null;
  private listeners: Array<(isAuthenticated: boolean) => void> = [];

  private constructor() {
    // Carregar token do localStorage ao inicializar
    this.token = localStorage.getItem('token');
  }

  public static getInstance(): AuthService {
    if (!AuthService.instance) {
      AuthService.instance = new AuthService();
    }
    return AuthService.instance;
  }

  /**
   * Fazer login com email e senha
   */
  public async login(email: string, password: string): Promise<void> {
    try {
      const response: LoginResponse = await apiClient.login(email, password);
      this.setToken(response.access_token);

      // Carregar dados do utilizador
      await this.loadCurrentUser();

      // Notificar listeners
      this.notifyListeners(true);
    } catch (error) {
      throw new Error(error instanceof Error ? error.message : 'Erro ao fazer login');
    }
  }

  /**
   * Definir token de autenticação
   */
  public setToken(token: string): void {
    this.token = token;
    localStorage.setItem('token', token);
  }

  /**
   * Obter token actual
   */
  public getToken(): string | null {
    return this.token;
  }

  /**
   * Verificar se está autenticado
   */
  public isAuthenticated(): boolean {
    return !!this.token;
  }

  /**
   * Obter utilizador actual
   */
  public getUser(): User | null {
    return this.user;
  }

  /**
   * Carregar dados do utilizador actual
   */
  public async loadCurrentUser(): Promise<void> {
    if (!this.token) return;

    try {
      this.user = await apiClient.getCurrentUser();
    } catch (error) {
      console.error('Erro ao carregar utilizador:', error);
      this.logout();
    }
  }

  /**
   * Fazer logout
   */
  public logout(): void {
    this.token = null;
    this.user = null;
    localStorage.removeItem('token');
    this.notifyListeners(false);
  }

  /**
   * Adicionar listener para mudanças de autenticação
   */
  public addAuthListener(listener: (isAuthenticated: boolean) => void): void {
    this.listeners.push(listener);
  }

  /**
   * Remover listener
   */
  public removeAuthListener(listener: (isAuthenticated: boolean) => void): void {
    this.listeners = this.listeners.filter(l => l !== listener);
  }

  /**
   * Notificar todos os listeners
   */
  private notifyListeners(isAuthenticated: boolean): void {
    this.listeners.forEach(listener => listener(isAuthenticated));
  }
}

// Instância singleton para uso global
export const authService = AuthService.getInstance();

// Funções de conveniência para uso direto
export const login = (email: string, password: string) => authService.login(email, password);
export const logout = () => authService.logout();
export const getToken = () => authService.getToken();
export const isAuthenticated = () => authService.isAuthenticated();
export const getCurrentUser = () => authService.getUser();
export const addAuthListener = (listener: (isAuthenticated: boolean) => void) =>
  authService.addAuthListener(listener);

// Hook personalizado para React (opcional)
export const useAuth = () => {
  const [isAuth, setIsAuth] = React.useState(authService.isAuthenticated());
  const [user, setUser] = React.useState(authService.getUser());

  React.useEffect(() => {
    const listener = (authenticated: boolean) => {
      setIsAuth(authenticated);
      setUser(authService.getUser());
    };

    authService.addAuthListener(listener);

    // Carregar utilizador se já estiver autenticado
    if (authService.isAuthenticated() && !authService.getUser()) {
      authService.loadCurrentUser().then(() => {
        setUser(authService.getUser());
      });
    }

    return () => authService.removeAuthListener(listener);
  }, []);

  return {
    isAuthenticated: isAuth,
    user,
    login: authService.login.bind(authService),
    logout: authService.logout.bind(authService),
  };
};
