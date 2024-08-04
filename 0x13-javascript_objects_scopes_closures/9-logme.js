#!/usr/bin/node

exports.logMe = function (item) {
	let count = 0;
	this.item = item;

	if (this.item) {
		console.log(count: this.item);
		count++;
	}
}
