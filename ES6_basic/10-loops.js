export default function appendToEachArrayValue(array, appendString) {
  const appendedArray = [];
  for (const [idx, value] of array.entries()) {
    appendedArray[idx] = appendString + value;
  }

  return appendedArray;
}
