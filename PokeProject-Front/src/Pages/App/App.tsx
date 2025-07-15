import { useState, useEffect } from 'react'
import './App.css'
import SearchBar from '../../Components/SearchBar/SearchBar.tsx'
import { useNavigate } from 'react-router-dom';

function App() {
  const [pokemons, setPokemons] = useState([]);
  const [pokemonList, setPokemon] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("http://localhost:8080/pokemon/getPokemons")
      .then((res) => res.json())
      .then((data) => {
        setPokemons(data);
        setPokemon(data);
      })
      .catch((err) => console.error("Error fetching pokemons:", err));
  }, []);
  console.log({pokemons});
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
  const handleImageClick = (pokemon) => {
  console.log(pokemon);
    navigate(`/detalle/${pokemon.name}`, {
        state: { pokemon }
      });
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
                 <td> <img src={p.url}
                        onClick={() => handleImageClick(p)}
                        style={{ cursor: 'pointer' }}
                 /> </td>
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
