import os
import html
import re

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
style_file = os.path.join(base_dir, 'style.css')

with open(style_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find where "/* Project Journey Section */" starts and truncate
split_str = "/* Project Journey Section */"
if split_str in css_content:
    css_content = css_content.split(split_str)[0]

new_css = """
/* Project Journey Section */
.project-journey-section {
  padding: 80px 24px;
  background: #f4f7fb;
  border-top: 1px solid var(--line);
}
.journey-header {
  text-align: center;
  margin-bottom: 60px;
}
.journey-header .eyebrow {
  color: var(--blue);
  font-weight: 700;
  letter-spacing: 2px;
  font-size: 13px;
  background: rgba(8, 102, 216, 0.1);
  padding: 6px 14px;
  border-radius: 99px;
  display: inline-block;
  margin-bottom: 16px;
}
.journey-text-section {
  margin-bottom: 40px;
  max-width: 1000px;
  margin-inline: auto;
}
.section-label {
  font-size: 15px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  margin-bottom: 16px;
  color: var(--navy);
  font-weight: 800;
  position: relative;
  display: inline-block;
}
.section-label::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -6px;
  width: 100%;
  height: 3px;
  background: linear-gradient(90deg, var(--blue), var(--cyan));
  border-radius: 2px;
}
.journey-desc {
  text-align: left;
  max-width: 100%;
  color: var(--muted);
  font-size: 17px;
  line-height: 1.7;
}
.codebase-section {
  max-width: 1000px;
  margin-inline: auto;
}
.codebase-section h3.section-label {
  margin-bottom: 24px;
}
.tabs-container {
  background: #1d1f21;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
}
.tabs-header {
  background: #111214;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
  padding-right: 16px;
}
.tabs-nav {
  display: flex;
  gap: 2px;
}
.tab-btn {
  background: transparent;
  color: #8b949e;
  border: none;
  padding: 14px 24px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  border-top: 2px solid transparent;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;
  font-family: inherit;
}
.tab-btn:hover {
  color: #c9d1d9;
  background: rgba(255, 255, 255, 0.03);
}
.tab-btn.active {
  color: #fff;
  background: #1d1f21;
  border-top-color: var(--blue);
}
.copy-wrapper {
  position: relative;
}
.copy-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8px;
  border-radius: 6px;
  color: #8b949e;
  transition: all 0.2s;
}
.copy-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}
.copy-icon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}
.tooltip {
  position: absolute;
  top: -32px;
  left: 50%;
  transform: translateX(-50%) scale(0.9);
  background: #fff;
  color: #000;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: bold;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s, transform 0.2s;
}
.copy-wrapper.copied .tooltip {
  opacity: 1;
  transform: translateX(-50%) scale(1);
}
.tab-content {
  display: none;
}
.tab-content.active {
  display: block;
}
/* PrismJS Overrides */
.tabs-container pre[class*="language-"] {
  margin: 0;
  padding: 24px;
  background: transparent;
  max-height: 500px;
  overflow-y: auto;
  border-radius: 0;
  text-shadow: none;
}
.tabs-container code[class*="language-"] {
  font-family: 'JetBrains Mono', Consolas, Monaco, 'Ubuntu Mono', monospace;
  font-size: 14px;
  line-height: 1.6;
  text-shadow: none;
}
.tabs-container pre::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.tabs-container pre::-webkit-scrollbar-thumb {
  background: #444;
  border-radius: 4px;
}
.tabs-container pre::-webkit-scrollbar-track {
  background: #1d1f21;
}
"""

with open(style_file, 'w', encoding='utf-8') as f:
    f.write(css_content.strip() + "\n\n" + new_css.strip() + "\n")

copy_svg = '''<svg class="copy-icon" viewBox="0 0 24 24"><path d="M16 1H4c-1.1 0-2 .9-2 2v14h2V3h12V1zm3 4H8c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h11c1.1 0 2-.9 2-2V7c0-1.1-.9-2-2-2zm0 16H8V7h11v14z"/></svg>'''

prism_css = '<link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />'

js_snippet = """
  <!-- PrismJS Core -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js"></script>
  <script>
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const container = btn.closest('.tabs-container');
        container.querySelectorAll('.tab-btn').forEach(t => t.classList.remove('active'));
        container.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        btn.classList.add('active');
        container.querySelector('#' + btn.getAttribute('data-target')).classList.add('active');
      });
    });

    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const container = this.closest('.tabs-container');
        const activePre = container.querySelector('.tab-content.active pre');
        
        navigator.clipboard.writeText(activePre.innerText).then(() => {
          const wrapper = this.closest('.copy-wrapper');
          wrapper.classList.add('copied');
          
          const originalIcon = this.innerHTML;
          this.innerHTML = '<svg class="copy-icon" viewBox="0 0 24 24"><path fill="#4ade80" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>';
          
          setTimeout(() => { 
            wrapper.classList.remove('copied'); 
            this.innerHTML = originalIcon;
          }, 2000);
        });
      });
    });
  </script>
"""

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
    
    # Strip old journey section
    clean_html = re.sub(r'<div class="project-showcase">\s*<main', '<main', html_content)
    clean_html = re.sub(r'</main>\s*</div>', '</main>', clean_html)
    clean_html = re.sub(r'<section class="project-journey-section">.*?</section>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<footer class="site-footer".*?</footer>', '', clean_html, flags=re.DOTALL)
    
    # Strip previous copy scripts and prism
    clean_html = re.sub(r'<script>\s*document\.querySelectorAll\(\'.copy-btn\'\).*?</script>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<!-- PrismJS Core.*?</script>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<link href=".*?prism-tomorrow.*?/>', '', clean_html)
    
    clean_html = re.sub(r'\s*</body>', '\n</body>', clean_html)
    clean_html = re.sub(r'\s*</head>', '\n</head>', clean_html)
    
    with open(css_file, 'r', encoding='utf-8') as f:
        css_code = f.read()
        
    js_code = ""
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_code = f.read()
            
    esc_html = html.escape(clean_html.strip())
    esc_css = html.escape(css_code.strip())
    esc_js = html.escape(js_code.strip()) if js_code else ""
    
    tabs_nav = f'<button class="tab-btn active" data-target="tab-html">index.html</button>'
    tabs_nav += f'\n              <button class="tab-btn" data-target="tab-css">style.css</button>'
    if esc_js:
        tabs_nav += f'\n              <button class="tab-btn" data-target="tab-js">script.js</button>'
        
    js_tab = ""
    if esc_js:
        js_tab = f"""
          <div class="tab-content" id="tab-js">
            <pre><code class="language-javascript">{esc_js}</code></pre>
          </div>"""
          
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
        <div class="tabs-container">
          <div class="tabs-header">
            <div class="tabs-nav">
              {tabs_nav.strip()}
            </div>
            <div class="copy-wrapper">
              <span class="tooltip">Copied!</span>
              <button class="copy-btn" aria-label="Copy code">
                {copy_svg}
              </button>
            </div>
          </div>
          
          <div class="tab-content active" id="tab-html">
            <pre><code class="language-markup">{esc_html}</code></pre>
          </div>
          <div class="tab-content" id="tab-css">
            <pre><code class="language-css">{esc_css}</code></pre>
          </div>
          {js_tab.strip()}
        </div>
      </div>
    </div>
  </section>
"""

    old_section_pattern = r'<section class="project-journey-section">.*?</section>'
    if re.search(old_section_pattern, html_content, flags=re.DOTALL):
        html_content = re.sub(old_section_pattern, journey_section.strip(), html_content, flags=re.DOTALL)
    else:
        # If it wasn't there (shouldn't happen)
        html_content = html_content.replace("</body>", journey_section + "\n</body>")
        
    # Inject Prism CSS in head
    if "prism-tomorrow" not in html_content:
        html_content = html_content.replace("</head>", f"  {prism_css}\n</head>")
        
    # Inject JS scripts at bottom
    if "PrismJS Core" not in html_content:
        html_content = html_content.replace("</body>", js_snippet + "\n</body>")
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Tabbed layout applied!")
