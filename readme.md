# Telegram listener
[![Pylint](https://github.com/alex-wahl/telegram_listener/actions/workflows/pylint.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/pylint.yml)
[![Mypy](https://github.com/alex-wahl/telegram_listener/actions/workflows/mypy.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/mypy.yml)
[![Flake8](https://github.com/alex-wahl/telegram_listener/actions/workflows/flake8.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/flake8.yml)

## What does this script do?
It reads messages in the user-defined group/channel and sends them to the user-defined group/channel.
At the moment, the script only understands and sends text messages and pictures. It doesn't send gif file, sound messages etc.

## Preparing for the start
Before you start, you need to do a few things:

1. Get the api:hash for the account that will "listen" to the group we want. You can get this api:hash from: https://my.telegram.org/auth
2. Create a telegram bot via botfather, read how to do this here: https://core.telegram.org/bots#3-how-do-i-create-a-bot
3. Save the received HTTP API token, which we will use in the future.
4. Add the bot created in step 2 to the channel or group we want to post something to.
5. Find out the ID of the group in which we are going to read the posts. You can google it or look it up on YouTube. In simple terms, the ID is displayed in the web version of Telegram in the address bar of your browser. Importantly, it has to be copied with a dash.
6. Find out the ID of the group we are going to send our messages to or if it has a name like @somethinglikethat we can use that as well.

Now we have all the data we need to run the script/service.

## Run the script

> **⚠ Important:**  
> The first time you run the script, it will ask you to enter your phone number and password and go through 2fa. After that the file with session will be created, which later will be used for script operation.

There are 2 ways to run the script:

1. You can run main.py directly by passing the launch parameters from the console. This method is more suitable for testing and debugging.
2. In this case the script will run as a service and in case of any errors the container will be restarted by itself.

### 1. Way - Run as a python script

```bash
python3 main.py -i 09231295 -s "8231ndapsa98hbqd8auhu23dnjxcsba72" -b "091237025:MAASDNBSAJIKSNd-pmc31-MNX9sas(SAdn1" -l -312336552 -g "@your_target_channel"
```

### Parameters:
> -i client_api_id (only integer),\
> -s client_api_hash (only string),\
> -b bot_token(only string),\
> -l id of listening_group (only integer),\
> -t id of target_group (as integer or as string with @)

### You can also set more explicit parameters:
```bash
python3 main.py --client_api_id 09231295 --client_api_hash "8231ndapsa98hbqd8auhu23dnjxcsba72" --bot_token "091237025:MAASDNBSAJIKSNd-pmc31-MNX9sas(SAdn1" --listening_group -312336552 --target_group "@your_target_channel"
```

### 2. Way - Run in a docker container
> **⚠ Important:**  
> If you run the script the first time, you should start the docker container 
> with parameter -it, so that you can interact with the telegram authentication.

Any docker container must be started with the volume mounted.
It helps you to save a session and logs.

#### 2.1 Before you run a docker container, make the docker image.

```bash
docker build -t telegram_bot:v1 .
```

#### 2.2 Now you are able to run your docker container
```bash
docker run -it --restart=always -v /absolute_path/to/your/root_directory_of_project:/usr/src/app telegram_bot:v1 -i 09231295 -s "8231ndapsa98hbqd8auhu23dnjxcsba72" -b "091237025:MAASDNBSAJIKSNd-pmc31-MNX9sas(SAdn1" -l -312336552 -g "@your_target_channel"
```

Once you have successfully started the container and authenticated, you can just close the console (don't use ctrl-c), the script will run itself.
Next time, you can run the container without the `-it` parameter, but with the `-d` parameter. 
Because the session file has already been saved in your project root.