async function getPokemonData(pokemonName) {
  try {
    const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
  }
}