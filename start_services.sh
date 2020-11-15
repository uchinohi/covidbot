cd app/
# Start rasa server with nlu model
rasa run actions \
        -p $PORT
rasa train
rasa run --model models --enable-api --cors "*" --debug \
         -p $PORT