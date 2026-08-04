// Find the message area
const message = document.getElementById("message");

// Find the buttons
const wowButton = document.getElementById("wowButton");
const laughButton = document.getElementById("laughButton");
const ohNoButton = document.getElementById("ohNoButton");
const victoryButton = document.getElementById("victoryButton");
const surpriseButton = document.getElementById("surpriseButton");
const tryAgainButton = document.getElementById("tryAgainButton");

// Find the sounds
const wowSound = document.getElementById("wowSound");
const laughSound = document.getElementById("laughSound");
const ohNoSound = document.getElementById("ohNoSound");
const victorySound = document.getElementById("victorySound");
const surpriseSound = document.getElementById("surpriseSound");
const tryAgainSound = document.getElementById("tryAgainSound");

// This function restarts and plays a sound
function playSound(sound, soundName) {
  sound.currentTime = 0;
  sound.play();
  message.textContent = soundName;
}

// Listen for button clicks
wowButton.addEventListener("click", function () {
  playSound(wowSound, "Wow!");
});

laughButton.addEventListener("click", function () {
  playSound(laughSound, "Laugh!");
});

ohNoButton.addEventListener("click", function () {
  playSound(ohNoSound, "Oh No!");
});

victoryButton.addEventListener("click", function () {
  playSound(victorySound, "Victory!");
});

surpriseButton.addEventListener("click", function () {
  playSound(surpriseSound, "Surprise!");
});

tryAgainButton.addEventListener("click", function () {
  playSound(tryAgainSound, "Try Again!");
});
