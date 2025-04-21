"""
Manual do Usuário - Sistema de Cobrança Automática com WhatsApp

Este manual contém instruções detalhadas sobre como instalar, configurar e utilizar
o Sistema de Cobrança Automática com WhatsApp.
"""

# Manual do Usuário
# Sistema de Cobrança Automática com WhatsApp

## Índice

1. [Introdução](#1-introdução)
2. [Requisitos do Sistema](#2-requisitos-do-sistema)
3. [Instalação](#3-instalação)
4. [Primeiros Passos](#4-primeiros-passos)
5. [Gerenciamento de Clientes](#5-gerenciamento-de-clientes)
6. [Gerenciamento de Cobranças](#6-gerenciamento-de-cobranças)
7. [Envio de Mensagens pelo WhatsApp](#7-envio-de-mensagens-pelo-whatsapp)
8. [Gerenciamento de Imagens](#8-gerenciamento-de-imagens)
9. [Dashboard e Relatórios](#9-dashboard-e-relatórios)
10. [Configurações Avançadas](#10-configurações-avançadas)
11. [Solução de Problemas](#11-solução-de-problemas)
12. [Perguntas Frequentes](#12-perguntas-frequentes)

## 1. Introdução

O Sistema de Cobrança Automática com WhatsApp é uma solução completa para gerenciar seus clientes, criar cobranças e enviar mensagens automáticas pelo WhatsApp. Com uma interface amigável e recursos avançados, o sistema permite automatizar todo o processo de cobrança, desde a criação até o acompanhamento de pagamentos.

### Principais Funcionalidades

- Cadastro e gerenciamento completo de clientes
- Criação e agendamento de cobranças
- Envio automático de mensagens pelo WhatsApp
- Suporte para envio de imagens junto com as mensagens
- Dashboard interativo com previsão de faturamento
- Relatórios detalhados de cobranças e pagamentos
- Personalização de mensagens e lembretes

## 2. Requisitos do Sistema

Para utilizar o Sistema de Cobrança Automática com WhatsApp, você precisará de:

### Requisitos de Hardware
- Computador com processador de 2 GHz ou superior
- Mínimo de 4 GB de RAM
- 500 MB de espaço livre em disco

### Requisitos de Software
- Sistema operacional: Windows 10/11, macOS 10.15+, ou Linux (Ubuntu 20.04+)
- Python 3.8 ou superior
- Google Chrome (versão mais recente)
- Conexão com a internet

### Requisitos para WhatsApp
- Conta ativa no WhatsApp
- Número de telefone válido para uso com WhatsApp Web
- Para recursos avançados: conta na API WhatsGW (opcional)

## 3. Instalação

### 3.1. Instalação do Python

Se você ainda não tem o Python instalado:

1. Acesse [python.org](https://www.python.org/downloads/)
2. Baixe a versão mais recente do Python para seu sistema operacional
3. Execute o instalador
4. **IMPORTANTE**: Marque a opção "Add Python to PATH" durante a instalação
5. Clique em "Install Now"

### 3.2. Instalação do Sistema

1. Extraia o arquivo `sistema_cobranca_whatsapp_web.zip` para uma pasta de sua preferência
2. Abra o terminal (Prompt de Comando no Windows, Terminal no macOS/Linux)
3. Navegue até a pasta onde você extraiu os arquivos:
   ```
   cd caminho/para/sistema_cobranca_whatsapp_web
   ```
4. Instale as dependências necessárias:
   ```
   pip install -r requirements.txt
   ```
5. Inicialize o banco de dados:
   ```
   python init_db.py
   ```

## 4. Primeiros Passos

### 4.1. Iniciando o Sistema

1. Na pasta do sistema, execute o comando:
   ```
   python run.py
   ```
2. O sistema será iniciado e estará disponível no navegador
3. Abra o Google Chrome e acesse:
   ```
   http://localhost:5000
   ```

### 4.2. Configuração Inicial

Ao acessar o sistema pela primeira vez, você deverá:

1. Configurar as opções de envio de WhatsApp em "Configurações"
2. Criar modelos de mensagens para cobranças
3. Configurar frequências de envio automático

## 5. Gerenciamento de Clientes

### 5.1. Cadastro de Clientes

1. No menu principal, clique em "Clientes"
2. Clique no botão "Novo Cliente"
3. Preencha os campos obrigatórios:
   - Nome completo
   - Telefone (formato: +5511987654321)
   - Email (opcional)
   - Endereço (opcional)
4. Clique em "Salvar"

### 5.2. Importação de Clientes

Para importar vários clientes de uma vez:

1. Prepare uma planilha Excel com as colunas: nome, telefone, email
2. No menu "Clientes", clique em "Importar"
3. Selecione o arquivo Excel
4. Mapeie as colunas conforme solicitado
5. Clique em "Importar Clientes"

### 5.3. Edição e Exclusão de Clientes

Para editar um cliente:
1. Na lista de clientes, clique no nome do cliente
2. Clique em "Editar"
3. Faça as alterações necessárias
4. Clique em "Salvar"

Para excluir um cliente:
1. Na lista de clientes, clique no nome do cliente
2. Clique em "Excluir"
3. Confirme a exclusão

## 6. Gerenciamento de Cobranças

### 6.1. Criação de Cobranças

1. No menu principal, clique em "Cobranças"
2. Clique no botão "Nova Cobrança"
3. Selecione o cliente
4. Preencha os campos:
   - Valor
   - Data de vencimento
   - Frequência (única, diária, semanal, mensal)
   - Observações (opcional)
5. Clique em "Salvar"

### 6.2. Importação de Cobranças

Para importar várias cobranças de uma vez:

1. Prepare uma planilha Excel com as colunas: cliente_id (ou telefone), valor, data_vencimento, frequencia
2. No menu "Cobranças", clique em "Importar"
3. Selecione o arquivo Excel
4. Mapeie as colunas conforme solicitado
5. Clique em "Importar Cobranças"

### 6.3. Gerenciamento de Status

As cobranças podem ter os seguintes status:
- **Pendente**: Cobrança criada, ainda não vencida
- **Vencida**: Data de vencimento já passou
- **Paga**: Cliente confirmou o pagamento
- **Cancelada**: Cobrança foi cancelada

Para alterar o status:
1. Na lista de cobranças, clique na cobrança
2. Clique em "Alterar Status"
3. Selecione o novo status
4. Adicione uma observação (opcional)
5. Clique em "Salvar"

## 7. Envio de Mensagens pelo WhatsApp

### 7.1. Configuração do WhatsApp Web

1. No menu "Configurações", acesse "WhatsApp"
2. Clique em "Conectar WhatsApp Web"
3. Uma janela do Chrome será aberta com o WhatsApp Web
4. Escaneie o QR code com seu celular
5. Após conectar, o sistema estará pronto para enviar mensagens

### 7.2. Envio Manual de Cobranças

Para enviar uma cobrança manualmente:

1. Na lista de cobranças, clique na cobrança
2. Clique em "Enviar via WhatsApp"
3. Selecione o modelo de mensagem
4. Personalize a mensagem se necessário
5. Clique em "Enviar"

### 7.3. Configuração de Envio Automático

Para configurar o envio automático:

1. No menu "Configurações", acesse "WhatsApp"
2. Na seção "Agendamento de Envios":
   - Configure o horário para envio diário
   - Configure o dia e horário para envio semanal
   - Configure o dia e horário para envio mensal
   - Configure o horário para verificação de cobranças vencidas
3. Ative ou desative cada tipo de envio conforme necessário
4. Clique em "Salvar Agendamento"

## 8. Gerenciamento de Imagens

### 8.1. Upload de Imagens

1. No menu principal, clique em "Imagens"
2. Clique em "Upload de Imagem"
3. Selecione o arquivo de imagem (formatos aceitos: JPG, PNG, GIF, WEBP)
4. Selecione o tipo de imagem (geral, cobrança, boleto, QR code)
5. Adicione uma descrição (opcional)
6. Clique em "Fazer Upload"

### 8.2. Associação de Imagens a Cobranças

Para associar uma imagem a uma cobrança:

1. Na lista de cobranças, clique na cobrança
2. Clique em "Imagens"
3. Clique em "Nova Imagem" para fazer upload de uma nova imagem
   OU
   Clique em "Associar Existente" para usar uma imagem já cadastrada
4. Marque a opção "Definir como imagem principal" se desejar que esta imagem seja enviada junto com a mensagem
5. Clique em "Salvar"

### 8.3. Envio de Cobranças com Imagens

Quando uma cobrança possui uma imagem principal definida, esta imagem será enviada automaticamente junto com a mensagem de cobrança pelo WhatsApp.

Para enviar uma cobrança com imagem:

1. Na lista de cobranças, clique na cobrança
2. Verifique se há uma imagem principal definida
3. Clique em "Enviar via WhatsApp"
4. Selecione a opção "Usar API WhatsGW" (necessário para envio de imagens)
5. Clique em "Enviar"

## 9. Dashboard e Relatórios

### 9.1. Dashboard Principal

O dashboard principal apresenta:

- Resumo de cobranças (pendentes, vencidas, pagas)
- Previsão de faturamento para os próximos dias
- Gráfico de cobranças por status
- Lista de próximos vencimentos
- Atividade recente

### 9.2. Relatórios Disponíveis

O sistema oferece os seguintes relatórios:

1. **Relatório de Cobranças**: Todas as cobranças filtradas por período, status ou cliente
2. **Relatório de Pagamentos**: Pagamentos recebidos em um período específico
3. **Relatório de Clientes**: Lista de clientes com status de pagamento
4. **Relatório de Mensagens**: Histórico de mensagens enviadas pelo WhatsApp

Para gerar um relatório:

1. No menu principal, clique em "Relatórios"
2. Selecione o tipo de relatório
3. Configure os filtros desejados
4. Clique em "Gerar Relatório"
5. O relatório pode ser visualizado na tela ou exportado em formato CSV ou PDF

## 10. Configurações Avançadas

### 10.1. Personalização de Modelos de Mensagem

1. No menu "Configurações", acesse "Modelos de Mensagem"
2. Clique em "Novo Modelo" ou selecione um existente para editar
3. Preencha os campos:
   - Título do modelo
   - Conteúdo da mensagem
   - Tipo (padrão, vencida, lembrete)
4. Use os placeholders disponíveis:
   - {nome} - Nome do cliente
   - {valor} - Valor da cobrança
   - {data_vencimento} - Data de vencimento
   - {dias_atraso} - Dias em atraso (para cobranças vencidas)
5. Clique em "Salvar"

### 10.2. Configuração da API WhatsGW

Para utilizar recursos avançados como envio de imagens:

1. Crie uma conta em [whatsgw.com.br](https://whatsgw.com.br) (ou outro provedor compatível)
2. Obtenha sua chave de API
3. No menu "Configurações", acesse "WhatsApp"
4. Na seção "Configurações da API WhatsGW", insira sua chave de API
5. Clique em "Salvar Configurações"

### 10.3. Backup do Sistema

Para fazer backup dos dados:

1. No menu "Configurações", acesse "Sistema"
2. Na seção "Backup", clique em "Gerar Backup"
3. O sistema criará um arquivo de backup contendo o banco de dados e configurações
4. Baixe o arquivo e guarde-o em local seguro

Para restaurar um backup:

1. No menu "Configurações", acesse "Sistema"
2. Na seção "Restaurar Backup", clique em "Selecionar Arquivo"
3. Selecione o arquivo de backup
4. Clique em "Restaurar"
5. O sistema será reiniciado após a restauração

## 11. Solução de Problemas

### 11.1. Problemas de Conexão com WhatsApp

Se o sistema não conseguir conectar ao WhatsApp Web:

1. Verifique se o Google Chrome está instalado e atualizado
2. Certifique-se de que seu celular está conectado à internet
3. Tente desconectar e reconectar o WhatsApp Web
4. Verifique se não há outras sessões do WhatsApp Web ativas
5. Reinicie o sistema e tente novamente

### 11.2. Mensagens Não Enviadas

Se as mensagens não estiverem sendo enviadas:

1. Verifique o status da conexão com WhatsApp Web
2. Certifique-se de que o formato do número de telefone está correto (+5511987654321)
3. Verifique se há limite de envio de mensagens (WhatsApp pode bloquear envios em massa)
4. Tente enviar manualmente para testar a conexão
5. Verifique os logs do sistema para identificar erros específicos

### 11.3. Problemas com Imagens

Se as imagens não estiverem sendo enviadas:

1. Verifique se a API WhatsGW está configurada corretamente
2. Certifique-se de que a imagem está marcada como "principal"
3. Verifique se o formato da imagem é suportado
4. Tente reduzir o tamanho da imagem se for muito grande
5. Teste o envio manual de uma imagem para verificar a conexão

## 12. Perguntas Frequentes

### 12.1. O sistema funciona com WhatsApp Business?
Sim, o sistema é compatível tanto com WhatsApp pessoal quanto com WhatsApp Business.

### 12.2. Posso enviar mensagens para vários clientes ao mesmo tempo?
Sim, você pode selecionar múltiplas cobranças e enviar mensagens em lote. No entanto, recomendamos limitar o número de mensagens enviadas em um curto período para evitar bloqueios pelo WhatsApp.

### 12.3. O sistema funciona sem internet?
Não, o sistema requer conexão com a internet para funcionar, especialmente para o envio de mensagens pelo WhatsApp.

### 12.4. Posso acessar o sistema de qualquer computador?
O sistema é instalado localmente, então você só pode acessá-lo no computador onde foi instalado. No entanto, você pode configurar o acesso remoto se necessário.

### 12.5. O que acontece se eu receber uma resposta do cliente?
O sistema não processa automaticamente as respostas recebidas. Você precisará verificar as respostas diretamente no WhatsApp e atualizar o status das cobranças manualmente.

### 12.6. Posso personalizar as mensagens para cada cliente?
Sim, você pode criar modelos de mensagem personalizados e também editar a mensagem antes de enviar para um cliente específico.

### 12.7. O sistema envia lembretes automáticos para cobranças vencidas?
Sim, você pode configurar o sistema para verificar diariamente as cobranças vencidas e enviar lembretes automáticos.

### 12.8. Quantas imagens posso associar a uma cobrança?
Você pode associar quantas imagens desejar a uma cobrança, mas apenas a imagem marcada como "principal" será enviada junto com a mensagem.

---

Para mais informações ou suporte técnico, entre em contato pelo email: suporte@sistemacobranca.com.br
