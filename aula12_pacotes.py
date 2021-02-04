import requests

#importando API de CEP:
def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    print(dados_cep)

#importando API de dados de pokemon:
def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    #retorna_dados_cep('01001000')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://github.com/leleh5/')
    print(response)