import type { APIRoute } from 'astro';

export const prerender = false;

export const POST: APIRoute = async ({ request }) => {
  if (request.method !== 'POST') {
    return new Response(JSON.stringify({ error: 'Method not allowed' }), { status: 405 });
  }

  return new Response(JSON.stringify({ success: true }), {
    status: 200,
    headers: {
      'Set-Cookie': 'admin_token=; HttpOnly; Secure; SameSite=Strict; Path=/admin; Max-Age=0',
      'Content-Type': 'application/json',
    },
  });
};
