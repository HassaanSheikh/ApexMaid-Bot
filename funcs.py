import os
import requests
import json
my_secret = os.environ['TOKEN']
apex_key = os.environ['apex_api']

def player_info(name):
  response = requests.get("https://api.mozambiquehe.re/bridge?version=5&platform=PC&player="+name+"&auth="+apex_key)

  json_data = json.loads(response.text)

  apex_name = json_data['global']['name']
  uid = json_data['global']['uid']
  lvl = json_data['global']['level']
  rank = json_data['global']['rank']['rankName']
  arena_rank = json_data['global']['arena']['rankName']

  output = apex_name+ " uid " +str(uid)+ " Level " +str(lvl)+ " Currently " +rank+ " in Battle Royale and " +arena_rank+ " in Arenas"
  return output

def br_rotation():
  response = requests.get("https://api.mozambiquehe.re/maprotation?version=2&auth="+apex_key)

  json_data = json.loads(response.text)

  norm_map = json_data['battle_royale']['current']['map']
  norm_time_left = json_data['battle_royale']['current']['remainingTimer']

  next_map = json_data['battle_royale']['next']['map']
  next_duration = json_data['battle_royale']['next']['DurationInMinutes']

  ranked_map = json_data['ranked']['current']['map']

  br_str = "Unranked: " + norm_map + " for the next " + norm_time_left + ", then " + next_map + " for " + str(next_duration) + " minutes\nRanked Map this split: " + ranked_map

  return br_str

def arena_rotation():
  response = requests.get("https://api.mozambiquehe.re/maprotation?version=2&auth="+apex_key)

  json_data = json.loads(response.text)

  norm_map = json_data['arenas']['current']['map']
  norm_time_left = json_data['arenas']['current']['remainingTimer']

  next_map = json_data['arenas']['next']['map']
  next_duration = json_data['arenas']['next']['DurationInMinutes']

  ranked_map = json_data['arenasRanked']['current']['map']
  ranked_time_left = json_data['arenasRanked']['current']['remainingTimer']

  ranked_next_map = json_data['arenasRanked']['next']['map']
  ranked_next_duration = json_data['arenasRanked']['next']['DurationInMinutes']

  arena_str = "Unranked: " + norm_map + " for the next " + norm_time_left + ", then " + next_map + " for " + str(next_duration) + " minutes\nRanked: " + ranked_map + " for the next " + ranked_time_left + ", then " + ranked_next_map + " for " + str(ranked_next_duration) + " minutes"

  return arena_str

def server_status():
  response = requests.get("https://api.mozambiquehe.re/servers?auth="+apex_key)

  json_data = json.loads(response.text)

  us_west_status = json_data['Origin_login']['US-West']['Status']
  us_west_ping = json_data['Origin_login']['US-West']['ResponseTime']

  us_east_status = json_data['Origin_login']['US-East']['Status']
  us_east_ping = json_data['Origin_login']['US-East']['ResponseTime']

  server_str = "US West: " + us_west_status + ", " + str(us_west_ping) + " ms\nUS East: " + us_east_status + ", " + str(us_east_ping) + " ms"

  return server_str