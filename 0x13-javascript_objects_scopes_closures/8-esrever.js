#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  for (let i = 0; i < list.length; i++) {
    newArray[i] = list[list.length - i - 1];
  }
  return newArray;
};
