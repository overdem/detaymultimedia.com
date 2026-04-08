import type { APIRoute } from 'astro';
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;
const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;

const supabase = createClient(supabaseUrl, supabaseAnonKey);
const adminClient = createClient(supabaseUrl, serviceRoleKey || '');

export const prerender = false;

export const POST: APIRoute = async (context) => {
  try {
    const { email, password } = await context.request.json();

    if (!email || !password) {
      return new Response(JSON.stringify({ error: 'Email and password required' }), {
        status: 400,
      });
    }

    // Sign in with Supabase Auth
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (error || !data.user) {
      return new Response(JSON.stringify({ error: error?.message || 'Invalid credentials' }), {
        status: 401,
      });
    }

    // Check if user is admin
    const { data: profile } = await adminClient
      .from('users')
      .select('role')
      .eq('id', data.user.id)
      .single();

    if (profile?.role !== 'admin') {
      return new Response(JSON.stringify({ error: 'Not an admin' }), {
        status: 403,
      });
    }

    const token = data.session?.access_token;

    // Set httpOnly cookie
    const response = new Response(
      JSON.stringify({ success: true, user: { id: data.user.id, email: data.user.email } }),
      {
        status: 200,
        headers: {
          'Content-Type': 'application/json',
          'Set-Cookie': `admin_token=${token}; HttpOnly; Secure; SameSite=Strict; Path=/admin; Max-Age=86400`,
        },
      }
    );

    return response;
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), {
      status: 500,
    });
  }
};
