import type { APIRoute } from 'astro';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;

export const prerender = false;

export const GET: APIRoute = async ({ request }) => {
  const token = request.headers.get('authorization')?.replace('Bearer ', '');

  if (!token) {
    return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
  }

  // Kullanıcının token'ıyla client oluştur (RLS doğru çalışsın)
  const supabase = createClient(supabaseUrl || '', supabaseAnonKey || '', {
    global: { headers: { Authorization: `Bearer ${token}` } },
  });

  try {
    const { data: { user }, error } = await supabase.auth.getUser(token);
    if (error || !user) {
      return new Response(JSON.stringify({ error: 'Unauthorized' }), { status: 401 });
    }

    // Bu kullanıcıya atanmış aktif demoları getir
    const { data, error: assignError } = await supabase
      .from('demo_assignments')
      .select('demos!inner(id, name, description, category, features, demo_url, is_active, created_at)')
      .eq('user_id', user.id)
      .eq('demos.is_active', true);

    if (assignError) {
      return new Response(JSON.stringify({ error: assignError.message }), { status: 400 });
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
