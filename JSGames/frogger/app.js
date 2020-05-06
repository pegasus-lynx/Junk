document.addEventListener("DOMContentLoaded", () => {
  // Reference to the DOM elements
  const grid = document.querySelector(".grid");
  const squares = document.querySelectorAll(".grid div");
  const btn = document.querySelector("#button");
  const timeLeft = document.querySelector("#time-left");

  // Global Variables
  let time, cur, intervals, timeinterval;
  let obs = [];
  let mode = 0;
  let obs_class = [];
  const width = 11;
  const end = 5;

  // For moving the frog
  function moveFrog(e) {
    squares[cur].classList.remove("frog");
    switch (e.keyCOde) {
      case 37:
        if (cur % width !== 0) cur -= 1;
        break;
      case 38:
        if (cur - width >= 0) cur -= width;
        break;
      case 39:
        if (cur % width < width - 1) cur += 1;
        break;
      case 40:
        if (cur + width < width * width) cur += width;
        break;
    }
    squares[cur].classList.add("frog");
    check();
  }

  // For checking if the game is over
  function check() {
    if (cur === end) {
      return stop();
    }

    if (cur < 33 || cur >= 88) {
      return;
    }

    let c = (cur - 33) % width;
    let r = (cur - (33 + c)) / width;

    if (obs_class[r][c] === "0") {
      return stop();
    }
  }

  // For moving the obstacles
  function move() {
    erase();
    for (let i = 3; i < 8; i++) {
      let dir = obs[i - 3][1];
      let t = obs[i - 3][2];
      intervals.push(
        setInterval((i) => {
          let st = obs_class[i - 3][0],
            en = obs_class[i - 3][10];
          if (dir === 0) {
            obs_class.shift();
            obs_class.push(st);
          } else {
            obs_class.pop();
            obs_class.unshift(en);
          }
        }, t * 1000)
      );
    }
    render();
  }

  // Function for creating obstacles
  function create() {
    let desc,
      class_list = [];
    class_list.push(["0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "1"]);
    class_list.push(["1", "0", "0", "1", "1", "1", "0", "0", "0", "0", "1"]);

    obs = [];
    obs_class = [];
    for (let i = 3; i < 8; i++) {
      desc = [];
      class_list = [];
      Math.random() > 0.4 ? desc.push(1) : desc.push(0);
      Math.random() > 0.5 ? desc.push(1) : desc.push(0);
      desc.push((Math.random() + 1) / 2);
      obs.push(desc);
      obs_class.push(class_list[desc[0]]);
    }

    console.log(obs_class.length);
  }

  // Function to render all the obstacles and start end points
  function render() {
    squares[cur].classList.add("frog");
    for (let i = 3; i < 8; i++) {
      for (let j = 0; j < width; j++) {
        squares[i * width + j].classList.add("o" + obs_class[i - 3][j]);
      }
    }
  }

  // Function to erase all the obstacles and start end points
  function erase() {
    squares[cur].classList.remove("frog");
    for (let i = 3; i < 8; i++) {
      for (let j = 0; j < width; j++) {
        squares[i * width + j].classList.remove("o" + obs_class[i - 3][j]);
      }
    }
  }

  // Function to stop the game
  function stop() {
    clearInterval(timeinterval);
    intervals.forEach(clearInterval);
  }

  // For starting the game
  btn.addEventListener("click", () => {
    if (mode) erase();
    time = 0;
    cur = 115;
    create();
    render();
    move();
    timeinterval = setInterval(() => {
      time += 1;
      timeLeft.textContent = time;
    }, 1000);
    mode = 1;
  });

  window.addEventListener("keyup", moveFrog);
});
