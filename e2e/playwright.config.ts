import { defineConfig } from '@playwright/test';

export default defineConfig({
    retries: process.env.CI ? 2 : 0,
    use: {
        baseURL: process.env.BASE_URL || 'http://localhost:8080',
        headless: true
    },
    reporter: [['list']]
});
