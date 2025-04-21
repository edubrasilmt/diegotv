"""
Script para inicializar o banco de dados e criar as tabelas.
"""

from app import create_app, db
from app.models import Cliente, Contato, Cobranca, AgendamentoCobranca
from app.models import ModeloMensagem, MensagemEnviada, Imagem, ImagemCobranca

app = create_app()

with app.app_context():
    # Criar todas as tabelas
    db.create_all()
    
    # Criar modelos de mensagens padrão
    if not ModeloMensagem.query.filter_by(titulo='Cobrança Padrão').first():
        modelo_cobranca = ModeloMensagem(
            titulo='Cobrança Padrão',
            conteudo='Olá {nome}, este é um lembrete de cobrança no valor de R$ {valor:.2f} com vencimento em {data_vencimento}. Por favor, efetue o pagamento para evitar juros e multas. Responda "PAGO" quando efetuar o pagamento. Obrigado!',
            tipo='cobranca'
        )
        db.session.add(modelo_cobranca)
    
    if not ModeloMensagem.query.filter_by(titulo='Cobrança Vencida').first():
        modelo_vencida = ModeloMensagem(
            titulo='Cobrança Vencida',
            conteudo='Atenção {nome}, sua cobrança no valor de R$ {valor:.2f} está vencida desde {data_vencimento}. Por favor, entre em contato conosco para regularizar sua situação o mais breve possível. Responda "PAGO" se já efetuou o pagamento. Obrigado!',
            tipo='vencida'
        )
        db.session.add(modelo_vencida)
    
    if not ModeloMensagem.query.filter_by(titulo='Confirmação de Pagamento').first():
        modelo_confirmacao = ModeloMensagem(
            titulo='Confirmação de Pagamento',
            conteudo='Olá {nome}, recebemos seu pagamento no valor de R$ {valor:.2f} referente à cobrança com vencimento em {data_vencimento}. Agradecemos sua pontualidade!',
            tipo='confirmacao'
        )
        db.session.add(modelo_confirmacao)
    
    db.session.commit()
    
    print("Banco de dados inicializado com sucesso!")
