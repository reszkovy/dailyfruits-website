// Blog CMS API — CRUD via GitHub API
// Required env vars: GITHUB_TOKEN, GITHUB_REPO (e.g. "reszkovy/dailyfruits-website")
// Optional: CMS_PASSWORD

const GITHUB_API = 'https://api.github.com';

function verifyAuth(req) {
  const auth = req.headers['x-cms-token'];
  if (!auth) return false;
  const decoded = Buffer.from(auth, 'base64').toString();
  return decoded === `cms:${process.env.CMS_PASSWORD}`;
}

async function githubFetch(path, options = {}) {
  const url = `${GITHUB_API}/repos/${process.env.GITHUB_REPO}/contents/${path}`;
  const res = await fetch(url, {
    ...options,
    headers: {
      'Authorization': `Bearer ${process.env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github.v3+json',
      'Content-Type': 'application/json',
      ...(options.headers || {})
    }
  });
  return res;
}

// Parse blog post HTML to extract metadata
function parsePost(html, filename) {
  const title = html.match(/<title>(.*?)<\/title>/)?.[1]?.replace(' – DailyFruits Blog', '') || '';
  const description = html.match(/<meta name="description" content="(.*?)">/)?.[1] || '';
  const date = html.match(/<time datetime="(.*?)">/)?.[1] || '';
  const dateDisplay = html.match(/<time[^>]*>(.*?)<\/time>/)?.[1] || '';
  const category = html.match(/data-category="(.*?)"/)?.[1] || '';
  const h1Match = html.match(/<h1[^>]*>(.*?)<\/h1>/s)?.[1] || title;
  const slug = filename.replace('.html', '').replace('wpis-', '');

  // Extract article body content
  const bodyMatch = html.match(/<div class="article-body">([\s\S]*?)<\/div>\s*<\/article>/);
  const body = bodyMatch ? bodyMatch[1].trim() : '';

  // Extract card info from blog.html pattern
  const excerpt = html.match(/<meta name="description" content="(.*?)">/)?.[1] || '';

  return { slug, filename, title, description, date, dateDisplay, category, h1: h1Match, body, excerpt };
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, X-CMS-Token');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (!verifyAuth(req)) return res.status(401).json({ error: 'Unauthorized' });

  const { method } = req;
  const { action, slug } = req.query;

  try {
    // LIST all blog posts
    if (method === 'GET' && action === 'list') {
      const response = await githubFetch('');
      if (!response.ok) return res.status(500).json({ error: 'GitHub API error' });

      const files = await response.json();
      const blogFiles = files.filter(f => f.name.startsWith('wpis-') && f.name.endsWith('.html'));

      // Get blog.html to extract card data (dates, excerpts)
      const blogIndexRes = await githubFetch('blog.html');
      const blogIndexData = await blogIndexRes.json();
      const blogHtml = Buffer.from(blogIndexData.content, 'base64').toString('utf-8');

      const posts = [];
      for (const file of blogFiles) {
        const fileSlug = file.name.replace('.html', '').replace('wpis-', '');

        // Extract card info from blog.html
        const cardRegex = new RegExp(`<a href="${file.name}"[^>]*class="blog-card[^"]*"[^>]*data-category="([^"]*)">[\\s\\S]*?<span class="blog-card-date">([^<]*)</span>[\\s\\S]*?<h3>([^<]*)</h3>[\\s\\S]*?<p>([^<]*)</p>`, 'i');
        const cardMatch = blogHtml.match(cardRegex);

        posts.push({
          slug: fileSlug,
          filename: file.name,
          title: cardMatch ? cardMatch[3] : file.name,
          category: cardMatch ? cardMatch[1] : '',
          date: cardMatch ? cardMatch[2] : '',
          excerpt: cardMatch ? cardMatch[4] : '',
          sha: file.sha
        });
      }

      return res.status(200).json({ posts });
    }

    // GET single post content
    if (method === 'GET' && action === 'get' && slug) {
      const filename = `wpis-${slug}.html`;
      const response = await githubFetch(filename);
      if (!response.ok) return res.status(404).json({ error: 'Post not found' });

      const data = await response.json();
      const html = Buffer.from(data.content, 'base64').toString('utf-8');
      const post = parsePost(html, filename);
      post.sha = data.sha;
      post.rawHtml = html;

      return res.status(200).json({ post });
    }

    // UPDATE post content
    if (method === 'PUT' && action === 'update' && slug) {
      const { html, sha, commitMessage } = req.body;
      if (!html || !sha) return res.status(400).json({ error: 'html and sha required' });

      const filename = `wpis-${slug}.html`;
      const response = await githubFetch(filename, {
        method: 'PUT',
        body: JSON.stringify({
          message: commitMessage || `CMS: update ${filename}`,
          content: Buffer.from(html).toString('base64'),
          sha: sha
        })
      });

      if (!response.ok) {
        const err = await response.json();
        return res.status(response.status).json({ error: err.message });
      }

      const result = await response.json();
      return res.status(200).json({ ok: true, sha: result.content.sha });
    }

    // UPDATE blog.html (index page — card data)
    if (method === 'PUT' && action === 'update-index') {
      const { html, sha, commitMessage } = req.body;
      if (!html || !sha) return res.status(400).json({ error: 'html and sha required' });

      const response = await githubFetch('blog.html', {
        method: 'PUT',
        body: JSON.stringify({
          message: commitMessage || 'CMS: update blog index',
          content: Buffer.from(html).toString('base64'),
          sha: sha
        })
      });

      if (!response.ok) {
        const err = await response.json();
        return res.status(response.status).json({ error: err.message });
      }

      const result = await response.json();
      return res.status(200).json({ ok: true, sha: result.content.sha });
    }

    // GET blog.html raw
    if (method === 'GET' && action === 'get-index') {
      const response = await githubFetch('blog.html');
      if (!response.ok) return res.status(500).json({ error: 'Cannot fetch blog.html' });
      const data = await response.json();
      const html = Buffer.from(data.content, 'base64').toString('utf-8');
      return res.status(200).json({ html, sha: data.sha });
    }

    return res.status(400).json({ error: 'Invalid action. Use: list, get, update, update-index, get-index' });
  } catch (err) {
    return res.status(500).json({ error: err.message });
  }
}
