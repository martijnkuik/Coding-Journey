
from exa_py import Exa

exa = Exa('71f70d74-0393-403d-aa22-156486ac6354')

query = input('Search here: ')

response = exa.search(
   query,
  num_results=10,
  type='keyword',
  include_domains=['https://www.twitter.com'],
)
print(response)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()