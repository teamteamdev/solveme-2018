FROM alpine:latest
# Tell that we need some ports
EXPOSE 5000
# Install required packages
RUN apk add -U python3 curl
# Set up permissions
RUN adduser -h /app -s /bin/sh -D flask
# Install dependencies
COPY --chown=flask:flask ./requirements.txt /app/requirements.txt
RUN pip3 install -Ur /app/requirements.txt --no-cache-dir
# Copy application
COPY --chown=flask:flask templates/base.html templates/index.html /app/templates/
COPY --chown=flask:flask app.py /app/app.py
# Configure entry point
USER flask:flask
WORKDIR /app
HEALTHCHECK --interval=1m --timeout=3s --start-period=5s CMD curl -f http://localhost:5000/ || exit 1
ENTRYPOINT ["/usr/bin/python3", "/app/app.py"]

