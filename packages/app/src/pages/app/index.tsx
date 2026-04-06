import { NextPage } from 'next';
import { useEffect, useMemo, useState } from 'react';
import emojis from '@emojis/data/emojis.json';

type EmojiMap = Record<string, string>;

const IMAGES_BASE =
  'https://raw.githubusercontent.com/hieudoanm/emojis/refs/heads/master/packages/data/emojis/images';

const AppPage: NextPage = () => {
  const [query, setQuery] = useState('');
  const [copied, setCopied] = useState<string | null>(null);

  /* =========================
     Filter
  ========================= */
  const filtered = useMemo(() => {
    const entries = Object.entries(emojis);
    if (!query) return entries;

    return entries.filter(([key]) =>
      key.toLowerCase().includes(query.toLowerCase())
    );
  }, [emojis, query]);

  /* =========================
     Copy
  ========================= */
  const handleCopy = async (value: string, key: string) => {
    try {
      await navigator.clipboard.writeText(value);
      setCopied(key);
      setTimeout(() => setCopied(null), 1200);
    } catch {
      alert('Failed to copy');
    }
  };

  /* =========================
     Download
  ========================= */
  const handleDownload = async (key: string) => {
    const url = `${IMAGES_BASE}/${key}.png`;

    const res = await fetch(url);
    const blob = await res.blob();

    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `${key}.png`;
    a.click();
  };

  /* =========================
     UI
  ========================= */
  return (
    <div
      data-theme="luxury"
      className="bg-base-100 text-base-content min-h-screen p-6">
      {/* Header */}
      <div className="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between">
        <h1 className="text-3xl font-bold tracking-wide">✨ Emoji Explorer</h1>

        <input
          type="text"
          placeholder="Search emoji..."
          className="input input-bordered input-md bg-base-200 focus:bg-base-100 w-full transition md:w-80"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </div>

      {/* Grid */}
      <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-6 xl:grid-cols-8">
        {filtered.map(([key, value]) => {
          const isUnicode = !value.startsWith('http');

          return (
            <div
              key={key}
              className="card bg-base-200/70 border-base-300 border shadow-md backdrop-blur transition-all duration-200 hover:-translate-y-1 hover:shadow-xl">
              <div className="card-body items-center gap-3 p-4 text-center">
                {/* Emoji */}
                <div
                  className="cursor-pointer text-4xl transition hover:scale-110"
                  onClick={() => handleCopy(value, key)}
                  title="Click to copy">
                  {isUnicode ? (
                    value
                  ) : (
                    <img
                      src={`${IMAGES_BASE}/${key}.png`}
                      alt={key}
                      className="h-10 w-10"
                    />
                  )}
                </div>

                {/* Name */}
                <div className="w-full truncate text-xs opacity-70">
                  :{key}:
                </div>

                {/* Actions */}
                <div className="flex gap-2">
                  <button
                    className={`btn btn-xs ${
                      copied === key ? 'btn-success' : 'btn-primary'
                    }`}
                    onClick={() => handleCopy(value, key)}>
                    {copied === key ? 'Copied' : 'Copy'}
                  </button>

                  <button
                    className="btn btn-xs btn-outline"
                    onClick={() => handleDownload(key)}>
                    PNG
                  </button>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Empty */}
      {filtered.length === 0 && (
        <div className="py-16 text-center text-lg opacity-60">
          No emojis found
        </div>
      )}
    </div>
  );
};

export default AppPage;
