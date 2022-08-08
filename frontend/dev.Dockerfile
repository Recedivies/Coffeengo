# Use an official node runtime as a parent image - Build stage
FROM node:16-alpine as build-image

WORKDIR /app/frontend

COPY package.json .

# Change npm ci to npm install since we are going to be in development mode
RUN npm install

RUN mkdir node_modules/.cache && chmod -R 777 node_modules/.cache

# Use an official node runtime as a parent image - Runtime
FROM node:16-alpine as runtime

WORKDIR /app/frontend

# copy node_modules from build stage
COPY --from=build-image /app/frontend/node_modules /app/frontend/node_modules

# copy rest of source code
COPY . .

# npm start is the command to start the application in development mode
CMD ["npm", "start"]
