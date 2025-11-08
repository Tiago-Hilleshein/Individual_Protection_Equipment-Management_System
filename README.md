Sistema de gerência de estoque/almoxarifado
📖 Descrição do Projeto
O nosso Sistema de Gerência de Estoque/Almoxarifado tem como objetivo organizar e controlar a movimentação de materiais, equipamentos e insumos dentro de uma instituição. Permite o registro de entradas, saídas e empréstimos de itens, garantindo rastreabilidade, eficiência e redução de perdas no estoque.

O sistema foi desenvolvido para auxiliar na administração do almoxarifado, facilitando o acompanhamento dos níveis de estoque e a geração de relatórios de controle.

✨ Funcionalidades
Cadastro de itens, categorias e unidades de medida;
Controle de entrada e saída de materiais;
Registro e acompanhamento de empréstimos (como EPIs e ferramentas);
Cadastro de colaboradores e usuários do sistema;
Relatórios de movimentações e níveis de estoque;
Controle de permissões por tipo de usuário.
💻 Tecnologias Utilizadas
Frontend: HTML, CSS, JavaScript
Backend: Python (Django)
📁 Estrutura do Projeto
O projeto é dividido nos seguintes apps principais:

/gerencia_epi_django/ (Pasta do projeto principal): Contém as configurações globais (settings.py) e as URLs principais (urls.py).
/core/ (App de Autenticação): App responsável por todo o fluxo de autenticação (login, criação de conta).
/static/: Contém todos os arquivos estáticos (CSS, JS, Imagens, Fontes).
/templates/: Contém os templates base (ex: base_login.html, base_app.html) e também todas as outras páginas da camada de apresentação (ex: login.html, app_ui_users.html).
🔐 Fluxo de Autenticação
O fluxo de autenticação é gerenciado pelo app core.

core/views.py:

login_view: Responsável por renderizar a página de login e validar as credenciais do usuário. Redireciona usuários já logados.
login_create: Responsável por renderizar a página de criação de conta, validar se as senhas coincidem e criar um novo User no banco.
app_welcome: Página principal da aplicação para onde o usuário é redirecionado após o login.
core/urls.py:

'' (raiz): Aponta para views.login_view (name='login').
'login_create': Aponta para views.login_create (name='login_create').
'app_welcome': Aponta para views.app_welcome (name='app_welcome').
📦 Modelos de Dados (Models)
Atualmente, o projeto utiliza o modelo User padrão do Django (django.contrib.auth.models.User).

Exemplo de Modelos Futuros:

Categoria(models.Model): (ex: Ferramenta, EPI, Material de Escritório)
Item(models.Model): (ex: Furadeira, Capacete, Resma A4)
nome: CharField
codigo: CharField (unique)
categoria: ForeignKey(Categoria)
quantidade_total: IntegerField
Emprestimo(models.Model):
item: ForeignKey(Item)
colaborador: ForeignKey(User)
data_retirada: DateTimeField
data_devolucao: DateTimeField (null=True, blank=True)
🎨 Padrões de Código
Este projeto segue padrões de código específicos para facilitar a manutenção.

Padrão de Classes CSS
As classes em CSS devem seguir uma ordem estrita de propriedades para facilitar a leitura.

Propriedades Flex (display: flex, flex-direction, align-items, etc.)
Propriedades de Localização/Alinhamento (width, height, margin, padding, text-align, etc.)
Propriedades de Formatação (font-family, font-size, border, border-radius, background-image, etc.)
Propriedades de Cor (color, background-color)
Se uma seção não for utilizada, um comentário /**/ deve ser usado como placeholder.

Referência: Veja o arquivo POC - Site EPI - Documentação
