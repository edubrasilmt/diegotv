import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Inicializar extensões
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    # Configurações
    database_url = os.environ.get('DATABASE_URL')
    if database_url and database_url.startswith('postgres://'):
        # Render usa postgres://, mas SQLAlchemy requer postgresql://
        database_url = database_url.replace('postgres://', 'postgresql://', 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Configuração local
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/cobranca.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'chave-secreta-para-desenvolvimento')
    app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'app', 'static', 'uploads')
    
    # Garantir que a pasta de uploads exista
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Inicializar extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    
    with app.app_context():
        # Importar modelos
        from app.models import Cliente, Cobranca, ModeloMensagem, MensagemEnviada, Imagem, ImagemCobranca
        
        # Importar e registrar blueprints
        from app.controllers.cliente_controller import cliente_bp
        from app.controllers.dashboard_controller import dashboard_bp
        from app.controllers.whatsapp_controller import whatsapp_bp
        from app.controllers.imagem_controller import imagem_bp
        from app.controllers.cobranca_controller import cobranca_bp
        
        app.register_blueprint(cliente_bp)
        app.register_blueprint(dashboard_bp)
        app.register_blueprint(whatsapp_bp)
        app.register_blueprint(imagem_bp)
        app.register_blueprint(cobranca_bp)
        
        # Registrar rota principal para redirecionar para o dashboard
        @app.route('/')
        def index():
            from flask import redirect, url_for
            return redirect(url_for('dashboard.index'))
        
        # Criar tabelas se não existirem
        try:
            db.create_all()
        except Exception as e:
            print(f"Erro ao criar banco de dados: {str(e)}")
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
