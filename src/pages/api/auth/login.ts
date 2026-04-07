import type { APIRoute } from 'astro';

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, password } = await request.json();

    if (!email || !password) {
      return new Response(JSON.stringify({ error: 'Email and password required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Demo mode: accept any email/password combination
    // In production: check against Supabase users table

    const token = btoa(`${email}:${password}:${Date.now()}`);

    return new Response(
      JSON.stringify({
        token,
        user: {
          id: email,
          email,
          name: email.split('@')[0],
        },
      }),
      {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      }
    );
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
