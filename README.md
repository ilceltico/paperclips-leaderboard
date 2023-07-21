Leaderboard for Universal Paperclips
=======================

[Universal Paperclips](https://www.decisionproblem.com/paperclips/) is a popular clicker game by Frank Lantz, all rights to him!

I wanted to play the game with friends in a competitive way to see who can finish it first, or who can create the most paperclips in a limited amount of time, so I decided to create a mechanism to retrieve the number of paperclips from each player and display it in a leaderboard. 

This makes the game so fun to play in groups!

![](img/demo.gif)


This is a small project developed for personal reasons in a few hours. It's a bit hacky and not refined, but it does work so I decided to share it. Feel free to contribute!

The leaderboard web UI is a slightly modified version of [this project](https://github.com/tgogos/leaderboard), support the original creator!

How it works
----------------

The games are executed on Chrome instances via Selenium, and the number of paperclips produced is retrieved by Selenium every 2 seconds. This number is sent to an MQTT server, which serves as a message broker.
The leaderboard is a simple web UI executed on another Chrome instance via Selenium: it retrieves the scores from the MQTT server by subscribing to it, and it displays them nicely (hopefully) every 5 seconds. You can run multiple leaderboards on multiple devices if so you wish.

### More details
One device needs to host a private MQTT server that will receive the messages from all the players and is located in a Docker image.

One device (it could be the same or another one) will host the leaderboard, which is a simple local website handled with Selenium which receives the MQTT messages from the server and caches them.

All the players will play the original game from the original website through a Selenium instance, and their scores will be sent to the MQTT server.

The device hosting the MQTT server and/or the leaderboard can also be used by a player. All the scripts contain a variable for the IP and Port to connect to, and one just needs to set them correctly (IP of another device, or localhost). This implies that all devices should either have a public IP or be in the same local network.

The information is sent to the MQTT server every 2 seconds.

The leaderboard is upadated every 5 seconds.

If the leaderboard crashes, it can be restarted without impacting the games.

If a game crashes or is closed by the user, it can be restarted with the same username and it will load the game cache from the local directory, so don't worry.

Everything should be platform-independent, but I only tested on macOS.

Pre-requisites
----------------

### MQTT server

1. Install Docker from the official website

   This step is only required for the device that will host the MQTT server.

### Leadeboard and players

Make sure to have Chrome installed and updated

1. Install Python, with or without Conda

2. Install Selenium 4

   `pip install selenium`

   Note: Conda installs Selenium 3, so make sure to install Selenium 4 with Pip

3. Install the Python MQTT client

   `pip install paho-mqtt`


Usage
------------------

1. Run the MQTT server

   `docker run -d --name emqx -p 1883:1883 -p 8083:8083 -p 8084:8084 -p 8883:8883 -p 18083:18083 emqx/emqx`

   Might need sudo, depending on your docker installation

2. Start the leaderboard

   You can specify in the file the IP and Port of the MQTT server. It can be localhost, of course.

   `python leaderboard.py`

3. Start the game

   You can specify in the file the IP and Port of the MQTT server. It can be localhost, of course.

   `python paperclips.py`

   It will ask you for your username to be displayed in the leaderboard.

   It will also use such username to save the game cache in your local directory.

