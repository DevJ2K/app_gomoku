import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  define: {
    'downloadProject': JSON.stringify("https://download-directory.github.io/?url=https://github.com/DevJ2K/template_webapp/tree/main/backend/project_name"),
    'authUrl': JSON.stringify("http://127.0.0.1:4000/auth/login"),
    'api_url': JSON.stringify("http://127.0.0.1:4000")
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
