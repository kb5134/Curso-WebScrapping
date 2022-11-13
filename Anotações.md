<html>
<head></head>
<body>
<h1>Aulas</h1> 
<a href="https://www.youtube.com/playlist?list=PLg3ZPsW_sghSkRacynznQeEs-vminyTQk">Clique aqui para acessar as aulas</a>
<br>
<br><h1>Aula 1</h1>
    <p>O webscrapping determina qual o elemento que deseja selecionar para tratar com o python</p>
<br>
<h1> Aula 2 - Requisições HTTP</h1>
    <p>&emsp;As requisições get acessam as informações que solciitamos</p>
    <p>&emsp;As respostas para estas requisições no python são através de string personalizadas, sendo elas:<br> &emsp;Códigos de status, Cabeçalho e Conteudo</p>
    <p>&emsp;Outro método muito utilizado é o POST, que é utilizado para enviar dados para o servidor.</p>
<br>
<h1>Aula 3 - BeautifulSoup</h1>
    <p>&emsp;Ao passarmos a url para o BeautifulSoup, precisamos passar além do caminho para o content, o tipo dessa pagina, no caso html.parser.</p>
    <p>&emsp;Ao utilizar o método pretify, o retorno do beautifulsoup, será um html muito mais legivel que o retornado pelo response.</p>
    <p>&emsp;Após converter a pagina para o BeautiflSoup, podemos utilziar o método find para procurar o primeiro elemento com o a tag HTML definida, dentro deste método, passamos a tag que estmos buscando, qual o atributo que será utilizado para localizar esta tag, passando da seguinte forma:</p>
    <code>&emsp;post = site.find('div', attrs={'class': 'feed-post-body'}) </code>
    <p>&emsp;Podemos após buscar a tag que precisamos, podemos filtrar o retorno para que traga somente o campo que estamos buscando, para isso iremos realizar novamente o método find dentro do retorno anterior</p>
<br>
<h1>Aula 4 - Automatizando a busca</h1>
    <p>&emsp;Para obtermos uma lista com todas as noticias que contenham a tag que desejamos buscar, devemos utilziar a tag findAll, no lugar do find</p>  
    <p>&emsp;Este ResultSet retornado pelo findAll, pode ser percorrido por um for para que então possamos acessar a informação que desejamos</p>  
    <p>&emsp;Todas as vezes que pegamos algum dado pelo BeautifulSoup, podemos acesssar os atributos da tag selecionara, desta forma podemos acessar os links de um href, acessar o caminho da imagem (src), dentre outros atributos.
    Para selecionarmos estes atributos da forma de um dicionario python passando entre chaves o atributo desejado, segue exemplo:</p>
    <code>titulo['href]</code>
    <p>&emsp;Este código trará o link do campo titulo que definimos anteriormente.</p>  
    <p>&emsp;para adicionarmos estes dados coletado em uma dataframe e depois em um arquiv csv, iremos utilziar o pandas </p> 
    <p>&emsp;O primeiro passo é realizar a isnerção destas noticias dentro de uma lista, para que possamos pegar todos estes campo no pandas, para isso dentro do for damos inserimos uma lista com os campos dentro de uma lista vazia criada anteriormente.</p> 
    <p>&emsp;Após criarmos a lista podemos chamar o pandas com a variavel DataFrame passando os dados,as colunas utilizando o parametro columns=['titulo', 'Demais colunas'].
    <br/><br>
    Para salvarmos o dataframe em um arquivo csv podemos utilziar o método .to_csv() e dentro dele, temos que informar o nome do arquivo e a extensão, index=False (para não salvar o indice)
    </p> 
    <br>
<h1>Aula 5 - Buscando por produtos no ML</h1>
    <p>&emsp; Podemos realizar buscar utilizando parametros informados pelos usuários, utilizando o padrão da URL
    <br/><br/>
    &emsp;Por conta disto, nosso primeiro passo será sempre analsiar como as buscas por são tratadas nestas na url que estamos utilizando
    <br/><br/>
    &emsp;Depois de descobrirmos como passar os dados na URL, definimos uma url de base e uma variavel recebendo os valores passados pelo cliente, após isto basta definir dentro do requests.get a url base e o produto
    <br/><br/>
    &emsp;Para acessarmos o preço temos mais trabalho, para isso, pesquisamos pela primeira tag que possui o real e a primeira com centavos.
    </p> 
</body>
