export default function signUpUser(firstName, lastName) {
  const user = {
    firstName: firstName,
    lastName: lastName,
  };
  return Promise.resolve({ firstName: `${user.firstName}`, lastName: `${user.lastName}`, })
}
