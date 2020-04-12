# Desafio 4

O desafio consistia em coletar dados de casos, mortes e recuperados do site sobre a nova pandemia do corona virus.

######Site
- https://www.worldometers.info/coronavirus/

######Bibliotecas utilizadas
- sys
- requests
- re
- csv
- datetime

######Passo a Passo
- Pega o site via biblioteca requests.
- Seleciona os três tipos de números que eu desejo, cases, deaths e recovered. Isso é feito através de regex.
- Após isso os dados são enviados para um csv.
- Por ultimo foi necessário fazer um crontab fazendo o procedimento acima a cada 20 minutos.

