/**
 * @jest-environment jsdom
 */

//Enable fake timers
jest.useFakeTimers();
jest.spyOn(global, "setTimeout");

test("remove flash message alerts", () => {
  const removeFlashMessage = require("../script");
  removeFlashMessage();
  //Test called 1 time with 3 seconds
  expect(setTimeout).toHaveBeenCalledTimes(1);
  expect(setTimeout).toHaveBeenLastCalledWith(expect.any(Function), 3000);
});
