import type { APIRoute } from 'astro';
import { requireCustomer } from '../../lib/auth';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;
const supabase = createClient(supabaseUrl, supabaseAnonKey);

export const prerender = false;

export const GET: APIRoute = async (context) => {
  const auth = await requireCustomer(context.request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), { status: auth.status || 401 });
  }

  try {
    // Get demos assigned to this user
    const { data, error } = await supabase
      .from('demo_assignments')
      .select('demos(id, name, description, category, features, demo_url, is_active, created_at)')
      .eq('user_id', auth.userId)
      .eq('demos.is_active', true);

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400 });
    }

    // Extract demos from assignments
    const demos = data?.map((assignment: any) => assignment.demos).filter(Boolean) || [];

    return new Response(JSON.stringify(demos), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};
