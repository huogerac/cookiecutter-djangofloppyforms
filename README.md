# cookiecutter-djangofloppyforms

## Pré requisitos

Primeiro, instale o cookiecutter

    $ pip install "cookiecutter>=1.7.0"


Tenha o NPM instalado

    npm -v



## Uso

Rode o cookiecutter apontando para este repo:

    cookiecutter https://github.com/huogerac/cookiecutter-djangofloppyforms


Responda as perguntas sobre seu novo projeto:

    project_name [My Awesome Project]: Minhas Tarefas
    project_slug [minhas_tarefas]: 
    main_app [todo]: tarefas
    main_model [Task]: Tarefa
    description [Behold My Awesome Project!]: Minha aplicação de tarefas bonitona
    author_name [Roger Camargo]: 
    domain_name [example.com]: minhastarefas.na-inter.net
    email [roger-camargo@example.com]: huogerac@gmail.com
    version [0.1.0]: 
    timezone [UTC]: 


Entre na pasta do seu novo projeto e faça o setup inicial:

    cd minhas_tarefas/

    pip install -r requirements.txt
    ./manage.py migrate
    npm install
    ./scripts/install_static.sh
    ./manage.py runserver
