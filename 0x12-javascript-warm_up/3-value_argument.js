#!/usr/bin/node
const argv = process.argv;
console.log(typeof argv[2] === 'undefined' ? 'No argument' : argv[2]);
