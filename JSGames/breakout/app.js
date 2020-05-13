document.addEventListener("DOMContentLoaded", () => {
  // Defining the DOM elements
  const canvas = document.querySelector("canvas");
  const stage = canvas.getContext("2d");
  const score = document.querySelector("#score");
  const btn = document.querySelector("#start");

  // Defining the global variables
  const wd = 800;
  const ht = 400;

  // Bricks, Ball and Paddle Variables
  let bricks = new Array();
  let b_layers = 0;
  let b_nums = new Array();

  let ball;
  let paddle;

  // Mouse Position Variables
  let mouseX;
  let mouseY;

  // Interval Variables
  let interval;

  // Classes Defined for use in the
  function Brick(x, y, h = 20, w = 90) {
    this.x = x;
    this.y = y;
    this.h = h;
    this.w = w;

    this.color = "cadetblue";

    this.draw = function () {
      stage.fillStyle = this.color;
      stage.fillRect(this.x, this.y, this.w, this.h);
    };

    this.update = function () {
      this.draw();
    };

    this.hit = (ball) => {};
  }

  function Ball(x, y, radius) {
    this.x = x;
    this.y = y;
    this.r = radius;

    this.vx = (-24 * Math.random()) - 6;
    this.vy = (-16 * Math.random()) - 4;

    this.color = "#dadada";

    this.update = () => {
      this.update_pos();
      this.draw();
    };

    this.draw = () => {
      stage.fillStyle = this.color;
      stage.beginPath();
      stage.arc(this.x, this.y, this.r, 0, Math.PI * 2, true);
      stage.fill();
    };

    this.bound = (by_x = false) => {
      by_x ? (this.vy = -this.vy) : (this.vx = -this.vx);
    };

    this.brick_hit = function () {

    }

    this.paddle_hit = function () {

    }
  }

  function Paddle(x, y, width = 100, height = 10) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;

    this.color = "#123123";

    this.draw = () => {
      stage.fillStyle = this.color;
      stage.fillRect(
        this.x - this.width / 2,
        this.y - this.height / 2,
        this.width,
        this.height
      );
    };

    this.update = () => {
      this.x = mouseX;
      this.draw();
    };

    this.hit = (ball) => {};
  }

  function MouseEvent(event) {
	  this.evt = event ? event : window.event;
	  this.x = event.pageX ? event.pageX : event.clientX;
	  this.y = event.pageY ? event.pageY : event.clientY;
  }

  function create_bricks(brick_wd = 90, brick_ht = 20) {
    let x_offset = 0;
    let y_offset = 10;
    let line_ht = brick_ht + 10;
    let unit_wd = brick_wd + 10;

    for (let i = 0; i < b_layers; i++) {
      x_offest = Math.floor((wd - (b_nums[i] * unit_wd - 10)) / 2);
      for (let j = 0; j < b_nums[i]; j++) {
        var brick = new Brick(x_offset + j * unit_wd, y_offset);
        bricks.push(brick);
      }
      y_offset += line_ht;
    }
  }

  // For drawing on the canvas
  function draw() {
    stage.clearRect(0, 0, wd, ht);
    // for (i = 0; i < bricks.length; i++) bricks[i].draw();
    bricks.forEach(element => {
      element.update();
    })
    ball.update();
    paddle.update();
  }

  function check() {

    let flag = false;

    if(!flag && paddle.hit(ball)){
      ball.paddle_hit();
      flag = true;
    }
    
    if(!flag && bricks_hit(ball)){
      ball.brick_hit();
      flag = true;
    }

    if(!flag) {
      ball.bound()
    }
  }


  // Interval and Mouse Functions
  function loop() {
    draw();
    check();
  }

  function getMousePostion(event) {
	  let e = MouseEvent(event);
	  let r = canvas.getBoundingClientRect();
	  mouseX = e.x - r.left;
	  mouseY = e.y - r.top;    
  }

  // Init Game
  function init() {
    b_layers = 5;
    b_nums = [8, 7, 8, 7, 8];
    create_bricks();
    ball = new Ball(400, 375, 5);
    paddle = new Paddle(400, 385);

    window.onmousemove = getMousePostion;
    interval = setInterval(loop, 1000 / 30);
  }
  
  btn.addEventListener("click", init);
});
