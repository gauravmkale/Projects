async function getRecommendations() {
  const title = document.getElementById("movieInput").value;
  const response = await fetch(`https://<your-backend-url>.onrender.com/recommend?title=${title}`);
  const data = await response.json();
  let html = "";

  if (data.error) {
    html = `<p style="color:red;">${data.error}</p>`;
  } else {
    data.forEach(movie => {
      html += `
        <div class="card">
          <h3>${movie.title} ⭐ ${movie.rating}</h3>
          <p><b>Actors:</b> ${movie.actors}</p>
          <p><b>Country:</b> ${movie.country}</p>
          <p>${movie.summary}</p>
        </div>
      `;
    });
  }

  document.getElementById("results").innerHTML = html;
}
