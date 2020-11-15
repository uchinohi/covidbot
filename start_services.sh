cd app/
# Start rasa server with nlu model
rasa run actions
rasa train
rasa run -p $PORT -m models --credentials credentials.yml --enable-api --log-file out.log --endpoints endpoints.yml” | sed ‘s/=//’