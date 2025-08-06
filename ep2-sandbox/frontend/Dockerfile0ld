# --- Stage 1: Build the React App ---
FROM node:18-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application source code
COPY . .

# Build the application for production
RUN npm run build

# --- Stage 2: Serve with Nginx ---
FROM nginx:1.25-alpine AS runtime

# Copy the built static files from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy the custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 8080 (as configured in nginx.conf)
EXPOSE 8080

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]
