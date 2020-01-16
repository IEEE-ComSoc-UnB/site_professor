# GitHub do site do professor Cadu, de psicologia

### Equipe do Front-end:
- Gobbi;
- Murilo;
- Mateus;
- Rômulo.

### Equipe do Back-end:
- Kfouri;
- Marcos;
- Pedro.

### Tecnologias usadas no front:
- HTML, CSS e JS;
- CSS:
  - SaSS;
  - Bootstrap;
- JS: 
  - React;
  - React Router;

### Tecnologias usadas no Back:
- Python 3.8.0:
  - Django 3.0.2;
    
### Ao clonar o repositório:
Instale as dependências do python3, rode essas linhas de código na pasta site_professor/site_login/
```shell 
  pip install -r requirements.txt
```
Sincronize o banco de dados
```shell
  python manage.py makemigrations
  python manage.py migrate
```
Para rodar o server
```shell
  python manage.py runserver
```
Caso seja realizada alguma mudança nas models, crie as migrações antes de sincronizar o banco de dados
```shell
   python manage.py makemigrations
```
