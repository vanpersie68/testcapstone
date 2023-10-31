from node:16 as dist
workdir /web
copy web .
run npm install --registry=https://registry.npmmirror.com -g pnpm \
    && pnpm install --registry=https://registry.npmmirror.com \
    && cp .env.docker .env.production \
    && pnpm build

from nginx:alpine
copy ./docker/web/nginx.conf /etc/nginx/conf.d/R1R3.conf
copy --from=DIST /web/dist /usr/share/nginx/html

