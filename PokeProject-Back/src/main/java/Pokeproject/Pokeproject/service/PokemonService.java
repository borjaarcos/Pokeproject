package Pokeproject.Pokeproject.service;

import Pokeproject.Pokeproject.model.DTO.PokeDamageResponse;
import Pokeproject.Pokeproject.model.Pokemon;
import org.springframework.http.*;
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

    @Override
    public Pokemon[] getDamagePokemon(String pokemonName) {
        System.out.println("PokemonName: "+pokemonName);
        RestTemplate restTemplate = new RestTemplate();
        String jsonBody = "{\"nombre\": \"" + pokemonName + "\"}";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<String> request = new HttpEntity<>(jsonBody, headers);
        String urlDamage = "http://localhost:5000/pokemons/calculateDamage";

        ResponseEntity<PokeDamageResponse[]> response = restTemplate.exchange(
                urlDamage,
                HttpMethod.POST,
                request,
                PokeDamageResponse[].class
        );

        PokeDamageResponse[] pokemonsResponse = response.getBody();

        Pokemon p = new Pokemon();
        p.PokeDamageToPokemon(pokemonsResponse[0]);
        System.out.println("PokemonName: "+p);
        List<Pokemon> p2 = new ArrayList<>();
        p2.add(p);
        Pokemon[] pokemons = p2.toArray(new Pokemon[0]);

        return pokemons;
    }
}
