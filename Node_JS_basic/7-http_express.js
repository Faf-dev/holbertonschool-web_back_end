const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  let output = 'This is the list of our students\n';
  const { log } = console.log;
  const tempLog = (...args) => {
    output += `${args.join(' ')}\n`;
  };
  console.log = tempLog;
  try {
    await countStudents(database);
    console.log = log;
    res.send(output.trim());
  } catch (err) {
    console.log = log;
    res.status(500).send(`${output}${err.message}`);
  }
});

app.listen(port);
module.exports = app;
