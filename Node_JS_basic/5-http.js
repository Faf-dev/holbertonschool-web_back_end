const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });

    let output = 'This is the list of our students\n';
    const { log } = console.log;
    const tempLog = (...args) => {
      output += `${args.join(' ')}\n`;
    };
    console.log = tempLog;

    countStudents(database)
      .then(() => {
        console.log = log;
        res.end(output.trim());
      })
      .catch((err) => {
        console.log = log;
        res.end(output + err.message);
      });
  }
});

app.listen(1245);
module.exports = app;
