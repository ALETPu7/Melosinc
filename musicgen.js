export async function generateMusic({ prompt, duration, model }) {
  const response = await fetch('http://localhost:8000/api/generate-music', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, duration, model_type: model }),
  });
  if (!response.ok) throw new Error('Error generando música');
  return await response.blob();
}