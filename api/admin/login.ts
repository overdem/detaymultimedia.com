import type { VercelRequest, VercelResponse } from '@vercel/node';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.PUBLIC_SUPABASE_ANON_KEY;
const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;

const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '');
const adminClient = createClient(supabaseUrl || '', serviceRoleKey || '');

export default async (req: VercelRequest, res: VercelResponse) => {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, password } = req.body;

  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }

  try {
    // Sign in with Supabase Auth
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (error || !data.user) {
      return res.status(401).json({ error: error?.message || 'Invalid credentials' });
    }

    // Check if user is admin
    const { data: profile } = await adminClient
      .from('users')
      .select('role')
      .eq('id', data.user.id)
      .single();

    if (profile?.role !== 'admin') {
      return res.status(403).json({ error: 'Not an admin' });
    }

    const token = data.session?.access_token;

    // Set httpOnly cookie
    res.setHeader(
      'Set-Cookie',
      `admin_token=${token}; HttpOnly; Secure; SameSite=Strict; Path=/admin; Max-Age=86400`
    );

    return res.status(200).json({
      success: true,
      user: { id: data.user.id, email: data.user.email }
    });
  } catch (err) {
    return res.status(500).json({ error: (err as Error).message });
  }
};
