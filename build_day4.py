import os
import re
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
html_file = os.path.join(base_dir, "Day Four", "mystery-loot-box", "day-four.html")

journey_data = [
    # HTML LEVELS
    {
        "part": "PART 1", "part_title": "HTML builds the structure", "part_desc": "First, we lay out the game interface. This includes the loot box, the button, and the message areas.",
        "section": "HTML", "level": 1, "total": 3,
        "title": "Title and Loot Box", "preview_text": "Preview: text and the main chest emoji", "filename": "index.html",
        "code": """<main class="game-card">
  <p class="day-label">DAY 4 PROJECT</p>
  <h1>Mystery Loot Box</h1>
  <p class="intro">Open the box and discover your reward!</p>
  
  <div class="chest" id="chest">🎁</div>
</main>""",
        "bullets": ["The <main> tag holds our game container", "The <div> with id='chest' holds the emoji", "We will animate this chest later with CSS and JS"],
        "lang": "markup",
        "iframe_html": "<main class='game-card'><p class='day-label'>DAY 4 PROJECT</p><h1>Mystery Loot Box</h1><p class='intro'>Open the box and discover your reward!</p><div class='chest' id='chest'>🎁</div></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 2, "total": 3,
        "title": "Result Box and Button", "preview_text": "Preview: the message area and open button appear", "filename": "index.html",
        "code": """<div class="result-box">
  <p id="message">Click the button to open the box.</p>
</div>

<button id="openButton">Open Box</button>""",
        "bullets": ["The result box will show the random reward", "id='message' gives JS a way to change the text", "id='openButton' is what the user clicks"],
        "lang": "markup",
        "iframe_html": "<main class='game-card'><p class='day-label'>DAY 4 PROJECT</p><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 3, "total": 3,
        "title": "Tracking Opens", "preview_text": "Preview: the counter text is added", "filename": "index.html",
        "code": """<p class="count">
  Boxes opened: <span id="count">0</span>
</p>""",
        "bullets": ["The <span> tag wraps the number 0", "id='count' will be updated every time we open a box", "Structure is complete!"],
        "lang": "markup",
        "iframe_html": "<main class='game-card'><p class='day-label'>DAY 4 PROJECT</p><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button><p class='count'>Boxes opened: <span id='count'>0</span></p></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    
    # CSS LEVELS
    {
        "part": "PART 2", "part_title": "CSS turns structure into design", "part_desc": "We style the game card to look like a clean interface and prepare an animation class for the chest.",
        "section": "CSS", "level": 1, "total": 4,
        "title": "Game Card Layout", "preview_text": "Preview: a white card centered on a blue background", "filename": "style.css",
        "code": """.game-card {
  margin: auto;
  width: 100%;
  max-width: 420px;
  padding: 32px;
  text-align: center;
  background: white;
  border-radius: 24px;
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}""",
        "bullets": ["max-width keeps the card from stretching too far", "text-align: center aligns all child elements", "box-shadow adds depth"],
        "lang": "css",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); }"
    },
    {
        "section": "CSS", "level": 2, "total": 4,
        "title": "The Chest & Animation", "preview_text": "Preview: the chest becomes massive", "filename": "style.css",
        "code": """.chest {
  margin: 24px 0;
  font-size: 110px;
  transition: 0.3s;
}
.chest.opening {
  transform: scale(1.15) rotate(5deg);
}""",
        "bullets": ["font-size: 110px makes the emoji huge", ".opening is a class we will add using JS", "transform makes it grow and tilt slightly"],
        "lang": "css",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; transition: 0.3s; } .chest:hover { transform: scale(1.15) rotate(5deg); }"
    },
    {
        "section": "CSS", "level": 3, "total": 4,
        "title": "Result Box Styling", "preview_text": "Preview: a light blue box wraps the message", "filename": "style.css",
        "code": """.result-box {
  min-height: 76px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 18px;
  background: #eff6ff;
  border: 2px solid #bfdbfe;
  border-radius: 14px;
}
#message {
  color: #1e3a8a;
  font-size: 18px;
  font-weight: bold;
}""",
        "bullets": ["min-height stops the box from shrinking when text is short", "display: flex centers the text perfectly", "A light blue background makes it stand out"],
        "lang": "css",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; } .result-box { min-height: 76px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; } #message { color: #1e3a8a; font-size: 18px; font-weight: bold; margin: 0; }"
    },
    {
        "section": "CSS", "level": 4, "total": 4,
        "title": "Button Polish", "preview_text": "Preview: an orange button that shrinks when clicked", "filename": "style.css",
        "code": """button {
  width: 100%;
  padding: 15px;
  border-radius: 12px;
  background: #f59e0b;
  color: white;
  font-size: 18px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.2s;
}
button:active {
  transform: scale(0.96);
}""",
        "bullets": ["background uses a vibrant orange", "button:active targets the moment the button is pressed", "scale(0.96) creates a physical pressing effect"],
        "lang": "css",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; } .result-box { min-height: 76px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; } #message { color: #1e3a8a; font-size: 18px; font-weight: bold; margin: 0; } button { width: 100%; padding: 15px; border: none; border-radius: 12px; background: #f59e0b; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; } button:active { transform: scale(0.96); }"
    },
    
    # JS LEVELS
    {
        "part": "PART 3", "part_title": "JavaScript makes it respond", "part_desc": "Now we use JavaScript to create a random reward generator and update the UI when the button is clicked.",
        "section": "JS", "level": 1, "total": 3,
        "title": "Define the Rewards Array", "preview_text": "Preview: no visual change yet", "filename": "script.js",
        "code": """const rewards = [
  "🪙 Gold Coin",
  "🧪 Health Potion",
  "⚔️ Magic Sword",
  "🛡️ Strong Shield",
  "💎 Treasure Gem",
  "📦 Empty Box"
];""",
        "bullets": ["An array ([]) holds a list of items", "Each item is a string of text", "We will pick one of these items randomly"],
        "lang": "javascript",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; } .result-box { min-height: 76px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; } #message { color: #1e3a8a; font-size: 18px; font-weight: bold; margin: 0; } button { width: 100%; padding: 15px; border: none; border-radius: 12px; background: #f59e0b; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; }"
    },
    {
        "section": "JS", "level": 2, "total": 3,
        "title": "Variables and Function setup", "preview_text": "Preview: no visual change yet", "filename": "script.js",
        "code": """const openButton = document.getElementById("openButton");
const message = document.getElementById("message");
let boxesOpened = 0;

function openLootBox() {
  boxesOpened = boxesOpened + 1;
  console.log("Opened!");
}

openButton.addEventListener("click", openLootBox);""",
        "bullets": ["We find the HTML elements we need", "let allows the boxesOpened number to change", "addEventListener triggers the function when clicked"],
        "lang": "javascript",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest' id='chest'>🎁</div><div class='result-box'><p id='message'>Click the button to open the box.</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; } .result-box { min-height: 76px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; } #message { color: #1e3a8a; font-size: 18px; font-weight: bold; margin: 0; } button { width: 100%; padding: 15px; border: none; border-radius: 12px; background: #f59e0b; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; }"
    },
    {
        "section": "JS", "level": 3, "total": 3,
        "title": "Randomness and Animation", "preview_text": "Preview: the message updates!", "filename": "script.js",
        "code": """function openLootBox() {
  // 1. Pick a random reward
  const randomIndex = Math.floor(Math.random() * rewards.length);
  const selectedReward = rewards[randomIndex];

  // 2. Update the message
  message.textContent = "You received: " + selectedReward;

  // 3. Animate the chest
  chest.classList.add("opening");
  setTimeout(function () {
    chest.classList.remove("opening");
  }, 300);
}""",
        "bullets": ["Math.random() generates a random decimal", "Math.floor() rounds it down to an index", "setTimeout removes the animation class after 300ms so it can replay"],
        "lang": "javascript",
        "iframe_html": "<main class='game-card'><h1>Mystery Loot Box</h1><div class='chest opening' id='chest'>🎁</div><div class='result-box'><p id='message'>You received: ⚔️ Magic Sword</p></div><button id='openButton'>Open Box</button></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #0f5bd8; } .game-card { margin: auto; width: 100%; max-width: 420px; padding: 32px; text-align: center; background: white; border-radius: 24px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2); } .chest { margin: 24px 0; font-size: 110px; } .chest.opening { transform: scale(1.15) rotate(5deg); } .result-box { min-height: 76px; display: flex; align-items: center; justify-content: center; margin-bottom: 18px; background: #eff6ff; border: 2px solid #bfdbfe; border-radius: 14px; } #message { color: #1e3a8a; font-size: 18px; font-weight: bold; margin: 0; } button { width: 100%; padding: 15px; border: none; border-radius: 12px; background: #f59e0b; color: white; font-size: 18px; font-weight: bold; cursor: pointer; transition: 0.2s; }"
    }
]

journey_html = """
<section class="project-journey-section">
  <div class="journey-shell">
    <div class="journey-header">
      <span class="eyebrow">BUILD JOURNEY</span>
      <h2 style="font-size: 38px; color: #12355b; margin: 10px 0;">Mystery Loot Box</h2>
      <p style="color: #62748a; font-size: 18px;">Start with the final output, then build it step by step using HTML, CSS and JS.</p>
    </div>
    
    <div class="journey-module" style="text-align: center;">
      <div class="module-eyebrow">PROJECT OUTPUT</div>
      <h3 class="module-title">What are we building?</h3>
      <p class="module-desc" style="margin-left: auto; margin-right: auto;">An interactive loot box that gives random rewards.</p>
      
      <div class="aim-card" style="text-align: left;">
        <h4>Project aim</h4>
        <p class="understand-title">Understand this:</p>
        <ul class="bullet-list">
          <li>Create an array of rewards</li>
          <li>Generate a random number</li>
          <li>Update the text message dynamically</li>
          <li>Use CSS animations via JS class toggling</li>
        </ul>
        <div class="aim-main-idea">Main idea: <strong>Click &rarr; Randomize &rarr; Reveal</strong></div>
      </div>
    </div>
    
    <!-- Interaction Flow -->
    <div class="journey-module" style="text-align: center;">
      <div class="module-eyebrow">HOW IT WORKS</div>
      <h3 class="module-title">The simple interaction flow</h3>
      <p class="module-desc" style="margin-left: auto; margin-right: auto;">Students should understand the array logic before writing code.</p>
      
      <div class="flow-steps" style="text-align: left;">
        <div class="flow-step"><div class="step-circle" style="background:#1d4ed8;">1</div><strong>Array</strong><p>List items</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#0ea5e9;">2</div><strong>Random</strong><p>Pick an index</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#f59e0b;">3</div><strong>Animate</strong><p>Add CSS class</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#8b5cf6;">4</div><strong>Result</strong><p>Show text</p></div>
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
        <li>The chest scales and rotates when clicked</li>
        <li>A random reward appears every time</li>
        <li>The counter accurately reflects opened boxes</li>
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
        print("Day 4 HTML updated!")
