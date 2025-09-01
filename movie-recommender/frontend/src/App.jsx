import React, {useState} from 'react'
import ResultCard from './ResultCard'

const BACKEND_URL = "https://movies-7af7.onrender.com"

export default function App() {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  async function handleSearch(e) {
    e?.preventDefault()
    setError(null)
    if (!query) return setError('Please enter a movie title.')
    setLoading(true)
    try {
      const res = await fetch(`${BACKEND_URL}/recommend?title=${encodeURIComponent(query)}`)
      const data = await res.json()
      if (!res.ok) throw new Error(data.error || 'Failed to fetch')
      setResults(data)
    } catch(err) {
      setError(err.message)
      setResults(null)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="max-w-3xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-4">🎬 Movie Recommender</h1>

      <form onSubmit={handleSearch} className="flex gap-2 mb-4">
        <input
          className="flex-1 border rounded px-3 py-2"
          placeholder="Enter your favorite movie title (e.g., Inception)"
          value={query}
          onChange={e => setQuery(e.target.value)}
        />
        <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">Find</button>
      </form>

      {error && <div className="text-red-600 mb-4">{error}</div>}
      {loading && <div className="mb-4">Loading…</div>}

      <div>
        {results && results.length === 0 && <div>No recommendations found.</div>}
        {results && results.map((m, i) => <ResultCard key={i} movie={m} />)}
      </div>

      <footer className="mt-8 text-sm text-gray-600">
        Built with React + Vite + Tailwind. Backend: https://movies-7af7.onrender.com
      </footer>
    </div>
  )
}
