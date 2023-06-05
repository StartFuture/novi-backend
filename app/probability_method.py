from dao.dao_probability_method import get_transport_and_tours_travel, get_tour_travel



def probability_calculation_travels(travels: dict, user_quiz: dict):
    travel_points = {}
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
        key = (best_tour['id_tour'], travel['id'])
        if key not in travel_points:
         total_price = float(travel['price']) + best_tour['transport_price'] 
         

         travel_points[key] = {'local_name': travel['local_name'],
                           'id_travel': travel['id'],
                           'points_travel': points ,'points_tour': best_tour['points_tour'],
                           'id_tour': best_tour['id_tour'], 'transport_points': best_tour['transport_points'], 
                           'id_transport': best_tour['id_transport'], 'travel_price': float(travel['price']),
                           'transport_price': best_tour['transport_price'], 'tour_price': best_tour['tour_price'],
                           'total_price': total_price, 'details_tour': best_tour['details_tour']}
    
    travel_points = list(travel_points.values())
    travel_points = sorted(travel_points, key=lambda x: x['points_travel'])
    travel_points = map_json(travels=travel_points)
    travel_points = total_price_travel(travels=travel_points)
    
    return travel_points


def probability_calculation_preference_and_transport(id_accommodation: int, user_quiz: dict):
   #calculo para passeios e transporte
   transport_points = []
   best_tours = []
   transports_and_tours = get_transport_and_tours_travel(id_accommodation=id_accommodation)
   for transport in transports_and_tours:
      transport_style = abs(transport['transport_style'] - user_quiz['transport_style'])
      transport_points.append({'transport_points': transport_style, 'id_transport': transport['id_transport'], 'transport_price': transport['transport_price']})
    
   transport_points = sorted(transport_points, key=lambda x: x['transport_points'])
   
   for tour in transports_and_tours: 
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
      
      best_tours.append({'points_tour': points_tour, 'id_tour': tour['id_tour'], 'transport_points': transport_points[0]['transport_points'],
                          'id_transport': transport_points[0]['id_transport'], 'transport_price': float(transport_points[0]['transport_price']),
                           'tour_price': float(tour['tour_price']), 'details_tour': tour['details_tour']})

   best_tours = sorted(best_tours, key=lambda x: x['points_tour'])
   

   return best_tours    



def map_json(travels: list):
   map_dict = dict()

   for travel in travels:
      id_travel = travel['id_travel']
      id_tour = travel['id_tour']
      if id_travel in map_dict.keys():
         if id_tour not in map_dict[id_travel]['tours'].keys():
            map_dict[id_travel]['tours'][id_tour] = {
               'points_travel': travel['points_travel'],
               'points_tour': travel['points_tour'],
               'id_tour': id_tour, 
               'transport_points': travel['transport_points'],
               'tour_details': travel['details_tour'],
               'price_tour': travel['tour_price']
            }
      else:
         map_dict[id_travel] = {
            'local_name': travel['local_name'],
            'id_travel': id_travel,
            'id_transport': travel['id_transport'],
            'total_price': travel['total_price'],
            'tours': {
               id_tour: {
                  'points_travel': travel['points_travel'],
                  'points_tour': travel['points_tour'],
                  'id_tour': id_tour, 
                  'transport_points': travel['transport_points'],
                  'tour_details': travel['details_tour'],
                  'price_tour': travel['tour_price']
                  }
               }
            }
   maped_travels = list()
   
   for travel in map_dict.values():
      list_tours = list()
      for tour in travel['tours'].values():
         
         list_tours.append(tour)
      travel['tours'] = list_tours
      maped_travels.append(travel)


   return maped_travels


def total_price_travel(travels: dict):
   for travel in travels:
      price_all_tours = 0
      tours = travel['tours']
      for tour in tours:
         price_all_tours = price_all_tours + tour['price_tour']
      travel['total_price'] += price_all_tours
   
   return travels
   