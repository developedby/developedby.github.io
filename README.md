# Static Site Generator for developedby.github.io

This project uses a custom Python script (`build.py`) to generate a static website from modular HTML content and templates. The site is output to the `docs/` directory.

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

---

## CSS Classes and IDs: How to Use the Site's Aesthetic

Below is a complete list of the main CSS classes and IDs used in this project, with explanations of their function and how to use them to create content with the same look and feel.

### Main Navigation
- `.main-nav`  
  Main navigation bar, horizontal, with spacing and border.
- `.nav-left`  
  Left side of the navigation (usually the logo or site name).
- `.nav-right`  
  Right side of the navigation (links, buttons, icons).

### Content and Layout
- `.info-rectangle`  
  Highlighted block for information, projects, or notices. Has border, padding, and background.
- `.project-separator`  
  Horizontal line to separate projects or sections.
- `.grid`  
  Flexible grid layout, automatically adjusts the number of columns.

### Blog
- `.blog-post`  
  Blog post container. Has border, padding, and background.
- `.post-date`  
  Post date, usually at the top of the post, with a different color.
- `.signature`  
  Author signature, right-aligned and italic.

### Footer
- `.site-footer`  
  Site footer, centered.
- `.footer-content`  
  Inner container for the footer, uses flexbox for alignment.
- `.footer-signature`  
  Signature in the footer, usually with an icon.
- `.footer-github-quote`  
  Phrase or link to GitHub in the footer.

### Blog List
- `#blog-list-container`  
  Container for the blog post list, with border and padding.
- `#blog-list`  
  Blog post list (ul), no default markers.
- `#blog-list li`  
  Blog post list item, with spacing and bottom border.
- `#blog-list .date`  
  Post date in the list, lighter color and smaller size.

### Utilities
- `.width-min`  
  Sets minimum width for an element.
- `.width-auto`  
  Sets automatic (100%) width for an element.

### Main IDs
- `#theme-toggle`  
  Button to toggle between light/dark theme.
- `#theme-icon`  
  Icon inside the theme toggle button.
- `#crow-tooltip`  
  Custom tooltip, appears when interacting with the crow icon.
- `#introduction`  
  Section title for introduction.
- `#articles`  
  Section title for projects.
- `#blog-post-title`  
  Blog post title.
- `#blog-list-container`  
  (already listed above)
- `#blog-list`  
  (already listed above)

---

## How to Use These Classes and IDs

- **Use the existing classes and IDs:** Structure your HTML using these classes (`main-nav`, `info-rectangle`, `blog-post`, etc.) to ensure the CSS is applied correctly.
- **No need to create new classes:** The system already covers navigation, lists, posts, footer, tooltips, grids, etc. Just use the classes/IDs as shown in the examples below.
- **Leverage CSS variables:** If you want to change colors or spacing, edit the variables at the top of `index.css`.
- **For new posts or sections:**
  - Use `<div class="blog-post">...</div>` for posts.
  - Use `<div class="info-rectangle">...</div>` for highlighted blocks.
  - For lists, use `<ul id="blog-list">...</ul>` and follow the item pattern.
- **For interactivity (dark/light theme):**
  Include the button `<button id="theme-toggle">` and the icon `<i id="theme-icon">` to toggle themes.
- **For section titles:**
  Use `<h2 id="introduction">`, `<h2 id="articles">`, or `<h2 id="blog-post-title">` as appropriate.

### Example HTML Structure

```html
<nav class="main-nav">
  <div class="nav-left">Logo</div>
  <div class="nav-right">
    <a href="#">Link</a>
    <button id="theme-toggle"><i id="theme-icon" class="fas fa-moon"></i></button>
  </div>
</nav>

<div class="info-rectangle">
  <h3>Title</h3>
  <p>Highlighted content.</p>
</div>

<div class="blog-post">
  <div class="post-date">May 1, 2024</div>
  <h2 id="blog-post-title">Post Title</h2>
  <p>Post text...</p>
  <span class="signature">– author</span>
</div>

<div id="blog-list-container">
  <ul id="blog-list">
    <li>
      <a href="blogs/example.html">Post Title</a>
      <span class="date">May 1, 2024</span>
    </li>
    <!-- more posts -->
  </ul>
</div>

<footer class="site-footer">
  <div class="footer-content">
    <span class="footer-signature"><i class="fas fa-feather-alt"></i> Crafted by ...</span>
    <span class="footer-github-quote">View Source <i class="fab fa-github"></i></span>
  </div>
</footer>

<span id="crow-tooltip">Tooltip text</span>
```

---

## Summary Table of Classes/IDs and Their Functions

| Class/ID                | Function/Description                                 |
|-------------------------|-----------------------------------------------------|
| `.main-nav`             | Main navigation bar                                 |
| `.nav-left`             | Left side of navigation                             |
| `.nav-right`            | Right side of navigation                            |
| `.info-rectangle`       | Highlighted information block                       |
| `.project-separator`    | Section/project separator line                      |
| `.grid`                 | Flexible grid layout                                |
| `.blog-post`            | Blog post container                                |
| `.post-date`            | Blog post date                                      |
| `.signature`            | Author signature                                    |
| `.site-footer`          | Site footer                                         |
| `.footer-content`       | Footer container                                    |
| `.footer-signature`     | Footer signature                                    |
| `.footer-github-quote`  | GitHub phrase/link in footer                        |
| `#theme-toggle`         | Theme toggle button                                 |
| `#theme-icon`           | Icon inside theme toggle                            |
| `#crow-tooltip`         | Custom tooltip                                      |
| `#introduction`         | Introduction section title                          |
| `#articles`             | Projects section title                              |
| `#blog-post-title`      | Blog post title                                     |
| `#blog-list-container`  | Blog post list container                            |
| `#blog-list`            | Blog post list                                      |
| `.width-min`            | Utility: minimum width                              |
| `.width-auto`           | Utility: automatic (100%) width                    |

---

## Customization

- To add a new blog post, create a new HTML file in `content/blogs/`.
- To change the layout, edit `docs/src/page_template.html`.
- To update styles, edit the CSS files in `docs/src/`.

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