import type { VercelRequest, VercelResponse } from '@vercel/node';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = process.env.PUBLIC_SUPABASE_ANON_KEY;
const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '');

function parseCookie(cookieHeader: string | undefined, name: string): string | null {
  if (!cookieHeader) return null;
  const cookies = cookieHeader.split(';');
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) return decodeURIComponent(value);
  }
  return null;
}

export default async (req: VercelRequest, res: VercelResponse) => {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const token = req.headers.authorization?.replace('Bearer ', '');

  if (!token) {
    return res.status(401).json({ error: 'Unauthorized' });
  }

  try {
    const { data: { user }, error } = await supabase.auth.getUser(token);
    if (error || !user) {
      return res.status(401).json({ error: 'Unauthorized' });
    }

    // Get demos assigned to this user
    const { data, error: assignError } = await supabase
      .from('demo_assignments')
      .select('demos(id, name, description, category, features, demo_url, is_active, created_at)')
      .eq('user_id', user.id)
      .eq('demos.is_active', true);

    if (assignError) {
      return res.status(400).json({ error: assignError.message });
    }

    // Extract demos from assignments
    const demos = data?.map((assignment: any) => assignment.demos).filter(Boolean) || [];

    return res.status(200).json(demos);
  } catch (err) {
    return res.status(500).json({ error: (err as Error).message });
  }
};
