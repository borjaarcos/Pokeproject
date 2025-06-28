import { useState, useEffect } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './App.css'
import SearchBar from './SearchBar.tsx'


function App() {
  const [pokemons, setPokemons] = useState([]);

    useEffect(() => {
      fetch("http://localhost:8080/pokemon/getPokemons")
        .then((res) => res.json())
        .then((data) => {
          setPokemons(data); // Asumiendo que data es un array de pokémon
        })
        .catch((err) => console.error("Error fetching pokemons:", err));
    }, []);

    const handleSearch = (query) => {
        const inputSearch = query.toLowerCase();
        setPokemons(
          pokemons.filter(p =>
            p.name.toLowerCase().includes(inputSearch)
          )
        );
      };
    return (
      <div>
      <SearchBar onSearch={handleSearch} />
        <h2>Pokémon List</h2>
        <ul>
          {pokemons.map((p, i) => (
            <li key={i}>{p.name}</li>
          ))}
        </ul>
      </div>
    );
}

export default App
