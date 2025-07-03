package Pokeproject.Pokeproject.controller;

import Pokeproject.Pokeproject.model.Pokemon;
import Pokeproject.Pokeproject.service.PokemonService;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;
@CrossOrigin(origins = "http://localhost:5173")
@RestController
@RequestMapping("/pokemon")
public class PokemonController {

    @Autowired
    PokemonService pokeService;

    @GetMapping("/getPokemons")
    public Pokemon[] getPokemons(){
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:5000/pokemons/getAllPokemons";
        Pokemon[] pokemons = restTemplate.getForObject(url, Pokemon[].class);
        return pokeService.getAllPokemon();
    }
//Checking if python api is working
    @PostConstruct
    public Pokemon[] recibirDatos() {
        // procesar datos o almacenarlos
        RestTemplate restTemplate = new RestTemplate();
        String url = "http://localhost:5000/pokemons/getAllPokemons";
        Pokemon[] pokemons = restTemplate.getForObject(url, Pokemon[].class);
        System.out.println("Datos recibidos: " + pokemons[0].getName());
        return pokemons;
    }
}