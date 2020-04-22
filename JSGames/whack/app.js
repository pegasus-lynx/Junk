const square = document.querySelectorAll('.sq')
const cf = document.querySelectorAll('.mole')
const timeLeft = document.querySelector('#time')
let score = document.querySelector('#score')

let result = 0
let currentTime = timeLeft.textContent

function randomSq() {
	square.forEach(className => {
		className.classList.remove('mole')
	})
	let randomPos = square[Math.floor(Math.random()*9)]
	randomPos.classList.add('mole')

	hitPosition = randomPos.id
}

square.forEach( id => {
	id.addEventListener('mouseup', () => {
		if(id.id === hitPosition){
			result = result+1
			score.textContent = result
		}
	})
})

function moveMole() {
	let timerId = null
	timerId = setInterval(randomSq, 1000)
}

moveMole()

function countDown() {
	currentTime--
	timeLeft.textContent = currentTime

	if(currentTime === 0){
		clearInterval(timerId)
		alert("Game OVer")
	}
}

let timerId = setInterval(countDown, 1000)