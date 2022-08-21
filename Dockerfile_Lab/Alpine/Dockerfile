# use alpine as base image
FROM alpine:latest as builder
# upgrade all alpine packages
RUN apk update && apk upgrade
# add your script into container fs
ADD docker_entrypoint.sh docker_entrypoint.sh
RUN chmod u+x docker_entrypoint.sh

# stage 2
FROM scratch

# shell
COPY --from=builder /bin/sh /bin/sh

ENV PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENTRYPOINT ["./docker_entrypoint.sh"]
