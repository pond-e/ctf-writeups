FROM python:3.9-alpine as flag-creator
ARG FLAG=flag{this_is_a_fake_flag}
COPY GenShinGothic-Bold.ttf .
RUN pip install Pillow
COPY create_flag.py .
ENV FLAG=$FLAG
RUN python create_flag.py

FROM node:21-alpine
WORKDIR /app
COPY app.js package.json GenShinGothic-Bold.ttf ./
COPY ./views/ ./views/
RUN npm install
COPY --from=flag-creator flag.png /flag.png

EXPOSE 3000
ENV NODE_ENV=production
CMD ["node", "app.js"]
