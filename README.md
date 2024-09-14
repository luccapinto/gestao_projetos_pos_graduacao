
# Sistema de Submissão e Avaliação de Projetos de Pós-Graduação

Bem-vindo ao projeto de **Sistema de Submissão e Avaliação de Projetos de Pós-Graduação**. Este sistema permite que alunos submetam seus projetos, acompanhem o status e visualizem suas notas. Os avaliadores podem gerenciar turmas, avaliar projetos e fornecer feedback.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Características Principais](#características-principais)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionalidades](#funcionalidades)
  - [Para Alunos](#para-alunos)
  - [Para Avaliadores](#para-avaliadores)
- [Uso](#uso)
  - [Para Alunos](#para-alunos-1)
  - [Para Avaliadores](#para-avaliadores-1)
- [Contribuindo](#contribuindo)
- [Licença](#licença)
- [Contato](#contato)

## Descrição do Projeto

Este projeto é uma aplicação web desenvolvida com o framework **Django**, que facilita o processo de submissão e avaliação de projetos na pós-graduação. O sistema oferece diferentes visões para alunos e avaliadores, permitindo uma gestão eficiente dos projetos acadêmicos.

## Características Principais

- **Autenticação de Usuários**: Login seguro com email e senha.
- **Visão do Aluno**:
  - Submissão de projetos.
  - Acompanhamento do status dos projetos.
  - Visualização do histórico de notas.
- **Visão do Avaliador**:
  - Gerenciamento de turmas.
  - Avaliação de projetos submetidos.
  - Fornecimento de feedback e notas.
- **Notificações**: Sistema de mensagens para manter os usuários informados sobre atualizações.
- **Interface Responsiva**: Design adaptado para diferentes dispositivos.

## Tecnologias Utilizadas

- **Back-end**: Python 3.x, Django 3.x
- **Front-end**: HTML5, CSS3, Bootstrap
- **Banco de Dados**: SQLite (para desenvolvimento), PostgreSQL (recomendado para produção)
- **Outros**: Virtualenv para gerenciamento de ambiente, Git para controle de versão

## Requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- Git (opcional, mas recomendado)

## Instalação

Siga os passos abaixo para configurar o projeto em sua máquina local.

### 1. Clonar o Repositório

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

### 2. Criar um Ambiente Virtual

Crie e ative um ambiente virtual para isolar as dependências do projeto:

```bash
python -m venv venv
```

Ative o ambiente virtual:

- **Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **Linux/MacOS**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar as Dependências

Instale as dependências necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

Se não houver um arquivo `requirements.txt`, instale o Django manualmente:

```bash
pip install django
```

## Configuração

### 1. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto para armazenar as variáveis de ambiente:

```bash
SECRET_KEY=sua_chave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

**Nota**: Substitua `sua_chave_secreta` por uma chave secreta real. Você pode gerar uma usando o Django ou outro método seguro.

### 2. Configurar o Banco de Dados

Por padrão, o projeto está configurado para usar o SQLite. Se desejar usar outro banco de dados (como PostgreSQL), atualize as configurações em `gestao_projetos/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Aplicar Migrações

Crie as tabelas no banco de dados:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar um Superusuário

Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

## Como Executar

Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

Acesse o sistema em `http://localhost:8000/`.

## Estrutura do Projeto

```
gestao_projetos/
├── contas/
│   ├── migrations/
│   ├── templates/
│   │   └── contas/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── projetos/
│   ├── migrations/
│   ├── templates/
│   │   └── projetos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── gestao_projetos/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   └── base.html
├── static/
│   └── css, js, img
├── manage.py
└── venv/
```

## Funcionalidades

### Para Alunos

- **Registro e Login**: Criação de conta e autenticação.
- **Submissão de Projetos**: Envio de documentos nos formatos permitidos.
- **Acompanhamento de Status**: Visualização do status atual dos projetos.
- **Histórico de Notas**: Acesso às notas e feedbacks recebidos.

### Para Avaliadores

- **Gerenciamento de Turmas**: Visualização das turmas atribuídas.
- **Avaliação de Projetos**: Download, avaliação e feedback dos projetos.
- **Devolução para Revisão**: Possibilidade de rejeitar projetos e solicitar revisões.

## Uso

### Para Alunos

1. **Registro**: Acesse `http://localhost:8000/contas/registrar/` e crie uma conta selecionando o tipo de usuário "Aluno".
2. **Login**: Faça login em `http://localhost:8000/contas/entrar/`.
3. **Submissão de Projetos**: Navegue até "Meus Projetos" e clique em "Submeter Novo Projeto".
4. **Acompanhamento**: Veja o status dos seus projetos na lista de projetos.
5. **Histórico de Notas**: Acesse a seção "Notas" para visualizar suas notas.

### Para Avaliadores

1. **Registro**: Acesse `http://localhost:8000/contas/registrar/` e crie uma conta selecionando o tipo de usuário "Avaliador".
2. **Login**: Faça login em `http://localhost:8000/contas/entrar/`.
3. **Gerenciamento de Turmas**: Acesse "Turmas" para ver as turmas atribuídas.
4. **Avaliação**: Selecione uma turma e avalie os projetos submetidos.

## Contribuindo

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch: `git checkout -b minha-feature`.
3. Faça suas alterações e commit: `git commit -m 'Minha nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Pull Request descrevendo suas alterações.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para dúvidas ou sugestões, entre em contato:

- **Nome**: *Seu Nome*
- **Email**: *seu.email@dominio.com*
- **GitHub**: [seu-usuario](https://github.com/seu-usuario)

---

Obrigado por utilizar o **Sistema de Submissão e Avaliação de Projetos de Pós-Graduação**!

---

