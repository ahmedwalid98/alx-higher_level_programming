#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (err, res, body) => {
  if (!err) console.log(res.statusCode);
});
