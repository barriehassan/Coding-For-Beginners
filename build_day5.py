import os
import re
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
html_file = os.path.join(base_dir, "Day Five", "loot-box-inventory", "day-five.html")

journey_data = [
    # HTML LEVELS
    {
        "part": "PART 1", "part_title": "HTML builds the structure", "part_desc": "We are expanding our Loot Box into a full two-panel interface: one for opening, one for the inventory.",
        "section": "HTML", "level": 1, "total": 3,
        "title": "Two-Panel Layout", "preview_text": "Preview: the left and right sides", "filename": "index.html",
        "code": """<main class="game-layout">
  <!-- Left Side: The Box -->
  <div class="left-panel">
    <h1>Loot Box</h1>
    <div class="chest" id="chest">🎁</div>
    <div class="result-box">
      <p id="result">Click to open!</p>
      <span id="rarity" class="rarity"></span>
    </div>
    <button id="openButton" class="btn-primary">Open Box</button>
  </div>
  
  <!-- Right Side: The Inventory -->
  <div class="right-panel">
    <h2>My Inventory</h2>
    <ul id="inventoryList">
      <li class="empty-message">No rewards collected yet.</li>
    </ul>
    <button id="clearButton" class="btn-danger">Clear Inventory</button>
  </div>
</main>""",
        "bullets": ["The <main> tag wraps both panels", "We have a left-panel for the game, and a right-panel for the inventory", "<ul id='inventoryList'> is where we will inject our items with JS"],
        "lang": "markup",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='result'>Click to open!</p></div><button class='btn-primary'>Open Box</button></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul><button class='btn-danger'>Clear Inventory</button></div></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 2, "total": 3,
        "title": "The Inventory List", "preview_text": "Preview: an empty unordered list", "filename": "index.html",
        "code": """<h2>My Inventory</h2>
<ul id="inventoryList">
  <li class="empty-message">No rewards collected yet.</li>
</ul>""",
        "bullets": ["<ul> stands for Unordered List (bullet points)", "<li> stands for List Item", "We use id='inventoryList' so our JS can find it easily"],
        "lang": "markup",
        "iframe_html": "<div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul></div>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 3, "total": 3,
        "title": "Action Buttons", "preview_text": "Preview: buttons have specific classes", "filename": "index.html",
        "code": """<button id="openButton" class="btn-primary">Open Box</button>

<button id="clearButton" class="btn-danger">Clear Inventory</button>""",
        "bullets": ["We give them different classes to style them differently", "btn-primary will be blue/green", "btn-danger will be red for the clear action"],
        "lang": "markup",
        "iframe_html": "<button id='openButton' class='btn-primary'>Open Box</button><br><br><button id='clearButton' class='btn-danger'>Clear Inventory</button>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    
    # CSS LEVELS
    {
        "part": "PART 2", "part_title": "CSS turns structure into design", "part_desc": "We will use Flexbox to place the panels side-by-side, and add colors for item rarity.",
        "section": "CSS", "level": 1, "total": 3,
        "title": "Side-by-Side Flexbox", "preview_text": "Preview: the panels sit next to each other", "filename": "style.css",
        "code": """.game-layout {
  display: flex;
  gap: 30px;
  max-width: 900px;
  margin: 40px auto;
  align-items: flex-start;
}
.left-panel, .right-panel {
  flex: 1;
  background: white;
  padding: 30px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
}""",
        "bullets": ["display: flex turns the parent into a row", "gap: 30px adds space between the two panels", "flex: 1 forces them to be equal width"],
        "lang": "css",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); }"
    },
    {
        "section": "CSS", "level": 2, "total": 3,
        "title": "Inventory List Styling", "preview_text": "Preview: the list items look like cards", "filename": "style.css",
        "code": """ul {
  list-style: none;
  padding: 0;
  max-height: 280px;
  overflow-y: auto;
}
li {
  padding: 12px;
  margin-bottom: 10px;
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-weight: bold;
}""",
        "bullets": ["list-style: none removes the default bullet dots", "overflow-y: auto makes the list scrollable if it gets too long", "li padding and border makes them look like individual items"],
        "lang": "css",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li>⚔️ Magic Sword — Rare</li><li>🪙 Gold Coin — Common</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); } ul { list-style: none; padding: 0; max-height: 280px; overflow-y: auto; } li { padding: 12px; margin-bottom: 10px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-weight: bold; }"
    },
    {
        "section": "CSS", "level": 3, "total": 3,
        "title": "Rarity Colors", "preview_text": "Preview: text changes color based on rarity", "filename": "style.css",
        "code": """.rarity {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: bold;
}
.common { background: #e2e8f0; color: #475569; }
.rare { background: #dbeafe; color: #1d4ed8; }
.legendary { background: #fef08a; color: #854d0e; }""",
        "bullets": ["We define general styles for all .rarity badges", "We define specific colors for .common, .rare, and .legendary", "We will use JS to assign these classes dynamically"],
        "lang": "css",
        "iframe_html": "<div style='display: flex; gap: 10px;'><span class='rarity common'>Common</span><span class='rarity rare'>Rare</span><span class='rarity legendary'>Legendary</span></div>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; } .rarity { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; } .common { background: #e2e8f0; color: #475569; } .rare { background: #dbeafe; color: #1d4ed8; } .legendary { background: #fef08a; color: #854d0e; }"
    },
    
    # JS LEVELS
    {
        "part": "PART 3", "part_title": "JavaScript makes it respond", "part_desc": "Now we step up our JS. We will use Objects, Arrays, and dynamically create HTML elements to build our inventory.",
        "section": "JS", "level": 1, "total": 4,
        "title": "Objects in an Array", "preview_text": "Preview: no visual change yet", "filename": "script.js",
        "code": """const rewards = [
  { name: "Gold Coin", rarity: "Common", emoji: "🪙" },
  { name: "Magic Sword", rarity: "Rare", emoji: "⚔️" },
  { name: "Dragon Crown", rarity: "Legendary", emoji: "👑" },
  { name: "Empty Box", rarity: "Empty", emoji: "📦" }
];

const inventory = [];""",
        "bullets": ["Instead of simple strings, our array now holds Objects {}", "Objects let us group related data together (name, rarity, emoji)", "inventory is an empty array where we will save our loot"],
        "lang": "javascript",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); } ul { list-style: none; padding: 0; max-height: 280px; overflow-y: auto; } li { padding: 12px; margin-bottom: 10px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-weight: bold; }"
    },
    {
        "section": "JS", "level": 2, "total": 4,
        "title": "Opening the Box", "preview_text": "Preview: the result box updates with an Object's data", "filename": "script.js",
        "code": """function openLootBox() {
  const randomIndex = Math.floor(Math.random() * rewards.length);
  const selectedReward = rewards[randomIndex]; // This is now an Object

  // Update UI using object properties
  result.textContent = selectedReward.emoji + " " + selectedReward.name;
  rarity.textContent = selectedReward.rarity;
  rarity.className = "rarity " + selectedReward.rarity.toLowerCase();

  // Save it!
  if (selectedReward.rarity !== "Empty") {
    inventory.push(selectedReward);
    showInventory();
  }
}""",
        "bullets": ["We access object data using dots (e.g. selectedReward.name)", "inventory.push() adds the item to the end of our array", "We only push it if it's not an 'Empty' box"],
        "lang": "javascript",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='result'>⚔️ Magic Sword</p><span class='rarity rare'>Rare</span></div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); } .rarity { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; margin-top: 10px; display: inline-block;} .rare { background: #dbeafe; color: #1d4ed8; } ul { list-style: none; padding: 0; }"
    },
    {
        "section": "JS", "level": 3, "total": 4,
        "title": "Creating HTML with JS", "preview_text": "Preview: items appear in the inventory list", "filename": "script.js",
        "code": """function showInventory() {
  inventoryList.innerHTML = ""; // Clear the list first

  inventory.forEach(function (item) {
    const listItem = document.createElement("li");
    
    listItem.textContent = item.emoji + " " + item.name + " — " + item.rarity;
    
    inventoryList.appendChild(listItem);
  });
}""",
        "bullets": ["inventoryList.innerHTML = \"\" clears the old items so we don't duplicate them", "forEach loops through every item in our array", "document.createElement('li') creates a new HTML tag entirely from JS", "appendChild() physically places the new <li> inside our <ul>"],
        "lang": "javascript",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li>🪙 Gold Coin — Common</li><li>⚔️ Magic Sword — Rare</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); } ul { list-style: none; padding: 0; max-height: 280px; overflow-y: auto; } li { padding: 12px; margin-bottom: 10px; background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; font-weight: bold; }"
    },
    {
        "section": "JS", "level": 4, "total": 4,
        "title": "Clearing the Inventory", "preview_text": "Preview: the game is fully functional", "filename": "script.js",
        "code": """function clearInventory() {
  inventory.length = 0; // This empties an array
  showInventory(); // Re-render the empty list
  
  result.textContent = "Inventory cleared";
  rarity.textContent = "Start collecting again";
  rarity.className = "rarity";
}

clearButton.addEventListener("click", clearInventory);""",
        "bullets": ["inventory.length = 0 is a quick way to empty an array", "We must call showInventory() again to update the visual UI", "We reset the message text to give feedback to the user"],
        "lang": "javascript",
        "iframe_html": "<main class='game-layout'><div class='left-panel'><h1>Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='result'>Inventory cleared</p><span class='rarity'>Start collecting again</span></div></div><div class='right-panel'><h2>My Inventory</h2><ul id='inventoryList'><li class='empty-message'>No rewards collected yet.</li></ul></div></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #e0f2fe; } .game-layout { display: flex; gap: 30px; max-width: 900px; margin: 40px auto; align-items: flex-start; } .left-panel, .right-panel { flex: 1; background: white; padding: 30px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1); } ul { list-style: none; padding: 0; max-height: 280px; overflow-y: auto; } .rarity { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: bold; margin-top: 10px; display: inline-block; background:#e2e8f0; color:#475569; }"
    }
]

journey_html = """
<section class="project-journey-section">
  <div class="journey-shell">
    <div class="journey-header">
      <span class="eyebrow">BUILD JOURNEY</span>
      <h2 style="font-size: 38px; color: #12355b; margin: 10px 0;">Loot Box Inventory</h2>
      <p style="color: #62748a; font-size: 18px;">Start with the final output, then build it step by step using HTML, CSS and JS.</p>
    </div>
    
    <div class="journey-module" style="text-align: center;">
      <div class="module-eyebrow">PROJECT OUTPUT</div>
      <h3 class="module-title">What are we building?</h3>
      <p class="module-desc" style="margin-left: auto; margin-right: auto;">An interactive loot box that saves your rewards to an inventory.</p>
      
      <div class="aim-card" style="text-align: left;">
        <h4>Project aim</h4>
        <p class="understand-title">Understand this:</p>
        <ul class="bullet-list">
          <li>Create an array of Objects</li>
          <li>Save items to a secondary array (Inventory)</li>
          <li>Dynamically create HTML elements with JS</li>
          <li>Render a list by looping over an array</li>
        </ul>
        <div class="aim-main-idea">Main idea: <strong>Randomize &rarr; Save to Array &rarr; Render DOM</strong></div>
      </div>
    </div>
    
    <!-- Interaction Flow -->
    <div class="journey-module" style="text-align: center;">
      <div class="module-eyebrow">HOW IT WORKS</div>
      <h3 class="module-title">The simple interaction flow</h3>
      <p class="module-desc" style="margin-left: auto; margin-right: auto;">Students should understand the flow of data before writing code.</p>
      
      <div class="flow-steps" style="text-align: left;">
        <div class="flow-step"><div class="step-circle" style="background:#1d4ed8;">1</div><strong>Random</strong><p>Pick Object</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#0ea5e9;">2</div><strong>Save</strong><p>Push to Array</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#f59e0b;">3</div><strong>Clear</strong><p>Empty HTML</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#8b5cf6;">4</div><strong>Render</strong><p>Create &lt;li&gt;</p></div>
      </div>
    </div>
"""

for level in journey_data:
    if "part" in level:
        journey_html += f"""
    <div class="journey-module" style="margin-top: 60px; padding: 40px; background: #082c66; border-radius: 16px; color: white; text-align: center;">
      <div class="module-eyebrow" style="background: #f59e0b; color: white;">{level['part']}</div>
      <h3 class="module-title" style="color: white; font-size: 32px;">{level['part_title']}</h3>
      <p style="color: #9bd8fa; font-size: 18px; max-width: 600px; margin: 0 auto;">{level['part_desc']}</p>
    </div>
"""
    
    srcdoc = f"<!DOCTYPE html><html><head><style>{level['iframe_css']}</style></head><body>{level['iframe_html']}</body></html>"
    srcdoc_escaped = html.escape(srcdoc, quote=True)
    bullets_html = "".join([f"<li>{b}</li>" for b in level['bullets']])
    
    journey_html += f"""
    <div class="level-card" style="text-align: left;">
      <div class="level-header">
        <div class="level-badge">{level['section']} {level['level']} OF {level['total']}</div>
        <h3>{level['section']} Level {level['level']}: {level['title']}</h3>
        <p>{level['preview_text']}</p>
      </div>
      <div class="level-grid">
        <div class="level-code">
          <div class="code-header">
            <span class="dots"><i></i><i></i><i></i></span><span class="filename">{level['filename']}</span>
          </div>
          <pre><code class="language-{level['lang']}">{html.escape(level['code'])}</code></pre>
        </div>
        <div class="level-preview">
          <div class="preview-header">
            <span class="dots"><i></i><i></i><i></i></span><span class="filename">Browser preview</span>
          </div>
          <div class="iframe-wrapper">
             <iframe srcdoc="{srcdoc_escaped}"></iframe>
          </div>
          <div class="understand-section">
            <h4>Understand this</h4>
            <ul class="bullet-list">{bullets_html}</ul>
          </div>
        </div>
      </div>
    </div>
"""

journey_html += """
    <div class="journey-module" style="margin-top: 80px; text-align: center;">
      <div class="module-eyebrow">TESTING</div>
      <h3 class="module-title">Before we say "finished"</h3>
      <ul class="check-list" style="text-align: left;">
        <li>Opening the box adds a new item to the inventory</li>
        <li>Empty boxes are NOT added to the inventory</li>
        <li>Clearing the inventory empties the list entirely</li>
      </ul>
    </div>
  </div>
</section>
"""

with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

inner_journey = journey_html.replace('<section class="project-journey-section">', '').replace('</section>', '')
cb_idx = html_content.find('<div class="codebase-section">')
sec_idx = html_content.find('<section class="project-journey-section">')

if cb_idx != -1 and sec_idx != -1:
    before = html_content[:sec_idx]
    after = html_content[cb_idx:]
    clean_journey = journey_html.rsplit('</div>\n</section>', 1)[0]
    new_html = before + clean_journey + "\n      " + after
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
        print("Day 5 HTML updated!")
