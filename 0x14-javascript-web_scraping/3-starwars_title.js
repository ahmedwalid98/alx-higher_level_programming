#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`)
  .on('response', (res) => {
    console.log(res.title);
  });
