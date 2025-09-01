import React from 'react'

export default function ResultCard({movie}) {
  return (
    <div className="bg-white shadow rounded p-4 mb-4">
      <div className="flex items-center justify-between">
        <h2 className="text-xl font-semibold">{movie.title}</h2>
        <span className="text-yellow-600 font-bold">⭐ {movie.rating}</span>
      </div>
      <p className="text-sm text-gray-700 mt-2"><strong>Actors:</strong> {movie.actors}</p>
      <p className="text-sm text-gray-700"><strong>Country:</strong> {movie.country}</p>
      <p className="mt-2 text-gray-800">{movie.summary}</p>
    </div>
  )
}
