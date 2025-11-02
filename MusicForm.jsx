import { useState } from 'react';
import { generateMusic } from '../api/musicgen';

export default function MusicForm() {
  const [prompt, setPrompt] = useState('');
  const [duration, setDuration] = useState(10);
  const [model, setModel] = useState('facebook/musicgen-small');
  const [audioUrl, setAudioUrl] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const blob = await generateMusic({ prompt, duration, model });
    setAudioUrl(URL.createObjectURL(blob));
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input value={prompt} onChange={(e) => setPrompt(e.target.value)} />
        <input type="range" min="5" max="30" value={duration} onChange={(e) => setDuration(e.target.value)} />
        <select value={model} onChange={(e) => setModel(e.target.value)}>
          <option value="facebook/musicgen-small">Small</option>
          <option value="facebook/musicgen-medium">Medium</option>
          <option value="facebook/musicgen-melody">Melody</option>
        </select>
        <button type="submit">Generar 🎧</button>
      </form>
      {audioUrl && <audio controls src={audioUrl} />}
    </div>
  );
}