FROM alpine
RUN apk add make sudo perl python3 py3-pip
RUN apk add --no-cache netcat-openbsd
WORKDIR /security
COPY . .