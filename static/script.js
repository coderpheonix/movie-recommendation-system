async function getRecommendations() {
  const movie = document.getElementById("movieInput").value.trim();
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";

  if (!movie) {
    resultsDiv.innerHTML = "<p>Please type a movie name.</p>";
    return;
  }

  try {
    const response = await fetch(`/recommend?movie=${encodeURIComponent(movie)}`);
    const data = await response.json();

    if (data.recommendations && data.recommendations.length > 0) {
      resultsDiv.innerHTML = `<h2>Because you watched <em>${data.query_movie}</em>...</h2>`;
      data.recommendations.forEach(rec => {
        const card = document.createElement("div");
        card.classList.add("movie-card");
        card.innerHTML = `
          <h3>${rec.title}</h3>
          <p class="similarity">Similarity: ${rec.similarity}</p>
        `;
        resultsDiv.appendChild(card);
      });
    } else {
      resultsDiv.innerHTML = "<p>No similar movies found.</p>";
    }
  } catch (error) {
    console.error(error);
    resultsDiv.innerHTML = "<p>Something went wrong. Please try again.</p>";
  }
}
