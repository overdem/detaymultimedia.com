import type { APIRoute } from 'astro';
import jwt from 'jsonwebtoken';

export const prerender = false;

const JWT_SECRET = import.meta.env.JWT_SECRET || 'demo-secret-key-change-in-production';

// In-memory feedback storage (for demo)
const feedbackStore: any[] = [];

export const POST: APIRoute = async ({ request }) => {
  try {
    const authHeader = request.headers.get('authorization');
    if (!authHeader) {
      return new Response(JSON.stringify({ error: 'No authorization header' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const token = authHeader.split(' ')[1];
    let decoded;

    try {
      decoded = jwt.verify(token, JWT_SECRET);
    } catch {
      return new Response(JSON.stringify({ error: 'Invalid token' }), {
        status: 401,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const { demoId, title, message, rating } = await request.json();

    if (!demoId || !title || !message || !rating) {
      return new Response(JSON.stringify({ error: 'Missing required fields' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const feedback = {
      id: Date.now().toString(),
      demoId,
      userId: (decoded as any).id,
      title,
      message,
      rating: parseInt(rating),
      createdAt: new Date().toISOString(),
    };

    feedbackStore.push(feedback);

    return new Response(JSON.stringify(feedback), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};

export const GET: APIRoute = async ({ url }) => {
  try {
    const demoId = url.searchParams.get('demoId');

    if (!demoId) {
      return new Response(JSON.stringify({ error: 'demoId parameter required' }), {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    const feedback = feedbackStore.filter((f) => f.demoId === demoId);

    return new Response(JSON.stringify(feedback), {
      status: 200,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    return new Response(JSON.stringify({ error: (err as Error).message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
};
