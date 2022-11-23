import requests

class TesteFilme:
    headers = {'Authorization': 'Token '}
    url_base_filmes = 'http://localhost:8000/api/v2/filmes/'

    # def test_get(self):
    #     resposta = requests.get(url=self.url_base_filmes, headers=self.headers)
    #
    #     assert resposta.status_code == 200
    #
    # def test_put(self):
    #     atualiza_dado = {
    #         "titulo": "Filme Teste",
    #         "diretor": "Erick Palma",
    #         "lancamento": "1993-10-18"
    #     }
    #
    #     resposta = requests.put(url=f'{self.url_base_filmes}1/', headers=self.headers, data=atualiza_dado)
    #
    #     assert resposta.status_code == 200

    def test_post(self):
        novo_dado = {
            "titulo": "Filme Teste2",
            "diretor": "Erick Palma",
            "lancamento": "1993-10-18"
        }

        resposta = requests.post(url=self.url_base_filmes, headers=self.headers, data=novo_dado)

        assert resposta.status_code == 201

    # def test_delete(self):
    #     resposta = requests.delete(url=f'{self.url_base_filmes}1/', headers=self.headers)
    #
    #     assert resposta.status_code == 204
