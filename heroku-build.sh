#!/bin/sh

# Navigate to the frontend and build it
cd frontend
npm install
npm run build

# Copy the build output to the Spring Boot static directory
rm -rf ../backend/src/main/resources/static/*
cp -r build/* ../backend/src/main/resources/static/

# Navigate to the backend and build it
cd ../backend
mvn clean install