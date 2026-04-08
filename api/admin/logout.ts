import type { VercelRequest, VercelResponse } from '@vercel/node';

export default (req: VercelRequest, res: VercelResponse) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  res.setHeader(
    'Set-Cookie',
    'admin_token=; HttpOnly; Secure; SameSite=Strict; Path=/admin; Max-Age=0'
  );

  return res.status(200).json({ success: true });
};
