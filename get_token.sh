#!/bin/bash

while true
    do
        python get_token.py
        git commit -am "change token"
        git push origin main
        sleep 60
    done
