#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

function fact (num) {
  if (isNaN(num) || num === 1 || num <= 0) {
    return (1);
  } else {
    return (num * fact(num - 1));
  }
}
console.log(fact(num));
