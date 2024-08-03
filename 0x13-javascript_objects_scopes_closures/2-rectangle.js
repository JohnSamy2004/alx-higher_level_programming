#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // leaves it empty or assign arguments with undefined
      // this.width = undefined;
      // this.height = undefined;
    }
  }
}

module.exports = Rectangle;
