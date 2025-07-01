package Pokeproject.Pokeproject.controller;

import Pokeproject.Pokeproject.model.Pokemon;
import Pokeproject.Pokeproject.service.PokemonService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
@CrossOrigin(origins = "http://localhost:5173")
@RestController
@RequestMapping("/pokemon")
public class PokemonController {

    @Autowired
    PokemonService pokeService;

    @GetMapping("/getPokemons")
    public List<Pokemon> getPokemons(){
        System.out.println("Llamada recibida en /getPokemons");
        return pokeService.getAllPokemon();
    }
}