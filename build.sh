#!/usr/bin/env bash

# System dependencies
apt-get update && apt-get install -y \
    python3-dev \
    gcc \
    libportaudio2 \
    portaudio19-dev \
    libasound2-dev

# Python environment
python -m pip install --upgrade pip
pip install wheel setuptools

# Install requirements
pip install -r requirements.txt