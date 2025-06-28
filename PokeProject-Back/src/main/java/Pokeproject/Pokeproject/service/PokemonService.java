package Pokeproject.Pokeproject.service;

import Pokeproject.Pokeproject.model.Pokemon;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class PokemonService implements IPokemonService{

    @Override
    public List<Pokemon>  getAllPokemon() {
        Pokemon pokemon = new Pokemon();
        List<Pokemon> pokemons = new ArrayList<>();

        pokemon.setName("Pikachu");
        pokemons.add(pokemon);

        return pokemons;
    }
}
