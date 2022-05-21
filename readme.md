# Telegram listener
[![Pylint](https://github.com/alex-wahl/telegram_listener/actions/workflows/pylint.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/pylint.yml)
[![Mypy](https://github.com/alex-wahl/telegram_listener/actions/workflows/mypy.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/mypy.yml)
[![Flake8](https://github.com/alex-wahl/telegram_listener/actions/workflows/flake8.yml/badge.svg)](https://github.com/alex-wahl/telegram_listener/actions/workflows/flake8.yml)

## What does this script do?
It reads messages in the user-defined group/channel and sends them to the user-defined group/channel.
At the moment, the script only understands and sends text messages and media files.
The script can also replace some words in the sending message via keys `--word` and `--new_word`

## Preparing for the start
Before you start, you need to do a few things:

1. Get the api:hash and api_id for the account that will "listen" to the group we want. You can get this api:hash and api_id from: https://my.telegram.org/auth
2. Find out the ID of the group in which we are going to read the posts. You can google it or look it up on YouTube. In simple terms, the ID is displayed in the web version of Telegram in the address bar of your browser. Importantly, it has to be copied with a dash.
3. Find out the ID of the group we are going to send our messages to or if it has a name like @somethinglikethat we can use that as well.

Now we have all the data we need to run the script/service.

## Run the script

> **⚠ Important:**  
> The first time you run the script, it will ask you to enter your phone number and password and go through 2fa. After that the file with session will be created, which later will be used for script operation.

There are 2 ways to run the script:

1. You can run main.py directly by passing the launch parameters from the console. This method is more suitable for testing and debugging.
2. In this case the script will run as a service and in case of any errors the container will be restarted by itself.

### 1. Way - Run it as a python script

```bash
python3 main.py --api_id 09231295 --api_hash 8231ndapsa98hbqd8auhu23dnjxcsba72 --listening_group -312336552 --target_group "-21312321342"  --word old_word --new_word new_word
```

### Parameters:
> --api_id client_api_id (integer),\
> --api_hash client_api_hash (string),\
> --listening_group id of listening_group (integer),\
> --target_group id of target_group (integer),\
> --word word which should be replaced (string),\
> --new_word the new word instead of replaced word (string)


### 2. Way - Run it in a docker container
> **⚠ Important:**  
> If you run the script the first time, you should start the docker container 
> with parameter -it, so that you can interact with the telegram authentication.

Any docker container must be started with the volume mounted.
It helps you to save a session and logs.

#### Before you run a docker container, make the docker image.

```bash
docker build -t telegram_bot:v1 .
```

#### Now you are able to run your docker container
```bash
docker run -it --restart=always -v /absolute_path/to/your/root_directory_of_project:/usr/src/telegram telegram_bot:v1 --api_id 09231295 --api_hash 8231ndapsa98hbqd8auhu23dnjxcsba72 --listening_group -312336552 --target_group -93372553
```

Once you have successfully started the container and authenticated, you can just close the console (don't use ctrl-c), the script will run itself.
Next time, you can run the container without the `-it` parameter, but with the `-d` parameter. 
Because the session file has already been saved in your project root.
