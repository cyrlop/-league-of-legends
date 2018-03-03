# -*- coding: utf-8 -*-

import requests

###########################################
############ GENERAL
###########################################
def test_api_key(api_key):
    dic = get_summoner_data("euw1", "Cyrlop", api_key)
    if "name" in dic.keys():
        print "API request successful"
        return True
    else:
        print "API request failed (regenerate key?)"
        return False


def get_json(url):
    return requests.get(url).json()


###########################################
############ REQUESTS
###########################################
def get_summoner_data(region, summoner_name, api_key):
    url = 'https://{}.api.riotgames.com/lol/summoner/v3/summoners/by-name/{}?api_key={}'.format(
        region,
        summoner_name,
        api_key
    )
    return get_json(url)


def get_summoner_league(summoner_id, region, api_key):
    url = 'https://{}.api.riotgames.com/lol/league/v3/positions/by-summoner/{}?api_key={}'.format(
        region,
        summoner_id,
        api_key
    )
    return get_json(url)


def get_league_data(league_id_id, region, api_key):
    url = 'https://{}.api.riotgames.com/lol/league/v3/leagues/{}?api_key={}'.format(
        region,
        league_id_id,
        api_key
    )
    return get_json(url)