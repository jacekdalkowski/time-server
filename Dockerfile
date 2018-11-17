FROM node:8.5.0

# Bundle app source
COPY src /src
# Install app dependencies
RUN cd /src; npm install; npm run compile-prod

EXPOSE  8090

WORKDIR /src/.compiled
CMD ["node", "index.js"]