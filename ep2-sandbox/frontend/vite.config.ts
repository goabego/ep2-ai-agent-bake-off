import { resolve } from "path"
import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"
import tailwindcss from "@tailwindcss/vite"

export default defineConfig({
  plugins: [react(), tailwindcss()],
  resolve: {
    alias: {
      "@": resolve(__dirname, "./src"),
    },
  },
  // Config for the dev server (vite dev)
  server: {
    host: true,
    port: 8080,
    strictPort: true,
    allowedHosts: ['frontend-ep2-426194555180.us-west1.run.app','*.run.app', 'localhost', '127.0.0.1' ,'*'],
    proxy: {
      '/api': {
        target: 'https://a2a-bfpwtp2iiq-uc.a.run.app',
        changeOrigin: true,
        secure: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
  // Config for the preview server (vite preview)
  preview: {
    host: true,
    port: 8080,
    strictPort: true,
    allowedHosts: ['frontend-ep2-426194555180.us-west1.run.app','*.run.app', 'localhost', '127.0.0.1','*'],
  },
})