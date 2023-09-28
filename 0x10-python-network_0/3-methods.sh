#!/bin/bash
# display all http methods
curl -sI "$1" | grep 'ALLOW' | cut -b 8-
