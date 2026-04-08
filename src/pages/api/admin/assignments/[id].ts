import type { APIRoute } from 'astro';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;
const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;

const adminClient = createClient(supabaseUrl || '', serviceRoleKey || '');

export const prerender = false;

async function requireAdmin(request: Request): Promise<{ userId?: string; error?: string }> {
  const cookie = request.headers.get('cookie');
  const token = cookie
    ?.split(';')
    .find(c => c.trim().startsWith('admin_token='))
    ?.split('=')[1];

  if (!token) {
    return { error: 'Unauthorized' };
  }

  const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '');
  const { data: { user }, error } = await supabase.auth.getUser(token);
  if (error || !user) {
    return { error: 'Unauthorized' };
  }

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

export const DELETE: APIRoute = async ({ request, params }) => {
  const auth = await requireAdmin(request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), {
      status: auth.error === 'Forbidden' ? 403 : 401,
    });
  }

  try {
    const { id } = params;

    const { error } = await adminClient.from('demo_assignments').delete().eq('id', id);

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400 });
    }

    return new Response(JSON.stringify({ success: true }), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};
