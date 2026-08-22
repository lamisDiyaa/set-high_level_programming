#!/bin/bash
# Sends a JSON POST request with contents of a file to a URL
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
