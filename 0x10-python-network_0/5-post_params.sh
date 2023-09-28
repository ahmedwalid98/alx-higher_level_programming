#!/bin/bash
# sending post req with body
curl -s --data "email=test@gmail.com&subject=I will always be here for PLD" "$1"
