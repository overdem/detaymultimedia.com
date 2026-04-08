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

export const POST: APIRoute = async ({ request }) => {
  const auth = await requireAdmin(request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), {
      status: auth.error === 'Forbidden' ? 403 : 401,
    });
  }

  try {
    const { name, email, password } = await request.json();

    if (!name || !email || !password) {
      return new Response(JSON.stringify({ error: 'Ad, email ve şifre zorunlu' }), { status: 400 });
    }

    // Supabase admin API ile kullanıcı oluştur
    const { data: authData, error: authError } = await adminClient.auth.admin.createUser({
      email,
      password,
      email_confirm: true,
    });

    if (authError) {
      return new Response(JSON.stringify({ error: authError.message }), { status: 400 });
    }

    // users tablosuna profil ekle
    const { error: profileError } = await adminClient.from('users').insert([{
      id: authData.user.id,
      email,
      name,
      role: 'customer',
    }]);

    if (profileError) {
      // Auth user oluşturuldu ama profil eklenemedi, geri al
      await adminClient.auth.admin.deleteUser(authData.user.id);
      return new Response(JSON.stringify({ error: profileError.message }), { status: 400 });
    }

    return new Response(JSON.stringify({
      id: authData.user.id,
      email,
      name,
      role: 'customer',
    }), { status: 201, headers: { 'Content-Type': 'application/json' } });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), { status: 500 });
  }
};

export const GET: APIRoute = async ({ request }) => {
  const auth = await requireAdmin(request);
  if (auth.error) {
    return new Response(JSON.stringify({ error: auth.error }), {
      status: auth.error === 'Forbidden' ? 403 : 401,
    });
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
