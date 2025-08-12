import { test, expect } from '@playwright/test';

test('homepage carrega', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByText(/GestOnGo/i)).toBeVisible();
});

test('API /health responde', async ({ request }) => {
    const res = await request.get('/health');
    expect(res.ok()).toBeTruthy();
    const body = await res.json();
    expect(body).toEqual({ ok: true });
});
