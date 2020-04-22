document.addEventListener('DOMContentLoaded', () => {

	const squares = document.querySelectorAll('.grid div')
	const startBtn = document.querySelector('.start')
	const scoreDisplay = document.querySelector('span')

	const width = 15

	let invaders = [0,1,2,3,4,15,16,17,18,19]
	let bullets = []
	let currentIndex = 128
	let direction = 1
	
	let score = 0 
	
	let speed = 0.5
	let intervalTime = 1000

	let intStep = 0
	let intBult = 0
	let intInv  = 0
	
	

	// to start
	function startGame() {
		
		removeInvaders()
		removeBullets()
		squares[currentIndex].classList.remove('player')
		
		clearInterval(intStep)
		clearInterval(intBult)
		clearInterval(intInv)
		
		score = 0
		direction = 1
		scoreDisplay.innerText = score
		
		invaders = [0,1,2,3,4,15,16,17,18,19]
		bullets = []
		currentIndex = 128

		colorInvaders()
		squares[currentIndex].classList.add('player')

		intStep = setInterval(step, intervalTime*0.5)
		intBult = setInterval(moveBullets, intervalTime*0.5)
		intInv = setInterval(moveInvader,intervalTime)
	}

	// invader functions
	function removeInvaders() {

		invaders.forEach(index => squares[index].classList.remove('invader'))
	}

	function colorInvaders() {
		
		invaders.forEach(index => squares[index].classList.add('invader'))	
	}

	function shiftInvaders(direction) {
		for(i=0;i<invaders.length;i++){
			invaders[i] += direction
		}
	}

	function moveInvader(){
		let maxCol = -1
		let minCol = 15
		invaders.forEach(index => {
			maxCol = Math.max(maxCol, index%15)
			minCol = Math.min(minCol, index%15)
		})

		console.log(maxCol)
		console.log(minCol)

		if((direction === 1 && maxCol === 14) || (direction === -1 && minCol===0)){
			removeInvaders()
			shiftInvaders(15)
			colorInvaders()
			direction = -direction
		}
		else{
			removeInvaders()
			shiftInvaders(direction)
			colorInvaders()
		}
	}

	//bullet functions
	function removeBullets(){
		
		bullets.forEach(index => squares[index].classList.remove('bullet'))
	}

	function addBullets(){
		
		bullets.forEach(index => squares[index].classList.add('bullet'))
	}

	function shiftBullets(){
		for(i=0;i<bullets.length;i++){
			bullets[i] -= 15
		}
		bullets = bullets.filter((index) => index>0)
	}

	function moveBullets(){
		removeBullets()
		shiftBullets()
		addBullets()
	}

	function getRow(){
		let row = -1

		invaders.forEach(index => {
			row = Math.max(row,Math.floor(index/15))
		})

		return row
	}

	// game step function
	function step() {
		if(invaders.length === 0 || getRow() === 13){
			clearInterval(intInv)
			clearInterval(intStep)
			clearInterval(intBult)
		}

		let intersection = invaders.filter((x) => bullets.includes(x))
		removeBullets()
		removeInvaders()
		invaders = invaders.filter((x) => !intersection.includes(x))
		bullets = bullets.filter((x) => !intersection.includes(x))
		colorInvaders()
		addBullets()

		score += intersection.length
		scoreDisplay.innerText = score



	}


	function control(e) {
		squares[currentIndex].classList.remove('snake')

		if(e.keyCode === 39) {
			squares[currentIndex].classList.remove('player')
			currentIndex += 1
			currentIndex = Math.min(currentIndex,134)
			squares[currentIndex].classList.add('player')
		}
		else if (e.keyCode === 37){
			squares[currentIndex].classList.remove('player')
			currentIndex -= 1
			currentIndex = Math.max(currentIndex,120)
			squares[currentIndex].classList.add('player')
		}
		else if (e.keyCode === 40){
			bullets.unshift(currentIndex - 15)
			squares[bullets[0]].classList.add('bullet')
		}
	}

	document.addEventListener('keyup',control)
	startBtn.addEventListener('click',startGame)
})