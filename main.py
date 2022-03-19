import requests


def query(lat, lon, _api_key):
    query_url = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(
        lat, lon, _api_key
    )

    r = requests.get(query_url)
    data = r.json()
    print(
        'Weather Description: {}, Country Code: {}'.format(data['weather'][0]['description'], data['sys']['country'])
    )


print(
    'Please enter your api key: '
)
api_key = input()

print(
    'Enter your coordinates: '
)
coords_str = input()
spl_coords_str = coords_str.split(', ')
query(
    spl_coords_str[0], spl_coords_str[1], api_key
)
