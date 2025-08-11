# --- Stage 1: Build the React App ---
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install all dependencies, including devDependencies needed for building
RUN npm install

# Copy the rest of the application source code
COPY . .

# Set build-time arguments
ARG VITE_API_URL
ARG VITE_TOKEN_URL

# Build the application for production
RUN VITE_API_URL=${VITE_API_URL} VITE_TOKEN_URL=${VITE_TOKEN_URL} npm run build

# --- Stage 2: Serve with Vite Preview Server ---
FROM node:20-alpine AS runner

WORKDIR /app

# Copy package.json and package-lock.json to install vite
COPY package*.json ./

# Install dependencies needed for the preview server
RUN npm install


# Copy the built static files from the builder stage
COPY --from=builder /app/ .


# Expose port 8080 to match docker-compose.yml
EXPOSE 8080

# Command to start the Vite preview server on port 8080 and expose it externally
CMD ["npm", "run", "preview"]