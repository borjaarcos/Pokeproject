import { Radar, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis } from 'recharts';


function HexChart(pokestats){
    const data = [
      { stat: 'HP', value: pokestats.pokestats.hp },
      { stat: 'Attack', value: pokestats.pokestats.attack },
      { stat: 'Defense', value: pokestats.pokestats.defense },
      { stat: 'Sp. Atk', value: pokestats.pokestats.special_attack },
      { stat: 'Sp. Def', value: pokestats.pokestats.special_defense },
      { stat: 'Speed', value: pokestats.pokestats.speed },
    ];

    return(

        <RadarChart outerRadius={90} width={400} height={300} data={data}>
          <PolarGrid />
          <PolarAngleAxis dataKey="stat" />
          <PolarRadiusAxis angle={30} domain={[0, 100]} />
          <Radar name="Stats" dataKey="value" stroke="#8884d8" fill="#8884d8" fillOpacity={0.6} />
        </RadarChart>
    );
}

export default HexChart;