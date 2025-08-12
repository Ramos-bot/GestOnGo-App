# Imagem oficial já com browsers
FROM mcr.microsoft.com/playwright:v1.46.0-jammy
WORKDIR /tests
COPY package*.json ./
RUN npm ci --no-audit --no-fund
COPY . .
# BASE_URL será injetado (ex.: http://web or http://localhost:8080)
ENV BASE_URL=http://web
CMD ["npm","test","--","--reporter=line"]
