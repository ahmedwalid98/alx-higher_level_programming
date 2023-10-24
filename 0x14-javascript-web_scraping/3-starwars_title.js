#!/usr/bin/node
const { argv } = require('process');
const request = require('request');
request.get(`https://swapi-api.alx-tools.com/api/films/${argv[2]}`,
  (error, response, body) => {
    if (!error) console.log(JSON.parse(body).title);
  });
