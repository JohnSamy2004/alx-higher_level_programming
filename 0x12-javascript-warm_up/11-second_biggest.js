#!/usr/bin/node

let max = [];
let sec = null;
let i;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  for (i = 2; i < process.argv.length; i++) {
    const num = parseInt(process.argv[i], 10);
    if (num > max) {
      sec = max;
      max = num;
    } else if (num > sec && num < max) {
      sec = num;
    }
  }
  console.log(sec);
}
/* or
 * #!/usr/bin/node
 * searches the second biggest integer in the list of arguments.
 *
 * if (process.argv.length <= 3) {
 *  console.log(0);
 *  } else {
 * const list = process.argv.sort();
 * console.log(list.reverse()[1]);
 * }
 **/
