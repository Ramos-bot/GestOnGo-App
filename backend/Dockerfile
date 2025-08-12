FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production --no-audit --no-fund

FROM node:20-alpine AS runner
ENV NODE_ENV=production
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN addgroup -S nodegrp && adduser -S nodeusr -G nodegrp
USER nodeusr
EXPOSE 8000
ENV PORT=8000
CMD ["node", "server.js"]
