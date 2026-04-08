import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);

export function createAdminClient() {
  const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;
  if (!serviceRoleKey) {
    throw new Error('SUPABASE_SERVICE_ROLE_KEY env var is not set');
  }
  return createClient(supabaseUrl, serviceRoleKey);
}

export async function signUp(email: string, password: string, name: string) {
  const { data, error } = await supabase.auth.signUp({
    email,
    password,
  });

  if (error) {
    return { error: error.message };
  }

  // Store name in users table
  const { error: insertError } = await supabase
    .from('users')
    .insert([{ id: data.user?.id, email, name, role: 'customer' }]);

  if (insertError) {
    return { error: insertError.message };
  }

  return { data, token: data.session?.access_token };
}

export async function signIn(email: string, password: string) {
  const { data, error } = await supabase.auth.signInWithPassword({
    email,
    password,
  });

  if (error) {
    return { error: error.message };
  }

  return { data, token: data.session?.access_token };
}

export async function signOut() {
  const { error } = await supabase.auth.signOut();
  return { error };
}

export async function addFeedback(
  demoId: string,
  userId: string,
  title: string,
  message: string,
  rating: number
) {
  const { data, error } = await supabase.from('feedback').insert([
    {
      demo_id: demoId,
      user_id: userId,
      title,
      message,
      rating,
    },
  ]);

  if (error) {
    return { error: error.message };
  }

  return { data };
}

export async function getFeedback(demoId: string) {
  const { data, error } = await supabase
    .from('feedback')
    .select('*')
    .eq('demo_id', demoId)
    .order('created_at', { ascending: false });

  if (error) {
    return { error: error.message };
  }

  return { data };
}
