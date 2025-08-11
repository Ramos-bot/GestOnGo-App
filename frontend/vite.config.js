import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Configuração base do Vite para React - GestOnGo
export default defineConfig({
    plugins: [react()],
    server: {
        host: true,
        port: 5173,
    },
});
