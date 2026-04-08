import type { APIRoute } from 'astro';
import { requireAdmin } from '../../../lib/auth';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;
const adminClient = createClient(supabaseUrl, serviceRoleKey || '');

export const prerender = false;

export const GET: APIRoute = async (context) => {
  const auth = await requireAdmin(context.request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), { status: auth.status || 401 });
  }

  try {
    const { data, error } = await adminClient
      .from('users')
      .select('id, email, name, role, created_at')
      .eq('role', 'customer')
      .order('created_at', { ascending: false });

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400 });
    }

    return new Response(JSON.stringify(data), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};
