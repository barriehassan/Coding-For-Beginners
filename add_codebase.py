import os
import html

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"

css_addition = """
/* Project Journey Section */
.project-journey-section {
  padding: 80px 24px;
  background: #f8fafc;
  border-top: 1px solid var(--line);
}
.project-showcase {
  min-height: calc(100vh - 88px);
  display: flex;
  flex-direction: column;
}
.journey-shell {
  width: min(1000px, calc(100% - 40px));
  margin-inline: auto;
}
.journey-header {
  text-align: center;
  margin-bottom: 40px;
}
.journey-header .eyebrow {
  margin-bottom: 12px;
}
.journey-header h2 {
  font-size: 32px;
  color: var(--navy);
  margin: 0;
}
.journey-desc {
  color: var(--muted);
  line-height: 1.6;
  text-align: center;
  max-width: 600px;
  margin: 0 auto 40px;
}
.codebase-section h3 {
  color: var(--navy);
  font-size: 20px;
  margin-bottom: 24px;
  border-bottom: 2px solid var(--line);
  padding-bottom: 8px;
}
.code-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 24px;
}
.code-block-wrapper {
  background: #1e1e1e;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  display: flex;
  flex-direction: column;
}
.code-block-wrapper.full-width {
  grid-column: 1 / -1;
}
.code-header {
  background: #2d2d2d;
  color: #a0a0a0;
  padding: 8px 16px;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.code-block-wrapper pre {
  margin: 0;
  padding: 20px;
  overflow-x: auto;
  color: #d4d4d4;
  font-family: Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace;
  font-size: 14px;
  line-height: 1.5;
  max-height: 500px;
  overflow-y: auto;
}
.code-block-wrapper pre::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.code-block-wrapper pre::-webkit-scrollbar-thumb {
  background: #555;
  border-radius: 4px;
}
.code-block-wrapper pre::-webkit-scrollbar-track {
  background: #1e1e1e;
}
@media (max-width: 768px) {
  .code-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open(os.path.join(base_dir, 'style.css'), 'a') as f:
    f.write(css_addition)

footer_html = """
  <footer class="site-footer" id="contact">
    <div class="section-shell footer-grid">
      <div class="footer-brand">
        <a class="brand" href="../../index.html#home">
          <span class="brand-words"><strong>CODING</strong> <b>STEM</b></span>
          <span class="brand-code">{ }</span>
          <span class="brand-line"></span>
        </a>
        <p>A practical coding programme helping young creators build, deploy and share real web projects.</p>
      </div>
      <div class="footer-column"><h3>Explore</h3><a href="../../index.html#home">Home</a><a href="../../index.html#about">About</a><a href="../../projects.html">Projects</a><a href="../../index.html#curriculum">Curriculum</a></div>
      <div class="footer-column"><h3>Programme</h3><a href="../../index.html#curriculum">Week 1</a><a href="../../index.html#curriculum">Week 2</a><a href="../../index.html#curriculum">Week 3</a><a href="../../index.html#curriculum">Week 4</a></div>
      <div class="footer-column"><h3>Contact</h3><span>Wilkinson Road, Freetown</span><a href="tel:+23275209846">+232 75 209 846</a><a href="mailto:info@easystemsl.com">info@easystemsl.com</a><span>@easystemsl</span></div>
    </div>
    <div class="section-shell footer-bottom"><span>Built by learners. Powered by curiosity.</span><span>© 2026 EasySTEM &amp; SkoolGrind</span></div>
  </footer>
"""

projects = [
    ('Day One/profile-card-lesson-project', 'day-one'),
    ('Day Two/kairo-project', 'day-two'),
    ('Day Three/day3-meme-soundboard', 'day-three'),
    ('Day Four/mystery-loot-box', 'day-four'),
    ('Day Five/loot-box-inventory', 'day-five')
]

for folder, name in projects:
    html_file = os.path.join(base_dir, folder, name + '.html')
    css_file = os.path.join(base_dir, folder, name + '.css')
    js_file = os.path.join(base_dir, folder, name + '.js')

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    if "project-journey-section" in html_content:
        continue
        
    with open(css_file, 'r', encoding='utf-8') as f:
        css_code = f.read()
        
    js_code = ""
    if os.path.exists(js_file):
        with open(js_file, 'r', encoding='utf-8') as f:
            js_code = f.read()
            
    esc_html = html.escape(html_content)
    esc_css = html.escape(css_code)
    esc_js = html.escape(js_code) if js_code else ""
    
    journey_section = f"""
  <section class="project-journey-section">
    <div class="journey-shell">
      <div class="journey-header">
        <span class="eyebrow">PROJECT JOURNEY</span>
        <h2>Explore the Codebase</h2>
        <p class="journey-desc">See the actual HTML, CSS, and JavaScript that powers this project.</p>
      </div>
      
      <div class="codebase-section">
        <div class="code-grid">
          <div class="code-block-wrapper">
            <div class="code-header"><span>HTML</span><span>{name}.html</span></div>
            <pre><code>{esc_html}</code></pre>
          </div>
          <div class="code-block-wrapper">
            <div class="code-header"><span>CSS</span><span>{name}.css</span></div>
            <pre><code>{esc_css}</code></pre>
          </div>
"""
    if esc_js:
        journey_section += f"""
          <div class="code-block-wrapper full-width">
            <div class="code-header"><span>JS</span><span>{name}.js</span></div>
            <pre><code>{esc_js}</code></pre>
          </div>
"""
    journey_section += """
        </div>
      </div>
    </div>
  </section>
"""

    html_content = html_content.replace("<main ", '<div class="project-showcase">\n  <main ')
    html_content = html_content.replace("</main>", '</main>\n  </div>')
    
    html_content = html_content.replace('<a class="active" href="#home"></a>', '<a class="active" href="#home">Home</a>')
    html_content = html_content.replace('<a href="#about"></a>', '<a href="#about">About</a>')
    html_content = html_content.replace('<a href="projects.html"></a>', '<a href="projects.html">Projects</a>')
    html_content = html_content.replace('<a href="#curriculum"></a>', '<a href="#curriculum">Curriculum</a>')
    html_content = html_content.replace('<a href="#partners"></a>', '<a href="#partners">Partners</a>')
    html_content = html_content.replace('<a href="#contact"></a>', '<a href="#contact">Contact</a>')
    
    html_content = html_content.replace("</body>", journey_section + footer_html + "\n</body>")
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
print("All projects updated!")
