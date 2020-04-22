document.addEventListener('DOMContentLoaded', () => {
	const cardArray = [
		{
			name: 'appathon',
			img: 'images/appathon.png'
		},
		{
			name: 'appathon',
			img: 'images/appathon.png'
		},
		{
			name: 'ctf',
			img: 'images/ctf.png'
		},
		{
			name: 'ctf',
			img: 'images/ctf.png'
		},
		{
			name: 'decipher',
			img: 'images/decipher.png'
		},
		{
			name: 'decipher',
			img: 'images/decipher.png'
		},
		{
			name: 'manthan',
			img: 'images/manthan.png'
		},
		{
			name: 'manthan',
			img: 'images/manthan.png'
		},
		{
			name: 'enigma',
			img: 'images/enigma.png'
		},
		{
			name: 'enigma',
			img: 'images/enigma.png'
		},
		{
			name: 'mathamania',
			img: 'images/mathamania.png'
		},
		{
			name: 'mathamania',
			img: 'images/mathamania.png'
		},
		{
			name: 'vista',
			img: 'images/vista.png'
		},
		{
			name: 'vista',
			img: 'images/vista.png'
		},
		{
			name: 'perplexed',
			img: 'images/perplexed.png'
		},
		{
			name: 'perplexed',
			img: 'images/perplexed.png'
		}
	]

	cardArray.sort(() => 0.5 - Math.random())

	const grid = document.querySelector('.grid')
	const resultDisplay = document.querySelector('#result')
	var cardsChosen = []
	var cardsChosenId = []
	var cardsWon = []

	//create your board
	function createBoard(){
		for (let i = 0; i< cardArray.length; i++) {
			var card = document.createElement('img')
			card.setAttribute('src', 'images/blank.png')
			card.setAttribute('width', '100px')
			card.setAttribute('height', '100px')
			card.setAttribute('data-id', i)
			card.addEventListener('click', flipcard)
			grid.appendChild(card)
		}
	}

	function check(){
		var cards = document.querySelectorAll('img')
		const a = cardsChosenId[0]
		const b = cardsChosenId[1]
		if(cardsChosen[0] === cardsChosen[1]){
			cards[a].setAttribute('src', 'images/white.png')
			cards[b].setAttribute('src', 'images/white.png')
			cardsWon.push(cardsChosen)
		}
		else{
			cards[a].setAttribute('src', 'images/blank.png')
			cards[b].setAttribute('src', 'images/blank.png')
		}
		cardsChosen = []
		cardsChosenId = []
		resultDisplay.textContent = cardsWon.length
		if(cardsWon.length === cardArray.length/2){
			resultDisplay.textContent = "Congrats!!!"
		}
	}

	function flipcard() {
		var cardId = this.getAttribute('data-id')
		cardsChosen.push(cardArray[cardId].name)
		cardsChosenId.push(cardId)
		this.setAttribute('src', cardArray[cardId].img)
		if(cardsChosen.length === 2){
			setTimeout(check, 500)
		}
	}

	createBoard()

})