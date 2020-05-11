document.addEventListener("DOMContentLoaded", () => {
  // Defining the global variables to be usedby all the functions
  const canvas = document.querySelector("canvas");
  const stage = canvas.getContext("2d");

  const score = document.querySelector("#score");
  const btn = document.querySelector("#start");

  const wd = 800;
  const ht = 400;

  let bricks = new Array();
  let b_layers = 0;
  let b_nums = new Array();
  let interval;

  // Init Game
  function init() {
    b_layers = 5;
    b_nums = [8, 7, 8, 7, 8];
    create_bricks();
    interval = setInterval(loop, 1000 / 30);
  }

  function loop() {
    draw();
    check();
  }

  function draw() {
    // Functions for drawing the ball and the bricks
  }

  function create_bricks(brick_wd = 90, brick_ht = 20) {
    let x_offset = 0;
    let y_offset = 10;
    let line_ht = brick_ht + 10;
    let unit_wd = brick_wd + 10;

    for (let i = 0; i < b_layers; i++) {
      x_offest = Math.floor((wd - (b_nums[i] * unit_wd - 10)) / 2);
      for (let j = 0; j < b_nums[i]; j++) {
        bricks.push(Brick(x_offset + j * unit_wd, y_offset));
      }
      y_offset += line_ht;
    }
  }

  // Classes Defined for use in the
  function Brick(x, y, h = 20, w = 90) {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;

    this.color = "#111111";

    this.draw = () => {};

    this.update = () => {};
  }

  function Ball(x, y, radius) {
    this.x = x;
    this.y = y;
    this.r = radius;

    this.vx = 0;
    this.vy = 0;

    this.color = "#dadada";

    this.update = () => {
      this.x += this.vx;
      this.y += this.vy;
      this.bound();
      this.draw();
    };

    this.draw = () => {
      stage.fillStyle = this.color;
      stage.beginPath();
      stage.arc(this.x, this.y, this.r, 0, Math.PI * 2, true);
      stage.fill();
    };

    this.bound = () => {};

    this.reflect = function (by_x = false) {
      by_x ? (this.vy = -this.vy) : (this.vx = -this.vx);
    };
  }
});
