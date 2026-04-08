import type { APIRoute } from 'astro';
import { requireAdmin } from '../../../../lib/auth';

import { createClient } from '@supabase/supabase-js';

export const prerender = false;

export const PUT: APIRoute = async (context) => {
  const auth = await requireAdmin(context.request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), { status: auth.status || 401 });
  }

  try {
    const { id } = context.params;
    const { name, description, category, features, demo_url, is_active } =
      await context.request.json();

    const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
    const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;
    const adminClient = createClient(supabaseUrl, serviceRoleKey || '');

    const { data, error } = await adminClient
      .from('demos')
      .update({
        name,
        description,
        category,
        features,
        demo_url,
        is_active,
      })
      .eq('id', id)
      .select();

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), { status: 400 });
    }

    return new Response(JSON.stringify(data[0]), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};

export const DELETE: APIRoute = async (context) => {
  const auth = await requireAdmin(context.request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), { status: auth.status || 401 });
  }

  try {
    const { id } = context.params;

    const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
    const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;
    const adminClient = createClient(supabaseUrl, serviceRoleKey || '');

    const { error } = await adminClient.from('demos').delete().eq('id', id);

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
