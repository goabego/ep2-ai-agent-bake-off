# ---- Base Stage ----
# Use an official Node.js image.
# https://hub.docker.com/_/node
FROM node:20 AS base

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./


# ---- Dependencies Stage ----
# Install dependencies. 'npm ci' is generally recommended for production builds
# as it's faster and uses the package-lock.json for deterministic installs.
FROM base AS deps
RUN npm ci


# ---- Build Stage ----
# Copy the source code and build the application
FROM deps AS builder
COPY . .
RUN npm run build


# ---- Production Stage ----
# Start from a clean, small image for the final production environment
FROM base AS runner
WORKDIR /app

# Copy the built application from the 'builder' stage
# Adjust the source folder if your build output is not '.next' (e.g., 'dist', 'build')
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json

# Expose the port your app will run on
EXPOSE 3000

# The command to start your application
# This typically uses the 'start' script from your package.json
CMD ["npm", "run", "dev"]