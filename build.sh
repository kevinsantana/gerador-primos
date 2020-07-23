#!/bin/bash

docker run -d --rm --hostname rabbit --name rabbit -e RABBITMQ_DEFAULT_USER=rabbitmq -e RABBITMQ_DEFAULT_PASS=rabbitmq rabbitmq:3-management
