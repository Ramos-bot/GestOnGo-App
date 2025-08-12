import { render, screen } from '@testing-library/react';
import React from 'react';
import App from './App';

test('renderiza título GestOnGo', () => {
    render(<App />);
    expect(screen.getByText(/GestOnGo/i)).toBeInTheDocument();
});
