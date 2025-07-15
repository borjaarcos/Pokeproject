import { Routes, Route } from 'react-router-dom';
import HomePage from '../Pages/App/App.tsx';
import Details from '../Pages/PokemonDetail/PokemonDetail.tsx';

const AppRoutes = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/detalle/:name" element={<Details />} />
    </Routes>
  );
};

export default AppRoutes;