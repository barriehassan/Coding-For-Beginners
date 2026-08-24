import os
import re

base_dir = r"c:\Users\hassa\Desktop\Coding for Beginners"
style_file = os.path.join(base_dir, 'style.css')

with open(style_file, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Find where "/* Project Journey Section */" starts (if it exists)
split_str1 = "/* Project Journey Section */"
split_str2 = "/* Project Journey Section Fixes */"

if split_str1 in css_content:
    css_content = css_content.split(split_str1)[0]
elif split_str2 in css_content:
    css_content = css_content.split(split_str2)[0]

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
.code-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 28px;
}
.code-block-wrapper {
  background: #0d1117;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 12px 35px rgba(0, 0, 0, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  flex-direction: column;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.code-block-wrapper:hover {
  transform: translateY(-4px);
  box-shadow: 0 16px 45px rgba(0, 0, 0, 0.2);
}
.code-header {
  background: #161b22;
  color: #8b949e;
  padding: 12px 16px;
  font-size: 13px;
  font-weight: 600;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}
.code-header .header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}
.code-header .dots {
  display: flex;
  gap: 6px;
  align-items: center;
}
.code-header .dots span {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #ff5f56;
}
.code-header .dots span:nth-child(2) { background: #ffbd2e; }
.code-header .dots span:nth-child(3) { background: #27c93f; }

.code-header .lang-label {
  font-family: monospace;
  letter-spacing: 0.5px;
  color: #c9d1d9;
}

.code-block-wrapper pre {
  margin: 0;
  padding: 24px;
  overflow-x: auto;
  color: #c9d1d9;
  font-family: 'JetBrains Mono', Consolas, Monaco, 'Ubuntu Mono', monospace;
  font-size: 14px;
  line-height: 1.6;
  max-height: 400px;
  overflow-y: auto;
  background: transparent;
}
.code-block-wrapper pre::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}
.code-block-wrapper pre::-webkit-scrollbar-thumb {
  background: #30363d;
  border-radius: 4px;
}
.code-block-wrapper pre::-webkit-scrollbar-track {
  background: #0d1117;
}
.copy-btn {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 6px;
  border-radius: 6px;
  color: #fff;
  transition: all 0.2s;
}
.copy-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: scale(1.05);
}
.copy-icon {
  width: 16px;
  height: 16px;
  fill: currentColor;
}
.js-block-wrapper {
  grid-column: 1 / -1;
  width: 100%;
}
@media (max-width: 900px) {
  .code-grid {
    grid-template-columns: 1fr;
  }
}
"""

with open(style_file, 'w', encoding='utf-8') as f:
    f.write(css_content.strip() + "\n\n" + new_css.strip() + "\n")

# Inject JS into HTML files and update the code-header to include the Mac dots
js_snippet = """
  <script>
    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const pre = btn.closest('.code-block-wrapper').querySelector('pre');
        navigator.clipboard.writeText(pre.innerText).then(() => {
          const originalIcon = btn.innerHTML;
          btn.innerHTML = '<svg class="copy-icon" viewBox="0 0 24 24"><path fill="#4ade80" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg>';
          setTimeout(() => { btn.innerHTML = originalIcon; }, 2000);
        });
      });
    });
  </script>
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
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
        
    # Replace the old headers with the new one containing the mac dots
    def replacer(match):
        lang = match.group(1)
        return f'''<div class="code-header">
              <div class="header-left">
                <div class="dots"><span></span><span></span><span></span></div>
                <span class="lang-label">{lang}</span>
              </div>'''
              
    html_content = re.sub(r'<div class="code-header">\s*<span>(.*?)</span>', replacer, html_content)
    
    # Add JS script before </body>
    if "navigator.clipboard.writeText" not in html_content:
        html_content = html_content.replace("</body>", js_snippet + "\n</body>")
        
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

print("Beautiful design applied and copy functionality fixed!")
