FROM alpine:latest

COPY home /home

RUN apk --update add openssh bash \
  && adduser -S -h /home -s /bin/bash -g "" run \
  && echo "run:run" | chpasswd \
  && ssh-keygen -A \
  && chown -R root:root home \
  && chmod 755 /home/flag \ 
  && sed -i 's/Subsystem\tsftp/#Subsystem sftp/' /etc/ssh/sshd_config

COPY motd /etc/motd

CMD ["bash", "-c", "exec /usr/sbin/sshd -D -e \"$@\""]

EXPOSE 22

