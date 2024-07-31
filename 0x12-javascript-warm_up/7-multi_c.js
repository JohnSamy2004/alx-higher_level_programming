#!/usr/bin/node

const num = parseInt(process.argv[2], 10);
const sen = 'C is fun';

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log(sen);
  }
}
