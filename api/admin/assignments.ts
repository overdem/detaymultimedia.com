import type { VercelRequest, VercelResponse } from '@vercel/node';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.PUBLIC_SUPABASE_URL;
const serviceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
const adminClient = createClient(supabaseUrl || '', serviceRoleKey || '');

async function requireAdmin(req: VercelRequest): Promise<{ userId?: string; error?: string }> {
  const cookie = req.headers.cookie;
  const token = cookie
    ?.split(';')
    .find(c => c.trim().startsWith('admin_token='))
    ?.split('=')[1];

  if (!token) {
    return { error: 'Unauthorized' };
  }

  const supabaseUrl = process.env.PUBLIC_SUPABASE_URL;
  const supabaseAnonKey = process.env.PUBLIC_SUPABASE_ANON_KEY;
  const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '');

  const { data: { user }, error } = await supabase.auth.getUser(token);
  if (error || !user) {
    return { error: 'Unauthorized' };
  }

  // Check admin role
  const { data: profile } = await adminClient
    .from('users')
    .select('role')
    .eq('id', user.id)
    .single();

  if (profile?.role !== 'admin') {
    return { error: 'Forbidden' };
  }

  return { userId: user.id };
}

export default async (req: VercelRequest, res: VercelResponse) => {
  const auth = await requireAdmin(req);
  if (auth.error) {
    return res.status(auth.error === 'Forbidden' ? 403 : 401).json({ error: auth.error });
  }

  try {
    if (req.method === 'GET') {
      const { data, error } = await adminClient
        .from('demo_assignments')
        .select('*, demos(id, name), users(id, email, name)')
        .order('assigned_at', { ascending: false });

      if (error) {
        return res.status(400).json({ error: error.message });
      }

      return res.status(200).json(data);
    }

    if (req.method === 'POST') {
      const { demo_id, user_id } = req.body;

      if (!demo_id || !user_id) {
        return res.status(400).json({ error: 'demo_id and user_id are required' });
      }

      const { data, error } = await adminClient
        .from('demo_assignments')
        .insert([{ demo_id, user_id }])
        .select();

      if (error) {
        return res.status(400).json({ error: error.message });
      }

      return res.status(201).json(data[0]);
    }

    return res.status(405).json({ error: 'Method not allowed' });
  } catch (err) {
    return res.status(500).json({ error: (err as Error).message });
  }
};
