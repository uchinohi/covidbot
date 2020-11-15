cd app/
# Start rasa server with nlu model
rasa train
rasa run actions -p $PORT | sed 's/=//'
rasa run -p $PORT | sed 's/=//'