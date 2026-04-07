import type { APIRoute } from 'astro';
import jwt from 'jsonwebtoken';

const JWT_SECRET = import.meta.env.JWT_SECRET || 'demo-secret-key-change-in-production';

// In-memory store (for demo - resets on deploy)
const usersStore: any[] = [];

export const POST: APIRoute = async ({ request }) => {
  try {
    const { email, password, name } = await request.json();

    if (!email || !password || !name) {
      return new Response(JSON.stringify({ error: 'Missing fields' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    // Check if user exists
    if (usersStore.find((u) => u.email === email)) {
      return new Response(JSON.stringify({ error: 'User already exists' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const user = {
      id: Date.now().toString(),
      email,
      password, // In production: hash with bcrypt!
      name,
      createdAt: new Date().toISOString(),
    };

    usersStore.push(user);

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
