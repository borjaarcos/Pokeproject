import { useState, useEffect } from 'react'
//import reactLogo from './assets/react.svg'
//import viteLogo from '/vite.svg'
import './App.css'
import SearchBar from './SearchBar.tsx'
import HexChart from './HexChart.tsx'
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';



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
      <div className="searchbar-container">
        <div className="searchbar-wrapper">
          <SearchBar onSearch={handleSearch} />
        </div>
      </div>
      <h2>Pokémon List</h2>
        <table>

              <tbody>
                {pokemonList.slice(0, 50).map((p, i) => (
                <tr key = {i}>
                 <td> <img src={p.url}/> </td>
                 <td> {p.name} </td>

                 <td > {pokemonTypes(p)} </td>


                </tr>
                ))}
            </tbody>
        </table>

    </div>
  );
}


export default App
