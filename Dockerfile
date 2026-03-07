# Stage 1: Build static site with Hugo
FROM hugomods/hugo:exts AS builder

WORKDIR /src
COPY . .
RUN hugo --minify

# Stage 2: Serve with Nginx
FROM nginx:alpine

COPY --from=builder /src/public /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
