FROM node:10.16.0-jessie

# working directory
WORKDIR /usr/src/web_app

# install and cache app dependencies
COPY backend/package.json backend/package.json
RUN cd backend && npm install --silent

COPY frontend/package.json frontend/package.json
RUN cd frontend && npm install --silent

#
COPY . .

# build front end
RUN cd frontend && npm run-script build

EXPOSE 3001

# start app
RUN cd backend 
CMD cd backend && npm start