import type { APIRoute } from 'astro';

// DEMO MODE: Feedback stored in-memory (resets on deployment)
// In production: use Supabase

const feedbackStore: any[] = [];

export const POST: APIRoute = async ({ request }) => {
  try {
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
