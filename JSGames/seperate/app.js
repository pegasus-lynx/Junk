document.addEventListener('DOMContentLoaded', () => {
	// DOM Elements
	btn = document.querySelector('#start')
	canvas = document.querySelector('canvas')
	stage = canvas.getContext("2d")
	clock = document.querySelector("#time")

	// Global Variables
	const wd=800, ht=400, nballs=60;
	let sep, balls;
	let colors = ['blue', 'red'];
	let time;
	let loopInterval, timeInterval;

	// Class Definitions
	function Ball(x,y,radius=5) {
		this.x = x;
		this.y = y;
		this.r = radius;
		this.color = colors[Math.floor(math.random()*2)]
		this.vx = -10 + (Math.random()*20);
		this.vy = -10 + (Math.random()*20);

		
		this.draw = () => {
			stage.fillStyle = this.color
			stage.beginPath()
			stage.arc(this.x, this.y, this.r, 0, Math.PI*2, true);
			stage.fill();
		}

		this.update_pos = () => {
			
			let x = this.x;
			let y = this.y;
			let r = this.r;
			
			if(y+r < sep.y - (sep.g/2) || y+r > sep.y + (sep.g/2)){
				if(x+r)
			}

			if(sep.collide(this)){
				this.vx *= -1;
				if(x<)
			}
			else{
				this.x = x+this.vx;
				this.y = y+this.vy;
			}


		};

		this.update = () => {
			this.update_pos();
			this.draw();
		};
	}

	function Seperator(gap, x=wd/2, y=ht/2, width=10) {
		this.x = x;
		this.y = y;
		this.w = width;
		this.gap = gap;

		this.color = 'rgb(100,100,100)';

		this.draw = () => {
			
			x_left = this.x - (this.width/2);
			h_upper = this.y - (this.g/2);
			h_lower = ht - (this.y + (this.g/2));

			stage.fillStyle = this.color;
			stage.fillRect(x_left,0,this.width,h_upper);
			stage.fillRect(x_left,ht-h_lower,this.width,h_lower);
		}

		this.update_pos = () => {

		}

		this.update = () => {
			this.update_pos();
			this.draw();
		}
	}

	// Create Balls
	function create_balls() {
		for(let i=0;i<nballs;i++){
			let ball = new Ball(Math.random()*800, Math.random()*400);
			balls.push(ball);
		}
	}

	// Drawing and Checking Functions
	function draw() {
		stage.clearRect(0,0,wd,ht);
		sep.update();
		balls.forEach(element => {
			element.update()
		});
	}

	function check() {
		let flag = true
		let color;
		for(let i=0;i<nballs;i++){
			color = balls[i].color;
			if(color === colors[0] && balls[i].x > x_right){
				flag = false;
				break;
			}
			else if(color === colors[1]&& balls[i].x < x_left){
				flag = false;
				break;
			}
		}


		if(flag){
			clearInterval(loopInterval);
			clearInterval(timeInterval);
			console.alert("You won");
		}
	}

	// Interval Functions
	function loop() {
		draw();
		check();
	}

	function timer() {
		time += 1;
		clock.innerText = time; 
	}

	// Game Starting Function
	function init() {
		sep = new Seperator(60);
		create_balls();

		time = 0;

		loopInterval = setInterval(loop,1000/30);
		timeInterval = setInterval(timer,1000);
	}

	btn.addEventListener("click", init);
})