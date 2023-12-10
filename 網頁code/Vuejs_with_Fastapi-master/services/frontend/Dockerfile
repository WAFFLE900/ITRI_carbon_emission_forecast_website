# FROM node:lts-alpine

# WORKDIR /app

# ENV PATH /app/node_modules/.bin:$PATH

# RUN npm install @vue/cli@4.5.13 -g

# COPY package.json .
# COPY package-lock.json .
# RUN npm install

# CMD ["npm", "run", "serve"]


FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package.json ./
RUN apk add --update python3 make g++\
   && rm -rf /var/cache/apk/*
RUN npm install --legacy-peer-deps
COPY . .
RUN npm run build
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]