package Pokeproject.Pokeproject.service;

import Pokeproject.Pokeproject.model.Pokemon;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.List;

@Service
public class PokemonService implements IPokemonService{

    @Override
    public Pokemon[]  getAllPokemon() {
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:5000/pokemons/getAllPokemons";
        Pokemon[] pokemons = restTemplate.getForObject(url, Pokemon[].class);

        return pokemons;
    }
}
