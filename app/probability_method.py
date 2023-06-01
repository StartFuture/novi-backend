from dao.dao_probability_method import get_transport_travel, get_tour_travel



def probability_calculation_travels(travels: dict, user_quiz: dict):
    travel_points = []
    #calculo para Viagens
    for travel in travels:
      travel_destination = abs(travel['travel_destination'] - user_quiz['travel_destination'])
      travel_style = abs(travel['travel_style'] - user_quiz['travel_style'])
      accommodation_style = abs(travel['accommodation_style'] - user_quiz['accommodation_style'])
      warm = abs(travel['warm'] - user_quiz['warm'])
      mild = abs(travel['mild'] - user_quiz['mild'])
      cold = abs(travel['cold'] - user_quiz['cold'])

      points = (travel_destination + travel_style + accommodation_style
                + warm + mild + cold)

      best_tours = probability_calculation_preference_and_transport(id_accommodation=travel['id'], user_quiz=user_quiz)
      for best_tour in best_tours:
        travel_points.append({'local_name': travel['local_name'],
                          'id_travel': travel["id"],
                          'points_travel': points ,'points_tour': best_tour['points_tour'],
                          'id_tour': best_tour['id_tour'], 'transport_points': best_tour['transport_points'], 
                          'id_transport': best_tour['id_transport']})
    

    travel_points = sorted(travel_points, key=lambda x: x['points_travel'])

    return travel_points


def probability_calculation_preference_and_transport(id_accommodation: int, user_quiz: dict):
   transport_points = []
   best_tours = []
   transports = get_transport_travel(id_accommodation=id_accommodation)
   tours = get_tour_travel(id_accommodation=id_accommodation)
   for transport in transports:
      transport_style = abs(transport['transport_style'] - user_quiz['transport_style'])
      transport_points.append({'transport_points': transport_style, 'id_transport': transport['id']})
    
   transport_points = sorted(transport_points, key=lambda x: x['transport_points'])
   
   for tour in tours: 
      night_style = abs(tour['night_style'] - user_quiz['night_style'])
      music_preference = abs(tour['music_preference'] - user_quiz['music_preference'])
      building_preference = abs(tour['building_preference'] - user_quiz['building_preference'])
      tradicion_preference = abs(tour['tradicion_preference'] - user_quiz['tradicion_preference'])
      party_preference = abs(tour['party_preference'] - user_quiz['party_preference'])
      water_preference = abs(tour['water_preference'] - user_quiz['water_preference'])
      walk_preference = abs(tour['walk_preference'] - user_quiz['walk_preference'])
      historic_preference = abs(tour['historic_preference'] - user_quiz['historic_preference'])
      sport_preference = abs(tour['sport_preference'] - user_quiz['sport_preference'])
      food_preference = abs(tour['food_preference'] - user_quiz['food_preference'])

      points_tour = (night_style + music_preference + building_preference + tradicion_preference + 
                      party_preference + water_preference + walk_preference + historic_preference +
                      sport_preference + food_preference)
      best_tours.append({'points_tour': points_tour, 'id_tour': tour['id'], 'transport_points': transport_points[0]['transport_points'], 'id_transport': transport_points[0]['id_transport']})

   best_tours = sorted(best_tours, key=lambda x: x['points_tour'])
   
   return best_tours    
