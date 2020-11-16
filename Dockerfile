FROM ubuntu:20.04
ENTRYPOINT []
COPY ./ /app/
WORKDIR /app

# Change back to root user to install dependencies
USER root
RUN apt-get update && apt-get install -y python3 python3-pip && python3 -m pip install --upgrade pip && pip install rasa --use-feature=2020-resolver


RUN chmod +x /app/start_services.sh

RUN cd /app


CMD /app/start_services.sh