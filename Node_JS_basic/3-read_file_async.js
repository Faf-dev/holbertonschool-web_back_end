const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');
    if (lines.length <= 1) {
      console.log('Number of students: 0');
      return;
    }
    const students = lines.slice(1).map((line) => line.split(','));
    const FieldsCs = [];
    const FieldsSwe = [];
    let total = 0;
    for (const student of students) {
      if (student.length >= 4) {
        const [firstname, , , field] = student;
        if (field === 'CS') {
          FieldsCs.push(firstname);
          total += 1;
        }
        if (field === 'SWE') {
          FieldsSwe.push(firstname);
          total += 1;
        }
      }
    }
    console.log(`Number of students: ${total}`);
    if (FieldsCs.length > 0) {
      console.log(`Number of students in CS: ${FieldsCs.length}. List: ${FieldsCs.join(', ')}`);
    }
    if (FieldsSwe.length > 0) {
      console.log(`Number of students in SWE: ${FieldsSwe.length}. List: ${FieldsSwe.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
