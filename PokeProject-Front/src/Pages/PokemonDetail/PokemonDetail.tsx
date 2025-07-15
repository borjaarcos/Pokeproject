import { useLocation, useParams } from 'react-router-dom';
import { useState, useEffect } from 'react';
import HexChart from './HexChart.tsx';
import './PokemonDetail.css';

const tipoColorMap: Record<string, string> = {
  grass: '#4CAF50',
  water: '#2196F3',
  fire: '#F44336',
  electric: '#FFEB3B',
  normal: '#9E9E9E',
  flying: '#90CAF9',
  ice: '#81D4FA',
  fighting: '#F44336',
  poison: '#9C27B0',
  ground: '#A1887F',
  fairy: '#F48FB1',
  bug: '#8BC34A',
  rock: '#A1887F',
  ghost: '#757575',
  dragon: '#673AB7',
  dark: '#424242',
  steel: '#B0BEC5',
  psychic: '#E91E63',
};

function PokemonDetail() {
  const { name } = useParams();
  const location = useLocation();
  const pokemon = location.state?.pokemon;

  const [damageData, setDamageData] = useState<any[]>([]); // ← nuevo estado

  useEffect(() => {
    if (pokemon) {
      fetch("http://localhost:8080/pokemon/getDamage", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: pokemon.name })
      })
        .then(res => res.json())
        .then(data => {
          console.log("Pokémons fuertes contra", pokemon.name, data);
          setDamageData(data); // ← guardar en estado
        })
        .catch(err => console.error("Error al obtener daño:", err));
    }
  }, [pokemon]);

  if (!pokemon) return <div>Cargando...</div>;

  const backgroundColor = tipoColorMap[pokemon.primary_type.toLowerCase()] || '#4CAF50';

  return (
    <div className="detail-card" style={{ backgroundColor }}>
      <img src={pokemon.url} alt={pokemon.name} />
      <div className="nombre">#{pokemon.id} {pokemon.name}</div>

      <div className="tipos">
        <span className="tipo">{pokemon.primary_type}</span>
        {pokemon.secondary_type && <span className="tipo">{pokemon.secondary_type}</span>}
      </div>

      <div className="chart-container">
        <HexChart pokestats={pokemon} />
      </div>

      <h3>Pokémons fuertes contra {pokemon.name}:</h3>
      {damageData.length === 0 ? (
        <p>No se encontraron resultados.</p>
      ) : (
        damageData.map((p, i) => (
          <div key={i}>{damageData[i].name}</div>
        ))
      )}
    </div>
  );
}

export default PokemonDetail;
