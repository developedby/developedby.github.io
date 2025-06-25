This repository uses a custom Python script (`build.py`) to generate a static website from modular HTML content and templates. The site is output to the `docs/` directory.

## What does `build.py` do?

- **Combines HTML templates and content:**
  - Reads a main HTML template (`docs/src/page_template.html`).
  - Inserts content from modular *_body.html files into the template.
- **Generates main site pages:**
  - Processes `content/index_body.html`, `content/blog_body.html`, and `content/projects_body.html` to create `docs/index.html`, `docs/blog.html`, and `docs/projects.html`.
- **Generates blog post pages:**
  - Reads all HTML files in `content/blogs/` and wraps them in the main template, outputting to `docs/blogs/`.
- **Builds a static blog list:**
  - Extracts blog post titles and dates from each blog HTML file.
  - Inserts a static list of blog posts into the blog page, replacing a placeholder JavaScript block.
- **Cleans up old files:**
  - Removes any previously generated HTML files in `docs/` and `docs/blogs/` that are no longer present in the source content.
- **Adjusts asset paths:**
  - Ensures all links and asset references (CSS, JS, etc.) are correct for both main pages and blog pages.

## How are the *_body.html files processed?

- Each main page (index, blog, projects) has a corresponding *_body.html file in the `content/` directory.
- The script reads the body file, then injects its content into the main template immediately after the closing `</nav>` tag.
- For the blog page, the script replaces a specific JavaScript block with a static, server-generated list of blog posts.
- The final HTML is written to the appropriate file in the `docs/` directory.

## CSS Classes

- **All HTML elements in the templates and content files already have CSS classes assigned.**
- The CSS files are located in `docs/src/` (e.g., `index.css`, `nav.css`, `reset.css`).
- You can customize the appearance of the site by editing these CSS files. There is no need to add new classes to the HTML; just update the styles as needed.

## Usage

1. **Install Python 3** (if not already installed).
2. Run the build script:
   ```sh
   python build.py
   ```
3. The generated site will be in the `docs/` directory.

## Directory Structure

```
content/
  index_body.html
  blog_body.html
  projects_body.html
  blogs/
    post1.html
    post2.html
    ...
docs/
  index.html
  blog.html
  projects.html
  blogs/
    post1.html
    post2.html
    ...
  src/
    index.css
    nav.css
    ...
```

## Customization

- To add a new blog post, create a new HTML file in `content/blogs/`.
- To change the layout, edit `docs/src/page_template.html`.
- To update styles, edit the CSS files in `docs/src/`. 
