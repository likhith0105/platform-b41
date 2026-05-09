import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  base: '/platform-b41/',
  build: {
    outDir: '../docs',
    emptyOutDir: true
  }
})
