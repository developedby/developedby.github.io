import os
import re

TEMPLATE_PATH = os.path.join('docs', 'src', 'page_template.html')
BODY_FILES = {
    'blog': os.path.join('content', 'blog_body.html'),
    'index': os.path.join('content', 'index_body.html'),
    'projects': os.path.join('content', 'projects_body.html'),
}
OUTPUT_DIR = 'docs'
BLOGS_SRC_DIR = os.path.join('content', 'blogs')  # Where to read blog sources
BLOGS_OUT_DIR = os.path.join('docs', 'blogs')  # Where to write generated blog pages

# Ensure output blog directory exists
os.makedirs(BLOGS_OUT_DIR, exist_ok=True)

# Read the template
with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
    template = f.read()

def clean_output(generated_main, generated_blogs):
    # Remove .html files in OUTPUT_DIR not in generated_main
    for fname in os.listdir(OUTPUT_DIR):
        if fname.endswith('.html') and fname not in generated_main:
            os.remove(os.path.join(OUTPUT_DIR, fname))
    # Remove .html files in BLOGS_OUT_DIR not in generated_blogs
    for fname in os.listdir(BLOGS_OUT_DIR):
        if fname.endswith('.html') and fname not in generated_blogs:
            os.remove(os.path.join(BLOGS_OUT_DIR, fname))

def adjust_paths(html, is_blog=False):
    # For main pages, all links/assets should be relative to docs/
    # For blog pages, they should be relative to docs/blogs/
    if is_blog:
        # Blog pages: asset paths should be ../src/...
        html = re.sub(r'href="(\.\./)*src/', 'href="../src/', html)
        html = re.sub(r'src="(\.\./)*src/', 'src="../src/', html)
        html = re.sub(r'href="(index|blog|projects)\.html"', r'href="../\1.html"', html)
        html = re.sub(r'href="blogs/', 'href="', html)  # blog links in blog posts are not expected
    else:
        # Main pages: asset paths should be src/...
        html = re.sub(r'href="(\.\./)*src/', 'href="src/', html)
        html = re.sub(r'src="(\.\./)*src/', 'src="src/', html)
        html = re.sub(r'href="(index|blog|projects)\.html"', r'href="\1.html"', html)
        html = re.sub(r'href="blogs/', 'href="blogs/', html)
    return html

# Find the position right after the closing </nav> tag
nav_close_match = re.search(r'</nav\s*>', template, re.IGNORECASE)
if not nav_close_match:
    raise Exception('No closing </nav> tag found in template!')
nav_end = nav_close_match.end()

def write_wrapped_html(body_content, output_path, template_str=None, is_blog=False):
    tpl = template_str if template_str is not None else template
    # Split at the first closing </nav> to ensure correct placement
    parts = tpl.split('</nav>', 1)
    if len(parts) != 2:
        raise Exception('No closing </nav> tag found in template!')
    new_html = parts[0] + '</nav>\n' + body_content + '\n' + parts[1]
    new_html = adjust_paths(new_html, is_blog=is_blog)
    with open(output_path, 'w', encoding='utf-8') as out:
        out.write(new_html)
    print(f'Generated {output_path}')

def extract_blog_info(blog_path):
    with open(blog_path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Extract date
    date_match = re.search(r'<div class="post-date">(.*?)</div>', html)
    date = date_match.group(1).strip() if date_match else ''
    # Extract title
    title_match = re.search(r'<h2[^>]*>(.*?)</h2>', html)
    title = title_match.group(1).strip() if title_match else os.path.splitext(os.path.basename(blog_path))[0]
    # Filename
    filename = os.path.basename(blog_path)
    return {'filename': filename, 'name': title, 'date': date}

def generate_blog_list():
    blogs = []
    for fname in os.listdir(BLOGS_SRC_DIR):
        if fname.endswith('.html'):
            blog_path = os.path.join(BLOGS_SRC_DIR, fname)
            info = extract_blog_info(blog_path)
            blogs.append(info)
    # Sort by date descending if possible
    try:
        from datetime import datetime
        blogs.sort(key=lambda x: datetime.strptime(x['date'], '%B %d, %Y'), reverse=True)
    except Exception:
        pass
    # Generate HTML
    items = [f'<li><a href="blogs/{b["filename"]}">{b["name"]}</a> <span class="date">{b["date"]}</span></li>' for b in blogs]
    return '\n'.join(items)

def main_pages():
    generated = []
    for page, body_path in BODY_FILES.items():
        with open(body_path, 'r', encoding='utf-8') as f:
            body_content = f.read()
        if page == 'blog':
            # Replace JS block with static blog list
            body_content = re.sub(
                r'<script>[\s\S]*?</script>\s*<h2 id="introduction">Blog Posts:</h2>\s*<div id="blog-list-container">\s*<ul id="blog-list"></ul>\s*</div>',
                f'<h2 id="introduction">Blog Posts:</h2>\n<div id="blog-list-container">\n  <ul id="blog-list">\n{generate_blog_list()}\n  </ul>\n</div>',
                body_content,
                flags=re.MULTILINE
            )
        output_path = os.path.join(OUTPUT_DIR, f'{page}.html')
        write_wrapped_html(body_content, output_path, is_blog=False)
        generated.append(f'{page}.html')
    return generated

def blog_pages():
    # Use the template as-is, asset paths will be fixed by adjust_paths
    blog_template = template
    generated = []
    for fname in os.listdir(BLOGS_SRC_DIR):
        if fname.endswith('.html'):
            blog_path = os.path.join(BLOGS_SRC_DIR, fname)
            with open(blog_path, 'r', encoding='utf-8') as f:
                blog_content = f.read()
            out_path = os.path.join(BLOGS_OUT_DIR, fname)
            write_wrapped_html(blog_content, out_path, template_str=blog_template, is_blog=True)
            generated.append(fname)
    return generated

def main():
    generated_main = main_pages()
    generated_blogs = blog_pages()
    clean_output(generated_main, generated_blogs)

if __name__ == '__main__':
    main()
