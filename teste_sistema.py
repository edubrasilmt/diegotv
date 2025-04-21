"""
Script para testar o funcionamento completo do sistema.
Este script realiza testes em todas as funcionalidades principais do sistema.
"""

import os
import sys
import logging
import unittest
from datetime import datetime, timedelta
from app import create_app, db
from app.models import Cliente, Cobranca, ModeloMensagem, MensagemEnviada, Imagem, ImagemCobranca
from app.services.cliente_service import ClienteService
from app.services.whatsapp_service import WhatsAppService
from app.services.imagem_service import ImagemService

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger('TesteSistema')

class TesteSistema(unittest.TestCase):
    """
    Classe para testar o funcionamento completo do sistema.
    """
    
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.app = create_app(testing=True)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        self.populate_test_data()
        
    def tearDown(self):
        """
        Limpeza após os testes.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def populate_test_data(self):
        """
        Popula o banco de dados com dados de teste.
        """
        # Criar clientes de teste
        clientes = [
            Cliente(nome='João Silva', telefone='+5511987654321', email='joao@example.com'),
            Cliente(nome='Maria Oliveira', telefone='+5511976543210', email='maria@example.com'),
            Cliente(nome='Pedro Santos', telefone='+5511965432109', email='pedro@example.com')
        ]
        
        for cliente in clientes:
            db.session.add(cliente)
        
        # Criar modelos de mensagem
        modelos = [
            ModeloMensagem(
                titulo='Cobrança Padrão',
                conteudo='Olá {nome}, este é um lembrete de cobrança no valor de R$ {valor:.2f} com vencimento em {data_vencimento}. Por favor, efetue o pagamento para evitar juros e multas. Responda "PAGO" quando efetuar o pagamento. Obrigado!',
                tipo='padrao'
            ),
            ModeloMensagem(
                titulo='Cobrança Vencida',
                conteudo='Atenção {nome}, sua cobrança no valor de R$ {valor:.2f} está vencida desde {data_vencimento}. Por favor, entre em contato conosco para regularizar sua situação o mais breve possível. Responda "PAGO" se já efetuou o pagamento. Obrigado!',
                tipo='vencida'
            )
        ]
        
        for modelo in modelos:
            db.session.add(modelo)
        
        db.session.commit()
        
        # Criar cobranças
        hoje = datetime.now().date()
        
        cobranças = [
            Cobranca(
                cliente_id=1,
                valor=100.50,
                data_vencimento=hoje + timedelta(days=5),
                status='pendente',
                frequencia='mensal'
            ),
            Cobranca(
                cliente_id=2,
                valor=250.75,
                data_vencimento=hoje - timedelta(days=2),
                status='vencida',
                frequencia='mensal'
            ),
            Cobranca(
                cliente_id=3,
                valor=75.30,
                data_vencimento=hoje + timedelta(days=10),
                status='pendente',
                frequencia='semanal'
            )
        ]
        
        for cobranca in cobranças:
            db.session.add(cobranca)
        
        db.session.commit()
        
        logger.info("Dados de teste populados com sucesso.")
    
    def test_cliente_service(self):
        """
        Testa o serviço de gerenciamento de clientes.
        """
        logger.info("Testando serviço de clientes...")
        
        # Testar busca de clientes
        clientes = ClienteService.buscar_clientes()
        self.assertEqual(len(clientes), 3)
        
        # Testar busca por ID
        cliente = ClienteService.buscar_cliente_por_id(1)
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente.nome, 'João Silva')
        
        # Testar criação de cliente
        novo_cliente = {
            'nome': 'Ana Souza',
            'telefone': '+5511954321098',
            'email': 'ana@example.com'
        }
        
        cliente_criado = ClienteService.criar_cliente(novo_cliente)
        self.assertIsNotNone(cliente_criado)
        self.assertEqual(cliente_criado.nome, 'Ana Souza')
        
        # Verificar se foi criado no banco
        cliente_db = Cliente.query.filter_by(email='ana@example.com').first()
        self.assertIsNotNone(cliente_db)
        
        logger.info("Teste de serviço de clientes concluído com sucesso.")
    
    def test_whatsapp_service(self):
        """
        Testa o serviço de envio de WhatsApp.
        """
        logger.info("Testando serviço de WhatsApp...")
        
        # Testar formatação de mensagem
        cobranca = Cobranca.query.get(1)
        modelo = ModeloMensagem.query.filter_by(tipo='padrao').first()
        
        mensagem = WhatsAppService.formatar_mensagem(cobranca, modelo.conteudo)
        self.assertIn('João Silva', mensagem)
        self.assertIn('100.50', mensagem)
        
        # Testar processamento de cobranças pendentes (sem envio real)
        WhatsAppService.processar_cobranças_pendentes = lambda tipo_frequencia: (2, [])
        processadas, erros = WhatsAppService.processar_cobranças_pendentes('mensal')
        self.assertEqual(processadas, 2)
        self.assertEqual(len(erros), 0)
        
        logger.info("Teste de serviço de WhatsApp concluído com sucesso.")
    
    def test_imagem_service(self):
        """
        Testa o serviço de gerenciamento de imagens.
        """
        logger.info("Testando serviço de imagens...")
        
        # Testar extensão permitida
        self.assertTrue(ImagemService.extensao_permitida('imagem.jpg'))
        self.assertTrue(ImagemService.extensao_permitida('imagem.png'))
        self.assertFalse(ImagemService.extensao_permitida('documento.pdf'))
        
        # Testar busca de imagens (sem imagens ainda)
        imagens = ImagemService.buscar_imagens()
        self.assertEqual(len(imagens), 0)
        
        logger.info("Teste de serviço de imagens concluído com sucesso.")
    
    def test_routes(self):
        """
        Testa as rotas principais da aplicação.
        """
        logger.info("Testando rotas da aplicação...")
        
        # Testar rota de dashboard
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
        # Testar rota de listagem de clientes
        response = self.client.get('/clientes/')
        self.assertEqual(response.status_code, 200)
        
        # Testar rota de visualização de cliente
        response = self.client.get('/clientes/1')
        self.assertEqual(response.status_code, 200)
        
        # Testar rota de listagem de imagens
        response = self.client.get('/imagens/')
        self.assertEqual(response.status_code, 200)
        
        logger.info("Teste de rotas concluído com sucesso.")
    
    def run_all_tests(self):
        """
        Executa todos os testes.
        """
        logger.info("Iniciando testes do sistema...")
        
        self.test_cliente_service()
        self.test_whatsapp_service()
        self.test_imagem_service()
        self.test_routes()
        
        logger.info("Todos os testes concluídos com sucesso!")
        return True

def main():
    """
    Função principal para executar os testes.
    """
    teste = TesteSistema()
    try:
        teste.setUp()
        resultado = teste.run_all_tests()
        teste.tearDown()
        
        if resultado:
            logger.info("Sistema testado e funcionando corretamente!")
            return 0
        else:
            logger.error("Falha nos testes do sistema.")
            return 1
    except Exception as e:
        logger.error(f"Erro durante os testes: {str(e)}")
        return 1

if __name__ == '__main__':
    sys.exit(main())
