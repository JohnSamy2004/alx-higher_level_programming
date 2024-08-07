#!/usr/bin/node

const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height)); // or the opposite because in square width value is euals to height value
      }
    }
  }
}

module.exports = Square;
