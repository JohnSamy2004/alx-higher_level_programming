#!/usr/bin/node

const num = parseInt(process.argv[2], 10);

if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
