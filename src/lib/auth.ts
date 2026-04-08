import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.PUBLIC_SUPABASE_URL;
const supabaseAnonKey = import.meta.env.PUBLIC_SUPABASE_ANON_KEY;
const serviceRoleKey = import.meta.env.SUPABASE_SERVICE_ROLE_KEY;

let supabase: any = null;
let adminClient: any = null;

function getSupabase() {
  if (!supabase) {
    supabase = createClient(supabaseUrl, supabaseAnonKey);
  }
  return supabase;
}

function getAdminClient() {
  if (!adminClient) {
    if (!serviceRoleKey) {
      throw new Error('SUPABASE_SERVICE_ROLE_KEY is not set');
    }
    adminClient = createClient(supabaseUrl, serviceRoleKey);
  }
  return adminClient;
}

export interface AuthResult {
  userId?: string;
  error?: string;
  status?: number;
}

// Parse cookie from header
export function parseCookie(cookieHeader: string | null, name: string): string | null {
  if (!cookieHeader) return null;
  const cookies = cookieHeader.split(';');
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) return decodeURIComponent(value);
  }
  return null;
}

// Verify admin token and check role
export async function requireAdmin(request: Request): Promise<AuthResult> {
  const cookie = request.headers.get('cookie');
  const token = parseCookie(cookie, 'admin_token');

  if (!token) {
    return { error: 'Unauthorized', status: 401 };
  }

  const supabaseClient = getSupabase();
  const { data: { user }, error } = await supabaseClient.auth.getUser(token);
  if (error || !user) {
    return { error: 'Unauthorized', status: 401 };
  }

  // Check admin role
  const adminClientInstance = getAdminClient();
  const { data: profile } = await adminClientInstance
    .from('users')
    .select('role')
    .eq('id', user.id)
    .single();

  if (profile?.role !== 'admin') {
    return { error: 'Forbidden', status: 403 };
  }

  return { userId: user.id };
}

// Verify customer token
export async function requireCustomer(request: Request): Promise<AuthResult> {
  const authHeader = request.headers.get('authorization');
  const token = authHeader?.replace('Bearer ', '');

  if (!token) {
    return { error: 'Unauthorized', status: 401 };
  }

  const supabaseClient = getSupabase();
  const { data: { user }, error } = await supabaseClient.auth.getUser(token);
  if (error || !user) {
    return { error: 'Unauthorized', status: 401 };
  }

  return { userId: user.id };
}
