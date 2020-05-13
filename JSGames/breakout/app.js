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
  function Brick(x, y, h = 20, w = 80) {
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

    this.hit = (ball) => {
      if(ball.vx > 0 && ball.x+ball.r+ball.vx > this.x && ball.x+ball.r < this.x && ball.y > this.y && ball.y < this.y + this.h) return 4;
      if(ball.vx < 0 && ball.x-ball.r+ball.vx < this.x+this.w && ball.x-ball.r > this.x + this.r && ball.y > this.y && ball.y < this.y + this.h) return 2;
      if(ball.vy > 0 && ball.y+ball.r+ball.vy > this.y && ball.y+ball.r < this.y && ball.x > this.x && ball.x < this.x + this.w) return 1;
      if(ball.vx < 0 && ball.y-ball.r+ball.vy < this.y+this.h && ball.y-ball.r > this.y + this.h && ball.x > this.x && ball.x < this.x + this.w) return 3;
      return 0;
    };
  }

  function Ball(x, y, radius) {
    this.x = x;
    this.y = y;
    this.r = radius;

    this.vx = (16 * Math.random()) - 8 ;
    this.vy = (-4 * Math.random());

    this.color = "#222222";

    this.update_pos = () => {
      // let flag = false;

      if(paddle.hit(this)){
        this.paddle_hit();
        // flag = true;
        return;
      }
      
      if(bricks_hit(ball)){
        ball.brick_hit();
        // flag = true;
        return;
      }
  
      if(true) {
        ball.bound()
        return;
      }   
    }

    this.draw = () => {
      stage.fillStyle = this.color;
      stage.beginPath();
      stage.arc(this.x, this.y, this.r, 0, Math.PI * 2, true);
      stage.fill();
    };

    this.update = () => {
      this.update_pos();
      this.draw();
    };

    this.bound = () => {
      
      let flag_x=true, flag_y=true;
      
      if(this.vx>0 && this.x+this.vx+this.r > wd){
        this.vx *= -1;
        this.x = wd-this.r;
        flag_x = false;
      }

      if(this.vx<0 && (this.x+this.vx)-this.r < 0){
        this.vx *= -1;
        this.x = this.r;
        flag_x = false;
      }

      if(this.vy<0 && (this.y+this.vy)-this.r < 0){
        this.vy *= -1;
        this.y = this.r;
        flag_y = false;
      }

      if(flag_y) this.y += this.vy;
      if(flag_x) this.x += this.vx;
    };

    this.brick_hit = function () {
      let hits = [];
      let flag_x=true, flag_y=true;
      let temp = [];
      for(let i=0;i<bricks.length;i++){
        let t = bricks[i].hit(this);
 
        switch(t) {
          case 0:
            hits.push(true);
            temp.push(bricks[i]);
            break;
          case 1:
            hits.push(false);
            this.vy *= -1;
            this.y = bricks[i].y - this.r;
            flag_y = false;
            break;
          case 3:
            hits.push(false);
            this.vy *= -1;
            this.y = bricks[i].y + this.r + bricks[i].h;
            flag_y = false;
            break;
          case 3:
            hits.push(false);
            this.xy *= -1;
            this.x = bricks[i].x + this.r + bricks[i].w;
            flag_x = false;
            break;
          case 4:
            hits.push(false);
            this.xy *= -1;
            this.x = bricks[i].x - this.r;
            flag_x = false;
            break;
        }
      }

      if(flag_x) this.x += this.vx;
      if(flag_y) this.y += this.vy;

      // See how to use filter method
      console.log(bricks.length);
      bricks = temp;
      console.log(bricks.length);
    }

    this.paddle_hit = function () {
      let offset = this.x - paddle.x;
      this.y = paddle.y - this.r;
      this.x += this.vx;
      this.vx = this.vx + (this.vx*offset*0.1)/paddle.width;
      this.vy *= -1;
      console.log(this.vy, this.x, this.y,this.vx);
    }
  }

  function Paddle(x, y, width = 100, height = 10) {
    this.x = x;
    this.y = y;
    this.width = width;
    this.height = height;

    this.color = "#123123";

    this.update_pos = () => {
      if(mouseX > 0 && mouseX < wd && mouseY > 0 && mouseY < ht){
        this.x = mouseX;
      }
    }

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
      this.update_pos();
      this.draw();
    };

    this.hit = (ball) => {
      if(
        (ball.vy > 0)  && 
        (ball.y+ball.r+ball.vy > paddle.y) && 
        (ball.y+ball.r < paddle.y) && 
        (ball.x > (paddle.x - (paddle.width/2))) && 
        (ball.x < (paddle.x+(paddle.width/2)))
      ){
        console.log(1);
        return true;
      }
      return false;
    };
  }

  function create_bricks(brick_wd = 80, brick_ht = 20) {
    let x_offset = 0;
    let y_offset = 10;
    let line_ht = brick_ht + 10;
    let unit_wd = brick_wd + 10;

    for (let i = 0; i < b_layers; i++) {
      x_offset = Math.floor((wd - ((b_nums[i] * unit_wd) - 10)) / 2);
      for (let j = 0; j < b_nums[i]; j++) {
        var brick = new Brick(x_offset + j * unit_wd, y_offset);
        bricks.push(brick);
      }
      y_offset += line_ht;
    }
  }

  function bricks_hit() {
    let flag = false;
    let t;
    bricks.forEach((element) => {
      t = element.hit(ball);
      if(t!==0){
        flag=true;

      }
    })
    return flag;
  }

  // For drawing on the canvas
  function draw() {
    stage.clearRect(0, 0, wd, ht);
    // for (i = 0; i < bricks.length; i++) bricks[i].draw();
    ball.update();
    bricks.forEach(element => {
      element.update();
    })
    paddle.update();
  }

  function check() {
    if(bricks.length === 0){
      clearInterval(interval);
      alert("You won");
    }

    if(ball.vy > 0 && ball.y+ball.r > paddle.y && !paddle.hit(ball)){
      clearInterval(interval);
      alert("You lose");
    }
  }


  // Interval and Mouse Functions
  function loop() {
    draw();
    check();
  }

  function getMousePostion(event) {
	  // let e = MouseEvent(event);
	  let r = canvas.getBoundingClientRect();
    let x = event.pageX || event.clientX;
    let y = event.pageY || event.clientY;
    mouseX = x - r.left;
    mouseY = y - r.top; 
    paddle.update();   
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
