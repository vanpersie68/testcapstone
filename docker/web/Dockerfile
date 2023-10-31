# from node:16 as dist
# workdir /web
# copy web .
# # run npm install --registry=https://registry.npmmirror.com -g pnpm \
# #     && pnpm install --registry=https://registry.npmmirror.com \
# #     && cp .env.docker .env.production \
# #     && pnpm build

# run npm install --legacy-peer-deps \
#     && npm run serve

# from nginx:alpine
# copy ./docker/web/nginx.conf /etc/nginx/conf.d/R1R3.conf
# copy --from=DIST /web/dist /usr/share/nginx/html

FROM node:16

# 设置工作目录
WORKDIR /web

# 复制 package.json 和 package-lock.json 文件到容器
COPY web/package*.json

# 使用 --legacy-peer-deps 安装依赖
RUN npm install --legacy-peer-deps

# 复制应用程序代码到容器
COPY web/

# 暴露容器内部端口，如果应用程序使用不同的端口，请进行相应的修改
EXPOSE 8080

# 启动应用程序
CMD ["npm", "run", "serve"]