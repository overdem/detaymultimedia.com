import type { APIRoute } from 'astro';
import jwt from 'jsonwebtoken';

const JWT_SECRET = import.meta.env.JWT_SECRET || 'demo-secret-key-change-in-production';

// Demo in-memory users (in production, use Supabase!)
const demoUsers = [
  { id: '1', email: 'demo@detay.com', password: 'demo123', name: 'Demo User' },
  { id: '2', email: 'test@detay.com', password: 'test123', name: 'Test User' },
];

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, password } = await request.json();

    if (!email || !password) {
      return new Response(JSON.stringify({ error: 'Email and password required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Check credentials against demo users
    const user = demoUsers.find((u) => u.email === email && u.password === password);

    if (!user) {
      return new Response(JSON.stringify({ error: 'Invalid credentials' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const token = jwt.sign({ id: user.id, email: user.email }, JWT_SECRET, {
      expiresIn: '7d',
    });

    return new Response(
      JSON.stringify({
        token,
        user: { id: user.id, email: user.email, name: user.name },
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
