#!/bin/bash

docker container run --name gerar_primos --network backend -p 3000:3000 gerar_primos:1.0.0
