// A list of possible rewards
const rewards = [
  "🪙 Gold Coin",
  "🧪 Health Potion",
  "⚔️ Magic Sword",
  "🛡️ Strong Shield",
  "💎 Treasure Gem",
  "📦 Empty Box"
];

// Find the HTML elements we need
const openButton = document.getElementById("openButton");
const message = document.getElementById("message");
const count = document.getElementById("count");
const chest = document.getElementById("chest");

let boxesOpened = 0;

// This function opens the loot box
function openLootBox() {
  const randomIndex = Math.floor(Math.random() * rewards.length);
  const selectedReward = rewards[randomIndex];

  boxesOpened = boxesOpened + 1;
  count.textContent = boxesOpened;

  if (selectedReward === "📦 Empty Box") {
    message.textContent = "Oh no! The box was empty.";
  } else {
    message.textContent = "You received: " + selectedReward;
  }

  chest.classList.add("opening");

  setTimeout(function () {
    chest.classList.remove("opening");
  }, 300);
}

// Run the function when the button is clicked
openButton.addEventListener("click", openLootBox);
