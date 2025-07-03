import { useState, useEffect } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './App.css'
import SearchBar from './SearchBar.tsx'


function App() {
  const [pokemons, setPokemons] = useState([]);
  const [pokemonList, setPokemon] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/pokemon/getPokemons")
      .then((res) => res.json())
      .then((data) => {
        setPokemons(data);
        setPokemon(data);
      })
      .catch((err) => console.error("Error fetching pokemons:", err));
  }, []);

  const handleSearch = (query) => {
    const inputSearch = query.toLowerCase();
    setPokemon(
      pokemons.filter(p =>
        p.name.toLowerCase().includes(inputSearch)
      )
    );
  };
  const pokemonTypes = (p) => {
    return `${p.primary_type}${p.secondary_type ? ' / ' + p.secondary_type : ''}`;
  };
  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <h2>Pokémon List</h2>
        <table>
            <thead>
              <tr>
                <th></th>
                <th></th>
              </tr>
             </thead>
              <tbody>
                {pokemonList.map((p, i) => (
                <tr key = {i}>
                 <td>
                   {p.name}
                 </td>
                 <td >
                   {pokemonTypes(p)}
                 </td>
                </tr>
                ))}
            </tbody>
        </table>

    </div>
  );
}


export default App
