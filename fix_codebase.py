import os
import html
import re

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"

# CSS overrides to append
css_overrides = """
/* Project Journey Section Fixes */
.project-journey-section {
  padding: 60px 24px;
  background: #ffffff;
}
.journey-header {
  text-align: center;
  margin-bottom: 60px;
}
.journey-header .eyebrow {
  color: #333;
  font-weight: 400;
  letter-spacing: 1px;
  font-size: 14px;
  background: transparent;
  padding: 0;
}
.journey-text-section {
  margin-bottom: 40px;
}
.section-label {
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 16px;
  color: #000;
  font-weight: bold;
}
.journey-desc {
  text-align: left;
  max-width: 100%;
  color: #555;
  font-size: 15px;
}
.codebase-section h3.section-label {
  margin-bottom: 24px;
  border: none;
  padding: 0;
  font-size: 12px;
}
.code-grid {
  gap: 32px;
}
.code-block-wrapper {
  background: #e5e5e5;
  border-radius: 4px;
  box-shadow: none;
}
.code-header {
  background: transparent;
  color: #333;
  font-weight: bold;
  padding: 12px 16px;
}
.code-block-wrapper pre {
  background: transparent;
  color: #333;
  padding: 0 16px 16px;
}
.copy-btn {
  background: transparent;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 4px;
  opacity: 0.6;
  transition: opacity 0.2s;
}
.copy-btn:hover {
  opacity: 1;
}
.copy-icon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}
.js-block-wrapper {
  grid-column: 1 / -1;
  width: 75%;
  margin: 0 auto;
}
@media (max-width: 768px) {
  .js-block-wrapper {
    width: 100%;
  }
}
"""

with open(os.path.join(base_dir, 'style.css'), 'a') as f:
    f.write(css_overrides)

copy_svg = '''<svg class="copy-icon" viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>'''

projects = [
    ('Day One/profile-card-lesson-project', 'day-one', 'A simple and clean profile card using HTML and CSS to display user information, social links, and an avatar. This project teaches fundamental layout skills and image positioning.'),
    ('Day Two/kairo-project', 'day-two', 'An interactive character trading card featuring hover effects and stylized statistics. This project introduces more advanced CSS styling, borders, and transitions.'),
    ('Day Three/day3-meme-soundboard', 'day-three', 'A fun meme soundboard that plays audio when buttons are clicked. This project introduces JavaScript for DOM manipulation and handling click events to trigger media.'),
    ('Day Four/mystery-loot-box', 'day-four', 'A mystery loot box simulator where clicking a button reveals a random reward. It demonstrates JavaScript arrays, Math.random(), and dynamic text updates.'),
    ('Day Five/loot-box-inventory', 'day-five', 'An expanded loot box system that tracks an inventory of items obtained over multiple pulls. It teaches state management, looping, and dynamically rendering lists in the DOM.')
]

for folder, name, desc in projects:
    html_file = os.path.join(base_dir, folder, name + '.html')
    css_file = os.path.join(base_dir, folder, name + '.css')
    js_file = os.path.join(base_dir, folder, name + '.js')

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    clean_html = re.sub(r'<div class="project-showcase">\s*<main', '<main', html_content)
    clean_html = re.sub(r'</main>\s*</div>', '</main>', clean_html)
    clean_html = re.sub(r'<section class="project-journey-section">.*?</section>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<footer class="site-footer".*?</footer>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'\s*</body>', '\n</body>', clean_html)
    
    with open(css_file, 'r', encoding='utf-8') as f:
        css_code = f.read()
        
    js_code = ""
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_code = f.read()
            
    esc_html = html.escape(clean_html.strip())
    esc_css = html.escape(css_code.strip())
    esc_js = html.escape(js_code.strip()) if js_code else ""
    
    journey_section = f"""
  <section class="project-journey-section">
    <div class="journey-shell">
      <div class="journey-header">
        <span class="eyebrow">PROJECT JOURNEY</span>
      </div>
      
      <div class="journey-text-section">
        <div class="section-label">DESCRIPTION</div>
        <p class="journey-desc">{desc}</p>
      </div>

      <div class="codebase-section">
        <h3 class="section-label">CODEBASE</h3>
        <div class="code-grid">
          <div class="code-block-wrapper">
            <div class="code-header">
              <span>HTML</span>
              <button class="copy-btn" aria-label="Copy HTML code">{copy_svg}</button>
            </div>
            <pre><code>{esc_html}</code></pre>
          </div>
          <div class="code-block-wrapper">
            <div class="code-header">
              <span>CSS</span>
              <button class="copy-btn" aria-label="Copy CSS code">{copy_svg}</button>
            </div>
            <pre><code>{esc_css}</code></pre>
          </div>
"""
    if esc_js:
        journey_section += f"""
          <div class="code-block-wrapper js-block-wrapper">
            <div class="code-header">
              <span>JS</span>
              <button class="copy-btn" aria-label="Copy JS code">{copy_svg}</button>
            </div>
            <pre><code>{esc_js}</code></pre>
          </div>
"""
    journey_section += """
        </div>
      </div>
    </div>
  </section>
"""

    old_section_pattern = r'<section class="project-journey-section">.*?</section>'
    html_content = re.sub(old_section_pattern, journey_section.strip(), html_content, flags=re.DOTALL)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Layout fixes applied successfully!")
