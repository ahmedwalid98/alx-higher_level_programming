#!/bin/bash
# display all http methods
curl -siX OPTIONS "$1" | tail -n 3 | head -n 1 | cut -b 8-
