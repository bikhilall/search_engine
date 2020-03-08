FROM node:10.16.0-jessie

# RUN npm install yarn -g
# working directory
WORKDIR /usr/src/web_app

# install and cache app dependencies
COPY backend/package.json backend/package.json
RUN cd backend && npm install

COPY frontend/package.json frontend/package.json
RUN cd frontend && npm install

#
COPY . .

# build front end
RUN cd frontend && npm run-script build

EXPOSE 3001

ENTRYPOINT ["npm"]

# start app
CMD ["start", "--prefix", "backend"]