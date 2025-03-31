export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }
  const valuesOfArray = [...set];

  const filteredValues = valuesOfArray.filter((value) => typeof value === 'string' && value.startsWith(startString));
  const mappedValues = filteredValues.map((value) => value.slice(startString.length));
  return mappedValues.join('-');
}
