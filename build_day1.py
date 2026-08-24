import os
import re
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
html_file = os.path.join(base_dir, "Day One", "profile-card-lesson-project", "day-one.html")

journey_data = [
    # HTML LEVELS
    {
        "part": "PART 1", "part_title": "HTML builds the structure", "part_desc": "First we lay out the text and images. It will look like a plain document at first.",
        "section": "HTML", "level": 1, "total": 5,
        "title": "Basic page skeleton", "preview_text": "Preview: a blank browser page", "filename": "index.html",
        "code": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Profile Card</title>
</head>
<body>
</body>
</html>""",
        "bullets": ["The browser understands this as an HTML5 document", "The body is empty, so the page is blank", "The title appears in the browser tab"],
        "lang": "markup",
        "iframe_html": "<!DOCTYPE html><html><head><style></style></head><body></body></html>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 2, "total": 5,
        "title": "Main card container", "preview_text": "Preview: a blank container", "filename": "index.html",
        "code": """<body>
  <main class="profile-card">
    <!-- Profile content goes here -->
  </main>
</body>""",
        "bullets": ["<main> tells the browser this is the main content", "class=\"profile-card\" is a name we give it to style later", "Nothing is visible yet"],
        "lang": "markup",
        "iframe_html": "<!DOCTYPE html><html><head><style></style></head><body><main class='profile-card'></main></body></html>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 3, "total": 5,
        "title": "Add the profile photo", "preview_text": "Preview: the image appears very large", "filename": "index.html",
        "code": """<main class="profile-card">
  <img class="profile-photo" src="images/hassan_pic_short.jpg" alt="Hassan smiling">
</main>""",
        "bullets": ["<img> adds an image to the page", "src points to where the image file lives", "alt describes the image for screen readers"],
        "lang": "markup",
        "iframe_html": "<!DOCTYPE html><html><head><style></style></head><body><main class='profile-card'><img style='max-width: 150px; display: block; margin: 10px;' src='images/hassan_pic_short.jpg' alt='Hassan'></main></body></html>",
        "iframe_css": ""
    },
    {
        "section": "HTML", "level": 4, "total": 5,
        "title": "Name, Title, and Bio", "preview_text": "Preview: plain text appears below the image", "filename": "index.html",
        "code": """<section class="profile-info">
  <div class="name-row">
    <h1>Hassan Barrie</h1>
    <span class="level">Level 5</span>
  </div>
  <h2>Software Developer</h2>
  <div class="small-line"></div>
  <p>Passionate about building cool web projects.</p>
</section>""",
        "bullets": ["<h1> is the biggest heading", "<span class='level'> creates a small inline badge", "<div class='small-line'> acts as a decorative underline"],
        "lang": "markup",
        "iframe_html": "<main class='profile-card'><img style='max-width: 100px; display: block; margin: 10px;' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><div class='name-row'><h1>Hassan Barrie</h1><span class='level'>Level 5</span></div><h2>Software Developer</h2><div class='small-line'></div><p>Passionate about building cool web projects.</p></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; } .level { background: #0b72d6; color: white; padding: 5px 10px; border-radius: 8px; font-weight: bold; } .small-line { width: 105px; height: 5px; background: #ffa514; border-radius: 5px; }"
    },
    {
        "section": "HTML", "level": 5, "total": 5,
        "title": "Social links", "preview_text": "Preview: social icons appear as a list of images", "filename": "index.html",
        "code": """<nav class="social-links" aria-label="Social media links">
  <a href="#"><img src="images/facebook.svg" alt="Facebook"></a>
  <a href="#"><img src="images/tiktok.svg" alt="TikTok"></a>
  <a href="#"><img src="images/github.svg" alt="GitHub"></a>
  <a href="#"><img src="images/website.svg" alt="Website"></a>
</nav>""",
        "bullets": ["<nav> wraps navigation links", "<a> makes the image clickable", "aria-label helps accessibility"],
        "lang": "markup",
        "iframe_html": "<main class='profile-card'><img style='max-width: 100px; display: block; margin: 10px;' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><div class='name-row'><h1>Hassan Barrie</h1><span class='level'>Level 5</span></div><h2>Software Developer</h2><div class='small-line'></div><p>Passionate about building cool web projects.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a> <a href='#'>GH</a> <a href='#'>WEB</a></nav></section></main>",
        "iframe_css": "body { font-family: sans-serif; padding: 20px; } .level { background: #0b72d6; color: white; padding: 5px 10px; border-radius: 8px; font-weight: bold; } .small-line { width: 105px; height: 5px; background: #ffa514; border-radius: 5px; }"
    },
    
    # CSS LEVELS
    {
        "part": "PART 2", "part_title": "CSS turns structure into design", "part_desc": "Now we use CSS to position the elements exactly where we want them over a beautiful background.",
        "section": "CSS", "level": 1, "total": 6,
        "title": "Page background and fonts", "preview_text": "Preview: the page gets a background color and cleaner font", "filename": "style.css",
        "code": """* {
  box-sizing: border-box;
}
body {
  margin: 0;
  min-height: 100vh;
  display: flex;
  background: #eef5fb;
  font-family: Arial, Helvetica, sans-serif;
  color: #081b3a;
}""",
        "bullets": ["* selects everything and fixes how width is calculated", "body gives the whole page a background color", "font-family changes the text style globally"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><h1>Hassan Barrie</h1><p>Software Developer</p></main>",
        "iframe_css": "body { margin: 0; min-height: 100vh; background: #eef5fb; font-family: Arial, Helvetica, sans-serif; color: #081b3a; padding: 20px; }"
    },
    {
        "section": "CSS", "level": 2, "total": 6,
        "title": "Background and Card size", "preview_text": "Preview: card takes shape with a background image", "filename": "style.css",
        "code": """.profile-card {
  margin: auto;
  position: relative;
  width: min(100%, 980px);
  aspect-ratio: 1536 / 940;
  background: url("images/background.jpg") center / 100% 100% no-repeat;
}""",
        "bullets": ["width restricts the maximum size", "aspect-ratio keeps the exact shape", "background loads the beautiful cover art"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><img class='profile-photo' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><h1>Hassan Barrie</h1><h2>Software Developer</h2><p>Passionate about building cool web projects and learning new technologies every day.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a></nav></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eef5fb; } .profile-card { margin: auto; position: relative; width: 100%; max-width: 600px; aspect-ratio: 16/9; background: #12355b; color: white; border-radius: 12px; overflow: hidden; padding: 20px; } .profile-photo { max-width: 100px; }"
    },
    {
        "section": "CSS", "level": 3, "total": 6,
        "title": "Positioning the Photo", "preview_text": "Preview: photo becomes a circle and moves to the left", "filename": "style.css",
        "code": """.profile-photo {
  position: absolute;
  left: 6.5%;
  top: 15%;
  width: 31%;
  height: 68%;
  object-fit: cover;
  border: 7px solid white;
  border-radius: 50%;
  box-shadow: 0 10px 25px rgba(0, 58, 140, 0.22);
}""",
        "bullets": ["position: absolute lets us place it exactly", "border-radius: 50% turns a square into a circle", "object-fit: cover stops the image from stretching"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><img class='profile-photo' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><h1>Hassan Barrie</h1><h2>Software Developer</h2><p>Passionate about building cool web projects and learning new technologies every day.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a></nav></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eef5fb; } .profile-card { margin: auto; position: relative; width: 100%; max-width: 600px; aspect-ratio: 16/9; background: #cce3f8; color: #081b3a; border-radius: 12px; overflow: hidden; } .profile-photo { position: absolute; left: 10%; top: 15%; width: 25%; height: 70%; object-fit: cover; border: 4px solid white; border-radius: 50%; box-shadow: 0 10px 25px rgba(0,0,0,0.2); } .profile-info { margin-left: 45%; padding-top: 10%; }"
    },
    {
        "section": "CSS", "level": 4, "total": 6,
        "title": "Typography and Spacing", "preview_text": "Preview: text looks clean and professional", "filename": "style.css",
        "code": """h1 {
  font-size: clamp(28px, 5vw, 58px);
}
.level {
  padding: 10px 16px;
  border-radius: 12px;
  background: #0b72d6;
  color: white;
}
.small-line {
  width: 105px;
  height: 5px;
  background: #ffa514;
}""",
        "bullets": ["clamp() makes font size responsive to screen width", "The .level class styles our small badge", "The .small-line creates the orange decorative underline"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><img class='profile-photo' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><div class='name-row'><h1>Hassan Barrie</h1><span class='level'>Level 5</span></div><h2>Software Developer</h2><div class='small-line'></div><p>Passionate about building cool web projects and learning new technologies every day.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a></nav></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eef5fb; } .profile-card { margin: auto; position: relative; width: 100%; max-width: 600px; aspect-ratio: 16/9; background: #cce3f8; color: #081b3a; border-radius: 12px; overflow: hidden; } .profile-photo { position: absolute; left: 10%; top: 15%; width: 25%; height: 70%; object-fit: cover; border: 4px solid white; border-radius: 50%; box-shadow: 0 10px 25px rgba(0,0,0,0.2); } .profile-info { margin-left: 45%; padding-top: 10%; } .name-row { display: flex; align-items: center; gap: 10px; } h1 { font-size: 32px; margin: 0; } .level { padding: 8px 12px; border-radius: 8px; background: #0b72d6; color: white; font-weight: bold; font-size: 14px; } h2 { color: #0b72d6; font-size: 20px; margin: 10px 0; } .small-line { width: 105px; height: 5px; border-radius: 5px; background: #ffa514; } p { color: #202b3d; line-height: 1.4; }"
    },
    {
        "section": "CSS", "level": 5, "total": 6,
        "title": "Social links styling", "preview_text": "Preview: social links become interactive buttons", "filename": "style.css",
        "code": """.social-links {
  display: flex;
  gap: 18px;
}
.social-links a {
  padding: 13px;
  border-radius: 16px;
  background: white;
  box-shadow: 0 7px 18px rgba(3, 45, 92, 0.16);
  transition: transform 0.2s ease;
}""",
        "bullets": ["display: flex lines the buttons up horizontally", "box-shadow gives them depth", "transition prepares the buttons for hover effects"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><img class='profile-photo' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><div class='name-row'><h1>Hassan Barrie</h1><span class='level'>Level 5</span></div><h2>Software Developer</h2><div class='small-line'></div><p>Passionate about building cool web projects.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a> <a href='#'>GH</a> <a href='#'>WEB</a></nav></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eef5fb; } .profile-card { margin: auto; position: relative; width: 100%; max-width: 600px; aspect-ratio: 16/9; background: #cce3f8; color: #081b3a; border-radius: 12px; overflow: hidden; } .profile-photo { position: absolute; left: 10%; top: 15%; width: 25%; height: 70%; object-fit: cover; border: 4px solid white; border-radius: 50%; box-shadow: 0 10px 25px rgba(0,0,0,0.2); } .profile-info { margin-left: 45%; padding-top: 10%; } h1 { font-size: 32px; margin: 0; } .level { padding: 8px 12px; border-radius: 8px; background: #0b72d6; color: white; font-weight: bold; font-size: 14px; } h2 { color: #0b72d6; font-size: 20px; margin: 10px 0; } .small-line { width: 105px; height: 5px; border-radius: 5px; background: #ffa514; } p { color: #202b3d; line-height: 1.4; margin-bottom: 20px; } .social-links { display: flex; gap: 12px; } .social-links a { display: grid; place-items: center; width: 40px; height: 40px; background: white; text-decoration: none; font-weight: bold; color: #081b3a; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }"
    },
    {
        "section": "CSS", "level": 6, "total": 6,
        "title": "Hover states and Responsiveness", "preview_text": "Preview: the card is interactive and resizes for mobile", "filename": "style.css",
        "code": """.profile-card:hover {
  transform: translateY(-8px);
}
.social-links a:hover {
  transform: translateY(-6px) scale(1.05);
}

@media (max-width: 650px) {
  body { padding: 10px; }
  h2 { margin-top: 14px; }
  p { margin: 18px 0 16px; }
  .social-links a { padding: 8px; border-radius: 10px; }
}""",
        "bullets": [":hover changes how elements look when the mouse is over them", "transform: translateY() moves elements up slightly", "@media allows us to change the design on smaller screens"],
        "lang": "css",
        "iframe_html": "<main class='profile-card'><img class='profile-photo' src='images/hassan_pic_short.jpg' alt='Hassan'><section class='profile-info'><div class='name-row'><h1>Hassan Barrie</h1><span class='level'>Level 5</span></div><h2>Software Developer</h2><div class='small-line'></div><p>Passionate about building cool web projects.</p><nav class='social-links'><a href='#'>FB</a> <a href='#'>TK</a> <a href='#'>GH</a> <a href='#'>WEB</a></nav></section></main>",
        "iframe_css": "body { padding: 20px; font-family: sans-serif; background: #eef5fb; } .profile-card { margin: auto; position: relative; width: 100%; max-width: 600px; aspect-ratio: 16/9; background: #cce3f8; color: #081b3a; border-radius: 12px; overflow: hidden; transition: transform 0.3s; } .profile-card:hover { transform: translateY(-8px); } .profile-photo { position: absolute; left: 10%; top: 15%; width: 25%; height: 70%; object-fit: cover; border: 4px solid white; border-radius: 50%; box-shadow: 0 10px 25px rgba(0,0,0,0.2); } .profile-info { margin-left: 45%; padding-top: 10%; } h1 { font-size: 32px; margin: 0; } .level { padding: 8px 12px; border-radius: 8px; background: #0b72d6; color: white; font-weight: bold; font-size: 14px; } h2 { color: #0b72d6; font-size: 20px; margin: 10px 0; } .small-line { width: 105px; height: 5px; border-radius: 5px; background: #ffa514; } p { color: #202b3d; line-height: 1.4; margin-bottom: 20px; } .social-links { display: flex; gap: 12px; } .social-links a { display: grid; place-items: center; width: 40px; height: 40px; background: white; text-decoration: none; font-weight: bold; color: #081b3a; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); transition: transform 0.2s; } .social-links a:hover { transform: translateY(-4px) scale(1.05); }"
    }
]

journey_html = """
<section class="project-journey-section">
  <div class="journey-shell">
    <div class="journey-header">
      <span class="eyebrow">BUILD JOURNEY</span>
      <h2 style="font-size: 38px; color: #12355b; margin: 10px 0;">Profile Card</h2>
      <p style="color: #62748a; font-size: 18px;">Start with the final output, then build it step by step using HTML and CSS.</p>
    </div>
    
    <div class="journey-module">
      <div class="module-eyebrow">PROJECT OUTPUT</div>
      <h3 class="module-title">What are we building?</h3>
      <p class="module-desc">A professional developer profile card.</p>
      
      <div class="aim-card">
        <h4>Project aim</h4>
        <p class="understand-title">Understand this:</p>
        <ul class="bullet-list">
          <li>Create an attractive layout</li>
          <li>Absolute positioning for images</li>
          <li>Responsive typography (clamp)</li>
          <li>Interactive hover states</li>
        </ul>
        <div class="aim-main-idea">Main idea: <strong>Structure &rarr; Position &rarr; Polish</strong></div>
      </div>
    </div>
"""

for level in journey_data:
    if "part" in level:
        journey_html += f"""
    <div class="journey-module" style="margin-top: 60px; padding: 40px; background: #082c66; border-radius: 16px; color: white;">
      <div class="module-eyebrow" style="background: #f59e0b; color: white;">{level['part']}</div>
      <h3 class="module-title" style="color: white; font-size: 32px;">{level['part_title']}</h3>
      <p style="color: #9bd8fa; font-size: 18px; max-width: 600px; margin: 0 auto;">{level['part_desc']}</p>
    </div>
"""
    
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
    <div class="journey-module" style="margin-top: 80px;">
      <div class="module-eyebrow">TESTING</div>
      <h3 class="module-title">Before we say "finished"</h3>
      <ul class="check-list">
        <li>The profile photo is perfectly circular</li>
        <li>Social links pop up when hovered</li>
        <li>The card resizes correctly on smaller screens</li>
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
        print("Day 1 HTML updated!")
