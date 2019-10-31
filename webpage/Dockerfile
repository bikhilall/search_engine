FROM node:10.16.0-jessie

RUN npm install yarn -g
# working directory
WORKDIR /usr/src/web_app

# install and cache app dependencies
COPY backend/package.json backend/package.json
RUN cd backend && yarn

COPY frontend/package.json frontend/package.json
RUN cd frontend && yarn

#
COPY . .

# build front end
RUN cd frontend && npm run-script build

EXPOSE 3001

# start app
CMD npm start --prefix backend