import os
import re
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
html_file = os.path.join(base_dir, "Day Two", "kairo-project", "day-two.html")

journey_data = [
    # HTML LEVELS
    {
        "part": "PART 1", "part_title": "HTML builds the structure", "part_desc": "We build the character card top-to-bottom. It will look like a plain web page at first.",
        "section": "HTML", "level": 1, "total": 4,
        "title": "Hero image and title", "preview_text": "Preview: image and basic text", "filename": "index.html",
        "code": """<main class="card">
  <img class="hero-image" src="images/kairo.jpg" alt="Kairo">
  <section class="content">
    <h1>KAIRO</h1>
    <p class="type">💧 WATER</p>
    <p class="description">A calm and focused warrior who controls the power of water.</p>
  </section>
</main>""",
        "bullets": ["<img> loads the character portrait", "<h1> is the main character name", "<p> holds the description text"],
        "lang": "markup",
        "iframe_html": "<main class='card'><img style='width: 150px; display: block;' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><p class='description'>A calm and focused warrior who controls the power of water.</p></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 2, "total": 4,
        "title": "Character stats", "preview_text": "Preview: stats appear as a vertical list", "filename": "index.html",
        "code": """<div class="stats">
  <div>
    <span>⚔️</span>
    <p>POWER</p>
    <strong>85</strong>
  </div>
  <div>
    <span>🪽</span>
    <p>SPEED</p>
    <strong>92</strong>
  </div>
</div>""",
        "bullets": ["<div> groups related data together", "We use nested divs for each stat column", "Emojis (⚔️) are just text characters!"],
        "lang": "markup",
        "iframe_html": "<main class='card'><img style='width: 150px; display: block;' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><p class='description'>A calm and focused warrior who controls the power of water.</p><div class='stats'><div><span>⚔️</span><p>POWER</p><strong>85</strong></div><div><span>🪽</span><p>SPEED</p><strong>92</strong></div></div></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 3, "total": 4,
        "title": "Special move", "preview_text": "Preview: special move text is added", "filename": "index.html",
        "code": """<div class="special-move">
  <span class="move-icon">🌊</span>
  <div>
    <small>SPECIAL MOVE</small>
    <h2>TIDAL SLASH</h2>
    <p>Unleashes a powerful wave that strikes all enemies.</p>
  </div>
</div>""",
        "bullets": ["<small> makes text slightly smaller by default", "<h2> is used for the move title", "The structure groups the icon and the text"],
        "lang": "markup",
        "iframe_html": "<main class='card'><img style='width: 100px; display: block;' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><div class='stats'>...</div><div class='special-move'><span class='move-icon'>🌊</span><div><small>SPECIAL MOVE</small><h2>TIDAL SLASH</h2><p>Unleashes a powerful wave.</p></div></div></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    {
        "section": "HTML", "level": 4, "total": 4,
        "title": "Select button", "preview_text": "Preview: a default browser button appears", "filename": "index.html",
        "code": """<button>SELECT CHARACTER</button>""",
        "bullets": ["<button> creates a clickable element", "It sits at the very bottom of the card", "HTML is finished, time for CSS!"],
        "lang": "markup",
        "iframe_html": "<main class='card'><img style='width: 100px; display: block;' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><div class='stats'>...</div><div class='special-move'>...</div><button>SELECT CHARACTER</button></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; }"
    },
    
    # CSS LEVELS
    {
        "part": "PART 2", "part_title": "CSS turns structure into design", "part_desc": "Now we style the card layout, add borders, and use Flexbox to align the stats perfectly.",
        "section": "CSS", "level": 1, "total": 4,
        "title": "The Main Card", "preview_text": "Preview: the card shape forms with a blue border", "filename": "style.css",
        "code": """.card {
  margin: auto;
  width: 360px;
  background: white;
  border: 8px solid #168ce2;
  border-radius: 25px;
  overflow: hidden;
  box-shadow: 0 14px 30px rgba(0, 91, 170, 0.22);
}
.hero-image {
  width: 100%;
  height: 220px;
  object-fit: cover;
}""",
        "bullets": ["border adds the thick blue outline", "overflow: hidden stops the image from breaking out of rounded corners", "object-fit: cover perfectly crops the image"],
        "lang": "css",
        "iframe_html": "<main class='card'><img class='hero-image' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><p class='description'>A calm and focused warrior.</p></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eaf7ff; } .card { margin: auto; width: 360px; background: white; border: 8px solid #168ce2; border-radius: 25px; overflow: hidden; box-shadow: 0 14px 30px rgba(0,0,0,0.2); } .hero-image { width: 100%; height: 220px; object-fit: cover; display: block; } .content { padding: 20px; text-align: center; }"
    },
    {
        "section": "CSS", "level": 2, "total": 4,
        "title": "Typography and Tags", "preview_text": "Preview: texts become bold and styled", "filename": "style.css",
        "code": """h1 {
  font-size: 46px;
  letter-spacing: 3px;
}
.type {
  display: inline-block;
  padding: 7px 22px;
  color: white;
  background: #087bea;
  border-radius: 20px;
}""",
        "bullets": ["letter-spacing spaces out the title", "display: inline-block allows the type tag to have padding", "border-radius creates the pill shape"],
        "lang": "css",
        "iframe_html": "<main class='card'><img class='hero-image' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><p class='description'>A calm and focused warrior.</p></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eaf7ff; } .card { margin: auto; width: 360px; background: white; border: 8px solid #168ce2; border-radius: 25px; overflow: hidden; } .hero-image { width: 100%; height: 220px; object-fit: cover; display: block; } .content { padding: 20px; text-align: center; } h1 { margin: 0; font-size: 46px; letter-spacing: 3px; color: #082c66;} .type { display: inline-block; margin: 8px 0 12px; padding: 7px 22px; color: white; font-weight: bold; background: #087bea; border-radius: 20px; } .description { margin: 0 0 18px; color: #263b60; line-height: 1.5; }"
    },
    {
        "section": "CSS", "level": 3, "total": 4,
        "title": "Flexbox Stats", "preview_text": "Preview: stats align side-by-side horizontally", "filename": "style.css",
        "code": """.stats {
  display: flex;
  justify-content: space-between;
  padding: 15px 5px;
  border: 2px solid #9bd8fa;
  border-radius: 16px;
  background: #f4fbff;
}
.stats div {
  flex: 1;
}""",
        "bullets": ["display: flex turns a vertical stack into a row", "justify-content: space-between pushes columns apart", "flex: 1 forces each column to be the exact same width"],
        "lang": "css",
        "iframe_html": "<main class='card'><img class='hero-image' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><div class='stats'><div><span>⚔️</span><p>POWER</p><strong>85</strong></div><div><span>🪽</span><p>SPEED</p><strong>92</strong></div></div></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eaf7ff; } .card { margin: auto; width: 360px; background: white; border: 8px solid #168ce2; border-radius: 25px; overflow: hidden; } .hero-image { width: 100%; height: 220px; object-fit: cover; display: block; } .content { padding: 20px; text-align: center; } h1 { margin: 0; font-size: 46px; letter-spacing: 3px; color: #082c66;} .type { display: inline-block; margin: 8px 0 12px; padding: 7px 22px; color: white; font-weight: bold; background: #087bea; border-radius: 20px; } .stats { display: flex; justify-content: space-between; gap: 8px; padding: 15px 5px; border: 2px solid #9bd8fa; border-radius: 16px; background: #f4fbff; } .stats div { flex: 1; } .stats p { margin: 5px 0 2px; font-size: 12px; font-weight: bold; } .stats strong { font-size: 27px; color: #087bea; }"
    },
    {
        "section": "CSS", "level": 4, "total": 4,
        "title": "Special Move & Button", "preview_text": "Preview: the card is completely styled", "filename": "style.css",
        "code": """.special-move {
  display: flex;
  align-items: center;
  gap: 12px;
  text-align: left;
}
button {
  width: 100%;
  padding: 14px;
  border-radius: 25px;
  color: white;
  background: #078bea;
  cursor: pointer;
}""",
        "bullets": ["align-items: center perfectly aligns the emoji and text", "width: 100% makes the button fill the card width", "cursor: pointer changes the mouse to a hand"],
        "lang": "css",
        "iframe_html": "<main class='card'><img class='hero-image' src='images/kairo.jpg' alt='Kairo'><section class='content'><h1>KAIRO</h1><p class='type'>💧 WATER</p><div class='special-move'><span class='move-icon'>🌊</span><div><small>SPECIAL MOVE</small><h2>TIDAL SLASH</h2><p>Unleashes a powerful wave.</p></div></div><button>SELECT CHARACTER</button></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eaf7ff; } .card { margin: auto; width: 360px; background: white; border: 8px solid #168ce2; border-radius: 25px; overflow: hidden; } .hero-image { width: 100%; height: 220px; object-fit: cover; display: block; } .content { padding: 20px; text-align: center; } h1 { margin: 0; font-size: 46px; letter-spacing: 3px; color: #082c66;} .type { display: inline-block; margin: 8px 0 12px; padding: 7px 22px; color: white; font-weight: bold; background: #087bea; border-radius: 20px; } .special-move { display: flex; align-items: center; gap: 12px; margin-top: 14px; padding: 14px; text-align: left; border: 2px solid #9bd8fa; border-radius: 16px; background: #e9f8ff; } .move-icon { font-size: 42px; } .special-move h2 { margin: 2px 0; font-size: 21px; color: #082c66;} .special-move small { font-weight: bold; color: #087bea; } .special-move p { margin: 0; font-size: 13px; color: #263b60; } button { width: 100%; margin-top: 16px; padding: 14px; border: none; border-radius: 25px; color: white; background: #078bea; font-size: 18px; font-weight: bold; cursor: pointer; }"
    }
]

journey_html = """
<section class="project-journey-section">
  <div class="journey-shell">
    <div class="journey-header">
      <span class="eyebrow">BUILD JOURNEY</span>
      <h2 style="font-size: 38px; color: #12355b; margin: 10px 0;">Kairo Project</h2>
      <p style="color: #62748a; font-size: 18px;">Start with the final output, then build it step by step using HTML and CSS.</p>
    </div>
    
    <div class="journey-module" style="text-align: center;">
      <div class="module-eyebrow">PROJECT OUTPUT</div>
      <h3 class="module-title">What are we building?</h3>
      <p class="module-desc" style="margin-left: auto; margin-right: auto;">A Trading Card Game character profile.</p>
      
      <div class="aim-card" style="text-align: left;">
        <h4>Project aim</h4>
        <p class="understand-title">Understand this:</p>
        <ul class="bullet-list">
          <li>Build an engaging character profile layout</li>
          <li>Use Flexbox for side-by-side stats</li>
          <li>Style buttons and badges</li>
          <li>Keep it responsive and clean</li>
        </ul>
        <div class="aim-main-idea">Main idea: <strong>Structure &rarr; Flexbox &rarr; Polish</strong></div>
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
        <li>The hero image completely covers the top of the card</li>
        <li>The stats columns are exactly the same width</li>
        <li>The button fills the bottom of the card</li>
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
        print("Day 2 HTML updated!")
