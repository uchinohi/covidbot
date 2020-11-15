FROM ubuntu:20.04
ENTRYPOINT []
COPY ./ /app/
RUN apt-get update && apt-get install -y python3 python3-pip && pip3 install rasa[spacy] && python3 -m spacy download en_core_web_md && python3 -m spacy link en_core_web_md en && pip3 install requests
RUN chmod +x /app/start_services.sh
CMD /app/start_services.sh