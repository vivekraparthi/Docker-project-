#FROM ubuntu:20.04
#FROM python:3.9
FROM alpine

RUN apk add --no-cache python3

#RUN apt-get update && apt-get install -y python3.9 python3.9-dev
ADD /Limerick.txt /home/data/Limerick.txt
ADD /IF.txt /home/data/IF.txt
ADD /main.py /home/main.py
RUN mkdir -p /home/output/
CMD ["/home/main.py"]
ENTRYPOINT ["python3"]