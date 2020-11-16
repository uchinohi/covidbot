FROM ubuntu:20.04
ENTRYPOINT []
COPY ./ /app/
WORKDIR /app

# Change back to root user to install dependencies
USER root
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install rasa


# By best practices, don't run the code with root user
USER 1001
# RUN chmod +x /app/start_services.sh
RUN cd /app

RUN rasa train
RUN rasa run actions
RUN rasa run --enable-api
# CMD /app/start_services.sh