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
      .from('demo_assignments')
      .select('*, demos(id, name), users(id, email, name)')
      .order('assigned_at', { ascending: false });

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

export const POST: APIRoute = async (context) => {
  const auth = await requireAdmin(context.request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), { status: auth.status || 401 });
  }

  try {
    const { demo_id, user_id } = await context.request.json();

    if (!demo_id || !user_id) {
      return new Response(JSON.stringify({ error: 'demo_id and user_id are required' }), {
        status: 400,
      });
    }

    const { data, error } = await adminClient
      .from('demo_assignments')
      .insert([{ demo_id, user_id }])
      .select();

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400 });
    }

    return new Response(JSON.stringify(data[0]), {
      status: 201,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};
