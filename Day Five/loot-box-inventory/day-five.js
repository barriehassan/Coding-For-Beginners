// Rewards are stored as objects.
// Each object has a name, rarity, and emoji.
const rewards = [
  { name: "Gold Coin", rarity: "Common", emoji: "🪙" },
  { name: "Health Potion", rarity: "Common", emoji: "🧪" },
  { name: "Wooden Shield", rarity: "Common", emoji: "🛡️" },
  { name: "Magic Sword", rarity: "Rare", emoji: "⚔️" },
  { name: "Treasure Gem", rarity: "Rare", emoji: "💎" },
  { name: "Dragon Crown", rarity: "Legendary", emoji: "👑" },
  { name: "Empty Box", rarity: "Empty", emoji: "📦" }
];

// This array stores collected rewards.
const inventory = [];

// This variable counts how many boxes were opened.
let boxesOpened = 0;

// Find the HTML elements.
const openButton = document.getElementById("openButton");
const clearButton = document.getElementById("clearButton");
const result = document.getElementById("result");
const rarity = document.getElementById("rarity");
const boxCount = document.getElementById("boxCount");
const inventoryList = document.getElementById("inventoryList");
const chest = document.getElementById("chest");

// Choose and display a random reward.
function openLootBox() {
  const randomIndex = Math.floor(Math.random() * rewards.length);
  const selectedReward = rewards[randomIndex];

  boxesOpened++;
  boxCount.textContent = boxesOpened;

  result.textContent = selectedReward.emoji + " " + selectedReward.name;
  rarity.textContent = selectedReward.rarity;
  rarity.className = "rarity " + selectedReward.rarity.toLowerCase();

  // Do not add an empty box to the inventory.
  if (selectedReward.rarity === "Empty") {
    result.textContent = "😢 The box was empty!";
  } else {
    inventory.push(selectedReward);
    showInventory();
  }

  animateChest();
}

// Display every reward stored in the inventory.
function showInventory() {
  inventoryList.innerHTML = "";

  if (inventory.length === 0) {
    inventoryList.innerHTML =
      '<li class="empty-message">No rewards collected yet.</li>';
    return;
  }

  inventory.forEach(function (item) {
    const listItem = document.createElement("li");
    listItem.textContent =
      item.emoji + " " + item.name + " — " + item.rarity;
    inventoryList.appendChild(listItem);
  });
}

// Remove all rewards from the inventory.
function clearInventory() {
  inventory.length = 0;
  showInventory();
  result.textContent = "Inventory cleared";
  rarity.textContent = "Start collecting again";
  rarity.className = "rarity";
}

// Add a small chest animation.
function animateChest() {
  chest.classList.add("opening");

  setTimeout(function () {
    chest.classList.remove("opening");
  }, 250);
}

// Listen for button clicks.
openButton.addEventListener("click", openLootBox);
clearButton.addEventListener("click", clearInventory);
