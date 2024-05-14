FROM node:20-buster-slim
EXPOSE 5173
WORKDIR /playground

COPY web web
COPY ./bin/start-web bin/start
RUN cd web && npm install
RUN cd web && npm run build
CMD ["bin/start"]
