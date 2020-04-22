document.addEventListener('DOMContentLoaded', () => {
	const grid = document.querySelector('.grid')
	const squares = document.querySelectorAll('.grid div')
	const startBtn = document.querySelector('.start')
	const scoreDisplay = document.querySelector('span')

	const width = 10

	let currentIndex = 0
	let appleIndex = 0
	let currentSnake = [2,1,0]
	let direction = 1
	let score = 0 
	let speed = 0.9
	let intervalTime = 0
	let interval = 0

	// to start
	function startGame() {
		currentSnake.forEach(index => squares[index].classList.remove('snake'))
		squares[appleIndex].classList.remove('apple')
		clearInterval(interval)
		randomApple()
		score = 0
		direction = 1
		scoreDisplay.innerText = score
		intervalTime = 1000
		currentSnake = [2,1,0]
		currentIndex = 0
		currentSnake.forEach(index => squares[index].classList.add('snake'))
		interval = setInterval(moveOutcome, intervalTime)
	}


	function moveOutcome() {
		if(
			(currentSnake[0] + width >= (width*width) && direction === width) ||
			(currentSnake[0] % width === width - 1 && direction === 1) ||
			(currentSnake[0] % width === 0 && direction === -1) ||
			(currentSnake[0] - width < 0 && direction === -width) ||
			squares[currentSnake[0] + direction].classList.contains('snake')
		){
			return clearInterval(interval)
		}

		const tail = currentSnake.pop()
		squares[tail].classList.remove('snake')
		currentSnake.unshift(currentSnake[0] + direction)

		if(squares[currentSnake[0]].classList.contains('apple')) {
			squares[currentSnake[0]].classList.remove('apple')
			squares[tail].classList.add('snake')
			randomApple()
			score++
			scoreDisplay.textContent = score
			clearInterval(interval)
			intervalTime = intervalTime * speed
			interval = setInterval(moveOutcome,intervalTime)

		}

		squares[currentSnake[0]].classList.add('snake')
	}

	function randomApple() {
		do{
			appleIndex = Math.floor(Math.random() * squares.length)
		} while(squares[appleIndex].classList.contains('snake'))
		squares[appleIndex].classList.add('apple')
	}

	function control(e) {
		squares[currentIndex].classList.remove('snake')

		if(e.keyCode === 39) {
			direction = 1
		}
		else if (e.keyCode === 38){
			direction = -width
		}
		else if (e.keyCode === 37){
			direction = -1
		}
		else if (e.keyCode === 40){
			direction = width
		}
	}

	document.addEventListener('keyup',control)
	startBtn.addEventListener('click',startGame)

})