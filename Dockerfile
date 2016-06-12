FROM alpine
MAINTAINER Sudeep Reddy Eleti <sudeepreddyeleti@gmail.com>
RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install Bottle requests

COPY weatherbot.py .
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["weatherbot.py"]
