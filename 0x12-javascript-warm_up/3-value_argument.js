#!/usr/bin/node

if (process.argv === process.argv[1]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
