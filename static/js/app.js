document.getElementById('search-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const searchWord = document.getElementById('search-word').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = 'Searching for synonyms...';

    const response = await fetch('/synonyms', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ word: searchWord })
    });

    const synonyms = await response.json();
    resultsDiv.innerHTML = synonyms.length > 0 ? synonyms.join(', ') : 'No synonyms found.';
});
