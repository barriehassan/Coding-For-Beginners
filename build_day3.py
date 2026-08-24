import os
import re
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
html_file = os.path.join(base_dir, "Day Three", "day3-meme-soundboard", "day-three.html")
style_file = os.path.join(base_dir, "style.css")

# --- DATA FOR DAY 3 JOURNEY ---
journey_data = [
    # HTML LEVELS
    {
        "part": "PART 1", "part_title": "HTML builds the content", "part_desc": "We start with the page structure. At first it will look plain - that is correct.",
        "section": "HTML", "level": 1, "total": 8,
        "title": "Basic page skeleton", "preview_text": "Preview: a blank browser page", "filename": "index.html",
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Meme Soundboard</title>
</head>
<body>
</body>
</html>""",
        "bullets": ["The browser understands this as HTML5", "The body is empty, so the page is blank", "The title appears in the browser tab"],
        "lang": "markup",
        "iframe_html": "",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 2, "total": 8,
        "title": "Main container", "preview_text": "Preview: still blank because the container has no text", "filename": "index.html",
        "code": """<body>
 <main class="soundboard">
 </main>
</body>""",
        "bullets": ["<main> holds the main page content", "class=\"soundboard\" gives CSS a name to style later", "No visible content yet"],
        "lang": "markup",
        "iframe_html": "<main class='soundboard'></main>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 3, "total": 8,
        "title": "Title and instructions", "preview_text": "Preview: plain text appears", "filename": "index.html",
        "code": """<main class="soundboard">
 <p class="day-label">DAY 3 PROJECT</p>
 <h1>🎵 Meme Soundboard</h1>   
 <p class="instructions">
   Click a button to play a reaction sound.
 </p>
</main>""",
        "bullets": ["<h1> is the main title", "<p> creates text paragraphs", "Classes help CSS target each part"],
        "lang": "markup",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p></main>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 4, "total": 8,
        "title": "Now Playing message", "preview_text": "Preview: message text appears under the title", "filename": "index.html",
        "code": """<div class="message-box">
 <span>Now Playing:</span>
 <strong id="message">Choose a sound!</strong>
</div>""",
        "bullets": ["<div> groups related content", "<strong> makes important text stand out", "id=\"message\" will be used by JavaScript"],
        "lang": "markup",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div></main>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 5, "total": 8,
        "title": "First sound button", "preview_text": "Preview: one normal browser button appears", "filename": "index.html",
        "code": """<div class="button-grid">
 <button id="wowButton" class="sound-button yellow">
   <span>😮</span>   
   Wow!
 </button>
</div>""",
        "bullets": ["<button> creates a clickable control", "id=\"wowButton\" identifies this exact button", "Two classes: sound-button and yellow"],
        "lang": "markup",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button id='wowButton' class='sound-button yellow'><span>😮</span> Wow!</button></div></main>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 6, "total": 8,
        "title": "Complete button grid", "preview_text": "Preview: all buttons appear as default browser buttons", "filename": "index.html",
        "code": """<button id="wowButton" class="sound-button yellow">😮 Wow!</button>   
<button id="laughButton" class="sound-button green">😂 Laugh</button>
<button id="ohNoButton" class="sound-button red">😱 Oh No!</button>   
<button id="victoryButton" class="sound-button blue">🏆 Victory</button>
<button id="surpriseButton" class="sound-button purple">🤯 Surprise</button>
<button id="tryAgainButton" class="sound-button orange">🔁 Try Again</button>""",
        "bullets": ["Six buttons are now on the page", "Each button has its own unique ID", "Still plain because CSS is not applied yet"],
        "lang": "markup",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button>😮 Wow!</button><button>😂 Laugh</button><button>😱 Oh No!</button><button>🏆 Victory</button><button>🤯 Surprise</button><button>🔁 Try Again</button></div></main>",
        "iframe_css": ""
    },
    
    # CSS LEVELS (condensed for script size, but keeping core ones)
    {
        "part": "PART 2", "part_title": "CSS turns structure into design", "part_desc": "We will improve the same HTML step by step until it becomes the final soundboard.",
        "section": "CSS", "level": 1, "total": 4,
        "title": "Page setup & Soundboard card", "preview_text": "Preview: content moves to center, white card appears", "filename": "style.css",
        "code": """body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: #0b63ce;
}
.soundboard {
  max-width: 720px;
  padding: 32px;
  text-align: center;
  background: white;
  border: 8px solid #ff9f1c;
  border-radius: 28px;
}""",
        "bullets": ["Centers the project with Flexbox", "max-width controls the card size", "border-radius and shadow make it feel polished"],
        "lang": "css",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button>😮 Wow!</button><button>😂 Laugh</button><button>😱 Oh No!</button><button>🏆 Victory</button><button>🤯 Surprise</button><button>🔁 Try Again</button></div></main>",
        "iframe_css": "body { display:flex; justify-content:center; padding: 20px; background: #0b63ce; font-family: sans-serif; } .soundboard { width: 100%; max-width: 720px; padding: 32px; text-align: center; background: white; border: 8px solid #ff9f1c; border-radius: 28px; }"
    },
    {
        "section": "CSS", "level": 2, "total": 4,
        "title": "Style text and message box", "preview_text": "Preview: headings and 'Now Playing' become clear", "filename": "style.css",
        "code": """h1 { color: #12355b; font-size: 42px; }
.message-box {
  margin-bottom: 24px;
  padding: 16px;
  color: #12355b;
  background: #eef6ff;
  border-radius: 14px;
}
.message-box strong {
  display: block;
  font-size: 22px;
}""",
        "bullets": ["Color creates hierarchy", "The message becomes a visual panel", "display: block puts each line on its own row"],
        "lang": "css",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button>😮 Wow!</button><button>😂 Laugh</button><button>😱 Oh No!</button><button>🏆 Victory</button><button>🤯 Surprise</button><button>🔁 Try Again</button></div></main>",
        "iframe_css": "body { display:flex; justify-content:center; padding: 20px; background: #0b63ce; font-family: sans-serif; } .soundboard { width: 100%; max-width: 720px; padding: 32px; text-align: center; background: white; border: 8px solid #ff9f1c; border-radius: 28px; } h1{margin:10px 0; color:#12355b;} .day-label{color:#ff8c00;font-weight:bold;} .message-box { margin-bottom: 24px; padding: 16px; color: #12355b; background: #eef6ff; border-radius: 14px; } .message-box strong { display: block; font-size: 22px; }"
    },
    {
        "section": "CSS", "level": 3, "total": 4,
        "title": "Button grid & base buttons", "preview_text": "Preview: buttons move into a two-column layout", "filename": "style.css",
        "code": """.button-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}
.sound-button {
  min-height: 125px;
  border: none;
  border-radius: 20px;
  font-size: 20px;
  font-weight: bold;
  cursor: pointer;
  box-shadow: 0 8px 0 rgba(0,0,0,0.15);
}""",
        "bullets": ["display: grid creates columns", "repeat(2, 1fr) means two equal columns", "min-height gives every button equal height"],
        "lang": "css",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button class='sound-button'><span>😮</span> Wow!</button><button class='sound-button'><span>😂</span> Laugh</button><button class='sound-button'><span>😱</span> Oh No!</button><button class='sound-button'><span>🏆</span> Victory</button><button class='sound-button'><span>🤯</span> Surprise</button><button class='sound-button'><span>🔁</span> Try Again</button></div></main>",
        "iframe_css": "body { display:flex; justify-content:center; padding: 20px; background: #0b63ce; font-family: sans-serif; } .soundboard { width: 100%; max-width: 720px; padding: 32px; text-align: center; background: white; border: 8px solid #ff9f1c; border-radius: 28px; } h1{margin:10px 0; color:#12355b;} .day-label{color:#ff8c00;font-weight:bold;} .message-box { margin-bottom: 24px; padding: 16px; color: #12355b; background: #eef6ff; border-radius: 14px; } .message-box strong { display: block; font-size: 22px; } .button-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; } .sound-button { min-height: 125px; border: none; border-radius: 20px; font-size: 20px; font-weight: bold; box-shadow: 0 8px 0 rgba(0,0,0,0.15); } .sound-button span { display: block; font-size: 46px; }"
    },
    {
        "section": "CSS", "level": 4, "total": 4,
        "title": "Add button colors", "preview_text": "Preview: buttons become colourful", "filename": "style.css",
        "code": """.yellow { background: #ffd43b; }
.green  { background: #69db7c; }
.red    { background: #ff8787; }
.blue   { background: #74c0fc; }
.purple { background: #b197fc; }
.orange { background: #ffa94d; }""",
        "bullets": ["Color classes customise individual buttons", "The shared button style stays the same", "The soundboard now feels playful"],
        "lang": "css",
        "iframe_html": "<main class='soundboard'><p class='day-label'>DAY 3 PROJECT</p><h1>🎵 Meme Soundboard</h1><p class='instructions'>Click a button to play a reaction sound.</p><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button class='sound-button yellow'><span>😮</span> Wow!</button><button class='sound-button green'><span>😂</span> Laugh</button><button class='sound-button red'><span>😱</span> Oh No!</button><button class='sound-button blue'><span>🏆</span> Victory</button><button class='sound-button purple'><span>🤯</span> Surprise</button><button class='sound-button orange'><span>🔁</span> Try Again</button></div></main>",
        "iframe_css": "body { display:flex; justify-content:center; padding: 20px; background: #0b63ce; font-family: sans-serif; } .soundboard { width: 100%; max-width: 720px; padding: 32px; text-align: center; background: white; border: 8px solid #ff9f1c; border-radius: 28px; } h1{margin:10px 0; color:#12355b;} .day-label{color:#ff8c00;font-weight:bold;} .message-box { margin-bottom: 24px; padding: 16px; color: #12355b; background: #eef6ff; border-radius: 14px; } .message-box strong { display: block; font-size: 22px; } .button-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; } .sound-button { min-height: 125px; border: none; border-radius: 20px; font-size: 20px; font-weight: bold; box-shadow: 0 8px 0 rgba(0,0,0,0.15); color: #102a43; } .sound-button span { display: block; font-size: 46px; } .yellow { background: #ffd43b; } .green { background: #69db7c; } .red { background: #ff8787; } .blue { background: #74c0fc; } .purple { background: #b197fc; } .orange { background: #ffa94d; }"
    },
    
    # JS LEVELS
    {
        "part": "PART 3", "part_title": "JavaScript makes it respond", "part_desc": "The design is complete. Now we connect button clicks to sounds and messages.",
        "section": "JS", "level": 1, "total": 3,
        "title": "Find the message, button and sound", "preview_text": "Preview: design stays the same", "filename": "script.js",
        "code": """const message = document.getElementById("message");

const wowButton = document.getElementById("wowButton");
const wowSound = document.getElementById("wowSound");""",
        "bullets": ["document means the current webpage", "getElementById finds an element by ID", "No visible change yet"],
        "lang": "javascript",
        "iframe_html": "<main class='soundboard'><div class='message-box'><span>Now Playing:</span><strong id='message'>Choose a sound!</strong></div><div class='button-grid'><button class='sound-button yellow'><span>😮</span> Wow!</button></div></main>",
        "iframe_css": "body{padding:20px;font-family:sans-serif;} .soundboard{text-align:center;background:white;padding:32px;border:8px solid #ff9f1c;border-radius:28px;} .message-box{background:#eef6ff;padding:16px;border-radius:14px;margin-bottom:24px;} .sound-button{min-height:125px;border:none;border-radius:20px;font-size:20px;font-weight:bold;box-shadow:0 8px 0 rgba(0,0,0,0.15);width:100%;} .yellow{background:#ffd43b;}"
    },
    {
        "section": "JS", "level": 2, "total": 3,
        "title": "Listen for a click & Update message", "preview_text": "Preview: Now Playing changes to Wow!", "filename": "script.js",
        "code": """wowButton.addEventListener("click", function () {
  wowSound.currentTime = 0;
  wowSound.play();
  message.textContent = "Wow!";
});""",
        "bullets": ["addEventListener waits for something", "\"click\" is the event we are watching", "textContent changes the visible text"],
        "lang": "javascript",
        "iframe_html": "<main class='soundboard'><div class='message-box'><span>Now Playing:</span><strong id='message'>Wow!</strong></div><div class='button-grid'><button class='sound-button yellow'><span>😮</span> Wow!</button></div></main>",
        "iframe_css": "body{padding:20px;font-family:sans-serif;} .soundboard{text-align:center;background:white;padding:32px;border:8px solid #ff9f1c;border-radius:28px;} .message-box{background:#eef6ff;padding:16px;border-radius:14px;margin-bottom:24px;} .sound-button{min-height:125px;border:none;border-radius:20px;font-size:20px;font-weight:bold;box-shadow:0 8px 0 rgba(0,0,0,0.15);width:100%;} .yellow{background:#ffd43b;}"
    },
    {
        "section": "JS", "level": 3, "total": 3,
        "title": "Make a reusable function", "preview_text": "Preview: the Wow button still works", "filename": "script.js",
        "code": """function playSound(sound, soundName) {
  sound.currentTime = 0;
  sound.play();
  message.textContent = soundName;
}

wowButton.addEventListener("click", function () {
  playSound(wowSound, "Wow!");
});""",
        "bullets": ["A function groups repeated instructions", "sound and soundName are inputs", "Now the same logic can support all buttons"],
        "lang": "javascript",
        "iframe_html": "<main class='soundboard'><div class='message-box'><span>Now Playing:</span><strong id='message'>Wow!</strong></div><div class='button-grid'><button class='sound-button yellow'><span>😮</span> Wow!</button></div></main>",
        "iframe_css": "body{padding:20px;font-family:sans-serif;} .soundboard{text-align:center;background:white;padding:32px;border:8px solid #ff9f1c;border-radius:28px;} .message-box{background:#eef6ff;padding:16px;border-radius:14px;margin-bottom:24px;} .sound-button{min-height:125px;border:none;border-radius:20px;font-size:20px;font-weight:bold;box-shadow:0 8px 0 rgba(0,0,0,0.15);width:100%;} .yellow{background:#ffd43b;}"
    }
]

# Generate Journey HTML
journey_html = """
<section class="project-journey-section">
  <div class="journey-shell">
    <div class="journey-header">
      <span class="eyebrow">BUILD JOURNEY</span>
      <h2 style="font-size: 38px; color: #12355b; margin: 10px 0;">Meme Soundboard</h2>
      <p style="color: #62748a; font-size: 18px;">Start with the final output, then build it step by step using HTML, CSS and JavaScript.</p>
    </div>
    
    <!-- Aim Section -->
    <div class="journey-module">
      <div class="module-eyebrow">PROJECT OUTPUT</div>
      <h3 class="module-title">What are we building?</h3>
      <p class="module-desc">A soundboard that reacts when a user clicks a button.</p>
      
      <div class="aim-card">
        <h4>Project aim</h4>
        <p class="understand-title">Understand this:</p>
        <ul class="bullet-list">
          <li>Click a reaction button</li>
          <li>Play the correct sound</li>
          <li>Update the "Now Playing" text</li>
          <li>Keep the page simple and fun</li>
        </ul>
        <div class="aim-main-idea">Main idea: <strong>Click &rarr; Action &rarr; Result</strong></div>
      </div>
    </div>
    
    <!-- Interaction Flow -->
    <div class="journey-module">
      <div class="module-eyebrow">HOW IT WORKS</div>
      <h3 class="module-title">The simple interaction flow</h3>
      <p class="module-desc">Students should understand the behaviour before writing code.</p>
      
      <div class="flow-steps">
        <div class="flow-step"><div class="step-circle" style="background:#1d4ed8;">1</div><strong>Click</strong><p>Press a button</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#0ea5e9;">2</div><strong>Detect</strong><p>JS hears click</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#f59e0b;">3</div><strong>Play</strong><p>Audio starts</p></div>
        <div class="flow-step"><div class="step-circle" style="background:#8b5cf6;">4</div><strong>Update</strong><p>Message changes</p></div>
      </div>
    </div>
    
    <!-- Levels -->
"""

for level in journey_data:
    if "part" in level:
        journey_html += f"""
    <div class="journey-module" style="margin-top: 60px; padding: 40px; background: #082c66; border-radius: 16px; color: white;">
      <div class="module-eyebrow" style="background: #f59e0b; color: white;">{level['part']}</div>
      <h3 class="module-title" style="color: white; font-size: 32px;">{level['part_title']}</h3>
      <p style="color: #9bd8fa; font-size: 18px; max-width: 600px;">{level['part_desc']}</p>
    </div>
"""
    
    # Generate the srcdoc for the iframe
    srcdoc = f"<!DOCTYPE html><html><head><style>{level['iframe_css']}</style></head><body>{level['iframe_html']}</body></html>"
    srcdoc_escaped = html.escape(srcdoc, quote=True)
    
    bullets_html = "".join([f"<li>{b}</li>" for b in level['bullets']])
    
    journey_html += f"""
    <div class="level-card">
      <div class="level-header">
        <div class="level-badge">{level['section']} {level['level']} OF {level['total']}</div>
        <h3>{level['section']} Level {level['level']}: {level['title']}</h3>
        <p>{level['preview_text']}</p>
      </div>
      
      <div class="level-grid">
        <div class="level-code">
          <div class="code-header">
            <span class="dots"><i></i><i></i><i></i></span>
            <span class="filename">{level['filename']}</span>
          </div>
          <pre><code class="language-{level['lang']}">{html.escape(level['code'])}</code></pre>
        </div>
        
        <div class="level-preview">
          <div class="preview-header">
            <span class="dots"><i></i><i></i><i></i></span>
            <span class="filename">Browser preview</span>
          </div>
          <div class="iframe-wrapper">
             <iframe srcdoc="{srcdoc_escaped}"></iframe>
          </div>
          <div class="understand-section">
            <h4>Understand this</h4>
            <ul class="bullet-list">
              {bullets_html}
            </ul>
          </div>
        </div>
      </div>
    </div>
"""

journey_html += """
    <!-- QA & Challenge -->
    <div class="journey-module" style="margin-top: 80px;">
      <div class="module-eyebrow">TESTING</div>
      <h3 class="module-title">Before we say "finished"</h3>
      <ul class="check-list">
        <li>Every button plays the correct sound</li>
        <li>The Now Playing message changes correctly</li>
        <li>Rapid clicking restarts the sound</li>
        <li>The layout works on mobile</li>
        <li>There are no console errors</li>
      </ul>
    </div>
  </div>
</section>
"""

# Now replace the old journey section in day-three.html with this new one
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()

# The old journey section starts at <section class="project-journey-section"> and ends at </section> (but there might be multiple </section>).
# We can use regex to replace everything from <section class="project-journey-section"> up to the next <!-- PrismJS Core --> or <footer
match = re.search(r'<section class="project-journey-section">.*?</section>', html_content, flags=re.DOTALL)

# But wait, the old one has a <section class="project-journey-section"> inside it there are no other sections, so .*?</section> works.
if match:
    # Just to be safe, replace the exact matched section
    # Wait, the old journey section also contained the CODEBASE section! We need to keep the codebase section!
    # The user said: "keep it at the end".
    # So we should insert `journey_html` BEFORE the codebase section, or just inject `journey_html` right before `<div class="codebase-section">` inside the old section!
    pass

# Better approach: find `<div class="codebase-section">` inside `html_content`.
# Replace everything from `<section class="project-journey-section">` to just before `<div class="codebase-section">` with our new journey_html, BUT journey_html already has the `<section>` tag.
# Let's strip the `<section class="project-journey-section">` and `</section>` from journey_html, and inject it inside the existing section, replacing the old DESCRIPTION area.

inner_journey = journey_html.replace('<section class="project-journey-section">', '').replace('</section>', '')

# We want to replace:
#     <div class="journey-shell">
#       <div class="journey-header">...</div>
#       <div class="journey-text-section">...</div>
# 
# With `inner_journey` + `<div class="codebase-section">...</div>`

old_header_pattern = r'<div class="journey-header">.*?</div>\s*<div class="journey-text-section">.*?</div>'
html_content = re.sub(old_header_pattern, inner_journey, html_content, flags=re.DOTALL)

# Let's actually refine this. inner_journey contains its own `<div class="journey-shell">`. I should just replace `<div class="journey-shell">` to `<div class="codebase-section">` with `<div class="journey-shell">` + inner_journey + `<div class="codebase-section">`.
# Wait, `inner_journey` already contains `<div class="journey-shell">` and `</div>`. Let me just recreate the string logic manually to avoid regex pain.

# Find where `<div class="codebase-section">` starts.
cb_idx = html_content.find('<div class="codebase-section">')
sec_idx = html_content.find('<section class="project-journey-section">')

if cb_idx != -1 and sec_idx != -1:
    before = html_content[:sec_idx]
    # Keep the codebase section and everything after it, but close the journey-shell and section appropriately.
    after = html_content[cb_idx:]
    
    # We will build the new structure:
    # before + journey_html (without the closing </div></section>) + after
    # journey_html ends with:
    #   </div>
    # </section>
    
    clean_journey = journey_html.rsplit('</div>\n</section>', 1)[0]
    # Now it is open. We append `after`.
    new_html = before + clean_journey + "\n      " + after
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
        print("HTML updated!")

# --- ADD NEW CSS TO STYLE.CSS ---
new_css = """
/* Detailed Build Journey Styles */
.journey-module {
  margin-bottom: 60px;
}
.module-eyebrow {
  display: inline-block;
  padding: 6px 14px;
  background: white;
  color: #082c66;
  font-weight: 700;
  font-size: 13px;
  border-radius: 99px;
  border: 1px solid #dde8f3;
  margin-bottom: 12px;
}
.module-title {
  font-size: 28px;
  color: #12355b;
  margin: 0 0 10px;
}
.module-desc {
  font-size: 18px;
  color: #62748a;
  margin-bottom: 24px;
}

/* Aim Card */
.aim-card {
  background: white;
  padding: 30px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  border: 1px solid #dde8f3;
}
.aim-card h4 {
  font-size: 24px;
  margin: 0 0 16px;
  color: #12355b;
}
.understand-title {
  color: #0866d8;
  font-weight: bold;
  margin-bottom: 12px;
}
.bullet-list {
  padding-left: 20px;
  color: #374151;
  line-height: 1.6;
}
.bullet-list li {
  margin-bottom: 8px;
}
.aim-main-idea {
  margin-top: 24px;
  padding-top: 20px;
  border-top: 1px solid #e5e7eb;
  color: #f59e0b;
  font-weight: bold;
  font-size: 18px;
}

/* Flow Steps */
.flow-steps {
  display: flex;
  align-items: center;
  gap: 16px;
  overflow-x: auto;
  padding-bottom: 10px;
}
.flow-step {
  background: white;
  padding: 24px;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  border: 1px solid #dde8f3;
  text-align: center;
  min-width: 160px;
}
.step-circle {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  font-weight: bold;
  margin: 0 auto 16px;
}
.flow-step strong {
  display: block;
  font-size: 20px;
  margin-bottom: 8px;
  color: #12355b;
}
.flow-step p {
  color: #62748a;
  font-size: 14px;
  margin: 0;
}

/* Level Cards */
.level-card {
  margin-bottom: 40px;
}
.level-header {
  margin-bottom: 20px;
}
.level-badge {
  display: inline-block;
  padding: 6px 14px;
  background: white;
  color: #0866d8;
  font-weight: 700;
  font-size: 13px;
  border-radius: 99px;
  border: 1px solid #dde8f3;
  margin-bottom: 12px;
}
.level-header h3 {
  font-size: 24px;
  color: #12355b;
  margin: 0 0 8px;
}
.level-header p {
  color: #62748a;
  margin: 0;
}
.level-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
}
@media(max-width: 900px) {
  .level-grid { grid-template-columns: 1fr; }
}

.level-code {
  background: #0d1117;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}
.code-header, .preview-header {
  background: #161b22;
  padding: 12px 16px;
  display: flex;
  align-items: center;
  gap: 12px;
  border-bottom: 1px solid rgba(255,255,255,0.05);
}
.preview-header {
  background: #1e293b;
}
.dots i {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #ff5f56;
  margin-right: 6px;
}
.dots i:nth-child(2) { background: #ffbd2e; }
.dots i:nth-child(3) { background: #27c93f; margin-right: 0;}
.filename {
  color: #8b949e;
  font-size: 13px;
  font-family: monospace;
}
.preview-header .filename {
  color: #cbd5e1;
}
.level-code pre {
  margin: 0 !important;
  padding: 24px !important;
  background: transparent !important;
  font-size: 14px !important;
}

.level-preview {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 25px rgba(0,0,0,0.1);
  border: 1px solid #dde8f3;
  display: flex;
  flex-direction: column;
}
.iframe-wrapper {
  flex: 1;
  background: #f8fafc;
  border-bottom: 1px solid #dde8f3;
  position: relative;
  min-height: 250px;
}
.iframe-wrapper iframe {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  border: none;
}
.understand-section {
  padding: 24px;
}
.understand-section h4 {
  color: #f59e0b;
  margin: 0 0 12px;
  font-size: 18px;
}

.check-list {
  list-style: none;
  padding: 0;
}
.check-list li {
  padding: 16px 20px;
  background: white;
  margin-bottom: 8px;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.02);
  border: 1px solid #dde8f3;
  display: flex;
  align-items: center;
  font-weight: bold;
  color: #12355b;
}
.check-list li::before {
  content: '✓';
  display: inline-flex;
  width: 24px; height: 24px;
  background: #10b981;
  color: white;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin-right: 12px;
}
"""

with open(style_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

if "/* Detailed Build Journey Styles */" not in css_content:
    with open(style_file, 'a', encoding='utf-8') as f:
        f.write("\n" + new_css)
        print("CSS updated!")
