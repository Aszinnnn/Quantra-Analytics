from data_generator import generate_fake_data
from data_processor import process_data
from visualizer import create_visualizations
from exportador import exportar_empresas
from utils.logger import setup_logger

logger = setup_logger("empresas_logger")

def main():
    logger.info("Gerando dados...")
    df = generate_fake_data(50)  # 50 empresas
    exportar_empresas(df)
    processed_data = process_data(df)
    create_visualizations(processed_data)

if __name__ == "__main__":
    main()