document.addEventListener("DOMContentLoaded", () => {
  // DOM Elements
  const grid = document.querySelector(".grid");
  const squares = document.querySelectorAll(".grid div");
  const startBtn = document.querySelector(".start");
  const scoreDisplay = document.querySelector("#score");

  // Other Constants
  const width = 12;
  const shapes = [];

  // Variables
  let curShape = [];
  let check_grid;

  // Functions
  function start() {}

  function control(e) {
    curShape.forEach((index) => squares[index].classList.remove("block"));

    switch (e.keyCode) {
      case 39:
        shift_shape(1);
        break;
      case 37:
        shift_shape(-1);
        break;
      // Write a case for rotation
    }

    curShape.forEach((index) => squares[index].classList.add("block"));
    check();
  }

  function check() {}

  function random_shape() {}

  document.addEventListener("keyup", control);
  document.addEventListener("click", start);
});
