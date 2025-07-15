package Pokeproject.Pokeproject.controller;

import Pokeproject.Pokeproject.model.DTO.NameRequest;
import Pokeproject.Pokeproject.model.Pokemon;
import Pokeproject.Pokeproject.service.PokemonService;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpEntity;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
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
        return pokeService.getAllPokemon();
    }

    @PostMapping("/getDamage")
    public Pokemon[] getDamagePokemon(@RequestBody NameRequest nameRequest){
        String name = nameRequest.getName();
        return pokeService.getDamagePokemon(name);
    }
//Checking if python api is working
@PostConstruct
public void recibirDatos() {
    RestTemplate restTemplate = new RestTemplate();

    // Obtener lista de pokémons
    String url = "http://localhost:5000/pokemons/getAllPokemons";
    Pokemon[] pokemons = restTemplate.getForObject(url, Pokemon[].class);
    System.out.println("Primer Pokémon: " + pokemons[0].getName());

    // Preparar POST para calcular daño
    String urlDamage = "http://localhost:5000/pokemons/calculateDamage";
    String jsonBody = "{\"nombre\": \"" + pokemons[0].getName() + "\"}";

    HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_JSON);

    HttpEntity<String> request = new HttpEntity<>(jsonBody, headers);

    ResponseEntity<String> response = restTemplate.postForEntity(urlDamage, request, String.class);

    System.out.println("Respuesta del daño:");
    System.out.println(response.getBody());
}

}