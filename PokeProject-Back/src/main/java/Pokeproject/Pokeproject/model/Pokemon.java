package Pokeproject.Pokeproject.model;

import Pokeproject.Pokeproject.model.DTO.PokeDamageResponse;
import lombok.Data;

@Data
public class Pokemon {
    private String name;
    private String primary_type;
    private String secondary_type;
    private String move_1;
    private String move_2;
    private String move_3;
    private String move_4;
    private String move_5;
    private String hp;
    private String attack;
    private String defense;
    private String special_attack;
    private String special_defense;
    private String speed;
    private String url;
    private int receivedDamage;
    public void PokeDamageToPokemon(PokeDamageResponse pokeDamage){
        this.setName(pokeDamage.getPokemon_defensor());
        this.setMove_1(pokeDamage.getNombre_mov());
        this.setReceivedDamage(pokeDamage.getDaño_estimado());
        this.setDefense(String.valueOf(pokeDamage.getDef()));
        this.setSpecial_defense(String.valueOf(pokeDamage.getDef_esp()));
    }
}
