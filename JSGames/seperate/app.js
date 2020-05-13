document.addEventListener("DOMContentLoaded", () => {
  // DOM Elements
  btn = document.querySelector("#start");
  canvas = document.querySelector("canvas");
  stage = canvas.getContext("2d");
  clock = document.querySelector("#time");

  // Global Variables
  const wd = 800,
    ht = 400,
    nballs = 30;
  let sep;
  let balls = [];
  let mouseX, mouseY;
  let x_left, x_right;
  let colors = ["blue", "red"];
  let time;
  let loopInterval, timeInterval;

  // Class Definitions
  function Ball(x, y, radius = 5) {
    this.x = x;
    this.y = y;
    this.r = radius;
    this.color = colors[Math.floor(Math.random() * 2)];
    this.vx = -10 + Math.random() * 20;
    this.vy = -10 + Math.random() * 20;

    this.draw = () => {
      stage.fillStyle = this.color;
      stage.beginPath();
      stage.arc(this.x, this.y, this.r, 0, Math.PI * 2, true);
      stage.fill();
    };

    this.update_pos = () => {
	  // If the ball collides with the seperator
      if (sep.collide(this)) {	
        this.vx *= -1;
        if(this.x < x_left){
          this.x = x_left-this.r;
          this.y += this.vy;
        }
        else{
          this.x = x_right+this.r;
          this.y += this.vy;
        }
      } 
      else{
        this.bound();
      }
    };

    this.update = () => {
      this.update_pos();
      this.draw();
    };
    
    this.bound = () => {

      let flag_y=false, flag_x=false;

      if(this.vy > 0 && this.y+this.r+this.vy > ht){
        this.vy *= -1;
        this.y = ht-this.r;
        flag_y=true;
      }

      if(this.vy < 0 && this.y-(this.r+this.vy) < 0){
        this.vy *= -1;
        this.y = this.r;
        flag_y = true;
      }

      if(this.vx < 0 && this.x-(this.r+this.vx) < 0){
        this.vx *= -1;
        this.x = this.r;
        flag_x = true;
      }

      if(this.vx > 0 && this.x+(this.r+this.vx) > wd){
        this.vx *= -1;
        this.x = wd-this.r;
        flag_x = true;
      }

      if(!flag_x){
        this.x += this.vx;
      }

      if(!flag_y){
        this.y += this.vy;
      }
    };
  }

  function Seperator(gap, x = wd / 2, y = ht / 2, width = 10) {
    this.x = x;
    this.y = y;
    this.w = width;
    this.g = gap;

    // console.log(this.x, this.y, this.w, this.g);

    x_left = this.x - (this.w/2);
    x_right = this.x + (this.w/2);

    this.color = "rgb(100,100,100)";

    this.draw = () => {
      h_upper = Math.max(0,this.y - (this.g / 2));
      h_lower = Math.max(0,ht - (this.y + (this.g / 2)));
      stage.fillStyle = this.color;
      stage.fillRect(x_left, 0, this.w, h_upper);
      stage.fillRect(x_left, ht - h_lower, this.w, h_lower);
    };

    this.update_pos = () => {
		if(mouseX>0 && mouseX<wd && mouseY>0 && mouseY<ht){
			this.y = mouseY;
		}
	};

    this.update = () => {
      this.update_pos();
      this.draw();
    };

    this.collide = (ball) => {
      let flag_x = false, flag_y = false;

      if (ball.x < x_left && ball.vx > 0) {
        flag_x = ball.x + ball.vx > x_left - ball.r;
      } 
      else if(ball.x > x_right && ball.vx < 0) {
        flag_x = ball.x + ball.vx < x_right + ball.r;
      }

      flag_y = ball.y < this.y - (this.g / 2) + (ball.r / 2);
      flag_y = ball.y > this.y + (this.g / 2) - (ball.r / 2) || flag_y;
      return (flag_y && flag_x);
    };
  }

  // function MouseEvent(event) {
	//   this.evt = event ? event : window.event;
	//   this.x = event.pageX ? event.pageX : event.clientX;
	//   this.y = event.pageY ? event.pageY : event.clientY;
  // }

  // Create Balls
  function create_balls() {
    for (let i = 0; i < nballs; i++) {
      let ball = new Ball(Math.random() * 800, Math.random() * 400);
      balls.push(ball);
    }
  }

  // Drawing and Checking Functions
  function draw() {
    stage.clearRect(0, 0, wd, ht);
    sep.update();
    balls.forEach((element) => {
      element.update();
    });
  }

  function check() {
    let flag = true;
    let color;
    for (let i = 0; i < nballs; i++) {
      color = balls[i].color;
      if (color === colors[0] && balls[i].x > x_right) {
        flag = false;
        break;
      } else if (color === colors[1] && balls[i].x < x_left) {
        flag = false;
        break;
      }
    }

    if (flag) {
      clearInterval(loopInterval);
      clearInterval(timeInterval);
      alert("You won");
    }
  }

  // Interval and Mouse Functions
  function loop() {
    draw();
    check();
  }

  function timer() {
    time += 1;
    clock.innerText = time;
  }

  function getMousePostion(event) {
	  // let e = MouseEvent(event);
    let r = canvas.getBoundingClientRect();
    let x = event.pageX || event.clientX;
    let y = event.pageY || event.clientY;
	  mouseX = x - r.left;
    mouseY = y - r.top;
    sep.update();
  }

  // Game Starting Function
  function init() {
    sep = new Seperator(60);
    create_balls();
	  time = 0;
	
	  window.onmousemove = getMousePostion;
    loopInterval = setInterval(loop, 1000 / 30);
    timeInterval = setInterval(timer, 1000);
  }

  btn.addEventListener("click", init);
});
