FROM alpine:latest
# Tell that we need some ports
EXPOSE 5000
# Copy app, set up permissions and install dependencies
COPY requirements.txt app.py /app/
COPY templates/base.html templates/index.html /app/templates/
RUN adduser -h /app -s /bin/sh -D flask && apk add --no-cache python3 && \
        pip3 install -Ur /app/requirements.txt --no-cache-dir
# Configure entry point
USER flask:flask
WORKDIR /app
ENTRYPOINT ["/usr/bin/python3", "/app/app.py"]

