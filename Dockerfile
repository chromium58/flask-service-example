# base image
FROM python:3.8.12-alpine as base
# fix for zombi processes
RUN apk add --update \
        alpine-sdk \
        tini \
    && rm -rf /var/cache/apk/*

RUN pip install --upgrade pip
ENV NON_ROOT_USER=user
RUN adduser -D $NON_ROOT_USER
USER ${NON_ROOT_USER}
ENV PATH="/home/$NON_ROOT_USER/.local/bin:$PATH"

# intermediate image
FROM base as build
COPY --chown=$NON_ROOT_USER [".", "/api"] && chmod +x /api/run.py
WORKDIR /api
RUN pip install --user .


# run tests
FROM build as test
RUN pip install --user tox
RUN tox

# release image
FROM base
EXPOSE 8080
COPY --chown=$NON_ROOT_USER --from=build ["/home/$NON_ROOT_USER/.local", "/home/$NON_ROOT_USER/.local"]
COPY --chown=$NON_ROOT_USER --from=build ["/api", "/api"]
WORKDIR /api

ENTRYPOINT ["gunicorn"]
CMD ["--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4", "run:app"]
