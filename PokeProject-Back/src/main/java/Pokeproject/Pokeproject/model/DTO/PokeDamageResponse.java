package Pokeproject.Pokeproject.model.DTO;

import lombok.Data;

@Data
public class PokeDamageResponse {
    String pokemon_atacante;
    String pokemon_defensor;
    String nombre_mov;
    String movimiento_tipo;
    int stab;
    int poder;
    String clase_daño;
    String tipos_defensor;
    int def;
    int def_esp;
    int multiplicador;
    int multiplicador_total;
    int daño_estimado;
}
