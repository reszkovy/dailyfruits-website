// Simple password authentication for CMS
// Set CMS_PASSWORD in Vercel environment variables

export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const { password } = req.body || {};
  const correct = process.env.CMS_PASSWORD;

  if (!correct) return res.status(500).json({ error: 'CMS_PASSWORD not configured' });
  if (password === correct) {
    return res.status(200).json({ ok: true, token: Buffer.from(`cms:${correct}`).toString('base64') });
  }
  return res.status(401).json({ error: 'Invalid password' });
}
