FROM node:16 as DIST
WORKDIR /web
COPY web .
RUN npm install --registry=https://registry.npmmirror.com -g pnpm \
    && pnpm install --registry=https://registry.npmmirror.com \
    && cp .env.docker .env.production \
    && pnpm build

FROM nginx:alpine
COPY ./docker/web/nginx.conf /etc/nginx/conf.d/R1R3.conf
COPY --from=DIST /web/dist /usr/share/nginx/html

