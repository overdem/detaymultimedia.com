import type { APIRoute } from 'astro';

// DEMO MODE: Uses localStorage on client-side, no server storage
// In production: use Supabase or another backend database

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, password, name } = await request.json();

    if (!email || !password || !name) {
      return new Response(JSON.stringify({ error: 'Missing fields' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Generate a simple token (not cryptographically secure - demo only)
    const token = btoa(`${email}:${password}:${Date.now()}`);

    const user = {
      id: Date.now().toString(),
      email,
      name,
    };

    return new Response(
      JSON.stringify({
        token,
        user,
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
