#!/usr/bin/env bash

apt-get update && apt-get install -y portaudio19-dev

pip install --upgrade pip
pip install -r requirements.txt
